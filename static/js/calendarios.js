$(document).ready(function(){

    

    $("#sendRequest").submit(function(e){
        
        e.preventDefault();
    })
    $("#liveToastBtn").click(function(){
        $.ajax({
            type:"POST",
            url: "/follow-calendar/",
            mode: 'same-origin',
            data: {"email": $("#solicit-follow").val()},          
            beforeSend: function(xhr) {
                xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'))
            },
        }).done(function(data) {
            if(data.status == "success"){
                $("#message").text(data.message)
                $("#message").css("color", "green");
            }else{
                $("#message").text(data.message)
                $("#message").css("color", "red");
            }
        });
        $('.toast').toast('show');
    })

    $("#notify").click(function(){
        if($(".notification").not(".active").length > 0 ) {
            $(".notification").addClass("active")
        }else{
            $(".notification").removeClass("active")
        }
    });




    $(document).on("click", "button[data-attr=accept]", function(){

        $.ajax({
            type:"POST",
            url: "/acceptUser/",
            mode: 'same-origin',
            data: {"id": $(this).attr("id")},          
            beforeSend: function(xhr) {
                xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'))
            },
        }).done(function(data) {
            window.location.reload()
        });

    })

    

    $(document).on("click", "button[data-attr=refuse]", function(){

        $.ajax({
            type:"POST",
            url: "/refuseUser/",
            mode: 'same-origin',
            data: {"id": $(this).attr("id")},          
            beforeSend: function(xhr) {
                xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'))
            },
        }).done(function(data) {
            window.location.reload()
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