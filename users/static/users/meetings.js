const app = document.getElementById('root');

const container = document.createElement('div');
container.setAttribute('class', 'container');

app.appendChild(container);

var request = new XMLHttpRequest();
request.open('GET', 'http://127.0.0.1:8000/api/meetings/?lead_id=' + localStorage["lead_id"], true);
request.onload = function () {

  // Begin accessing JSON data here
  var data = JSON.parse(this.response);
  if (request.status >= 200 && request.status < 400) {
    var count = 0;
    data.forEach(item => {
        const card = document.createElement('div');
        card.setAttribute('class', 'card');

        const h1 = document.createElement('h1');
        h1.textContent =  "Type: " + item.type;

        const p1 = document.createElement('p');
        p1.textContent = `Date: ${item.date}`;

        const p2 = document.createElement('p');
        p2.textContent = `Time: ${item.time}`;

        const p3 = document.createElement('p');
        p3.textContent = `Venue: ${item.venue}`;

        container.appendChild(card);
        card.appendChild(h1);
        card.appendChild(p1);
        card.appendChild(p2);
        card.appendChild(p3);
        count++;
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
    h.textContent = `No Meetings Found!`;
    container.appendChild(card);
    card.appendChild(h);
  }
}

request.send();