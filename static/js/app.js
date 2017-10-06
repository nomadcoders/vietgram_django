$(document).ready(function() {
  var $heart = $(".feedHeart");
  $heart.click(function() {
    var imageId = $(this).attr("data-id");
    // if ($(this).hasClass("fa-heart-o")) {
    //   $(this).removeClass("fa-heart-o");
    //   $(this).addClass("fa-heart clickedHeart");
    // } else {
    //   $(this).removeClass("fa-heart clickedHeart");
    //   $(this).addClass("fa-heart-o");
    // }
    $(this).toggleClass("fa-heart-o fa-heart clickedHeart");
  });
});
