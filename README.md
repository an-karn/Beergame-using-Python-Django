# se-01-team-29
SE Sprint 01, Team 29

Looking at the documentation provided for implementation, there seems to be no backend system to store the data into a database. Therefore an important improvement on the current designs seems to be necessary by providing an ER diagram for the beer game using the information provided in the documentation such as the UML diagram. To access and edit the ER diagram use the link https://app.diagrams.net/#Hlorenzorota%2Fse-01-team-29%2Fmain%2FER_Diagram%20edit and authenticate using your github. 

Improvement made till : March 09
Web platform:
- Folder labeled as "SE" is the Django framework used to create the server side of the beer game. For better understanding regarding this file, please refer to the comments which can be found in the "readme" file provided in the folder with instructions on how to run the code. 
- Folder labeled as "beergame" containing work for the Frontend React.js interface.
- Using the "sqlite" file provided by Django framework, one can include all the "create tables" command in the file ctreate_tables.sql. This allows our Django web platform to interact with the tables and store values in the tables like a database. 
- There are comments on the code suggesting improvement not implemented due to a shortage of time. In addition, taking into consideration that half of the given time for this assignment was spent on learning how to use Django for the web service the implementation could not be efficiently done.


All the above changes RE towards the web platform. Now we have also included requirements files and creating entity functions :
- The main functions for the player entity can be found in the "player.py" file regarding role,demand, order, inventory.
- Furthermore, a simple layout for the user interface was added to the "user interface file" providing the 4 screen divisions and simple interaction between them.
- Regarding the plots required for Screen 3,a file labeled as "supplychainstatics.py" was created using the "matplotlib.pyplot" library provided by Python in order to create plots for the different player entities (Retailer,Distributor, Wholesaler,Factory)

 
