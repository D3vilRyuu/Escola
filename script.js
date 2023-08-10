function enviar(){
    var frutas = ["abacaxi", "abacate", "laranja"]
    var fruta = document.getElementById("fruta").value
    var controle = false

    if(fruta == ""){ 
        alert("A caixa de texto está em branco")
    }else{
        
        for(i=0; i<frutas.length; i++){
            frutinha = fruta.toLowerCase()
            if (frutinha == frutas[i]){
                controle = true
                alert("Você acertou!!")
            }
        }
        if(controle == false){
                alert("Desculpe, você errou!!")
            }
    }
}

function dica(){
    alert("Todas tem letras A")
}