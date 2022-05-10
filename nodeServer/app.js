var http = require('http'); 
const fs = require('fs');
const port = 3000;

//create web server
var server = http.createServer(function (req, res) {   
    
    if (req.url == '/') {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        fs.readFile('./template/index.html', function(error,data){
            if (error){
                res.writeHead(404);
                res.write('Error: File Not Found');
            } else {
                res.write(data);
            }
        })
    }

    else if (req.url == '/data') {
    
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.write(JSON.stringify({ message: "Hello World"}));  
        res.end();  
    }

    else if (req.url == "/admin") {
        
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.write('<html><body><p>This is admin Page.</p></body></html>');
        res.end();
    
    }
    
    else
        res.end('Invalid Request!');

});

server.listen(port, function(error){
    if (error){
        console.log("something went wrong", error)
    } else {
        console.log("Server is listening on the port " + port + ", http://localhost:"+ port +"/" )
    }
});
