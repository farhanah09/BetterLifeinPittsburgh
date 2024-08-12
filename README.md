<a href="https://app.commanddash.io/agent?github=https://github.com/farhanah09/BetterLifeinPittsburgh"><img src="https://img.shields.io/badge/AI-Code%20Gen-EB9FDA"></a>

# Better Life In Pittsburgh

This is an innovative application designed specifically for students to find housing in Pittsburgh. With the increasing demand for student accommodation in Pittsburgh, this aims to simplify the process of finding and securing suitable housing for students in the area. 

The application provides students with a provides information such as the crime statistics and the displays the distance from each campus. 

This application currrently uses websites such Rockwell, Walnut Capital and RentCollegePads.com to populate the database.


## Installation

1) First ensure that these packages are installed in order for smooth running of the application.

The packages getting installed are- 
beautifulsoup4==4.11.2
numpy==1.23.4
pandas==1.5.1
pandasgui==0.2.14
Pillow==9.4.0
pyscreenshot==3.0
requests==2.28.1
tkinter==8.6

```bash
pip install -r requirements.txt
```

2) All the paths of the CSV files and images mentioned in the code are relative, meaning it should work as they are in the same folder. 

However, in case it doesn't work, do change the addresses to the path of the particular file on the system it is being installed on. 

3) Run the file named "RUN_ME.py" in the folder.

```bash
python RUN_ME.py
```

## Features 

This application currently offers two ways of displaying information to the user. 

1) Live scraping. 
2) Stored database

In the stored database, we are able to provide the map of the properties and which universities are in the radius of the selected university. 

This also has an option of analyzing crime statistics of the neighborhoods in Pittsburgh to enable the students to make a more informed decision of their housing situation.

The crime statistics and the location of the houses have been analyzed and plotted using ArcGIS pro. 

## Limitations

This application currently has a limited number of houses on its database as currently the wensites for housing allow scraping of only a particular number of houses. 

This application also currently, does not have an interactive GUI and doesn't enable a user to click on the property to see it's details. 

## Authors

1) Keyi Chai 
2) Farhan Ahmad
3) Luyi Sun
4) Harish Balaji 
5) Yikun Yang

## More information

For more information on the working of the code do follow this youtube link in which two of our developer explain the code and how it runs!

Link - https://youtu.be/hGN2BHYrhno

## Appendix

The sites used for the housing database are- 
1) https://rockwelrealty.com/
2) https://www.walnutcapital.com/
3) https://www.rentcollegepads.com/off-campus-housing/carnegie-mellon/search

The site used for crime stastistics- 

https://data.wprdc.org/dataset/arrest-data/resource/e03a89dd-134a-4ee8-a2bd-62c40aeebc6f?view_id=a9e7e08a-9433-4263-8d1d-820002b48353
