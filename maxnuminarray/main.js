function getBiggest(arr){
    return arr.reduce((acc,el)=>
        acc > el ? acc : el
    ); 
}
console.log(getBiggest([1,6,8,3,7,3,66,89,35,12]));