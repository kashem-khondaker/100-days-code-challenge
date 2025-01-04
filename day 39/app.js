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
    p.innerText = input_handle;

    home.appendChild(p);

  });
