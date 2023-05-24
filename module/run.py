import os
import subprocess

# NOTES:
# 0. To run this example script simply type:
#       >> python run.py
# 1. ProjectStreamCom.exe expects the following parameters:
#   --site_name $SITE               # name of the site to simulate (site file in input folder)          (REQUIRED)
#   --num_mc $NUM                   # number of monte carlo simulations to run                          (REQUIRED)
#   --sim_duration $DURATION        # duration of a single mc simulation in days                        (REQUIRED)
#   --input_path $INPUT             # path to input files                                               (REQUIRED)
#   --output_path $OUTPUT           # path to output folder                                             (REQUIRED)
#   --species $SPECIES_LIST         # names of species to include in simulation (comma separated list)  (REQUIRED)
#   --start_biomass $METHOD         # initial biomass method                                            (REQUIRED) 
#   --tox_name $TOX                 # name of tox to use in simulation (tox file in input folder)       (optional, no toxicity assumed if parameter isn't used)
# 2. Valid sites names are: site_vichtbach.txt
# 3. Valid species names are: "Gammarus fossarum, Asellus aquaticus, Cloeon dipterum" (species names MUST NOT contain commas)
# 4. Valid tox names are: tox_Deltamethrin_day.txt
# 5. Valid start_biomass methods are: Ind/m^2, g/m^2
# 6. Input_path, output_path need to be passed as absolute paths
# 7. Needed input files are: exposure.txt, spec.xml, temp.txt, biomass.txt (, site_X.txt, tox_Y.txt)


exe_path = "../ProjectStreamCom.exe"

site_name = "site_vichtbach.txt"                  
num_monte_carlo = 1                                              
sim_duration = 3650                                      
input_path = "../input"                            
output_path = "../output"                               
tox_name = "tox_Deltamethrin.txt"                      
species = ['Gammarus pulex', 'Asellus aquaticus', 'Cloeon dipterum']
start_biomass = "Ind/m^2"

assert(os.path.isdir(input_path) and os.path.isdir(output_path))

subprocess.call([
    exe_path,
    "--site_name", site_name, 
    "--num_monte_carlo", str(num_monte_carlo), 
    "--sim_duration", str(sim_duration),    
    "--input_path", os.path.abspath(input_path), 
    "--output_path", os.path.abspath(output_path),
    "--species", ','.join(species),
    "--tox_name", tox_name,    
    "--start_biomass", start_biomass,
])
