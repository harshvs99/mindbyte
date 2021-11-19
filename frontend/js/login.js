// Author: Harshvardhan Singh (harshvardhans3@kpmg.com)
// Demo login form to demonstrate API functions to team

var loggedIn = {};
var varToken= "";

function httpGet(theUrl){
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", theUrl, false); // false for synchronous request
    xmlHttp.send(null);
    return xmlHttp.responseText;
}

function validate(){
    var username = document.getElementById("user").value;
    var password = document.getElementById("password").value;
//    var hitServer = "http://127.0.0.1:6003"
    var hitServer = "http://1ea8-203-92-61-66.ngrok.io";
    var hitString = hitServer+"/login?username="+username+"&password="+password;
    const retObj = JSON.parse(httpGet(hitString));
//    console.log(retObj);
//    alert(retObj["login"]);
    if(retObj["login"] == "authenticated"){
//        alert("Welcome "+retObj["user_display_name"]);
        loggedIn[retObj["user_display_name"]] = retObj["token"];
        localStorage.setItem(retObj["user_display_name"], retObj["token"]);
//        window.location = "operations.html"; 
    }
    else{
        alert(retObj["errorMessage"]);
    }
    
}
