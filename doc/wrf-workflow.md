# The modularity


![image](img/WRF-flowchart.png)

WPS (preprocessing) programs to be run every simulation
- ungrib.exe
- metgrid.exe
- 
WRF programs to be run every simulation
- real.exe
- wrf.exe

## Automatise this!

1. **download script**

1. **script_WPS**

   a. find dates/times to be used
   
   a. find downloaded files

   a. start **run_ungrib.sh**
      - insert correct dates into a "namelist"
      - run **ungrib.exe**
      
   a. start **run_metgrid.sh**
      - insert correct dates into a "namelist"
      - run **metgrid.exe**

   a. start next script **script_WRF**
   
1. **scipt_WRF**

   a. find output from the last script
   
   a. run ./run_real.sh
      - insert correct dates into a "namelist"
      - run **real.exe**

   a. run ./run_wrf.sh
      - insert correct dates into a "namelist"
      - run **wrf.exe**

   a. run ./analysis_script.sh
     

```plantuml



```
