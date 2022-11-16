function utilizouHoraExtra(id) {
    token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    console.log(id)

    $.ajax({
        type: 'POST',
        url: '/horas-extras/utilizou-he/' + id + '/',
        data: {
            csrfmiddlewaretoken: token
        },
        success: function(result) {
            console.log(result)
            $("#mensagem").text(result.mensagem);
            $("#horas_atualizadas").text(result.horas);
        }
    });
}

function naoUtilizouHoraExtra(id) {
    token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    console.log(id)

    $.ajax({
        type: 'POST',
        url: '/horas-extras/nao-utilizou-he/' + id + '/',
        data: {
            csrfmiddlewaretoken: token
        },
        success: function(result) {
            console.log(result)
            $("#mensagem").text(result.mensagem);
            $("#horas_atualizadas").text(result.horas);
        }
    });
}