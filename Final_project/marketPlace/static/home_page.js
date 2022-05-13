function submit_signin_Form(){
    $("#sign_in_form").submit(function(event) {
        
        event.preventDefault()
        console.log("submit");

        var user_login = {
            "user_name": $("#input-usename").val().trim(),
            "password": $("#input-password").val().trim()
        }

        $.ajax({
            type: "POST",
            url: "login",
            dataType : "json",
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify(user_login),
            success: function (response) {
                console.log("Post successfully!");
                if (response["url"] == 'shop_items'){
                    $('.alert').show()
                    $("#success-notification").empty()
                    $("#success-notification").html("Login Successfully! <a href='" + response["url"] + "'>Go to the Market here!<\a>")
                    $(".form-control").val("")
                    $("#input-name").focus();
                    // $('#sign_in_form').hide()
                } else {
                    $('.alert').show()
                    $("#success-notification").empty()
                    $("#success-notification").html("Login Failed, please check your username and password.")
                    $(".form-control").val("")
                    $("#input-name").focus();
                }
            },
            error: function(request, status, error){
                console.log("Error");
                console.log(request)
                console.log(status)
                console.log(error)
            }
        }); 
    });
}

function submit_signup_Form(){
    $("#sign_up_form").submit(function(event) {
        
        event.preventDefault()
        console.log("submit");

        var user_register = {
            "user_name": $("#input-usename-up").val().trim(),
            "password": $("#input-password-up").val().trim(),
            "email": $("#input-email").val().trim(),
            "ale_id": $("#input-aleid").val().trim()
        }

        $.ajax({
            type: "POST",
            url: "register",
            dataType : "json",
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify(user_register),
            success: function (response) {
                console.log("Post successfully!");
                if (response["url"] == '/'){
                    $('.alert').show()
                    $("#success-notification").empty()
                    $("#success-notification").html("Sign up Successfully! <a href='" + response["url"] + "'>Sign in to access the Market!<\a>")
                    $(".form-control").val("")
                    $("#input-name-up").focus();
                    // $('#sign_up_form').hide()
                } else {
                    console.log('impossible')
                }
            },
            error: function(request, status, error){
                console.log("Error");
                console.log(request)
                console.log(status)
                console.log(error)
            }
        }); 
    });
}

function show_signup(){
    $('#sign_in_form').hide()
    $('#sign_up_form').show()
}

function show_signin(){
    $('#sign_up_form').hide()
    $('#sign_in_form').show()
}


$(document).ready(function () {

    $('.alert').hide()
    $('#sign_up_form').hide()
    $("#go_sign_in").hover(
        function() {
            $(this).addClass("when_hover")
        },
        function() {
            $(this).removeClass("when_hover")
        }
    )
    $("#go_sign_up").hover(
        function() {
            $(this).addClass("when_hover")
        },
        function() {
            $(this).removeClass("when_hover")
        }
    )

});
