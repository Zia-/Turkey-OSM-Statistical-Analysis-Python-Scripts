# Turkey-OSM-Statistical-Analysis-Python-Scripts.
A guide about how Planet OSM dump file was processed using Python scripts for the scientific article, entitled: "Analysing growth and governing factors of Turkey OpenStreetMap dataset".

Kindly follow the following steps:

1. The Planet dump file, dated Sep. 2015, was downloaded from [here](http://planet.openstreetmap.org/planet/full-history/).

2. A PostGIS enabled PostgreSQL database was already up and running on Linux OS (v 14.01) for data import. Find details about [how to setup PostgreSQL (PostGIS) on Linux OS](http://trac.osgeo.org/postgis/wiki/UsersWikiPostGIS21UbuntuPGSQL93Apt).

3. Osm-history-splitter was installed from [here](https://github.com/MaZderMind/osm-history-splitter).

4. Its [README.md](https://github.com/MaZderMind/osm-history-splitter/blob/master/README.md) was used to crop down the Planet dump file to our desired regions, i.e. 81 provinces of Turkey.

5. Three PostgreSQL databases were setup, namely, Point, Edge, and Polygon; with 81 schemas (s1, s2, s3, .... s86, s87).

6. [README.md](https://github.com/MaZderMind/osm-history-splitter/blob/master/README.md) was again used to import 81 provinces data into the database and simple SQL queries were used to select Point, Edge, and Polygon features, thus, dumping each one of them to its corresponding schema.

7. Finally, each schema table was further sub-divided into 18 time slices (tables) using valid_from column values in SQL editor. The selected time intervals were like this: 01/04/2004-01/04/2007 (named: april_seven), 01/04/2007-01/09/2007 (sep_seven), 01/09/2007-01/04/2008 (april_eight) ..... 01/09/2014-01/04/2015 (april_fifteen), 01/04/2015-01/09/2015 (sep_fifteen).

8. Also turkey province shapefile was uploaded in order to calculate provincal area in public schema.

9. The final database structure was like this:

| Database | Schema | Table | Database | Schema | Table  | Database | Schema | Table  |
| -------- |:------:| -----:| -------- |:------:| ------:| -------- |:------:| ------:|
| Point    | public | turkey_province | Edge    | public | turkey_province | Polygon    | public | turkey_province |
|          | s1     |   april_seven   |         |   s1   |   april_seven   |            |    s1  |   april_seven   |
|          |        |    sep_seven    |         |        |    sep_seven    |            |        |    sep_seven    | 
|          |        |    april_eight  |         |        |    april_eight  |            |        |    april_eight  |
|          |        |    sep_eight    |         |        |    sep_eight    |            |        |    sep_eight    | 
|          |        |    april_nine   |         |        |    april_nine   |            |        |    april_nine   |
|          |        |    sep_nine     |         |        |    sep_nine     |            |        |    sep_nine     | 
|          |        |    april_ten    |         |        |    april_ten    |            |        |    april_ten    | 
|          |        |    sep_ten      |         |        |    sep_ten      |            |        |    sep_ten      | 
|          |        |    april_eleven |         |        |    april_eleven |            |        |    april_eleven | 
|          |        |    sep_eleven   |         |        |    sep_eleven   |            |        |    sep_eleven   | 
|          |        |    april_twelve |         |        |    april_twelve |            |        |    april_twelve |    
|          |        |    sep_twelve   |         |        |    sep_twelve   |            |        |    sep_twelve   |    
|          |        |   april_thirteen|         |        |   april_thirteen|            |        |   april_thirteen|  
|          |        |    sep_thirteen |         |        |    sep_thirteen |            |        |    sep_thirteen |
|          |        |   april_fourteen|         |        |   april_fourteen|            |        |   april_fourteen|  
|          |        |    sep_fourteen |         |        |    sep_fourteen |            |        |    sep_fourteen |     
|          |        |    april_fifteen|         |        |    april_fifteen|            |        |    april_fifteen|  
|          |        |    sep_fifteen  |         |        |    sep_fifteen  |            |        |    sep_fifteen  |    
|          | s2     |   april_seven   |         |   s2   |   april_seven   |            |    s2  |   april_seven   |
|          |        |    sep_seven    |         |        |    sep_seven    |            |        |    sep_seven    | 
|          |        |    april_eight  |         |        |    april_eight  |            |        |    april_eight  |
|          |        |    sep_eight    |         |        |    sep_eight    |            |        |    sep_eight    | 
|          |        |    april_nine   |         |        |    april_nine   |            |        |    april_nine   |
|          |        |    sep_nine     |         |        |    sep_nine     |            |        |    sep_nine     | 
|          |        |    april_ten    |         |        |    april_ten    |            |        |    april_ten    | 
|          |        |    sep_ten      |         |        |    sep_ten      |            |        |    sep_ten      | 
|          |        |    april_eleven |         |        |    april_eleven |            |        |    april_eleven | 
|          |        |    sep_eleven   |         |        |    sep_eleven   |            |        |    sep_eleven   | 
|          |        |    april_twelve |         |        |    april_twelve |            |        |    april_twelve |    
|          |        |    sep_twelve   |         |        |    sep_twelve   |            |        |    sep_twelve   |    
|          |        |   april_thirteen|         |        |   april_thirteen|            |        |   april_thirteen|  
|          |        |    sep_thirteen |         |        |    sep_thirteen |            |        |    sep_thirteen |
|          |        |   april_fourteen|         |        |   april_fourteen|            |        |   april_fourteen|  
|          |        |    sep_fourteen |         |        |    sep_fourteen |            |        |    sep_fourteen |     
|          |        |    april_fifteen|         |        |    april_fifteen|            |        |    april_fifteen|  
|          |        |    sep_fifteen  |         |        |    sep_fifteen  |            |        |    sep_fifteen  |
|          |    -   |                 |         |    -   |                 |            |   -    |                 | 
|          |    -   |                 |         |    -   |                 |            |   -    |                 |
|          |    -   |                 |         |    -   |                 |            |   -    |                 |
|          | s86    |   april_seven   |         |   s86  |   april_seven   |            |    s86 |   april_seven   |
|          |        |    sep_seven    |         |        |    sep_seven    |            |        |    sep_seven    | 
|          |        |    april_eight  |         |        |    april_eight  |            |        |    april_eight  |
|          |        |    sep_eight    |         |        |    sep_eight    |            |        |    sep_eight    | 
|          |        |    april_nine   |         |        |    april_nine   |            |        |    april_nine   |
|          |        |    sep_nine     |         |        |    sep_nine     |            |        |    sep_nine     | 
|          |        |    april_ten    |         |        |    april_ten    |            |        |    april_ten    | 
|          |        |    sep_ten      |         |        |    sep_ten      |            |        |    sep_ten      | 
|          |        |    april_eleven |         |        |    april_eleven |            |        |    april_eleven | 
|          |        |    sep_eleven   |         |        |    sep_eleven   |            |        |    sep_eleven   | 
|          |        |    april_twelve |         |        |    april_twelve |            |        |    april_twelve |    
|          |        |    sep_twelve   |         |        |    sep_twelve   |            |        |    sep_twelve   |    
|          |        |   april_thirteen|         |        |   april_thirteen|            |        |   april_thirteen|  
|          |        |    sep_thirteen |         |        |    sep_thirteen |            |        |    sep_thirteen |
|          |        |   april_fourteen|         |        |   april_fourteen|            |        |   april_fourteen|  
|          |        |    sep_fourteen |         |        |    sep_fourteen |            |        |    sep_fourteen |     
|          |        |    april_fifteen|         |        |    april_fifteen|            |        |    april_fifteen|  
|          |        |    sep_fifteen  |         |        |    sep_fifteen  |            |        |    sep_fifteen  |
|          | s87    |   april_seven   |         |   s87  |   april_seven   |            |    s87 |   april_seven   |
|          |        |    sep_seven    |         |        |    sep_seven    |            |        |    sep_seven    | 
|          |        |    april_eight  |         |        |    april_eight  |            |        |    april_eight  |
|          |        |    sep_eight    |         |        |    sep_eight    |            |        |    sep_eight    | 
|          |        |    april_nine   |         |        |    april_nine   |            |        |    april_nine   |
|          |        |    sep_nine     |         |        |    sep_nine     |            |        |    sep_nine     | 
|          |        |    april_ten    |         |        |    april_ten    |            |        |    april_ten    | 
|          |        |    sep_ten      |         |        |    sep_ten      |            |        |    sep_ten      | 
|          |        |    april_eleven |         |        |    april_eleven |            |        |    april_eleven | 
|          |        |    sep_eleven   |         |        |    sep_eleven   |            |        |    sep_eleven   | 
|          |        |    april_twelve |         |        |    april_twelve |            |        |    april_twelve |    
|          |        |    sep_twelve   |         |        |    sep_twelve   |            |        |    sep_twelve   |    
|          |        |   april_thirteen|         |        |   april_thirteen|            |        |   april_thirteen|  
|          |        |    sep_thirteen |         |        |    sep_thirteen |            |        |    sep_thirteen |
|          |        |   april_fourteen|         |        |   april_fourteen|            |        |   april_fourteen|  
|          |        |    sep_fourteen |         |        |    sep_fourteen |            |        |    sep_fourteen |     
|          |        |    april_fifteen|         |        |    april_fifteen|            |        |    april_fifteen|  
|          |        |    sep_fifteen  |         |        |    sep_fifteen  |            |        |    sep_fifteen  |

10. Now "script_number_of_nodes_per_feature.py", "script_number_of_nodes_per_feature_by_particular_user.py", and "script_degree_of_street_junctions.py" were executed to generate data for graphical analysis.
