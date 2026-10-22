data = """manufacturer,year,color,body_type,engine_type,transmission,fuel_type,seating_capacity,kilometers_driven,vehicle_condition,wholesale_price,selling_price,client_name,client_age,client_gender,client_continent,client_country,income_level,client_profession,estimated_income,client_retail_date,season
Honda,2008,LemonChiffon,Hatchback,petrol,manual,hybrid,2,45804.14,inactive,13600,18585,Noah Rhodes,23,Male,Africa,Anguilla,medium,Therapeutic radiographer,2339,2023-07-14,tourism_peak
Toyota,2023,DarkGoldenRod,Van,electric,manual,electric,2,136179.06,active,14271,19751,Jonathan Johnson,61,Male,North America,Antigua and Barbuda,medium,Sports administrator,1009,2021-06-12,tourism_peak
Nissan,2017,LightSeaGreen,Sedan,diesel,manual,gasoline,5,109721.94,active,10886,16088,Abigail Shaffer,69,Female,North America,Cyprus,medium,"Librarian, public",2624,2025-01-05,normal
Toyota,2008,MediumSlateBlue,Sedan,electric,manual,diesel,2,75261.29,inactive,14152,19877,James Howard,31,Female,Europe,Cape Verde,medium,Trade mark attorney,2646,2023-01-09,normal
Honda,2020,Salmon,SUV,petrol,automatic,gasoline,6,245150.24,active,19784,22440,Valerie Gray,51,Female,Europe,Sri Lanka,medium,Water engineer,1997,2021-07-24,tourism_peak
Honda,2012,CornflowerBlue,SUV,petrol,automatic,diesel,7,43599.95,inactive,13921,16667,Darren Roberts,21,Male,Europe,Morocco,medium,"Exhibitions officer, museum/gallery",1349,2022-10-30,normal
Hyundai,2011,SaddleBrown,Hatchback,hybrid,automatic,gasoline,2,131092.4,active,13485,15895,Holly Wood,21,Male,Africa,Hong Kong,medium,"Geologist, engineering",2055,2023-07-23,tourism_peak
Hyundai,2013,White,Hatchback,electric,manual,electric,6,188418.49,inactive,13736,18589,Carla Gray,42,Male,Africa,New Caledonia,medium,"Journalist, broadcasting",2797,2022-08-25,tourism_peak
Toyota,2021,Maroon,Hatchback,electric,manual,gasoline,4,256647.52,inactive,17323,22999,Austin Gentry,20,Female,Africa,Denmark,medium,"Engineer, petroleum",2957,2021-06-19,tourism_peak
Honda,2004,DarkTurquoise,Sedan,hybrid,automatic,diesel,4,72806.27,inactive,13229,15733,David Hoffman,59,Female,North America,Indonesia,medium,Television/film/video producer,2121,2025-02-04,normal
Nissan,2016,PaleGoldenRod,Van,hybrid,automatic,diesel,3,59241.34,inactive,15853,18719,Zachary Taylor,39,Female,North America,Ukraine,medium,"Chemist, analytical",2342,2026-02-26,normal
Nissan,2019,DeepSkyBlue,SUV,petrol,automatic,gasoline,8,219775.48,active,15979,20682,Rebecca Henderson,24,Male,Africa,Tokelau,medium,Musician,1130,2022-02-15,normal
Toyota,2008,Wheat,Sedan,hybrid,automatic,gasoline,8,39750.19,active,18119,23417,Juan Dunlap,47,Male,North America,Nepal,medium,Software engineer,2412,2025-03-05,normal
Honda,2003,DarkOliveGreen,Sedan,hybrid,automatic,hybrid,7,166851.76,inactive,20246,23940,Christopher Smith,66,Female,Europe,Seychelles,medium,"Restaurant manager, fast food",1928,2024-02-01,normal
Hyundai,2020,Lime,Truck,diesel,automatic,hybrid,2,123069.98,active,17770,21966,Katie Gonzalez,33,Female,Asia,Madagascar,medium,"Designer, television/film set",2114,2022-02-05,normal
Honda,2013,AliceBlue,Van,electric,manual,gasoline,6,212084.21,inactive,14032,19452,Katherine Rodriguez,38,Female,South America,Zimbabwe,medium,Information systems manager,1532,2025-09-14,normal
Nissan,2019,Cyan,SUV,diesel,manual,gasoline,6,146108.69,active,16699,20053,John Jones,52,Male,Asia,Azerbaijan,medium,"Conservation officer, historic buildings",1926,2023-03-30,normal
Toyota,2010,FireBrick,Van,petrol,automatic,hybrid,3,36806.87,inactive,17316,21758,Shane Henderson,30,Male,North America,Yemen,medium,"Solicitor, Scotland",2407,2025-11-14,holiday_sales
Toyota,2022,PaleGoldenRod,SUV,electric,manual,electric,5,114966.17,inactive,10596,16417,Marie Kim DDS,36,Male,Asia,Rwanda,medium,Firefighter,1803,2023-11-05,holiday_sales
Honda,2012,Beige,SUV,hybrid,manual,diesel,3,62385.81,active,21324,24090,Crystal Robinson,43,Male,Asia,Bahrain,medium,Barrister's clerk,2752,2024-01-26,normal
Hyundai,2019,MediumPurple,SUV,diesel,automatic,electric,5,3466.36,inactive,13182,18026,David Caldwell,66,Male,Asia,Bangladesh,medium,"Solicitor, Scotland",1475,2021-06-17,tourism_peak
Hyundai,2017,Sienna,Truck,petrol,manual,electric,7,237687.94,active,18341,22087,John Russell,48,Male,Asia,Saint Kitts and Nevis,medium,Chief Strategy Officer,2203,2026-01-19,normal
Honda,2016,PaleVioletRed,Sedan,hybrid,automatic,gasoline,8,103674.47,inactive,16249,21186,Nicholas Nunez,62,Male,North America,Guinea,medium,"Biochemist, clinical",1765,2024-10-18,normal
Honda,2000,DarkMagenta,Van,electric,manual,diesel,2,238943.69,inactive,14468,20288,Connor West,56,Female,North America,Saint Lucia,medium,"Education officer, museum",1448,2024-01-30,normal
Honda,2025,Crimson,SUV,diesel,automatic,gasoline,7,209815.03,active,18280,22038,Scott Pierce,41,Male,Europe,Kyrgyz Republic,medium,"Sound technician, broadcasting/film/video",2869,2023-04-27,normal
Honda,2015,FireBrick,Hatchback,petrol,automatic,diesel,8,251946.04,inactive,17983,20930,John Hancock,23,Male,Africa,Bermuda,medium,"Development worker, international aid",2676,2023-03-16,normal
Nissan,2014,LightGray,Van,diesel,manual,hybrid,5,98293.7,active,19751,24573,Rachel Mitchell,64,Female,North America,Afghanistan,medium,"Designer, fashion/clothing",2319,2024-07-06,tourism_peak
Hyundai,2013,Chartreuse,SUV,petrol,automatic,gasoline,8,290189.59,inactive,15099,18787,Kimberly Adkins,66,Male,Asia,French Polynesia,medium,Arts administrator,1138,2023-01-17,normal
Toyota,2015,Wheat,Van,electric,manual,gasoline,6,170973.42,inactive,12988,15804,Tyler Miller,60,Male,South America,Lesotho,medium,Broadcast presenter,1259,2025-06-21,tourism_peak
Hyundai,2012,PaleGreen,Van,electric,manual,diesel,8,7783.44,active,13231,18075,Steve Sanchez,44,Male,South America,Bangladesh,medium,Water quality scientist,2915,2023-03-12,normal
"""

with open(r"c:\Users\user\Documents\Year 3\ML\vehicle_ml_dashboard\dummy_data\vehicles_data_1000.csv", "w", encoding="utf-8", newline="") as f:
    f.write(data.lstrip())

print("Done - wrote", len(data.strip().split("\n")) - 1, "rows")
