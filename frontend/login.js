// Author: Harshvardhan Singh (harshvardhans3@kpmg.com)
// Demo login form to demonstrate API functions to team

var loggedIn = {};

function httpGet(theUrl){
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", theUrl, false); // false for synchronous request
    xmlHttp.send(null);
    return xmlHttp.responseText;
}

function validate(){
    var username = document.getElementById("user").value;
    var password = document.getElementById("password").value;
    var hitString = "http://127.0.0.1:6003/login?user="+username+"&password="+password
    console.log(hitString)
    const retObj = JSON.parse(httpGet(hitString));
    console.log(retObj);
    console.log(retObj["login"]);
    if(retObj["login"] == "authenticated"){
        alert("Welcome "+retObj["user_display_name"]);
        loggedIn[retObj["user_display_name"]] = retObj["token"];
        localStorage.setItem(retObj["user_display_name"], retObj["token"]);
    }
    else{
        alert(retObj["errorMessage"]);
    }
    window.location = "login.html"; 
}

