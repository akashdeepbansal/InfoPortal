function increaseFont() {
	$("body, input,ul,li,a,p,select, textarea, button").css("font-size", (parseInt($("body").css("fontSize")) * 1.1) + "px");
	console.log("Done");
}
function decreaseFont() {
	$("body, input, ul,li,a ,p,select, textarea, button").css("font-size", (parseInt($("body").css("fontSize")) * 0.9) + "px");
}
function contrastChange() {
	$("p,#about,#service,.card,body,.navbar,.morelink ,#client,.agileits-footer,.navbar-default .navbar-nav > li > a, .col,.row, .row teal, .row white,  footer").css({
      "color": "#F2E84E",
      "background-color": "rgba(0, 0, 0, 1.5)",
      "font-family": "Arial",
      "border": "0px"
    });
    $('.white').removeClass("white");
    $("p,#about,#service,.card,body,.navbar,.morelink ,#client,.agileits-footer,.navbar-default .navbar-nav > li > a, .col,.row, .row teal, .row white, footer").addClass("black");
    $('.white-text').removeClass('white-text');    
    $("h2,.wthree-footer-grid ul li a,.location,#title,ul li a,p").css({
      "color": "#F2E84E",

      "font-family": "Arial",
      "padding": "2px;"
    });
}