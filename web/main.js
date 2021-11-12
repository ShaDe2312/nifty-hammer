
var isPressed= false;
displayList=[]
//Async communication
function logger(n){
    console.log("Got this from python:\t",n);

    for (let i = 0; i < n.length; i++) {
        // const element = n[i];
        const element = document.createElement("a");
        element.innerText= "(" + n[i][1] + ") " + n[i][0];
        element.className = "stockList"
        element.href="https://in.tradingview.com/chart/?symbol=NSE%3A" + n[i][0];
        displayList.push(element);
    }
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
    if(displayList.length < 0){
    var loading = document.createElement("h3");
    loading.id = "loading";
    loading.innerText="Loading...";
    document.body.appendChild(loading);
    isPressed=true;
    }
    else{
        displayer(displayList);
    }
}

function displayer(List) {
        console.log(List);
        for (let index = 0; index < List.length; index++) {
            document.body.append(List[index]);
        }

    // var load = document.getElementById("loading");
    // load.remove();
}
