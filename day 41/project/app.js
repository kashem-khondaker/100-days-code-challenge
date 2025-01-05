fetch("https://jsonplaceholder.typicode.com/users")
  .then((response) => response.json())
  .then((data) => {
    // aikane ami data pabo
    displayData(data);
    // console.log(data);
  })
  .catch((err) => {
    console.log(err);
  });

const displayData = (data) => {
  for (const element of data) {
    // console.log(data);
    // console.log(element.company.name);
    // console.log(element);

    const container = document.getElementById("user-data-container");
    // console.log(container);
  }

  //   alternative
  data.forEach((element) => {
    // console.log(element);
    const container = document.getElementById("user-data-container");
    const div = document.createElement("div");
    div.classList.add("data-container");
    div.innerHTML = `
    
    <img src="${element.name}" alt="${element.name}">
    <h1>${element.name}</h1>
    <p>${element.email}</p>
    <p>${element.address}</p>
    <button>${element.address.street}</button>
    
    `;
    console.log(div);
    container.appendChild(div);
  });
};
