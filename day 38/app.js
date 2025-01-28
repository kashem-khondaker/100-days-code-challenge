// const x = document.getElementById("h-title");
// x.document.background='red'
// console.log(x);

// const allbox = document.getElementsByClassName('box');
// console.log(allbox)
// for (let i = 0; i < allbox.length; i++) {
//     const element = allbox[i];
//     console.log(element);
//     element.style.backgroundColor = 'green';
//     if (element.innerText == "box-5") {
//     element.style.backgroundColor = 'red';
//     }
// }

document.getElementById("btn").addEventListener("click", (e) => {
  const input_value = document.getElementById("input-handle").value;
  console.log(input_value);

  const container = document.getElementById("container");
  const p = document.createElement("p");
  p.classList.add("child");
  p.innerText = input_value;

  container.appendChild(p);

  const allcomments = document.getElementsByClassName("child");

  for (const element of allcomments) {
    element.addEventListener("click", (e) => {
      // console.log(e.target);
      e.target.parentNode.removeChild(element);
    });
  }
});

// const handleSearch = () => {
//   console.log("hello dom tom ...");
// };
