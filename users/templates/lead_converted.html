<!DOCTYPE html>
<html lang="en">
<head>

    <!-- Required meta tags -->
    <meta charset="utf-8">
    <!-- Chrome, Firefox OS and Opera -->
    <meta name="theme-color" content="#3367D6">
    <!-- Windows Phone -->
    <meta name="msapplication-navbutton-color" content="#3367D6">
    <!-- iOS Safari -->
    <meta name="apple-mobile-web-app-status-bar-style" content="#3367D6">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- icon in the highest resolution we need it for -->
    <link rel="icon" sizes="192x192" href="../static/users/images/icons-192.png">

    <!-- reuse same icon for Safari -->
    <link rel="apple-touch-icon" href="../static/users/images/icons-192.png">

    <!-- multiple icons for IE -->
    <meta name="msapplication-square310x310logo" content="../static/users/images/icons-192.png">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <!-- Custom CSS -->
    {% load static %}
    <link href="{% static "users/style.css" %}" rel="stylesheet">

    <!--Manifest.json-->
    <link rel="manifest" href="{% static "users/manifest.json" %}" rel="manifest">

    <title>Update Status</title>

</head>
<body>
    {% block content %}
    <div class="topnav">
        <a href="#">
            {% if request.user.is_authenticated %}
                Welcome '{{ request.user.username }}', Manage your Work Here!
            {% endif %}
        </a>
        <a style="float: right;" href="{% url 'logout' %}">Logout</a>
        <a style="float: right;" href="{% url 'converted' %}">Closed</a>
        <a style="float: right;" href="{% url 'home' %}">In Progress</a>
    </div>
    <div class="card form login">
        <form>
            {% csrf_token %}
            <h1 class="title border-bottom mb-4">Mark Lead As Converted</h1>

            <label for="registered">Registered Phone Numbers</label>
            <textarea type="textarea" rows="4" id="registered" name="registered"></textarea>
            <span class="alerts" id="registered-alert" style="display: none;">*This field can't be empty</span> 

            <label for="details">More Details</label>
            <textarea type="textarea" rows="4" id="details" name="details"></textarea>

            <input onClick="check()" class="submit" value="Submit" readonly>
        </form>
        <div style="display:none;" id="message"></div>   
    </div>
    {% endblock %}
    {% load static %}
    <script>
        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = cookies[i].trim();
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        function check(event) {
            const url1 = "https://vendor-django-app.herokuapp.com/api/leads/" + localStorage["lead_id"] + "/";
            const url2 = "https://vendor-django-app.herokuapp.com/api/lead_history/";
            var count = 0;
            const data1 = {
                "status" : "CONVERTED",
            };
            const data2 = {
                "lead" : localStorage["lead_id"],
                "status" : "CONVERTED",
                "registered_phone_nos" : document.getElementById('registered').value,
                "more_details" : document.getElementById('details').value
            };
            if(document.getElementById('registered').value == ""){
                document.getElementById('registered-alert').style.display = 'block';
            }
            else{
                document.getElementById('registered-alert').style.display = 'none';
                count+=1;
            }
            if(count==1){
                fetch(url1, {
                method: "PATCH",
                credentials: "same-origin",
                headers: {
                    "X-CSRFToken" : getCookie('csrftoken'),
                    "Accept": "application/json",
                    "Content-Type": "application/json; charset=UTF-8"
                },
                body: JSON.stringify(data1)
                }).then(function(response) {
                    if (response.ok) {
                        return response.json();
                    } else {
                        throw new Error("Could not reach the API: " + response.statusText);
                    }
                }).then(function(data1) {
                    document.getElementById("message").innerHTML = data1.encoded;
                }).catch(function(error) {
                    document.getElementById("message").innerHTML = error.message;
                    alert(error);
                });
                console.log(data1.encoded);
                fetch(url2, {
                method: "POST",
                credentials: "same-origin",
                headers: {
                    "X-CSRFToken" : getCookie('csrftoken'),
                    "Accept": "application/json",
                    "Content-Type": "application/json; charset=UTF-8"
                },
                body: JSON.stringify(data2)
                }).then(function(response) {
                    if (response.ok) {
                        return response.json();
                    } else {
                        throw new Error("Could not reach the API: " + response.statusText);
                    }
                }).then(function(data2) {
                    document.getElementById("message").innerHTML = data2.encoded;
                    window.location = "https://vendor-django-app.herokuapp.com/home/";
                }).catch(function(error) {
                    document.getElementById("message").innerHTML = error.message;
                    alert(error);
                });
            } 
        }
    </script>
    <script>
        var serviceWorkerPath = "/serviceworker.js";
        var charchaServiceWorker = registerServiceWorker(serviceWorkerPath);
        function registerServiceWorker(serviceWorkerPath){
            if('serviceWorker' in navigator){
            navigator.serviceWorker
                .register(serviceWorkerPath)
                .then(
                    function(reg){
                    console.log('service worker registered');
                    }
                ).catch(function(error){
                    console.log(error)
                });
            }
        }
    </script>
</body>
</html>