$(document).ready(function() {
  var $heart = $(".feedHeart");
  $heart.click(function() {
    var imageId = $(this).attr("data-id");
    var heart = $(this);
    $.ajax({
      url: "/images/" + imageId + "/like/",
      statusCode: {
        204: function() {
          heart.toggleClass("fa-heart-o fa-frown-o");
        },
        200: function() {
          heart.toggleClass("fa-heart-o fa-frown-o fa-heart clickedHeart");
        }
      }
    });
  });
  // TODO:
  // 1) Get the comment from the textarea
  // 2) Detect when somebody presses enter
  // 3) Send a POST request to a 'images/{image_id}/comment
  // 4) Create a new comment in the database
});
