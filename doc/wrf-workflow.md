# The modularity


![image](img/WRF-flowchart.png)

WPS (preprocessing) programs to be run every simulation
- ungrib.exe
- metgrid.exe

WRF programs to be run every simulation
- real.exe
- wrf.exe

## WRF source code github

Look at file tree for a feeling of modules.

- Interesting directories related to the codes:
    - dyn_em/
    - phys/
<https://github.com/wrf-model/WRF>

- Below is some module dependencies in the physics section of the code

![image](img/WRF-flowchart.png)
*Source: <https://opensky.ucar.edu/islandora/object/opensky:2898>*


## Automatise this!

1. **download script**

    - download large-scale weather data

1. **script_WPS**

   - find dates/times to be used
   
   - find downloaded files

   - start **run_ungrib.sh**
      - insert correct dates into a "namelist"
      - run **ungrib.exe**
      
    - start **run_metgrid.sh**
      - insert correct dates into a "namelist"
      - run **metgrid.exe**

   - start next script **script_WRF**
   
1. **script_WRF**

   - find output from the last script
   
   - run ./run_real.sh
      - insert correct dates into a "namelist"
      - run **real.exe**

   - run ./run_wrf.sh
      - insert correct dates into a "namelist"
      - run **wrf.exe**

   - run ./analysis_script.sh
      - inserts correct time
      - runs a python script that plots some graphs
     
     

