const array = [
    {id: 1 , name:'Iphone' , description: "this is Iphone " , price: 200 , color : "golden"},
    {id: 2 , name:'Xiaomi' , description: "this is Xiaomi " , price: 200 , color : "navy"},
    {id: 3 , name:'Iphone' , description: "this is Iphone " , price: 300 , color : "golden"},
    {id: 4 , name:'Samsumg' , description: "this is samsumg " , price: 400 , color : "golden iris"},
    {id: 5 , name:'Iphone' , description: "this is Iphone " , price: 200 , color : "black diamond"},
]

// map() creates a new array from calling a function for every array element.
// map() does not execute the function for empty elements.
// map() does not change the original array.



// const numbers = [4, 9, 16, 25];
// const newArr = numbers.map(Math.sqrt)
// console.log(newArr);
// console.log(numbers);

const numbers = [65, 44, 12, 4];
const newArr = numbers.map(myFunction)

function myFunction(num) {
  return num * 10;
}
console.log(newArr);


const persons = [
    {firstname : "Malcom", lastname: "Reynolds"},
    {firstname : "Kaylee", lastname: "Frye"},
    {firstname : "Jayne", lastname: "Cobb"}
  ];
  
const persons_name =  persons.map(getFullName);
  
  function getFullName(item) {
    return [item.firstname,item.lastname].join(" ");
  }

console.log(persons_name);