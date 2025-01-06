fetch("https://fakestoreapi.com/products")
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
  //   alternative
  data.forEach((data) => {
    // console.log(data);
    const container = document.getElementById("user-data-container");
    const div = document.createElement("div");
    div.classList.add("data-container");

    const div2 = document.createElement("div");
    div2.classList.add("img-container");
    div2.innerHTML = `
    <img class="img" src="${data.image}" alt="${data.title.slice(0, 5)}">
    `;

    const div3 = document.createElement("div");
    div3.classList.add("cart-info");
    div3.innerHTML = `
    <h1>${data.title}</h1>
    <p>${data.email}</p>
    <p> price : ${data.price}</p>
    <p>${data.category}</p>
    <button>details</button>
    <button>add to cart</button>
    `;

    const cart_div = document.createElement("div");
    cart_div.classList.add("cart-container");
    cart_div.innerHTML = `
    <p>add to cart</p>
    <button></button>
    `;

    div.appendChild(div2);
    div.appendChild(div3);
    container.appendChild(div);
    container.appendChild(cart_div);
  });
};
