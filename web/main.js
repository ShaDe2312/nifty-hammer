//This is for lightning fast replies only.
async function doSomething(){
let result = await eel.abcd()();
console.log((result));
}

doSomething();

//Async communication
function logger(n){
    console.log("Got this from python:\t",n);
}
eel.hammerList()(logger) //try adding ()
