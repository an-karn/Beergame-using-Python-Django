March 09:
We are using Django framwork for this section of the Software project Devel- opment. Django is a python framwork that is used to create a interactive web service

To install the Django framwork you need to use pip3 install functional to down- load python programs. Run command
pip3 install Django

Now to start or create a project using Django, type in the command :
/django-admin startproject SE

If the above command doesn’t you may have to provide the exact path to django-admin. To find the where the file is use
on the terminal.

A great advantage of using Django is that it allows the programming to use python logic if statements and classes to render the page according. An simple example is isitchristmas.com where the entire page is render over the date check.

To be able to run the Django project on your local machine after an git clone of the project you can use the commmand :
python3 manage runserver 
to initialize the Django manager program this will allow you to navigate the website. Currently the python logic checks for an exten eg http://127.0.0.1:8000/server/registration.php if the end ends with an .html or .php there should be a page given to the user however is a string is provided there is just and example page.

There are additional css files created in the static folder unser SE/server/templates/server/syles.css these are stactics files and Django can interpret them in the same way. 

The test are created in the tests.py file provided by Django. This can be used to create objects for each type of class. This was done for the players in the player app(folder).
