# se-01-team-29
SE Sprint 01, Team 29

Looking at the documentation provided for implementation, there seems to be no backend system to store the data into a database. Therefore, an important improvement on the current design seems to be necessary by providing an ER diagram ("improved documentation folder") for the beer game using the information provided in the documentation such as the UML diagram. To access and edit the ER diagram use the link https://app.diagrams.net/#Hlorenzorota%2Fse-01-team-29%2Fmain%2FER_Diagram%20edit and authenticate using your github. 

Improvement made till: March 09
Web platform:
- Folder labeled as "SE" is the Django framework used to create the server side of the beer game. For better understanding regarding this file, please refer to the comments which can be found in the "readme" file provided in the folder with instructions on how to run the code. 
- Folder labeled as "beergame" containing work for the Frontend React.js interface.
- Folder labeled as "Sprint 1" contains information regarding the SQL(creating,clearing, checking and populating).
- Using the "mysql" file provided by Django framework, one can include all the "create tables" command in the file create_tables.sql. This allows our Django web platform to interact with the tables and store values in the tables like a database. This requires additional installations such as "pip install mysql".
- There are comments on the code suggesting improvement not implemented due to a shortage of time.
- Test cases for the Django web interface were provided in the SE/player/test.py. However, these test cases do not function yet as the table functionality provided by Django is not implemented yet.


Regarding the created tests:
- One would be testing if the user enters as a player or an instructor. This is saved in the boolean variable in the registration form.
- A second test was added in the "player/test.py" file. It tests whether the player is looged_in currently as no session_variables are created. We were only checking if the logged_in.html page is rendered or not. Suggestion: later this should be changed to a session variable.

Additional tests should be:
- Once a player is logged_in, it should be tested if plots can be accessed. 
- In addition, test if the different screens are available for the player. This can be done by checking if the different html pages can be rendered.
- In the "active_in game check" file, test cases were created in order to check which player is active in which game. This is also helpful for the "player_index.html" as all the   active games are to be shown instead of sample "Game #" number.

All the above changes are towards the web platform. Now we have also included requirements files and creating entity functions:
- The main functions for the player entity can be found in the "player.py" file regarding role,demand, shipment, inventory.
- Furthermore, a simple layout for the user interface was added to the "user interface file" providing the 4 screen divisions and simple interaction between them.
- Regarding the plots required for Screen 3,a file labeled as "supplychainstatics.py" was created using the "matplotlib.pyplot" library provided by Python in order to create plots for the different player entities (Retailer,Distributor, Wholesaler,Factory)
- Furthermore, two files labeled as "Node.js Tests" and "Node.js Tests role" were created that generate test cases using Node modules available for testing: Mocha and Chai.

Finally, we added migrations (communications with an sqlite3 database) using the Python "manage.py makemigrations". In addition, some instructions would be to run python "manage.py migrate" library to apply all (create the tables) and to store all the data. To continue, run the command "python manage.py shell" and by using that it makes it possible to add new inputs like: 

                                 from player.models import player;
                                 p = player(id = 1, name='Hamlet', role='distributor', demand=20,cost='10',inventory='5');
                                 p.save();

To check the above added details, please refer to the test using "player.objects.all()" which returns the number of objects found in the set.
All migrations are saved in the "0001.inital file" that can be found in the "player/migrations".
