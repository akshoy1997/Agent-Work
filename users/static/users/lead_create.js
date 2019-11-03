function check(event) {
    event.preventDefault();
    const url = "https://127.0.0.1/api/leads/";
    console.log(url);
    const data = {
        "name" : document.getElementById('name').value,
        'phone_number' : document.getElementById('phone_number').value,
        'address' : document.getElementById('address').value,
        'status' : "ONGOING"
        };
    const other_params = {
        headers : { "content-type" : "application/json; charset=UTF-8"},
        body : data,
        method : "POST",
        mode : "cors"
    };

    fetch(url, other_params)
        .then(function(response) {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error("Could not reach the API: " + response.statusText);
        }
    }).then(function(data) {
        document.getElementById("message").innerHTML = data.encoded;
    }).catch(function(error) {
        document.getElementById("message").innerHTML = error.message;
    });
}
