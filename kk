<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style2.css">

</head>

<body>
    <center>
        <h1>Como esta o seu dia?</h1>
        <label>Digite como você está? (bem, mais ou menos, mal)</label><br><br>
        <input id="emocional" type="text"><br><br>

        <button id="Botao" onclick="botao()">Gerar Frase</button><br>

        <div id="quadrado">

        </div><br>

        <div id="frase">

        </div>
    </center>

    <script>
        function botao() {
            var foto = document.getElementById("quadrado")
            var frase = document.getElementById("frase")
            var emocional = document.getElementById("emocional")
            var imagem = document.createElement('img')

            imagem.src = "nationalgeographic2723148-copia.jpg"
            imagem.style.width = "300px"
            imagem.style.height = "500px"
            foto.appendChild(imagem)

            if (emocional == "bem"){
                frase.innerText = "Que continue assim"
            }else if (emocional == "mais ou menos"){
                frase.innerText = "Descubra quem voce é seja essa pessoa. Essa alma foi colocada nesse mundo para ser isso, então viva essa verdade e todo resto virá"
            }else if(emocional == "mal"){
                frase.innerText = "Se voce está na merda nao ligue alguem pode esta pior"
            }
        }
    </script>
</body>

</html>
