const array = [
    {id: 1 , name:'Iphone' , description: "this is Iphone " , price: 200 , color : "golden"},
    {id: 2 , name:'Xiaomi' , description: "this is Xiaomi " , price: 200 , color : "navy"},
    {id: 3 , name:'Iphone' , description: "this is Iphone " , price: 300 , color : "golden"},
    {id: 4 , name:'Samsumg' , description: "this is samsumg " , price: 400 , color : "golden iris"},
    {id: 5 , name:'Iphone' , description: "this is Iphone " , price: 200 , color : "black diamond"},
]

// find by loop 
for (let i = 0; i < array.length; i++) {
    const element = array[i];
    if (element.id == 3) {
        console.log(element);
    };
};

// const result = array.find(pd => pd.id == 5);
// single product return kore .. jodi akta product chai tahole find babohar korte pari ....
// jodi find function kiso khoje nah pai tahole undefined return kore ...
// ekadik item takle first item ta return kore ..
const result = array.find(pd => pd.id == 10);
console.log(result);