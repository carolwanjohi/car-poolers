$(document).ready(function(){

    $('form').submit(function(event){

        event.preventDefault()

        var url = "/ajax/book-seat"+ $('form').attr('action') + "/"

        console.log(url)

        form = $("form")

        $.ajax({
            'url':url,
            'type':'POST',
            'data': form.serialize(),
            'dataType': 'json',
            'success':function(data){
                alert(data['success'])
            }
        }) 
    })

}) 