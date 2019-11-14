const app = document.getElementById('root');

const container = document.createElement('div');
container.setAttribute('class', 'container');

app.appendChild(container);

function storeID(value){
  localStorage["lead_id"] = value;
}

var request = new XMLHttpRequest();
request.open('GET', 'http://127.0.0.1:8000/api/leads/', true);
request.onload = function () {

  // Begin accessing JSON data here
  var data = JSON.parse(this.response);
  if (request.status >= 200 && request.status < 400) {
    var count = 0;
    data.forEach(item => {
      if(item.status.toUpperCase() == "ONGOING"){
        const card = document.createElement('div');
        card.setAttribute('class', 'card');

        const h1 = document.createElement('h1');
        h1.textContent =  "Name: " + item.name;

        const p1 = document.createElement('p');
        p1.textContent = `Phone Number: ${item.phone_number}`;

        const p2 = document.createElement('p');
        p2.textContent = `Address: ${item.address}`;

        const p3 = document.createElement('p');
        p3.textContent = `Status: ${item.status}`;

        const A = document.createElement('a');
        A.setAttribute('href', "lead/status_update/");

        const Btn = document.createElement('button');
        Btn.setAttribute('class', 'submit status_update');
        Btn.setAttribute('onClick', `storeID(${item.id})`);
        Btn.textContent = "Change Status";

        const a = document.createElement('a');
        a.setAttribute('href', "meetings/");

        const btn = document.createElement('button');
        btn.setAttribute('class', 'submit meeting');
        btn.setAttribute('onClick', `storeID(${item.id})`);
        btn.textContent = "View Meetings";

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

        card.appendChild(a);
        a.appendChild(btn);
        card.appendChild(A);
        A.appendChild(Btn);
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