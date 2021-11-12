//This is for fast replies only.
async function doSomething(){
let result = await eel.abcd()();
console.log((result));
}

doSomething();

//Async communication
function logger(n){
    console.log("Got this from python:\t",n);
    for (let i = 0; i < n.length; i++) {
        // const element = n[i];
        const element = document.createElement("a");
        element.innerText= "(" + n[i][1] + ") " + n[i][0];
        element.className = "stockList"
        element.href="https://in.tradingview.com/chart/?symbol=NSE%3A" + n[i][0];
        document.body.append(element);
    }
    const load = document.getElementById("loading");
    load.remove();

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

//    showElems();
    createLoading();
}

function createLoading(){
    var loading = document.createElement("h3");
    loading.id = "loading";
    loading.innerText="Loading...";
    document.body.appendChild(loading);
}

