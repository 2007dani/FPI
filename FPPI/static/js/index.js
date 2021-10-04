function search(){
    var s=document.getElementById("input").value;
    var div_null=document.getElementById("otttdtttft")
    var i =0;
    while (true){
        i=i+1;
        var div=document.getElementById(i);
        if (div_null==div){
            break;
        }
        else{
            if(div.getAttribute("value").includes(s)){
                div.style.display="block"
            }else{
                div.style.display="none"
            }
        }

    }
}

function click_(_id) {
    window.location.assign('index/show/'+_id);    
}