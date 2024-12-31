var test=12
var node = false
var cursor = 'pointer'

console.log(cursor)
console.log(node)
console.log(test)


// string dynamic templet litarels and spread operator

const name = "kashem";
const str = `My name is ${name}`;
console.log(str);

// spread operator 

const num = [1,2,3 , 4 ,5 ,6];
const num2 = [11 , 12 , 13 , 14];
// console.log([num , num2]);
// using spread operator 
console.log([...num , ...num2]);