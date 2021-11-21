// Author: Harshvardhan Singh (harshvardhans3@kpmg.com)
// Get requests and table populating
function httpGet(theUrl) {
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

function append_json_projects(){
    let choice = "projects" // choice - projects, people, pipeline
    let hitServer = "http://1ea8-203-92-61-66.ngrok.io";
    let hitString = hitServer+"/operations?choice="+choice;
    let data = JSON.parse(httpGet(hitString));

    var table = document.getElementById('projects-table');
    data.forEach(
        function(object){
            var tr = document.createElement('tr');
            tr.className = "mdc-data-table__header-row";
            tr.innerHTML = 
                    '<th class="mdc-data-table__cell" scope="row">'+ object.clientname + '</th>' +
                    '<th class="mdc-data-table__cell" scope="row">'+ object.projectname+'</th>' +
                    '<td class="mdc-data-table__cell mdc-data-table__cell--numeric">'+ (object.startdate).replace('00:00:00 GMT','') +'</td>'+
                    '<td class="mdc-data-table__cell mdc-data-table__cell--numeric">'+ (object.enddate).replace('00:00:00 GMT','') +'</td>'+
                    '<td class="mdc-data-table__cell">'+ object.skillsrequired +'</td>'+
                    '<td class="mdc-data-table__cell">'+ object.status+'</td>';
                    table.append(tr);
        });
}

function append_json_people(){
    let choice = "people" // choice - projects, people, pipeline
    let hitServer = "http://1ea8-203-92-61-66.ngrok.io";
    let hitString = hitServer+"/operations?choice="+choice;
    let data = JSON.parse(httpGet(hitString));

    var table = document.getElementById('people-table');
    data.forEach(
        function(object){
            var tr = document.createElement('tr');
            tr.className = "mdc-data-table__header-row";
            tr.innerHTML = 
                    '<th class="mdc-data-table__cell" scope="row">'+ object.name + '</th>' +
                    '<th class="mdc-data-table__cell" scope="row">'+ object.role+'</th>' +
                    '<td class="mdc-data-table__cell">'+ object.designation +'</td>'+
                    '<td class="mdc-data-table__cell">'+ object.skill+'</td>'+
                    '<td class="mdc-data-table__cell">'+ object.project+'</td>';
            table.append(tr);
        });
}

function append_json_pipeline(){
    let choice = "pipeline" // choice - projects, people, pipeline
    let hitServer = "http://1ea8-203-92-61-66.ngrok.io";
    let hitString = hitServer+"/operations?choice="+choice;
    let data = JSON.parse(httpGet(hitString));

    var table = document.getElementById('pipeline-table');
    data.forEach(
        function(object){
            var tr = document.createElement('tr');
            tr.className = "mdc-data-table__header-row";
            tr.innerHTML = 
                    '<th class="mdc-data-table__cell" scope="row">'+ object.clientname + '</th>' +
                    '<th class="mdc-data-table__cell" scope="row">'+ object.projectname+'</th>' +
                    '<td class="mdc-data-table__cell mdc-data-table__cell--numeric">'+ (object.startdate).replace('00:00:00 GMT','') +'</td>'+
                    '<td class="mdc-data-table__cell mdc-data-table__cell--numeric">'+ (object.enddate).replace('00:00:00 GMT','') +'</td>'+
                    '<td class="mdc-data-table__cell">'+ object.skillsrequired +'</td>'+
                    '<td class="mdc-data-table__cell">'+ object.status+'</td>';
                    table.append(tr);
        });
}