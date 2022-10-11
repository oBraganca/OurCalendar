
$(document).ready(function() {
    var pageUrl = window.location.pathname;
    $(".menu-itens a[href='"+pageUrl+"'] li").addClass("active");
});