$(document).ready(function () {

    $("#sign_in_form").submit(function(event) {
        
        event.preventDefault()
        console.log("submit");

        var user_login = {
            "user_name": $("#username_input").val().trim(),
            "password": $("#password_input").val().trim()
        }

        $.ajax({
            type: "POST",
            url: "/login",
            dataType : "json",
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify(user_login),
            success: function () {
                console.log("post successfully!");
            },
            error: function(request, status, error){
                console.log("Error");
                console.log(request)
                console.log(status)
                console.log(error)
            }
        }); 
    });
});