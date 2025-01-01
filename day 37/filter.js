const array = [
    {id: 1 , name:'Iphone' , description: "this is Iphone " , price: 200 , color : "golden"},
    {id: 2 , name:'Xiaomi' , description: "this is Xiaomi " , price: 200 , color : "black"},
    {id: 3 , name:'Iphone' , description: "this is Iphone " , price: 300 , color : "golden"},
    {id: 4 , name:'Samsumg' , description: "this is samsumg " , price: 400 , color : "golden"},
    {id: 5 , name:'Iphone' , description: "this is Iphone " , price: 200 , color : "black diamond"},
]


const result = array.filter(product => product.color == "golden");
console.log(result);

// jokon multiple value return korte hoi tokon filter function babohar korbo 
// filter korle akta array return paua jai ..
// filter korar por kono value nah paile empty array return kore 
// filter dara sohojei kaj kora jai ..
