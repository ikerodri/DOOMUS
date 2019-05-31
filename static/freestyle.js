var llista=[]
var llista2=[]
$(document).ready(function () {

    $(".afegirllista").click(function () {
        console.log("entra")
        var id = $(this).attr("id")
        if (document.getElementById(id).className == "btn-change2 afegirllista"){
            document.getElementById(id).className = "btn-change3 afegirllista"
            document.getElementById(id).innerText = "On"
        }  else {
            document.getElementById(id).className = "btn-change2 afegirllista"
            document.getElementById(id).innerText = "Off"
        }

        var existent=0;
        if (llista.length==0){
            llista.push(id)
        } else{
            var existe = false;
            for (let i = 0; i <llista.length; i++) {
                if (llista[i] == id) {
                    existe=true;
                    existent=llista[i]
                }
                if (existe==true){
                    for (let j = 0; j <llista.length ; j++) {
                        if (llista[j]!=existent){
                            llista2[j]=llista[j]
                        }
                    }
                    llista=llista2
                    llista2 = []
                }
            }
            if (!existe) {
                llista.push(id)
            }
        }
        console.log(llista)
    })
})



/* PLAY */

function playindividual(nombre){
    document.getElementById(nombre).play();
    console.log(nombre)
}

/* STOP */


function stopindividual(nombre){
    document.getElementById(nombre).load();
}



/* MUTE */


function muteindividual(nombre){
    var so= document.getElementById(nombre);
    if(so.muted==false){
        so.muted = true;
    } else{
        so.muted = false;
    }
}


/* PAUSE */



function pauseindividual(){
    document.getElementById('').pause();
}




/* FUNCIONS GLOBALS */


function playglobal(){
    for (let i = 0; i <llista.length ; i++) {
        document.getElementById("audio" + llista[i]).play();
    }

}

function stopglobal (){
    for (let i = 0; i <llista.length ; i++) {
        document.getElementById("audio" + llista[i]).load();
    }
}

function pauseglobal (){
    for (let i = 0; i <llista.length ; i++) {
        document.getElementById("audio" + llista[i]).pause();
    }
}


