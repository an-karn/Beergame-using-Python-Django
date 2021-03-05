<?php
    if(!isset($_COOKIE['is_auth'])):
        header("Location: ./admin_login.php?status=sign_in_required");
    endif;
    $servername = "localhost";
    $db_user = "group7";
    $db_pass = "KVSzuH";
    $db_name = "group7";
    $conn = mysqli_connect($servername, $db_user, $db_pass, $db_name);
    // Check connection
    if (!$conn) {
        die("Connection failed: " . mysqli_connect_error());
    }
?>
<!DOCTYPE html>
<html lang="en">
    <h1>Welcome to the beer Game</h1>
    <p id = "Miscellanous_p">
        The Beer Game is used to simulate the supply chain concept in Economics
    </p>
    <p>
        To continue please login.
    </p>
    
    <div id = "login_part">
    <form action="registration.php" method="POST">
                <div class="container">
                    <div class="row">
                        <div class="col-sm-3">
                            <h2>Registration</h2>
                            <p>Please fill out details to add to the sub_account table</p>
                            <div>
                                <label for="firstname">Firstname</label>
                                <input class = "form-control" name="firstname" type="text">
                            </div>
                            <div>
                                <label for="lastname">Lastname</label>
                                <input class = "form-control" name="lastname" type="text">
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
                            </div>
                            <input name = 'create' type="submit" class = "buttons" value="Register"></input>
                            <div>
                                <?php
                                    if(isset($_POST['create'])){
                                        if(!$_POST['email']){
                                            $error.="<br/>please Enter Your Email";	
                                        }
                                                    
                                        if(!$_POST['sub_pass']){
                                            $error.="<br/>please Enter Your Password";
                                        }
                                                                
                                        else {
                                            if (strlen($_POST['sub_pass'])<8){
                                                $error.="<br/>please Enter long Password";
                                            }
                                        }
                                        if (isset($error)) {
                                            echo "There Were error(s) In Your Signup Details :" .$error;	
                                        } 
                                        else {
                                                include('config.php');
                                                if($results) echo "Email is already registered ,, Do you want log In ";
                                            else {
                                                $email = $_POST['email'];
                                                $user_name = $_POST['user_name'];
                                                $password = $_POST['sub_pass'];
                                                $query ="INSERT INTO subs_account(email,username,sub_pass) VALUES ('".mysqli_real_escape_string($conn,$email)."','$user_name', '$password');";
                                                if (mysqli_query($conn, $query)) {
                                                    echo "New record created successfully";
                                                } else {
                                                    echo "Error: " . $sql . "<br>" . mysqli_error($conn);
                                                }
                                            }
                                        }
                                    }
                                ?>
                            </div>
                        </div>
                    </div>
                </div>
            </form>
</html>