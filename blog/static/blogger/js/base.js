$(document).ready(function() {
  let $topbar = $("header .topbar");
  let $title = $("#title");
  let $topbarInitialBgColor = $topbar.css("background-color");
  $(document).scroll(function() {
    $topbar.css("transition", "background-color 0.4s ease")
    $title.css("transition", "color 0.4s ease")
    if ($(this).scrollTop() > $topbar.height()) {
      $topbar.css("background-color", "rgba(50, 50, 50, 0.6)");
      $title.removeClass("text-dark");
      $title.addClass("text-light");
    }
    else {
      $topbar.css("background-color", $topbarInitialBgColor);
      $title.removeClass("text-light");
      $title.addClass("text-dark");
    }
  });
});