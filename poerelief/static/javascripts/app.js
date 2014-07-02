$( document ).ready(function() {
  $(".text-navigation a").on("click", function(e) {
    e.preventDefault();
    var current = $("a.active");
    current.removeClass("active");
    $(current.data("target")).hide();
    $(this).addClass("active");
    $($(this).data("target")).show();
  });
});
