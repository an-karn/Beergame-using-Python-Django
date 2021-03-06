{% extends "server/layout.html"%}
   
{% block body %}
<h1>Welcome to the beer Game</h1>
<p id = "Miscellanous_p">
    Please register yourself here
</p>
<div id = "login_part">
    <form action="registration.php" method="POST">
    {% csrf_token %}
        <div class="container">
            <div class="row">
                <div class="col-sm-3">
                    <h2>Registration</h2>
                        <p>Please fill out details</p>
                        {% csrf_token %}
                        {{ form }}
                        <!-- <div>
                            <label for="firstname">Firstname</label>
                            <input class = "form-control" name="firstname" type="text" required>
                        </div>
                        <div>
                            <label for="lastname">Lastname</label>
                            <input class = "form-control" name="lastname" type="text" required>
                        </div>
                        <div>
                            <label for="email">Email</label>
                            <input class = "form-control" name="email" type="email" required>
                        </div>
                        <div>
                            <label for="username">Username</label>
                            <input class = "form-control" name="user_name" type="text" required>
                        </div>
                        <div>
                            <label for="password">Password</label>
                            <input class = "form-control" name="sub_pass" type="password" required>
                        </div> -->
                        <div>
                        <input name='register' type="submit" class = "buttons" value="Register"></input>
                        </div>
                    </div>
                </div>
            </div>
    </form>
</div>
{% endblock %}