#Proposed structure of the project: 
```
PRIM/
-----api/
-----data/
----------processed/
---------------20151017/
----------raw/
---------------20151017/
requirement.txt
serer.py
```
####DESCRIPTION:
**api/**
everything relates to api services.

**data/**
store data files

**data/processed/**
store processed files in seperate folders, folder name is in format: YYYYMMDD

**data/raw/**
store raw data files, directly downloaded from Meteo France, in seperate folders, folder name is in format: YYYYMMDD

#API:
Use Flask framework
##How to run the code
####Install tools and libraries
You need to install pip, python, git, npm
> sudo apt-get install python-pip python-dev npm

Enter the directory of the project, and continue to:
Install all the necessary Python libraries:

>pip install -r requirements.txt

#### Run the API server and static server
Run the API server:
> python server.py

Then go to [localhost](http://localhost:5000) to use the website !

####Tool to play with ReST services
Install the useful tool httpie from https://github.com/jakubroztocil/httpie
Exemple: 
>http GET 127.0.0.1:5000/wind/speed/point/38/-8/"2015-10-17 18:00:00"/"2015-10-17 19:00:00"

NOTE: the ReST services might return an errof if it is requested using the address bar from web browser

####To run the script for processing data
>./script.sh date_du_run

Ex: ./script.sh 20151211
Note: for the moment, the data is stored at the same level with this script
###For more details on API services, please read the Wiki

