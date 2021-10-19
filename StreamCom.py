"""Class definition of the StreamCom Landscape Model component."""
import base
import os
import shutil
import xml.etree.ElementTree
import numpy as np
import datetime
import attrib


class StreamCom(base.Component):
    """Encapsulates the StreamCom module for the Landscape Model."""
    # RELEASES
    VERSION = base.VersionCollection(
        base.VersionInfo("2.2.2", "2021-10-14"),
        base.VersionInfo("2.2.1", "2021-10-14"),
        base.VersionInfo("2.2.0", "2021-10-13"),
        base.VersionInfo("2.1.5", "2021-10-12"),
        base.VersionInfo("2.1.4", "2021-10-11"),
        base.VersionInfo("2.1.3", "2021-09-17"),
        base.VersionInfo("2.1.2", "2021-08-31"),
        base.VersionInfo("2.1.1", "2021-08-23"),
        base.VersionInfo("2.1.0", "2021-08-09"),
        base.VersionInfo("2.0.5", "2021-08-05"),
        base.VersionInfo("2.0.4", "2021-07-20"),
        base.VersionInfo("2.0.3", "2021-07-19"),
        base.VersionInfo("2.0.2", "2021-01-25"),
        base.VersionInfo("2.0.1", "2020-12-03"),
        base.VersionInfo("2.0.0", "2020-10-22"),
        base.VersionInfo("1.3.35", "2020-08-12"),
        base.VersionInfo("1.3.34", "2020-08-04"),
        base.VersionInfo("1.3.33", "2020-07-30"),
        base.VersionInfo("1.3.32", "2020-07-17"),
        base.VersionInfo("1.3.31", "2020-06-23"),
        base.VersionInfo("1.3.27", "2020-05-20"),
        base.VersionInfo("1.3.25", "2020-04-06"),
        base.VersionInfo("1.3.24", "2020-04-02"),
        base.VersionInfo("1.3.22", "2020-03-27"),
        base.VersionInfo("1.3.21", "2020-03-26")
    )

    # AUTHORS
    VERSION.authors.extend((
        "Sascha Bub (component) - sascha.bub@gmx.de",
        "Thorsten Schad (component) - thorsten.schad@bayer.com",
        "Tido Strauß (module) - strauss@gaiac-eco.de",
        "Jana Gerhard (module) - gerhard@gaiac-eco.de"
    ))

    # ACKNOWLEDGEMENTS
    VERSION.acknowledgements.extend((
        "[NumPy](https://numpy.org)",
        "[StreamCom](https://gaiac-eco.de/oekotoxikologie/effektmodellierung/)"
    ))

    # ROADMAP
    VERSION.roadmap.extend((
        """Start module GUI in background
        ([#1](https://gitlab.bayer.com/aqrisk-landscape/streamcom-component/-/issues/1))""",
    ))

    # CHANGELOG
    VERSION.added("1.3.21", "`components.StreamCom` component")
    VERSION.fixed("1.3.22", "Reach indexing in `components.StreamCom` ")
    VERSION.changed("1.3.24", "`components.StreamCom` uses base function to call module")
    VERSION.changed("1.3.25", "`components.StreamCom` updated to module version 2.0.4")
    VERSION.changed("1.3.27", "`components.StreamCom` specifies scales")
    VERSION.changed("1.3.31", "`components.StreamCom` updated to module version 2.0.10")
    VERSION.changed("1.3.32", "`components.StreamCom` updated to module version 2.0.17")
    VERSION.changed("1.3.33", "`components.StreamCom` checks input types strictly")
    VERSION.fixed("1.3.33", "`components.StreamCom` where slicing of exposure input was incorrect")
    VERSION.changed("1.3.33", "`components.StreamCom` checks for physical units")
    VERSION.changed("1.3.33", "`components.StreamCom` checks for scales")
    VERSION.fixed("1.3.34", "Physical units of killing rate in `components.StreamCom` ")
    VERSION.fixed("1.3.35", "`components.StreamCom` receives CommonProgramFiles(x86) environment variable")
    VERSION.changed("2.0.0", "First independent release")
    VERSION.added("2.0.1", "Changelog and release history")
    VERSION.changed("2.0.2", "Error message when reach could not be found")
    VERSION.added("2.0.3", ".gitignore")
    VERSION.changed(
        "2.0.4", "Increased portability by shipping Microsoft's data access components with Landscape Model component")
    VERSION.added("2.0.5", "Support of multiple module runs")
    VERSION.changed("2.1.0", "Updated the module to version 2.0.20")
    VERSION.changed("2.1.1", "Ensured to run in normal window mode")
    VERSION.changed("2.1.2", "Added base documentation")
    VERSION.changed("2.1.3", "Make use of generic types for class attributes")
    VERSION.changed("2.1.4", "Replaced legacy format strings by f-strings")
    VERSION.changed("2.1.5", "Switched to Google docstring style")
    VERSION.changed("2.2.0", "Updated the module to version 2.0.21")
    VERSION.changed("2.2.1", "Usage of report.txt as indicator for successful StreamCom runs")
    VERSION.changed("2.2.2", "Specified working directory for module")

    def __init__(self, name, observer, store):
        """
        Initializes a StreamCom component.

        Args:
            name: The name of the component.
            observer: The default observer of the component.
            store: The default store of the component.
        """
        super(StreamCom, self).__init__(name, observer, store)
        # noinspection SpellCheckingInspection
        self._module = base.Module("STREAM-com", "2.0.21")
        self._inputs = base.InputContainer(self, [
            base.Input(
                "ProcessingPath",
                (attrib.Class(str, 1), attrib.Unit(None, 1), attrib.Scales("global", 1)),
                self.default_observer,
                description="""The working directory for the module. It is used for all files prepared as module inputs
                or generated as module outputs."""
            ),
            base.Input(
                "Reaches",
                (attrib.Class(list[int], 1), attrib.Unit(None, 1), attrib.Scales("space/reach", 1)),
                self.default_observer,
                description="""The numeric identifiers for individual reaches (in the order of the hydro,logical inputs)
                that apply scenario-wide."""
            ),
            base.Input(
                "Reach",
                (attrib.Class(int, 1), attrib.Unit(None, 1), attrib.Scales("global", 1)),
                self.default_observer,
                description="The numerical identifier of the reach that is selected for the StreamCom simulation."
            ),
            base.Input(
                "Concentrations",
                (
                    attrib.Class(np.ndarray, 1),
                    attrib.Unit("ng/l", 1),
                    attrib.Scales("time/hour, space/base_geometry", 1)
                ),
                self.default_observer,
                description="The substance concentrations in water phase."
            ),
            base.Input(
                "Species",
                (attrib.Class(list[str], 1), attrib.Unit(None, 1), attrib.Scales("other/species", 1)),
                self.default_observer,
                description="""The list of species simulated by StreamCom. See the scenario description for the 
                available species."""
            ),
            base.Input(
                "DominantRateConstantsForLm",
                (attrib.Class(list[float], 1), attrib.Unit("1/d", 1), attrib.Scales("other/species", 1)),
                self.default_observer,
                description="The dominant rate constants for the GUTS functions applied to the simulated species."
            ),
            base.Input(
                "ThresholdsForLethalEffects",
                (attrib.Class(list[float], 1), attrib.Unit("ng/l", 1), attrib.Scales("other/species", 1)),
                self.default_observer,
                description="The thresholds for lethal effects for the GUTS functions applied to the simulated species."
            ),
            base.Input(
                "KillingRates",
                (
                    attrib.Class(list[float], 1),
                    attrib.Unit("l/(ng*d)", 1),
                    attrib.Scales("other/species", 1)
                ),
                self.default_observer,
                description="The killing rates for the GUTS functions applied to the simulated species."
            ),
            base.Input(
                "SiteInformation",
                (attrib.Class(str, 1), attrib.Unit(None, 1), attrib.Scales("global", 1)),
                self.default_observer,
                description="The path to the XML file describing the simulated site."
            ),
            base.Input(
                "SpeciesParameters",
                (attrib.Class(str, 1), attrib.Unit(None, 1), attrib.Scales("global", 1)),
                self.default_observer,
                description="The path to the XML file containing the database of species parameters."
            ),
            base.Input(
                "WaterTemperature",
                (attrib.Class(str, 1), attrib.Unit(None, 1), attrib.Scales("global", 1)),
                self.default_observer,
                description="The path to a TSV file containing a time-series of water temperatures."
            ),
            base.Input(
                "Site",
                (attrib.Class(str, 1), attrib.Unit(None, 1), attrib.Scales("global", 1)),
                self.default_observer,
                description="The name of the site."
            ),
            base.Input(
                "FirstDay",
                (attrib.Class(datetime.date, 1), attrib.Unit(None, 1), attrib.Scales("global", 1)),
                self.default_observer,
                description="The first simulated day."
            ),
            base.Input(
                "LastDay",
                (attrib.Class(datetime.date, 1), attrib.Unit(None, 1), attrib.Scales("global", 1)),
                self.default_observer,
                description="The last simulated day."
            ),
            base.Input(
                "UseSubLethalToxEffects",
                (attrib.Class(bool, 1), attrib.Unit(None, 1), attrib.Scales("global", 1)),
                self.default_observer,
                description="Specifies whether sub-lethal effects are simulated."
            ),
            base.Input(
                "ThresholdPopulationSizeForSuperIndividuals",
                (attrib.Class(int, 1), attrib.Unit("1", 1), attrib.Scales("global", 1)),
                self.default_observer,
                description="The population size threshold for super-individuals."
            ),
            base.Input(
                "NumberOfSiblingsPerSuperIndividual",
                (attrib.Class(int, 1), attrib.Unit("1", 1), attrib.Scales("global", 1)),
                self.default_observer,
                description="The number of siblings per super-individual."
            ),
            base.Input(
                "MaximumPeriphytonGrowthRate",
                (attrib.Class(float, 1), attrib.Unit("1/d", 1), attrib.Scales("global", 1)),
                self.default_observer,
                description="The maximum periphyton growth rate."
            ),
            base.Input(
                "PeriphytonCarryingCapacity",
                (attrib.Class(float, 1), attrib.Unit("g/m²", 1), attrib.Scales("global", 1)),
                self.default_observer,
                description="The periphyton carrying capacity."
            ),
            base.Input(
                "PeriphytonArrheniusTemperature",
                (attrib.Class(float, 1), attrib.Unit("K", 1), attrib.Scales("global", 1)),
                self.default_observer,
                description="The periphyton Arrhenius temperature."
            ),
            base.Input(
                "InitialLeafLitterDensity",
                (attrib.Class(float, 1), attrib.Unit("g/m²", 1), attrib.Scales("global", 1)),
                self.default_observer,
                description="The initial leaf-litter density."
            ),
            base.Input(
                "LeafLitterEnergyDensity",
                (attrib.Class(float, 1), attrib.Unit("J/g", 1), attrib.Scales("global", 1)),
                self.default_observer,
                description="The energy-density of leaf-litter."
            ),
            base.Input(
                "DayOfYearForLitterAddition",
                (attrib.Class(int, 1), attrib.Unit("d", 1), attrib.Scales("global", 1)),
                self.default_observer,
                description="The day of the year when leaf-litter is added to the stream."
            ),
            base.Input(
                "C-PomSettlementRate",
                (attrib.Class(float, 1), attrib.Unit("1/d", 1), attrib.Scales("global", 1)),
                self.default_observer,
                description="The C-Pom settlement rate."
            ),
            base.Input(
                "MaximumVelocityClassForC-PomAddition",
                (attrib.Class(int, 1), attrib.Unit(None, 1), attrib.Scales("global", 1)),
                self.default_observer,
                description="The maximum velocity class for C-Pom additions."
            ),
            base.Input(
                "SettlementRateForFPomAndAnimalRemains",
                (attrib.Class(float, 1), attrib.Unit("1/d", 1), attrib.Scales("global", 1)),
                self.default_observer,
                description="The settlement rate for F-Pom and animal remains."
            ),
            base.Input(
                "InitialF-PomDensity",
                (attrib.Class(float, 1), attrib.Unit("J/m²", 1), attrib.Scales("global", 1)),
                self.default_observer,
                description="The initial F-Pom density."
            ),
            base.Input(
                "InitialS-PomDensity",
                (attrib.Class(float, 1), attrib.Unit("J/m²", 1), attrib.Scales("global", 1)),
                self.default_observer,
                description="The initial S-Pom density."
            ),
            base.Input(
                "FractionOfS-PomAvailableToFilterFeeders",
                (attrib.Class(float, 1), attrib.Unit("1", 1), attrib.Scales("global", 1)),
                self.default_observer,
                description="The fraction of S-Pom available to filter-feeders."
            ),
            base.Input(
                "PeriphytonEnergyDensity",
                (attrib.Class(float, 1), attrib.Unit("J/g", 1), attrib.Scales("global", 1)),
                self.default_observer,
                description="The periphyton energy-density."
            ),
            base.Input(
                "UsePopulationDensity",
                (attrib.Class(bool, 1), attrib.Unit(None, 1), attrib.Scales("global", 1)),
                self.default_observer,
                description="Specifies whether to use population density."
            ),
            base.Input(
                "SavePopulationSize",
                (attrib.Class(bool, 1), attrib.Unit(None, 1), attrib.Scales("global", 1)),
                self.default_observer,
                description="Specifies whether to output the population size."
            ),
            base.Input(
                "SaveTraitSize",
                (attrib.Class(bool, 1), attrib.Unit(None, 1), attrib.Scales("global", 1)),
                self.default_observer,
                description="Specifies whether to output trait size."
            ),
            base.Input(
                "SavePopulationDistribution",
                (attrib.Class(bool, 1), attrib.Unit(None, 1), attrib.Scales("global", 1)),
                self.default_observer,
                description="Specifies whether to output population distributions."
            ),
            base.Input(
                "SaveTraitDistribution",
                (attrib.Class(bool, 1), attrib.Unit(None, 1), attrib.Scales("global", 1)),
                self.default_observer,
                description="Specifies whether to output trait distributions."
            ),
            base.Input(
                "Biomass",
                (attrib.Class(str, 1), attrib.Unit(None, 1), attrib.Scales("global", 1)),
                self.default_observer,
                description="The path to a text file specifying initial biomass."
            ),
            base.Input(
                "StartBiomass",
                (attrib.Class(str), attrib.Unit(None), attrib.Scales("global"), attrib.InList(("Ind/m^2", "g/m^2"))),
                self.default_observer,
                description="Specifies the unit odf initial biomass."
            ),
            base.Input(
                "NumberRuns",
                (attrib.Class(int), attrib.Unit("1"), attrib.Scales("global")),
                self.default_observer,
                description="The number of module-internal Monte Carlo runs."
            )
        ])
        self._store = store
        self._selectedSpecies = []

    def run(self):
        """
        Runs the component.

        Returns:
            Nothing.
        """
        processing_path = self.inputs["ProcessingPath"].read().values
        input_path = os.path.join(processing_path, "in")
        output_path = os.path.join(processing_path, "out")
        os.makedirs(input_path)
        os.makedirs(output_path)
        self.prepare_chemical_input(os.path.join(input_path, "exposure.txt"))
        self.prepare_toxicological_parameters(os.path.join(input_path, "tox_parameters.txt"))
        self.prepare_site_information_input(os.path.join(input_path, "site.txt"))
        self.prepare_species_input(os.path.join(input_path, "spec.xml"))
        self.prepare_water_temperature_input(os.path.join(input_path, "temp.txt"))
        self.write_settings(os.path.join(input_path, "Settings.txt"))
        self.prepare_biomass_input(os.path.join(input_path, "biomass.txt"))
        self.run_module(input_path, output_path)
        self.read_outputs(output_path)

    def prepare_chemical_input(self, chemical_file):
        """
        Prepares the module's chemical input.

        Args:
            chemical_file: The file path of the chemical input.

        Returns:
            Nothing.
        """
        reaches = np.asarray(self.inputs["Reaches"].read().values, np.int)
        reach = self.inputs["Reach"].read().values
        indices = np.nonzero(reaches == int(reach))
        if len(indices[0]) != 1:
            raise ValueError(f"Error finding reach {reach}")
        index = int(indices[0])
        hours = self.inputs["Concentrations"].describe()["shape"][0]
        first_day = self.inputs["FirstDay"].read().values
        with open(chemical_file, "w", encoding="utf-8") as f:
            f.write("Date\tConcentration [ng/L]\n")
            for day in range(int(hours / 24)):
                data = self.inputs["Concentrations"].read(slices=(slice(day * 24, day * 24 + 24), index)).values
                f.write(
                    f"{datetime.datetime.strftime(first_day + datetime.timedelta(day), '%d/%m/%Y')}\t{np.max(data)}\n")

    def prepare_toxicological_parameters(self, parameter_file):
        """
        Prepares the toxicological parameters.

        Args:
            parameter_file: The file path of the toxicological parameter file.

        Returns:
            Nothing.
        """
        with open(parameter_file, "w") as f:
            f.write("Information\tValue\tComment\n")
            f.write("Substance\tCMP_A\n")
            f.write("Concentration_unit\tµg/L\t[Unit of concentration for exposure and parameter values]\n")
            # noinspection SpellCheckingInspection
            f.write('PMoA\tfeeding\t"[feeding, maintenance costs, growht, oogenesis hazard]"\n\n\n\n')
            species = "\t".join(self.inputs["Species"].read().values)
            f.write(f"Parameter\tDescription\tUnit\t{species}\n")
            dominant_rate_constants_for_lm = "\t".join(
                [str(x) for x in self.inputs["DominantRateConstantsForLm"].read().values])
            f.write(f"kd\tdominant rate constant for Lm/L\t1/d\t{dominant_rate_constants_for_lm}\n")
            thresholds_for_lethal_effects = "\t".join(
                [str(x) for x in self.inputs["ThresholdsForLethalEffects"].read().values])
            f.write(
                f"z\tthreshold for lethal effect\tunit of external concentration\t{thresholds_for_lethal_effects}\n")
            killing_rates = "\t".join([str(x) for x in self.inputs["KillingRates"].read().values])
            f.write(f"kk\tkilling rate\t1/d\t{killing_rates}\n")
            thresholds_for_sub_lethal_effects = "\t".join(["1000" for _ in self.inputs["KillingRates"].read().values])
            # noinspection SpellCheckingInspection
            # noinspection GrazieInspection
            f.write(
                "c0\tthreshold for sublethal effect\tunit of external concentration\t"
                f"{thresholds_for_sub_lethal_effects}\n"
            )
            tolerance_concentrations = "\t".join(['1' for _ in self.inputs["KillingRates"].read().values])
            f.write(f"cT\ttolerance concentration\tunit of external concentration\t{tolerance_concentrations}\n")

    def prepare_site_information_input(self, site_information_file):
        """
        Prepares the module's site information.

        Args:
            site_information_file: The file path of the site information.

        Returns:
            Nothing.
        """
        shutil.copyfile(self.inputs["SiteInformation"].read().values, site_information_file)

    def prepare_species_input(self, species_file):
        """
        Prepares the module's species input.

        Args:
            species_file: The file pah of the species input.

        Returns:
            Nothing.
        """
        selected_species = self.inputs["Species"].read().values
        species_database = xml.etree.ElementTree.parse(self.inputs["SpeciesParameters"].read().values)
        # noinspection SpellCheckingInspection
        data = species_database.find("{urn:schemas-microsoft-com:rowset}data")
        rows_to_remove = []
        for row in data:
            if row.attrib["species"] in selected_species:
                selected_species.remove(row.attrib["species"])
                self._selectedSpecies.append(row.attrib["species"])
            else:
                rows_to_remove.append(row)
        for row in rows_to_remove:
            data.remove(row)
        for species in selected_species:
            self.default_observer.write_message(2, f"No parameters found for {species}")
        species_database.write(species_file)

    def prepare_water_temperature_input(self, input_path):
        """
        Prepares the water temperature input.

        Args:
            input_path: File path of the water temperature input.

        Returns:
            Nothing.
        """
        input_file = self.inputs["WaterTemperature"].read().values
        shutil.copyfile(input_file, input_path)

    def run_module(self, input_path, output_path):
        """
        Runs the module.

        Args:
            input_path: The file path containing the module's input files.
            output_path: The file path for the module's outputs.

        Returns:
            Nothing.
        """
        number_days = int((self.inputs["LastDay"].read().values - self.inputs["FirstDay"].read().values).days) + 1
        # noinspection SpellCheckingInspection
        base.run_process(
            (
                os.path.join(os.path.dirname(__file__), "module", "ProjectStreamCom.exe"),
                "--site_name",
                "site.txt",
                "--num_mc",
                str(self.inputs["NumberRuns"].read().values),
                "--sim_duration",
                str(number_days),
                "--input_path",
                input_path,
                "--output_path",
                output_path,
                "--tox_name",
                "tox_parameters.txt",
                "--tox_sublethal" if self.inputs["UseSubLethalToxEffects"].read().values else "",
                "--species",
                ",".join(self._selectedSpecies),
                "--start_biomass",
                self.inputs["StartBiomass"].read().values
            ),
            output_path,
            self.default_observer,
            {"CommonProgramFiles(x86)": os.path.join(os.path.dirname(__file__), "dac")},
            False
        )

    def read_outputs(self, output_path):
        """
        Imports the module's outputs into the Landscape Model.

        Args:
            output_path: The file path of the module's outputs.

        Returns:
            Nothing.
        """
        number_runs = self.inputs["NumberRuns"].read().values
        run_successful = False
        for output in os.listdir(output_path):
            self.outputs.append(base.Output(output, self._store, self))
            with open(os.path.join(output_path, output)) as f:
                data = [row[:-1].split("\t") for row in f.readlines()[1:]]
            if output[:2] in ["f_", "h_"]:
                values = np.zeros((len(data), number_runs))
                for record in data:
                    for run in range(number_runs):
                        values[int(record[0]) - 1, run] = float(record[run + 1].replace(",", "."))
                self.outputs[output].set_values(values, scales="time/day_of_year, other/runs")
            elif output[:11] == "population_":
                values = np.zeros((len(data), number_runs), np.int)
                for record in data:
                    for run in range(number_runs):
                        values[int(record[0]) - 1, run] = int(record[run + 1].replace(",", "."))
                self.outputs[output].set_values(values, scales="time/day_of_year, other/runs")
            elif output[:3] == "xy_":
                x_values = [int(record[0]) for record in data]
                y_values = [int(record[1]) for record in data]
                results = [[]] * number_runs
                for run in range(number_runs):
                    results[run] = [float(record[run + 3].replace(",", ".")) for record in data]
                values = np.zeros((max(x_values) + 1, max(y_values) + 1, number_runs))
                for run in range(number_runs):
                    for i in range(len(results[run])):
                        values[x_values[i], y_values[i], run] = results[run][i]
                self.outputs[output].set_values(values, scales="space/x_5dm, space/y_5dm, other/runs")
            elif output == "report.txt":
                run_successful = True
            else:
                self.default_observer.write_message(2, f"Unknown output: {output}")
        if run_successful is False:
            self.default_observer.write_message(1, "StreamCom run was not successful, no report.txt was found")

    def write_settings(self, settings_file):
        """
        Writes the StreamCom parameterization file.

        Args:
            settings_file: The file path of the parameterization file.

        Returns:
            Nothing.
        """
        with open(settings_file, "w") as f:
            f.write(
                "Threshold population size for super individuals [#],"
                f"{self.inputs['ThresholdPopulationSizeForSuperIndividuals'].read().values}\n"
            )
            # noinspection SpellCheckingInspection
            f.write(
                "Number of siblings per super indiviual [#],"
                f"{self.inputs['NumberOfSiblingsPerSuperIndividual'].read().values}\n"
            )
            f.write(
                f"Maximum periphyton growth rate [1/d],{self.inputs['MaximumPeriphytonGrowthRate'].read().values}\n")
            # noinspection SpellCheckingInspection
            f.write(f"Periphyton carying capacity [g/m^2],{self.inputs['PeriphytonCarryingCapacity'].read().values}\n")
            f.write(
                f"Periphyton Arrhenius temperature [K],{self.inputs['PeriphytonArrheniusTemperature'].read().values}\n")
            f.write(f"Initial leaf litter density [g/m^2],{self.inputs['InitialLeafLitterDensity'].read().values}\n")
            f.write(f"Leaf litter energy density [J/g],{self.inputs['LeafLitterEnergyDensity'].read().values}\n")
            f.write(f"Day of year for litter addition [d],{self.inputs['DayOfYearForLitterAddition'].read().values}\n")
            f.write(f"C-POM settlement rate [1/d],{self.inputs['C-PomSettlementRate'].read().values}\n")
            f.write(
                "Maximum velocity class for C-POM addition [1...6],"
                f"{self.inputs['MaximumVelocityClassForC-PomAddition'].read().values}\n"
            )
            f.write(
                "Settlement rate for F-POM and animal remains [1/d],"
                f"{self.inputs['SettlementRateForFPomAndAnimalRemains'].read().values}\n"
            )
            f.write(f"Initial F-POM density [J/m^2],{self.inputs['InitialF-PomDensity'].read().values}\n")
            f.write(f"Initial S-POM density [J/m^2],{self.inputs['InitialS-PomDensity'].read().values}\n")
            f.write(
                "Fraction of S-POM available to filter feeders [-],"
                f"{self.inputs['FractionOfS-PomAvailableToFilterFeeders'].read().values}\n"
            )
            f.write(f"Periphyton energy density [J/g],{self.inputs['PeriphytonEnergyDensity'].read().values}\n")
            f.write(f"use population density [#/m^2] as output,{self.inputs['UsePopulationDensity'].read().values}\n")
            f.write(f"save population size,{self.inputs['SavePopulationSize'].read().values}\n")
            f.write(f"save trait size,{self.inputs['SaveTraitSize'].read().values}\n")
            f.write(f"save population distribution,{self.inputs['SavePopulationDistribution'].read().values}\n")
            f.write(f"save trait distribution,{self.inputs['SaveTraitDistribution'].read().values}\n")

    def prepare_biomass_input(self, biomass_file):
        """
        Prepares the module's biomass information.

        Args:
            biomass_file: The file path of the site information.

        Returns:
            Nothing.
        """
        shutil.copyfile(self.inputs["Biomass"].read().values, biomass_file)
