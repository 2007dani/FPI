
function show_more(){
    var x=document.getElementById("info")
    if (x.style.display==""){
        x.style.display="block"
        x.style.fontSize="25px"
        x.style.color="#121211"
        x.style.fontFamily="Calibri"
        x.style.backgroundColor="#e6ede6"
    }else{
        x.style.display=""
        x.style.fontSize="25px"
        x.style.color="#121211"
        x.style.fontFamily="Calibri"   
    }
}