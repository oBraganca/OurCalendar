
$(document).ready(function() {
    $('#exampleModal').modal('show');
    $('#exampleModal').on('hidden.bs.modal', function () {
        window.location.href="/"
    })

    $('#form-merge').submit(function(){
        $("#form-merge :disabled").removeAttr('disabled');
    });
    
    // $(document).on("click", "button[attr='data-dismiss']", function(){
    // }); 
});