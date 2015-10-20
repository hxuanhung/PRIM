#Proposed structure of storing files: 
```
PRIM/
-----api/
-----data/
----------processed/
---------------20151017/
----------raw/
---------------20151017/
-----grib2/
requirement.txt
serer.py
```
--------------------------------------------
#DESCRIPTION:
**api/**
everything relates to api services.

**data/**
store data files

**data/processed/**
store processed files in seperate folders, folder name is in format: YYYYMMDD

**data/raw/**
store raw data files, directly downloaded from Meteo France, in seperate folders, folder name is in format: YYYYMMDD

**grib2/**
code for processing raw data files in grib2 format

---------------------------------------------
#API:
Use Flask framework
##How to run the code
###Install tools and libraries
You need to install pip, python, git, npm
> sudo apt-get install python-pip python-dev npm

Enter the directory of the project, and continue to:
Install all the necessary Python libraries:

>pip install -r requirements.txt

### Run the API server and static server
Run the API server:
> python server.py

Then go to [localhost](http://localhost:5000) to use the website !


