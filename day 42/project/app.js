fetch("https://fakestoreapi.com/products")
  .then((res) => res.json())
  .then((data) => {
    loadProduct(data);
  });

const loadProduct = (data) => {
  //   alert("Products page is under construction!");
  const productContainer = document.getElementById("product-container");
  const productCartSection = document.getElementById("product-cart-section");

  data.forEach((element) => {
    const div = document.createElement("div");
    div.classList.add("product-cart");
    div.innerHTML = `
        <img class="product-img" src=${element.image} alr="product img">
        <div>
            <h1>${element.title}</h1>
            <p>${element.rating.rate}</p>
            <p>${element.category}</p>
            <h3> price : ${element.price}</h3>
            <p>${element.description.slice(0, 50)}</p>
            <button>details</button>
            <button onclick="addProduct('${element.title}' , '${
      element.price
    }')">add to cart</button>
        </div>
        `;

    productCartSection.appendChild(div);
    productContainer.appendChild(productCartSection);
  });
};

const addProduct = (title, price) => {
  const addProductSection = document.getElementById("add-product-section");
  //   console.log(title, price);
  const div = document.createElement("div");
  div.classList.add("cart-div");
  div.id = "cart-div";
  div.innerHTML = `
        
        <div class="cart-title-price">
            <p>${title.slice(0, 5)}</p>
            <p class="price">${price}</p>
        </div>
        <hr>
        
    `;
  addProductSection.appendChild(div);
  updateTotal();
};

const updateTotal = () => {
  const cartDiv = document.getElementById("cart-div");
  const prices = document.getElementsByClassName("price");

  let sum = 0;
  for (const element of prices) {
    // console.log(element.innerText);
    const em = parseFloat(element.innerText);
    sum += em;
  }

  const p = document.createElement("p");
  p.innerText = sum;
  cartDiv.appendChild(p);
};

// const updateTotal = () => {
//   const cartDiv = document.getElementById("cart-div");
//   const prices = document.getElementsByClassName("price");

//   let sum = 0;
//   for (const element of prices) {
//     // Parse the inner text of each price element as a float and add it to the sum
//     const priceValue = parseFloat(element.innerText);
//     sum += priceValue;
//   }

//   // Clear any previous total to avoid duplicating it
//   const existingTotal = document.getElementById("total");
//   if (existingTotal) {
//     existingTotal.remove();
//   }

//   // Create a new <p> element to display the total
//   const p = document.createElement("p");
//   p.id = "total"; // Set an ID for the total element
//   p.innerHTML = `Total: ${sum.toFixed(2)}`; // Format the sum to 2 decimal places

//   // Append the total to the cartDiv
//   cartDiv.appendChild(p);
// };
