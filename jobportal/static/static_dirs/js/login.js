/* login form validation */
function validateLogin() {
var emaidid, atpos, dotpos, password, passwordLength;

emailid = document.loginform.email.value;
atpos = emailid.indexOf('@');
dotpos = emailid.lastIndexOf('.');
password = document.loginform.password.value;
passwordLength = password.length;

if(emailid == null || emailid == '') {
document.getElementById('errors').innerHTML = "Email id do not empty!";
document.loginform.email.focus();
return false;
}

if(atpos < 1 || dotpos < atpos+2 || dotpos+2 >= emailid.length) {
document.getElementById('errors').innerHTML = "It's not a valid email address!";
document.loginform.email.focus();
return false;
}

if(password == null || password == '') {
document.getElementById('errors').innerHTML = "Password do not empty!";
document.loginform.password.focus();
return false;
}

if(passwordLength < 6 ) {
document.getElementById('errors').innerHTML = "Password Wrong!";
document.loginform.password.focus();
return false;
}
}

/* register form validation */
function validateRegister() {
var emaidid, atpos, dotpos, password, passwordMatch, username;


username = document.registerform.username.value;
password = document.registerform.password.value;
passwordMatch = document.registerform.cpassword.value;

emailid = document.registerform.email.value;
atpos = emailid.indexOf('@');
dotpos = emailid.lastIndexOf('.');

if (username == null || username == '') {
document.getElementById('registererrors').innerHTML = 'Username do not empty!';
document.registerform.username.focus();
return false;
}
if(username.length < 6 ) {
document.getElementById('registererrors').innerHTML = "Username do not short!";
document.registerform.username.focus();
return false;
}

if(password == null || password == '') {
document.getElementById('registererrors').innerHTML = "Password do not empty!";
document.registerform.password.focus();
return false;
}

if(password.length < 6 ) {
document.getElementById('registererrors').innerHTML = "Password do not short!";
document.registerform.password.focus();
return false;
}

if(password.length != passwordMatch.length) {
document.getElementById('registererrors').innerHTML = "Password do not match!";
document.registerform.cpassword.focus();
return false;
}

if(emailid == null || emailid == '') {
document.getElementById('registererrors').innerHTML = "Email id do not empty!";
document.registerform.email.focus();
return false;
}

if(atpos < 1 || dotpos < atpos+2 || dotpos+2 >= emailid.length) {
document.getElementById('registererrors').innerHTML = "It's not a valid email address!";
document.registerform.email.focus();
return false;
}

}


$(document).ready(function(){

var formInputs = $('input[type="email"], input[type="password"], input[type="text"');
formInputs.focus(function() {
$(this).parent().children(".formLabel").addClass("active");
});
formInputs.focusout(function() {
if($(this).val().length == 0) {
$(this).parent().children(".formLabel").removeClass("active");
}
});

/* tab code */
$(".formCtlWrapper a").click(function() {
var tabId = $(this).attr('data-tab');
$(".formCtlWrapper a").removeClass("active");
$(".formBlock").removeClass("active");
$(this).addClass("active");
$("#"+tabId).addClass("active");
});

});