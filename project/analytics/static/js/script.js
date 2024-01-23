var togButton = document.getElementById("togButton");

darkOn = localStorage.getItem("dark") == "true" ? true : false;
setTheme();

function setTheme(){
    localStorage.setItem("dark", darkOn ? "true" : "false");
    if(darkOn){
        document.body.classList.remove("light-theme");
        document.body.classList.add("dark-theme");
    }
    else{
        document.body.classList.remove("dark-theme");
        document.body.classList.add("light-theme");
    }
}

var darkOn = false;
function toggle(){
    darkOn = !darkOn;
    setTheme();
}

togButton.addEventListener("click", toggle);