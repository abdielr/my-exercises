const multiply = (a,b)=>{
    let result = 0;
    const positive = Math.abs(b) == b;
    for(i=0;i<Math.abs(b);i++){
        result = positive ? result + a : result - a;
    }
    return result;
}

const a = multiply(5,3);
console.log(a);