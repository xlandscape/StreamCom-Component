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
version of this document is from 2021-10-13.  

### Built with
* Landscape Model core version 1.9
* STREAM-com version 2.0.21 


## Getting Started
The component can be used in any Landscape Model based on core version 1.9 or newer. See the Landscape
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
<ProcessingPath>$(_MCS_BASE_DIR_)\$(_MC_NAME_)\processing\effect\com_steps_1</ProcessingPath>
    <Reaches>
<FromOutput component="StepsRiverNetwork" output="Reaches" />
    </Reaches>
    <Reach
type="int">$(StreamComReach1)</Reach>
    <Concentrations>
        <FromOutput component="StepsRiverNetwork"
output="PEC_SW" />
    </Concentrations>
    <Species type="list[str]"
scales="other/species">$(Species1)|$(Species2)|$(Species3)</Species>
    <DominantRateConstantsForLm type="list[float]"
scales="other/species" unit="1/d">
        $(Species1DominantRateConstantSD) $(Species2DominantRateConstantSD)
$(Species3DominantRateConstantSD)
    </DominantRateConstantsForLm>
    <ThresholdsForLethalEffects type="list[float]"
scales="other/species" unit="ng/l">
        $(Species1ThresholdConcentrationSD) $(Species2ThresholdConcentrationSD)
$(Species3ThresholdConcentrationSD)
    </ThresholdsForLethalEffects>
    <KillingRates type="list[float]"
scales="other/species" unit="l/(ng*h)">
        $(Species1KillingRateSD) $(Species2KillingRateSD)
$(Species3KillingRateSD)
    </KillingRates>
    <SiteInformation>$(:SiteInformation)</SiteInformation>
<SpeciesParameters>$(:SpeciesParameters)</SpeciesParameters>
<WaterTemperature>$(:WaterTemperature)</WaterTemperature>
    <Site>Niers_Peutenweg</Site>
    <FirstDay
type="date">$(SimulationStart)</FirstDay>
    <LastDay type="date">$(SimulationEnd)</LastDay>
<UseSubLethalToxEffects type="bool">$(UseSubLethalToxEffects)</UseSubLethalToxEffects>
<ThresholdPopulationSizeForSuperIndividuals type="int" unit="1">
        $(ThresholdPopulationSizeForSuperIndividuals)
</ThresholdPopulationSizeForSuperIndividuals>
    <NumberOfSiblingsPerSuperIndividual type="int" unit="1">
$(NumberOfSiblingsPerSuperIndividual)
    </NumberOfSiblingsPerSuperIndividual>
    <MaximumPeriphytonGrowthRate
type="float" unit="1/d">
        $(MaximumPeriphytonGrowthRate)
    </MaximumPeriphytonGrowthRate>
<PeriphytonCarryingCapacity type="float" unit="g/m&#178;">
        $(PeriphytonCarryingCapacity)
</PeriphytonCarryingCapacity>
    <PeriphytonArrheniusTemperature type="float" unit="K">
$(PeriphytonArrheniusTemperature)
    </PeriphytonArrheniusTemperature>
    <InitialLeafLitterDensity type="float"
unit="g/m&#178;">$(InitialLeafLitterDensity)</InitialLeafLitterDensity>
    <LeafLitterEnergyDensity type="float"
unit="J/g">$(LeafLitterEnergyDensity)</LeafLitterEnergyDensity>
    <DayOfYearForLitterAddition type="int"
unit="d">$(DayOfYearForLitterAddition)</DayOfYearForLitterAddition>
    <C-PomSettlementRate type="float"
unit="1/d">$(C-PomSettlementRate)</C-PomSettlementRate>
    <MaximumVelocityClassForC-PomAddition type="int">
$(MaximumVelocityClassForC-PomAddition)
    </MaximumVelocityClassForC-PomAddition>
<SettlementRateForFPomAndAnimalRemains type="float" unit="1/d">
        $(SettlementRateForFPomAndAnimalRemains)
</SettlementRateForFPomAndAnimalRemains>
    <InitialF-PomDensity type="float" unit="J/m&#178;">$(InitialF-
PomDensity)</InitialF-PomDensity>
    <InitialS-PomDensity type="float" unit="J/m&#178;">$(InitialS-
PomDensity)</InitialS-PomDensity>
    <FractionOfS-PomAvailableToFilterFeeders type="float" unit="1">
$(FractionOfS-PomAvailableToFilterFeeders)
    </FractionOfS-PomAvailableToFilterFeeders>
    <PeriphytonEnergyDensity
type="float" unit="J/g">$(PeriphytonEnergyDensity)</PeriphytonEnergyDensity>
    <UsePopulationDensity
type="bool">$(UsePopulationDensity)</UsePopulationDensity>
    <SavePopulationSize
type="bool">$(SavePopulationSize)</SavePopulationSize>
    <SaveTraitSize type="bool">$(SaveTraitSize)</SaveTraitSize>
<SavePopulationDistribution type="bool">$(SavePopulationDistribution)</SavePopulationDistribution>
<SaveTraitDistribution type="bool">$(SaveTraitDistribution)</SaveTraitDistribution>
    <Biomass>$(:Biomass)</Biomass>
<StartBiomass>$(StreamComStartBiomass)</StartBiomass>
    <NumberRuns type="int"
unit="1">$(NumberStreamComRuns)</NumberRuns>
</StreamCom1_StepsRiverNetwork>
```

### Inputs
#### ProcessingPath
The working directory for the module. It is used for all files prepared as module inputs
or generated as module outputs.  
`ProcessingPath` expects its values to be of type `str`.
Values of the `ProcessingPath` input may not have a physical unit.
Values have to refer to the `global` scale.

#### Reaches
The numeric identifiers for individual reaches (in the order of the hydro,logical inputs)
that apply scenario-wide.  
`Reaches` expects its values to be of type `list`.
Values of the `Reaches` input may not have a physical unit.
Values have to refer to the `space/reach` scale.

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
The list of species simulated by StreamCom. See the scenario description for the 
available species.  
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

### Outputs


## Roadmap
The following changes will be part of future `StreamCom` versions:
* Start module GUI in background
([#1](https://gitlab.bayer.com/aqrisk-landscape/streamcom-component/-/issues/1))
* Unknown output: report.txt
([#3](https://gitlab.bayer.com/aqrisk-landscape/streamcom-component/-/issues/3))


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
