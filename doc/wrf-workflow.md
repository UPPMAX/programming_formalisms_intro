# The modularity of WRF weather model


## WRF (ARW) source code github

Look at file tree for a feeling of modules. <https://github.com/wrf-model/WRF>

- Interesting directories related to the codes:
    - dyn_em/
    - phys/

- Below is some module dependencies in the physics section of the code

![image](img/wrf-physics.PNG)

*Source: <https://opensky.ucar.edu/islandora/object/opensky:2898>*

## The WRF suite with flow chart

![image](img/WRF-flowchart.png)

WPS (preprocessing) programs to be run every simulation
- ungrib.exe
- metgrid.exe

WRF programs to be run every simulation
- real.exe
- wrf.exe


## Personal workflow script of different parts

Script 

```mermaid
flowchart LR
    Download --> Preprocess --> Development --> Test --> D["Deployment and maintenance"] --> Requirements



```

### Workflow consisting of several bash scripts. 

1. **download script**

    - download large-scale weather data

1. **script_WPS**

   - find dates/times to be used
   
   - find downloaded files

   - start **run_ungrib.sh**
      - insert correct dates into a "namelist"
      - run **ungrib.exe** (Fortran)
      
    - start **run_metgrid.sh**
      - insert correct dates into a "namelist"
      - run **metgrid.exe** (Fortran)

   - start next script **script_WRF**
   
1. **script_WRF**

   - find output from the last script
   
   - run ./run_real.sh
      - insert correct dates into a "namelist"
      - run **real.exe** (Fortran)

   - run ./run_wrf.sh
      - insert correct dates into a "namelist"
      - run **wrf.exe** (Fortran)

   - run ./analysis_script.sh
      - inserts correct time
      - runs a python script that plots some graphs
     
     

