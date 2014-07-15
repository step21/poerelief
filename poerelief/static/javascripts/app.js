$( document ).ready(function() {
  $(".text-navigation a").on("click", function(e) {
    e.preventDefault();
    var current = $("a.active");
    current.removeClass("active");
    /* Maybe change such as here for animation? http://jqueryui.com/removeClass/ */
    $(current.data("target")).hide();
    $(this).addClass("active");
    $($(this).data("target")).show();
  });
});
/* var S = require('string'); */
function getDoc(docid) {

	$.getJSON('/poerelief/doc/' + docid, function( data ) {
		/* Name, date and pictures work quite well, though sometimes I have seen that there is no name and pictures are very different from each other */
		/* The rest of the text however is a problem ... translation works best  (except it needs whitespace stripped, or something ... I alread strip ab/lb tags that were still in the source date, but it's not enough)
		 hebrew is more of a problem, as it is not always pure hebrew ... according to Thomas from the institute, recto/verso (as the original is called in the source)
		  should almost always be hebrew. That is not always true though, sometimes it also is mixed with german ...  (and either one can be empty) */
		/* Also, if a a specific record is requested, that should be injected instead of a random one ... though not sure how to pass that through atm. In the template it is {{ret}} but not sure how to inser that into javascript */		  
		var translation = S(data.translation).stripTags().trim();
		$('#translation').text(translation);
		$('#original').html(data.edition);
    $('.left').html(data.edition);
    $('.right').text(translation);
		/*$('#original').append();*/
		$('.center-cropped').css('background-image', "url("+data.graphicsurl+")");
		$('#pname').html(data.pname + " [" + data.date + "]");
    /* window.history.pushState({}, "Poetic Relief", "/" + data.locid); */
    window.history.pushState({}, "Poetic Relief", "/poerelief/" + data.locid);
	});

};
