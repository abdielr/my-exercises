let text= "Hola este es un texto que no se si se repita. Espero que todos esten bien";
function normalize(word){
    return word.toLowerCase().replace(",","").replace(".","").replace("!","").replace("?","")
}
function wordRepeat(text){
    let dict = {};
    let separatedWords = text.split(" ");
    for(var word of separatedWords){
        if(normalize(word) in dict){
            ++dict[normalize(word)];
        }else{
            dict[normalize(word)] = 1;
        }
    }
    console.log(dict);
}
wordRepeat(text);