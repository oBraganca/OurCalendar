
$(document).ready(function() {
    id = window.location.href.substring(window.location.href.lastIndexOf('/') + 1)
    const chatSocket = new WebSocket('ws://'+ window.location.host+'/ws/sendEvent/'+id);
  
    chatSocket.onopen = function(message) {
      console.log("open", message);
    }
  
    chatSocket.onerror = function(message) {
        console.log("error", message);
    }
  
    chatSocket.onclose = function(message) {
        console.log("close", message);
    }
  
  
    chatSocket.onmessage = function(e) {
        const data = JSON.parse(e.data);
  
        if (data) {
          calendar.addEvent(data);
          calendar.render();
          
        } else {
            alert('The message was empty!')
        }
  
    };
    $('#exampleModal').modal('show');
    $('#exampleModal').on('hidden.bs.modal', function () {
      
            // var title = $("input[name='name']").val();
            // var description = $("textarea[name='description']").val();
            // var date_start = $("input[name='date_start']").val();
            // var date_end = $("input[name='date_end']").val();
            // var access = $("select[name='access'] option:selected").val();
      
      
            // chatSocket.send(JSON.stringify({
            //     'title': title,
            //     'description': description,
            //     'date_start': date_start,
            //     'date_end': date_end,
            //     'access': access,
            //     'idcalendar': id
            // }));
      

        window.location.href="/"
    })

    $('#form-merge').submit(function(){
        $("#form-merge :disabled").removeAttr('disabled');
    });
    
    // $(document).on("click", "button[attr='data-dismiss']", function(){
    // }); 
});