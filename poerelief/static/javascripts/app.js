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

	$.getJSON('/doc/' + docid, function( data ) {
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
    window.history.pushState({}, "Poetic Relief", "/" + data.locid);
	});

};
/*
<div class="center-cropped" 
       style="background-image: url('http://www.steinheim-institut.de/daten/picsdu4/xl/0002_du4_2009.png');">
  </div>​
</div>
<div>
  <div class="text-navigation">
    <a href='#' data-target="#original_and_translation">Side to Side</a>
    <a href='#' data-target="#translation">Translation</a>
    <a href='#' data-target="#original" class="active">Original</a>
  </div>
  <div class="clear"></div>
  <div id="original" class="text hebrew">
פ״נ‏‎
‎‏איש תם וישר צעיר לימים‏‎
‎‏כמ״ר יוסף בר צבי נפטר כ״א‏‎
‎‏לחודש מנחם אב שנת תר״ץ‏‎
‎‏תנצב״ה‏‎
  </div>
  <div id="translation" class="text">
Hier ist begraben
ein lauterer und aufrechter Mann, jung an Tagen,
der geehrte Herr Josef, Sohn des Zwi, verschieden 21.
des Monats Menachem Aw des Jahres 690.
Seine Seele sei eingebunden in das Bündel des Lebens
  </div>
  <div id="original_and_translation">
    <div class="text hebrew left">
פ״נ‏‎
‎‏איש תם וישר צעיר לימים‏‎
‎‏כמ״ר יוסף בר צבי נפטר כ״א‏‎
‎‏לחודש מנחם אב שנת תר״ץ‏‎
‎‏תנצב״ה‏‎
    </div>
    <div class="text right">
Hier ist begraben
ein lauterer und aufrechter Mann, jung an Tagen,
der geehrte Herr Josef, Sohn des Zwi, verschieden 21.
des Monats Menachem Aw des Jahres 690.
Seine Seele sei eingebunden in das Bündel des Lebens
    </div>
    <div class="clear"></div>
  </div>*/