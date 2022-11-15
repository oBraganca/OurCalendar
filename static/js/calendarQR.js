
$(document).ready(function() {
    
    
    $(document).on("click", "button[data-attr=gerar-codigo]", function(){
        $.ajax({
            type:"POST",
            url: "/getCodeMerge/",
            mode: 'same-origin',      
            beforeSend: function(xhr) {
                xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'))
            },
        }).done(function(data) {
            console.log(data)
            if(data.status){
                $('#exampleModal .modal-title').empty()
                $('#exampleModal .modal-title').append(data.header);
                
                $('#exampleModal .modal-body .form-group').empty()
                $('#exampleModal .modal-body .form-group').append(data.form);
                // $('#exampleModal .modal-footer input').val(data.action)button
                $('#exampleModal .modal-footer button').text(data.action)
                $('#exampleModal .modal-footer input').attr("hidden",true)
                $('#exampleModal').modal('show');
            }
            
        });
    }); 

    $(document).on("click", "button[data-attr=usar-codigo]", function(){

        $.ajax({
            type:"POST",
            url: "/getUseCoder/",
            mode: 'same-origin',
            data: {"id": $(this).attr("id")},          
            beforeSend: function(xhr) {
                xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'))
            },
        }).done(function(data) {
            console.log(data)
            if(data.status){
                $('#exampleModal .modal-title').empty()
                $('#exampleModal .modal-title').append(data.header);
                
                $('#exampleModal .modal-body .form-group').empty()
                $('#exampleModal .modal-body .form-group').append(data.form);
                $('#exampleModal .modal-footer button').empty()
                $('#exampleModal .modal-footer input').val("")
                $('#exampleModal .modal-footer button').text("Cancelar")
                $('#exampleModal .modal-footer input').val(data.action)
                $('#exampleModal .modal-footer input').attr("hidden",false)
                $('#exampleModal').modal('show');
            }
        });

    })

});


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}