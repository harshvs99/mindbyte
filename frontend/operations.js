// Author: Harshvardhan Singh (harshvardhans3@kpmg.com)
// Get requests and table populating
function httpGet(theUrl){
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", theUrl, false); // false for synchronous request
    xmlHttp.send(null);
    return xmlHttp.responseText;
}

function side_open(){
            if(document.getElementById("mySideBar").style.display === "block"){
                document.getElementById("mySideBar").style.display = "none";
                document.getElementById("body").style.display = "none";}
            else
                document.getElementById("mySideBar").style.display = "block";
        }

function append_json(choice){
    let hitServer = "http://127.0.0.1:6003";
    let hitString = hitServer+"/operations?choice="+choice;
    // choice - projects, people, pipeline
    const data = JSON.parse(httpGet(hitString));
    console.log(data)
    alert("Get data")
    var table = document.getElementById('gable');
            data.forEach(function(object) {
                var tr = document.createElement('tr');
                tr.innerHTML = '<td>' + object.name + '</td>' +
                '<td>' + object.startdate + '</td>' +
                '<td>' + object.enddate + '</td>' +
                '<td>' + object.status + '</td>';
                table.appendChild(tr);
            });

}