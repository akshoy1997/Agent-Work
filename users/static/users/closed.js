const app = document.getElementById('root');

const container = document.createElement('div');
container.setAttribute('class', 'container');

app.appendChild(container);

var request = new XMLHttpRequest();
request.open('GET', 'https://' + window.location.hostname + '/api/leads/', true);
request.onload = function () {

  // Begin accessing JSON data here
  var data = JSON.parse(this.response);
  if (request.status >= 200 && request.status < 400) {
    var count = 0;
    data.forEach(item => {
      if(item.status.toUpperCase() == "CLOSED"){
        const card = document.createElement('div');
        card.setAttribute('class', 'card');

        const h1 = document.createElement('h1');
        h1.textContent =  "Name: " + item.name;

        const p1 = document.createElement('p');
        p1.textContent = `Phone Number: ${item.phone_number}`;

        const p2 = document.createElement('p');
        p2.textContent = `Address: ${item.address}`;

        const p3 = document.createElement('p');
        p3.textContent = `Status: LOST`;

        container.appendChild(card);
        card.appendChild(h1);
        card.appendChild(p1);
        card.appendChild(p2);
        card.appendChild(p3);

        if(item.target){
          const p4 = document.createElement('p');
          p4.textContent = `Target for: ${item.target}`;
          card.appendChild(p4);
        }

        if(item.details){
          const p5 = document.createElement('p');
          p5.textContent = `Lead Details: ${item.details}`;
          card.appendChild(p5);
        }

        count++;
      }
    });
  } else {
    const errorMessage = document.createElement('marquee');
    errorMessage.textContent = `Gah, it's not working!`;
    app.appendChild(errorMessage);
  }
  if(count==0){
    const card = document.createElement('div');
    card.setAttribute('class', 'card');
    const h = document.createElement('h1');
    h.textContent = `No Leads Found!`;
    container.appendChild(card);
    card.appendChild(h);
  }
}

request.send();