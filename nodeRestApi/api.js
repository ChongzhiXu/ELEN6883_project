const express = require("express");
const app = express();
const port = 3000;

// Enable the api to listening
app.listen(port, function(error){
    if (error){
        console.log("something went wrong", error)
    } else {
        console.log("Api is listening on the port " + port + ", http://localhost:"+ port +"/" )
    }
});

// Render the homepage
app.get("/",(req, res) => {
    // res.send("Hello world");
    // console.log(__dirname)
    res.sendFile(__dirname + "/template/index.html");
});

