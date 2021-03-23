# se-02-team-29
SE Sprint 02, Team 29

Contributors: Nodirbek Ibragimov, Ankit Karn

## Instructions:
1. Clone the repository:
```git clone https://github.com/lorenzorota/se-02-team-29.git``` 
2. Go to SE folder
3. Make sure you have python3, pip3, django installed
4. Install dependencies:
  ```
     pip3 install django-filter
     pip3 install matplotlib
     pip3 install pandas
     pip3 install mpld3 
 ```
5. Start django project:
```python3 manage.py runserver```
6. For logging as instructor, use credentials: 
   email: ```nodib7034@gmail.com```
   password: ```nodir1234```
   
   For logging as admin, use credentials: 
   email:```nodirbek@gmail.com```
   password: ```manager```


## Improvements made in sprint 2:

1. In 'beergame' folder React app contained no functionality, we decided React unnecessary for the app and deleted the folder.
2. In 'SE' folder we noticed that the previous sprint team used both Sqlite and Mysql for managing DB, we decided to focus on using Sqlite for this sprint. We left sql commands in Sprint 1 folder, in case the next sprint decides to switch to Mysql.
3. Due to the usage of templates and Django in this codebase and almost no progress made on it, we added some features from our previous work of sprint 1.
## Features added on this sprint:
### Features from previous sprint work:
- unit tests 
- register/logging in for instructor
- registration for student
- game and instructor models
- templates for instructor, game and student apps
- Instructor dashboard
### Features from current sprint work:
- added freeze/unfreeze game functionality on instructor dashboard
- added enter game with email and game_id for players/students
- extended game, student and instructor model 
- added template for game-page: a split game screen is created with all the features according to the documentation provided. It consist of 4 screens: 1st one is order input screen, 2nd one is past information about their positions, 3rd one is status information of other chain members, and 4th one is plot and settings screen. 
- added template for about page
- updated .gitignore file for .py files
- updated supplystatistics.py, demand plotting script, with django project with necessary libraries for plotting. Since, no data were fetched, the plot is empty for the moment.


We are not sure how player.py can be used, so we leave as it is to next sprint team.

## Improvements made in sprint 1
### Web platform:
- Folder labeled as "SE" is the Django framework used to create the server side of the beer game. For better understanding regarding this file, please refer to the comments which can be found in the "readme" file provided in the folder with instructions on how to run the code. 
- Folder labeled as "beergame" containing work for the Frontend React.js interface.
- Folder labeled as "Sprint 1" contains information regarding the SQL(creating,clearing, checking and populating).
- Using the "mysql" file provided by Django framework, one can include all the "create tables" command in the file create_tables.sql. This allows our Django web platform to interact with the tables and store values in the tables like a database. This requires additional installations such as "pip install mysql".
- There are comments on the code suggesting improvement not implemented due to a shortage of time.
- Test cases for the Django web interface were provided in the SE/player/test.py. However, these test cases do not function yet as the table functionality provided by Django is not implemented yet.

## Testing
In SE directory run the command:  
```
python manage.py test
```
If you want to run a subset of your tests you can do so by specifying the full dot path to the package(s), module, TestCase subclass:

Run the specified module
```
python3 manage.py test instructor.tests
```
Run the specified module
```
python3 manage.py test instructor.tests.test_models
```
Run the specified class
```
python3 manage.py test instructor.tests.test_models.YourTestClass
```
You might find this [guide](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing) on testing Django projects helpful.

### Ideas for additional tests:
- Once a player is logged_in, it should be tested if plots can be accessed. 
- In addition, test if the different screens are available for the player. This can be done by checking if the different html pages can be rendered.
- In the "active_in game check" file, test cases were created in order to check which player is active in which game. This is also helpful for the "player_index.html" as all the active games are to be shown instead of sample "Game #" number.

All the above changes are towards the web platform. Now we have also included requirements files and creating entity functions:
- The main functions for the player entity can be found in the "player.py" file regarding role,demand, shipment, inventory.
- Furthermore, a simple layout for the user interface was added to the "user interface file" providing the 4 screen divisions and simple interaction between them.
- Regarding the plots required for Screen 3,a file labeled as "supplychainstatics.py" was created using the "matplotlib.pyplot" library provided by Python in order to create plots for the different player entities (Retailer,Distributor, Wholesaler,Factory)
- Furthermore, two files labeled as "Node.js Tests" and "Node.js Tests role" were created that generate test cases using Node modules available for testing: Mocha and Chai.

## Acknowledgements
1. [Django project from sprint 1 team 30](https://github.com/lorenzorota/se-01-team-30)

