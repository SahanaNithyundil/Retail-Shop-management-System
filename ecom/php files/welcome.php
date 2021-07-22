<?php

$server="localhost";
$username="root";
$password="";
$con = mysqli_connect($server,$username,$password);
$select_db=mysqli_select_db($con,'dbName');
$select_db=mysqli_select_db($con,'store');
if(!$con)
{
 die("connection to database failed");   
}
else{
    //echo "successfull";
}
if(isset($_POST['shop'])){
    header("Location:signin.php");
}






?>

<style>
    .bg{
    width: 100%;
    position: absolute;
    z-index: -1;
    opacity: 0.6;
    }
    .btn{
    color: white;
    background: orange;
    padding: 20px 30px;
    font-size: 20px;
    border: 5px solid white;
    border-radius: 30px;
    cursor: pointer;
}
.container p ,h1{
    text-align: center;
    font-size: 50px;
}
    form{
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;


}


</style>




<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ONLINE RETAIL SHOP</title>
    
    
</head>
<body>
<img class="bg" src="w.jpg" alt="onlineretailshop">

    <div class="container">
    
    <h1 style="color:blue";>WELCOME, SHOP TILL YOU DROP!! </h1><br>
    
    <form action="Welcome.php" method="post" >
        
    <button class="btn"name=" shop" value="shop">Click Here To Shop</button><br>
    

    
</body>
</html>