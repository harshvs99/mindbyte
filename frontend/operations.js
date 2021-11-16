function side_open(){
            if(document.getElementById("mySideBar").style.display === "block"){
                document.getElementById("mySideBar").style.display = "none";
                document.getElementById("body").style.display = "none";}
            else
                document.getElementById("mySideBar").style.display = "block";
        }

