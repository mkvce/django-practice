$(document).ready(function() {
  var $topbar = $("header .topbar");
  var $title = $("#title");
  var $topbarInitialBgColor = $topbar.css("background-color");
  var $titleInitialColor = $title.css("color");
  $(document).scroll(function() {
    $topbar.css("transition", "background-color 0.4s ease")
    $title.css("transition", "color 0.4s ease")
    if ($(this).scrollTop() > 2 * $topbar.height()) {
      $topbar.css("background-color", "rgba(50, 50, 50, 0.4)");
      $title.css("color", "white");
    }
    else {
      $topbar.css("background-color", $topbarInitialBgColor);
      $title.css("color", $titleInitialColor);
    }
  });
});