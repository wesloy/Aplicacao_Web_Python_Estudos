function mostrarSenha(id_campo, id_imagem) {
    tipo = document.getElementById(id_campo); //instanciando o obj alvo
    tipoImg = document.getElementById(id_imagem); //instanciando o obj alvo
    if (tipo.type == "password") {
        tipo.type = "text";
        tipoImg.src = "/static/img/mostrar_senha.png";
    } else {
        tipo.type = "password";
        tipoImg.src = "/static/img/ocultar_senha.png";
    }
}

function forcaSenha(id_campo) {
    senha = document.getElementById(id_campo).value;
    forca = 0;

    if (senha.length >= 8) {
        forca += 25;
    }
    if (senha.match(/[a-z]+/)) {
        forca += 10;
    }
    if (senha.match(/[A-Z]+/)) {
        forca += 15;
    }
    if (senha.match(/[0-9]+/)) {
        forca += 25;
    }
    if (senha.match(/[~`!@#$%\^&*+=\-\[\]\\';,/{}|\":<>\?]+/)) {
        forca += 25;
    }
    return exibir_forca();
}


function exibir_forca() {

    ///Necessário incrementar na página a tabela:
    ///<div class="table-responsive-xl ">
    ///<table id="forcaSenhaTbl"></table>
    ///</div>

    exibir = document.getElementById("forcaSenhaTbl");
    if (forca <= 25) {
        exibir.innerHTML = '<th>Força:</th><tr><td bgcolor="red" width="' +
            forca + '"></td><td>Fraca</td></tr>';
    } else if ((forca > 25) && (forca <
            50)) {
        exibir.innerHTML = '<th>Força:</th><tr><td bgcolor="yellow" width="' + forca + '"></td><td>Média</td></tr>';;
    } else if ((forca >= 50) && (forca <
            85)) {
        exibir.innerHTML = '<th>Força:</th><tr><td bgcolor="blue" width="' + forca + '"></td><td>Forte</td></tr>';
    } else {
        exibir.innerHTML = '<th>Força:</th><tr><td bgcolor="green" width="' + forca +
            '"></td><td>Excelente</td></tr>';
    }
}