$(document).ready(function(){

    $('form').submit(function(event){

        event.preventDefault()

        var url = "/ajax/review-driver"+ $('form').attr('action') + "/"

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

        $('#id_review_content').val('')
    })

}) 
