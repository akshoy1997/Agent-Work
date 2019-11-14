const app = document.getElementById('root');

const container = document.createElement('div');
container.setAttribute('class', 'container');

app.appendChild(container);

var request = new XMLHttpRequest();
request.open('GET', 'https://' + window.location.hostname + '/api/meetings/?lead_id=' + localStorage["lead_id"], true);
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

        container.appendChild(card);
        card.appendChild(h1);
        if(item.date){
          const p1 = document.createElement('p');
          p1.textContent = `Date: ${item.date}`;
          card.appendChild(p1);
        }

        if(item.time){
          const p2 = document.createElement('p');
          p2.textContent = `Time: ${item.time}`;
          card.appendChild(p2);
        }

        if(item.follow_up_date){
          const p4 = document.createElement('p');
          p4.textContent = `Follow-Up Date: ${item.follow_up_date}`;
          card.appendChild(p4);
        }

        if(item.status){
          const p5 = document.createElement('p');
          p5.textContent = `Lead Status: ${item.status}`;
          card.appendChild(p5);
        }

        if(item.details){
          const p6 = document.createElement('p');
          p6.textContent = `Meeting Details: ${item.details}`;
          card.appendChild(p6);
        }
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