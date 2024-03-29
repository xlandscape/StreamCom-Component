## Table of Contents

* [About the project](#about-the-project)
    * [Built With](#built-with)
* [Getting Started](#getting-started)
    * [Prerequisites](#prerequisites)
    * [Installation](#installation)
* [Usage](#usage)
    * [Inputs](#inputs)
    * [Outputs](#outputs)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)

## About the project

Encapsulates the StreamCom module for the Landscape Model.  
This is an automatically generated documentation based on the available code and in-line documentation. The current
version of this document is from 2023-09-12.

### Built with

* Landscape Model core version 1.15.2
* STREAM-com version 3.2.2 

## Getting Started

The component can be used in any Landscape Model based on core version 1.15.2 or newer. See the Landscape
Model core's `README` for general tips on how to add a component to a Landscape Model.

### Prerequisites

A model developer that wants to add the `StreamCom` component to a Landscape Model needs to set up the general
structure for a Landscape Model first. See the Landscape Model core's `README` for details on how to do so.

### Installation

1. Copy the `StreamCom` component into the `model\variant` sub-folder.
2. Make use of the component by including it into the model composition using `module=StreamCom` and
   `class=StreamCom`.

## Usage

The following gives a sample configuration of the `StreamCom` component. See [inputs](#inputs) and
[outputs](#outputs) for further details on the component's interface.

```xml
<StreamCom1_StepsRiverNetwork module="StreamCom" class="StreamCom" enabled_expression="'$(RunStepsRiverNetwork)' ==
'true' and '$(RunStreamCom)' == 'true' and                 '$(StreamComReach1)' != ''">
    <ProcessingPath
scales="global">
        $(_MCS_BASE_DIR_)\$(_MC_NAME_)\processing\effect\com_steps_1
    </ProcessingPath>
    <Reach
type="int" scales="global">$(StreamComReach1)</Reach>
    <Concentrations>
        <FromOutput
component="StepsRiverNetwork" output="PEC_SW" />
    </Concentrations>
    <Species type="list[str]"
scales="other/species" element_names="StreamCom1_StepsRiverNetwork/Species">
        $(Species1)|$(Species2)|$(Species3)
</Species>
    <DominantRateConstantsForLm type="list[float]" scales="other/species" unit="1/d"
element_names="StreamCom1_StepsRiverNetwork/Species">
        $(Species1DominantRateConstantSD)
$(Species2DominantRateConstantSD) $(Species3DominantRateConstantSD)
    </DominantRateConstantsForLm>
<ThresholdsForLethalEffects type="list[float]" scales="other/species" unit="ng/l"
element_names="StreamCom1_StepsRiverNetwork/Species">
        $(Species1ThresholdConcentrationSD)
$(Species2ThresholdConcentrationSD)
        $(Species3ThresholdConcentrationSD)
    </ThresholdsForLethalEffects>
<KillingRates type="list[float]" scales="other/species" unit="l/(ng*h)"
element_names="StreamCom1_StepsRiverNetwork/Species">
        $(Species1KillingRateSD) $(Species2KillingRateSD)
$(Species3KillingRateSD)
    </KillingRates>
    <SiteInformation scales="global">$(:SiteInformation)</SiteInformation>
<SpeciesParameters scales="global">$(:SpeciesParameters)</SpeciesParameters>
    <WaterTemperature
scales="global">$(:WaterTemperature)</WaterTemperature>
    <Site scales="global">Niers_Peutenweg</Site>
    <FirstDay
type="date" scales="global">$(SimulationStart)</FirstDay>
    <LastDay type="date"
scales="global">$(SimulationEnd)</LastDay>
    <UseSubLethalToxEffects type="bool"
scales="global">$(UseSubLethalToxEffects)</UseSubLethalToxEffects>
    <ThresholdPopulationSizeForSuperIndividuals
type="int" unit="1" scales="global">
        $(ThresholdPopulationSizeForSuperIndividuals)
</ThresholdPopulationSizeForSuperIndividuals>
    <NumberOfSiblingsPerSuperIndividual type="int" unit="1"
scales="global">
        $(NumberOfSiblingsPerSuperIndividual)
    </NumberOfSiblingsPerSuperIndividual>
<MaximumPeriphytonGrowthRate type="float" unit="1/d" scales="global">
        $(MaximumPeriphytonGrowthRate)
</MaximumPeriphytonGrowthRate>
    <PeriphytonCarryingCapacity type="float" unit="g/m&#178;" scales="global">
$(PeriphytonCarryingCapacity)
    </PeriphytonCarryingCapacity>
    <PeriphytonArrheniusTemperature type="float"
unit="K" scales="global">
        $(PeriphytonArrheniusTemperature)
    </PeriphytonArrheniusTemperature>
<InitialLeafLitterDensity type="float" unit="g/m&#178;" scales="global">
        $(InitialLeafLitterDensity)
</InitialLeafLitterDensity>
    <LeafLitterEnergyDensity type="float" unit="J/g" scales="global">
$(LeafLitterEnergyDensity)
    </LeafLitterEnergyDensity>
    <DayOfYearForLitterAddition type="int" unit="d"
scales="global">
        $(DayOfYearForLitterAddition)
    </DayOfYearForLitterAddition>
    <C-PomSettlementRate
type="float" unit="1/d" scales="global">
        $(C-PomSettlementRate)
    </C-PomSettlementRate>
<MaximumVelocityClassForC-PomAddition type="int" scales="global">
        $(MaximumVelocityClassForC-PomAddition)
</MaximumVelocityClassForC-PomAddition>
    <SettlementRateForFPomAndAnimalRemains type="float" unit="1/d"
scales="global">
        $(SettlementRateForFPomAndAnimalRemains)
    </SettlementRateForFPomAndAnimalRemains>
<InitialF-PomDensity type="float" unit="J/m&#178;" scales="global">$(InitialF-PomDensity)</InitialF-PomDensity>
<InitialS-PomDensity type="float" unit="J/m&#178;" scales="global">$(InitialS-PomDensity)</InitialS-PomDensity>
<FractionOfS-PomAvailableToFilterFeeders type="float" unit="1" scales="global">
        $(FractionOfS-
PomAvailableToFilterFeeders)
    </FractionOfS-PomAvailableToFilterFeeders>
    <PeriphytonEnergyDensity type="float"
unit="J/g" scales="global">
        $(PeriphytonEnergyDensity)
    </PeriphytonEnergyDensity>
    <UsePopulationDensity
type="bool" scales="global">$(UsePopulationDensity)</UsePopulationDensity>
    <SavePopulationSize type="bool"
scales="global">$(SavePopulationSize)</SavePopulationSize>
    <SaveTraitSize type="bool"
scales="global">$(SaveTraitSize)</SaveTraitSize>
    <SavePopulationDistribution type="bool" scales="global">
$(SavePopulationDistribution)
    </SavePopulationDistribution>
    <SaveTraitDistribution type="bool"
scales="global">$(SaveTraitDistribution)</SaveTraitDistribution>
    <Biomass scales="global">$(:Biomass)</Biomass>
<StartBiomass scales="global">$(StreamComStartBiomass)</StartBiomass>
    <NumberRuns type="int" unit="1"
scales="global">$(NumberStreamComRuns)</NumberRuns>
    <SaveEnvironmentalConditions type="bool" scales="global">
$(SaveEnvironmentalConditions)
    </SaveEnvironmentalConditions>
    <MinimumPeriphytonDensity type="float"
scales="global" unit="g/m&#178;">
        $(MinimumPeriphytonDensity)
    </MinimumPeriphytonDensity>
<ReproductionSuccessRate type="float" scales="global" unit="1">
        $(ReproductionSuccessRate)
</ReproductionSuccessRate>
    <LeafLitterEntryDensity type="float" scales="global" unit="g/m&#178;">
$(LeafLitterEntryDensity)
    </LeafLitterEntryDensity>
</StreamCom1_StepsRiverNetwork>
```

### Inputs

#### ProcessingPath

The working directory for the module. It is used for all files prepared as module inputs or generated as module outputs.
`ProcessingPath` expects its values to be of type `str`.
Values of the `ProcessingPath` input may not have a physical unit.
Values have to refer to the `global` scale.

#### Reach

The numerical identifier of the reach that is selected for the StreamCom simulation.
`Reach` expects its values to be of type `int`.
Values of the `Reach` input may not have a physical unit.
Values have to refer to the `global` scale.

#### Concentrations

The substance concentrations in water phase.
`Concentrations` expects its values to be of type `ndarray`.
The physical unit of the `Concentrations` input values is `ng/l`.
Values have to refer to the `time/hour, space/base_geometry` scale.

#### Species

The list of species simulated by StreamCom. See the scenario description for the available species.
`Species` expects its values to be of type `list`.
Values of the `Species` input may not have a physical unit.
Values have to refer to the `other/species` scale.

#### DominantRateConstantsForLm

The dominant rate constants for the GUTS functions applied to the simulated species.
`DominantRateConstantsForLm` expects its values to be of type `list`.
The physical unit of the `DominantRateConstantsForLm` input values is `1/d`.
Values have to refer to the `other/species` scale.

#### ThresholdsForLethalEffects

The thresholds for lethal effects for the GUTS functions applied to the simulated species.
`ThresholdsForLethalEffects` expects its values to be of type `list`.
The physical unit of the `ThresholdsForLethalEffects` input values is `ng/l`.
Values have to refer to the `other/species` scale.

#### KillingRates

The killing rates for the GUTS functions applied to the simulated species.
`KillingRates` expects its values to be of type `list`.
The physical unit of the `KillingRates` input values is `l/(ng*d)`.
Values have to refer to the `other/species` scale.

#### SiteInformation

The path to the XML file describing the simulated site.
`SiteInformation` expects its values to be of type `str`.
Values of the `SiteInformation` input may not have a physical unit.
Values have to refer to the `global` scale.

#### SpeciesParameters

The path to the XML file containing the database of species parameters.
`SpeciesParameters` expects its values to be of type `str`.
Values of the `SpeciesParameters` input may not have a physical unit.
Values have to refer to the `global` scale.

#### WaterTemperature

The path to a TSV file containing a time-series of water temperatures.
`WaterTemperature` expects its values to be of type `str`.
Values of the `WaterTemperature` input may not have a physical unit.
Values have to refer to the `global` scale.

#### Site

The name of the site.
`Site` expects its values to be of type `str`.
Values of the `Site` input may not have a physical unit.
Values have to refer to the `global` scale.

#### FirstDay

The first simulated day.
`FirstDay` expects its values to be of type `date`.
Values of the `FirstDay` input may not have a physical unit.
Values have to refer to the `global` scale.

#### LastDay

The last simulated day.
`LastDay` expects its values to be of type `date`.
Values of the `LastDay` input may not have a physical unit.
Values have to refer to the `global` scale.

#### UseSubLethalToxEffects

Specifies whether sub-lethal effects are simulated.
`UseSubLethalToxEffects` expects its values to be of type `bool`.
Values of the `UseSubLethalToxEffects` input may not have a physical unit.
Values have to refer to the `global` scale.

#### ThresholdPopulationSizeForSuperIndividuals

The population size threshold for super-individuals.
`ThresholdPopulationSizeForSuperIndividuals` expects its values to be of type `int`.
The physical unit of the `ThresholdPopulationSizeForSuperIndividuals` input values is `1`.
Values have to refer to the `global` scale.

#### NumberOfSiblingsPerSuperIndividual

The number of siblings per super-individual.
`NumberOfSiblingsPerSuperIndividual` expects its values to be of type `int`.
The physical unit of the `NumberOfSiblingsPerSuperIndividual` input values is `1`.
Values have to refer to the `global` scale.

#### MaximumPeriphytonGrowthRate

The maximum periphyton growth rate.
`MaximumPeriphytonGrowthRate` expects its values to be of type `float`.
The physical unit of the `MaximumPeriphytonGrowthRate` input values is `1/d`.
Values have to refer to the `global` scale.

#### PeriphytonCarryingCapacity

The periphyton carrying capacity.
`PeriphytonCarryingCapacity` expects its values to be of type `float`.
The physical unit of the `PeriphytonCarryingCapacity` input values is `g/m²`.
Values have to refer to the `global` scale.

#### PeriphytonArrheniusTemperature

The periphyton Arrhenius temperature.
`PeriphytonArrheniusTemperature` expects its values to be of type `float`.
The physical unit of the `PeriphytonArrheniusTemperature` input values is `K`.
Values have to refer to the `global` scale.

#### InitialLeafLitterDensity

The initial leaf-litter density.
`InitialLeafLitterDensity` expects its values to be of type `float`.
The physical unit of the `InitialLeafLitterDensity` input values is `g/m²`.
Values have to refer to the `global` scale.

#### LeafLitterEnergyDensity

The energy-density of leaf-litter.
`LeafLitterEnergyDensity` expects its values to be of type `float`.
The physical unit of the `LeafLitterEnergyDensity` input values is `J/g`.
Values have to refer to the `global` scale.

#### DayOfYearForLitterAddition

The day of the year when leaf-litter is added to the stream.
`DayOfYearForLitterAddition` expects its values to be of type `int`.
The physical unit of the `DayOfYearForLitterAddition` input values is `d`.
Values have to refer to the `global` scale.

#### C-PomSettlementRate

The C-Pom settlement rate.
`C-PomSettlementRate` expects its values to be of type `float`.
The physical unit of the `C-PomSettlementRate` input values is `1/d`.
Values have to refer to the `global` scale.

#### MaximumVelocityClassForC-PomAddition

The maximum velocity class for C-Pom additions.
`MaximumVelocityClassForC-PomAddition` expects its values to be of type `int`.
Values of the `MaximumVelocityClassForC-PomAddition` input may not have a physical unit.
Values have to refer to the `global` scale.

#### SettlementRateForFPomAndAnimalRemains

The settlement rate for F-Pom and animal remains.
`SettlementRateForFPomAndAnimalRemains` expects its values to be of type `float`.
The physical unit of the `SettlementRateForFPomAndAnimalRemains` input values is `1/d`.
Values have to refer to the `global` scale.

#### InitialF-PomDensity

The initial F-Pom density.
`InitialF-PomDensity` expects its values to be of type `float`.
The physical unit of the `InitialF-PomDensity` input values is `J/m²`.
Values have to refer to the `global` scale.

#### InitialS-PomDensity

The initial S-Pom density.
`InitialS-PomDensity` expects its values to be of type `float`.
The physical unit of the `InitialS-PomDensity` input values is `J/m²`.
Values have to refer to the `global` scale.

#### FractionOfS-PomAvailableToFilterFeeders

The fraction of S-Pom available to filter-feeders.
`FractionOfS-PomAvailableToFilterFeeders` expects its values to be of type `float`.
The physical unit of the `FractionOfS-PomAvailableToFilterFeeders` input values is `1`.
Values have to refer to the `global` scale.

#### PeriphytonEnergyDensity

The periphyton energy-density.
`PeriphytonEnergyDensity` expects its values to be of type `float`.
The physical unit of the `PeriphytonEnergyDensity` input values is `J/g`.
Values have to refer to the `global` scale.

#### UsePopulationDensity

Specifies whether to use population density.
`UsePopulationDensity` expects its values to be of type `bool`.
Values of the `UsePopulationDensity` input may not have a physical unit.
Values have to refer to the `global` scale.

#### SavePopulationSize

Specifies whether to output the population size.
`SavePopulationSize` expects its values to be of type `bool`.
Values of the `SavePopulationSize` input may not have a physical unit.
Values have to refer to the `global` scale.

#### SaveTraitSize

Specifies whether to output trait size.
`SaveTraitSize` expects its values to be of type `bool`.
Values of the `SaveTraitSize` input may not have a physical unit.
Values have to refer to the `global` scale.

#### SavePopulationDistribution

Specifies whether to output population distributions.
`SavePopulationDistribution` expects its values to be of type `bool`.
Values of the `SavePopulationDistribution` input may not have a physical unit.
Values have to refer to the `global` scale.

#### SaveTraitDistribution

Specifies whether to output trait distributions.
`SaveTraitDistribution` expects its values to be of type `bool`.
Values of the `SaveTraitDistribution` input may not have a physical unit.
Values have to refer to the `global` scale.

#### Biomass

The path to a text file specifying initial biomass.
`Biomass` expects its values to be of type `str`.
Values of the `Biomass` input may not have a physical unit.
Values have to refer to the `global` scale.

#### StartBiomass

Specifies the unit odf initial biomass.
`StartBiomass` expects its values to be of type `str`.
Values of the `StartBiomass` input may not have a physical unit.
Values have to refer to the `global` scale.
Allowed values are: `Ind/m^2`, `g/m^2`.

#### NumberRuns

The number of module-internal Monte Carlo runs.
`NumberRuns` expects its values to be of type `int`.
The physical unit of the `NumberRuns` input values is `1`.
Values have to refer to the `global` scale.

#### SaveEnvironmentalConditions

Specifies whether to output environmental conditions.
`SaveEnvironmentalConditions` expects its values to be of type `bool`.
Values of the `SaveEnvironmentalConditions` input may not have a physical unit.
Values have to refer to the `global` scale.

#### MinimumPeriphytonDensity

The minimum periphyton density.
`MinimumPeriphytonDensity` expects its values to be of type `float`.
The physical unit of the `MinimumPeriphytonDensity` input values is `g/m²`.
Values have to refer to the `global` scale.

#### ReproductionSuccessRate

The rate at which reproduction succeeds.
`ReproductionSuccessRate` expects its values to be of type `float`.
The physical unit of the `ReproductionSuccessRate` input values is `1`.
Values have to refer to the `global` scale.

#### LeafLitterEntryDensity

The density with which litter enters the water body.
`LeafLitterEntryDensity` expects its values to be of type `float`.
The physical unit of the `LeafLitterEntryDensity` input values is `g/m²`.
Values have to refer to the `global` scale.

### Outputs

## Roadmap

The following changes will be part of future `StreamCom` versions:

* Start module GUI in background ([#1](https://github.com/xlandscape/StreamCom-Component/issues/1))
* Placement of StreamCom scenario ([#1](https://github.com/xlandscape/StreamCom-Component/issues/2))

## Contributing

Contributions are welcome. Please contact the authors (see [Contact](#contact)). Also consult the `CONTRIBUTING`
document for more information.

## License

Distributed under the CC0 License. See `LICENSE` for more information.

## Contact

Sascha Bub (component) - sascha.bub@gmx.de
Thorsten Schad (component) - thorsten.schad@bayer.com
Tido Strauß (module) - strauss@gaiac-eco.de
Jana Gerhard (module) - gerhard@gaiac-eco.de

## Acknowledgements

* [NumPy](https://numpy.org)
* [StreamCom](https://gaiac-eco.de/oekotoxikologie/effektmodellierung/)
