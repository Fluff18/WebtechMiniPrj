<?php
    //Extract the parameters sent by the client
    //IN this case, only one - USN
    extract($_POST);
    
    
    if($usn !=' ')
    {
        echo ";";
        $servername = "localhost";
        $username = "newuser";
        $password = "password";
        $dbname = "login";

        // Create connection
        $conn = new mysqli($servername, $username, $password, $dbname);
        // Check connection
        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        }

        $sql = "INSERT INTO search2 (user,data)
        VALUES ('".$usn."','".$data."')";

        if ($conn->query($sql) === TRUE) {
            echo "New record created successfully";
        } else {
            echo "Error: " . $sql . "<br>" . $conn->error;
        }
        header("Access-Control-Allow-Origin: *");
        //header("Location: http://localhost:8090/search",true);
        $conn->close();

    
    }

    
    

?>