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
eel.hammerList()(logger) 


function clearPage(){
   var wd= document.getElementById("waterdrop");
   var an= document.getElementById("appname");
   var desc= document.getElementById("description");
   var cont= document.getElementById("continue");

   wd.remove();
   an.remove();
   desc.remove();
   cont.remove();
}

