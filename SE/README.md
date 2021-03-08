March 09:

We are using Django framwork for this section of the Software project Devel- opment. Django is a python framwork that is used to create a interactive web service

To install the Django framwork you need to use pip3 install functional to down- load python programs. Run command
pip3 install Django

Now to start or create a project using Django, type in the command :
"/django-admin startproject SE"

If the above command doesn’t work, you may have to provide the exact path to django-admin. To find the where the file is used on the terminal.

A great advantage of using Django is that it allows the programming to use python logic regarding the if statements and classes to render the page according. A simple example is isitchristmas.com where the entire page is render over the date check.

To be able to run the Django project on your local machine after a git clone of the project you can use the commmand :
"python3 manage runserver" to initialize the Django manager program which will allow you to navigate the website.

There are additional css files created in the static folder "user SE/server/templates/server/syles.css". These are stactics files which Django interprets them in the same way. 
The test are created in the tests.py file provided by Django. This can be used to create objects for each type of class. This was done for the players in the player app(folder).

In addition below you can find some links to test once the server is running on your computer using first "source newenv/bin/activate" and then run "python3 manage.py runserver". There would be an output of the localhost ip and port 8000 using those credential open the following links:

- http://127.0.0.1:8000/ -> here you can also view registration.html
- http://127.0.0.1:8000/create.html
- http://127.0.0.1:8000/player/
- http://127.0.0.1:8000/player/logged_in.html -> this has to be changed to actually view the inventory , backlog , button to demand plots etc.
