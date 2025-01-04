// const input_handle = document
//   .getElementById("submit-btn")
//   .addEventListener("click", (e) => {
//     const input_value = document.getElementById("input-area").value;

//     const home = document.getElementById("home");
//     const p = document.createElement("p");

//     p.innerText = input_value;
//     home.appendChild(p);

//     console.log("hello   ..");
//     console.log(input_value);
//     console.log(home);
//     console.log(p);
//   });

const submit_btn = document
  .getElementById("submit-btn")
  .addEventListener("click", (e) => {
    const input_handle = document.getElementById("input-area").value;
    const home = document.getElementById("home");

    const p = document.createElement("p");
    p.classList.add("child");
    p.innerText = input_handle;

    home.appendChild(p);
    // console.log(home);
    const all_child = document.getElementsByClassName("child");
    for (const element of all_child) {
      element.addEventListener("click", (e) => {
        // console.log("this is p class name child...");
        e.target.parentNode.removeChild(element);
      });
    }
  });

fetch("https://jsonplaceholder.typicode.com/users")
  .then((res) => res.json())
  .then((data) => {
    // console.log(data);
    displayData(data);
  })
  .catch((err) => {
    console.log(err);
  });

const displayData = (userData) => {
  const container = document.getElementById("userData-Container");

  userData.forEach((element) => {
    // console.log(element);
    const div = document.createElement("div");
    div.innerHTML = `
        <h4>title</h4>
        <p>Description</p>
        <button>Derails</button>
        `;
    container.appendChild(div);
  });
};
