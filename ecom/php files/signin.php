<?php

session_start();
error_reporting(~E_ALL & ~E_NOTICE);

if(isset($_POST['signin'])){
    header("Location:cart.php");

// Set connection variables
    $server = "localhost";
    $username = "root";
    $password = "";

    // Create a database connection
    $con = mysqli_connect($server, $username, $password);
    $select_db=mysqli_select_db($con,'dbName');
$select_db=mysqli_select_db($con,'store');


    // Check for connection success
    if(!$con){
        die("connection to this database failed due to" . mysqli_connect_error());
    }
    
    echo "Success connecting to the db";
    
    

    
      

    // Collect post variables
    $cid=$_POST['cid'];
    
    $fname = $_POST['fname'];
    $lname = $_POST['lname'];
    $adress = $_POST['adress'];
    $phoneno = $_POST['phoneno'];
    $email= $_POST['email'];
    $cust_password = $_POST['cust_password'];
    $sql = "INSERT INTO customer( cid,fname,lname,adress,phoneno,email, cust_password) VALUES ('$cid','$fname',  '$lname','$adress', '$phoneno', '$email', '$cust_password')";
    // echo $sql;
    $result = mysqli_query($con,$sql);
    // Execute the query
    if($con->query($sql) == true){
        echo "Successfully inserted";

        // Flag for successful insertion
        $insert = true;
    }
    else{
        echo "ERROR: $sql <br> $con->error";
    }

    // Close the database connection
    $con->close();
}

?>
<style>
    *{
    margin: 0px;
    padding: 0px;
    box-sizing: border-box;
}


.container{
    max-width:70%;
    
    padding:34px;
    margin:auto;
}
.container p ,h3{
    text-align: center;
    font-size: 50px;
    
}
input, textarea,select,label{
    
    
    width: 50%;
    margin:9px auto;
    padding:10px ;
    font-size: 18px;

    



}
form{
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;


}

.btn{
    color: white;
    background: purple;
    padding: 8px 12px;
    font-size: 20px;
    border: 2px solid white;
    border-radius: 14px;
    cursor: pointer;
}
.bg{
    width: 100%;
    position: absolute;
    z-index: -1;
    opacity: 0.6;
}
</style>

    

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ONLINE RETAIL SHOP</title>
    <link href="https://fonts.googleapis.com/css?family=Roboto|Sriracha&display=swap" rel="stylesheet">
    
</head>
<body>
    <img class="bg" src="bg.jpg" alt="Onlineretailshop">
    
    <div class="container">
        <h3>Welcome to our shop</h3>
    
        
        
    
        
   
        <form action="signin.php" method="post">
        
 
           
           <input type="number" name="cid" id="cid" placeholder="Enter your user id">
           
            <input type="text" name="fname" id="fname" placeholder="Enter your first name">
              <input type="text" name="lname" id="lname" placeholder="Enter your last name">
              <input type="text" name="adress" id="adress" placeholder="Enter your adress">
          
            <input type="phoneno" name="phoneno" id="phoneno" placeholder="Enter your phoneno">
            <input type="email" name="email" id="email" placeholder="Enter your email">
            <input type="cust_password" name="cust_password" id="cust_password" placeholder="Enter your password">
            
            
            
     
            <button class="btn" name="signin" value="signin">Submit</button> 
     
    
   
			
			
        </form>
        


    </div>
    <script src="index.js"></script>
    <script>
    if ( window.history.replaceState ) {
        window.history.replaceState( null, null, window.location.href );
    }

    
    
</body>
</html>
