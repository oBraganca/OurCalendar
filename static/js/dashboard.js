
$(document).ready(function() {
    $('#table').DataTable({
        "language": {
            "url": "http://cdn.datatables.net/plug-ins/9dcbecd42ad/i18n/Portuguese-Brasil.json"
        }
    });
    
    
    $(document).on("click", "button[data-attr=edit]", function(){
        $.ajax({
            type:"POST",
            url: "/getForm/",
            mode: 'same-origin',
            data: {"id": $(this).attr("id")},          
            beforeSend: function(xhr) {
                xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'))
            },
        }).done(function(data) {
            $('#modal .modal-body').empty()
            $('#modal .modal-body').append(data);
            $('#modal').modal('show');
        });
    }); 

    $(document).on("click", "button[data-attr=exclude]", function(){

        $.ajax({
            type:"POST",
            url: "/getInfo/",
            mode: 'same-origin',
            data: {"id": $(this).attr("id")},          
            beforeSend: function(xhr) {
                xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'))
            },
        }).done(function(data) {
            
            $('#exampleModal .modal-title').empty()
            $('#exampleModal .modal-title').append("Excluir o evento: "+data.event_name+" ?");
            
            $('#exampleModal .modal-body').empty()
            $('#exampleModal .modal-body').append("<h6>Nome do evento: "+data.event_name+"</h6><h6>Descrição: "+data.description+"</h6>");
            $('#exampleModal').modal('show');
            
            $( "#excludeEvent" ).attr( "attr-id", data.event_id );
        });

    })

    $(document).on("click", '#excludeEvent', function(e) {
        $.ajax({
            type:"POST",
            url: "/excludeEvent/",
            mode: 'same-origin',
            data: {"id": $(this).attr("attr-id")},          
            beforeSend: function(xhr) {
                xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'))
            },
        }).done(function(data) {
            location.reload();
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