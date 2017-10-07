$(document).ready(function() {
  var $heart = $(".feedHeart"),
    $commentInput = $(".comment-input");
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
  $commentInput.keypress(function(event) {
    var keyCode = event.keyCode;
    var imageId = $(this).attr("data-id");
    if (keyCode === 13) {
      event.preventDefault();
      var commentToSend = event.target.value;
      $(this)
        .val("")
        .blur();
      $.ajax({
        type: "POST",
        url: "/images/" + imageId + "/comment/",
        data: JSON.stringify({
          comment: commentToSend
        })
      });
    }
  });
  // TODO:
  // 3) Send a POST request to a 'images/{image_id}/comment/
  // 4) Create a new comment in the database
  // 5) Put the new comment on the comment list (<ul>)
  // YOU (DAVID ALSO):
  // 1) Create a URL for 'images/{image_id}/comment
  // 2) Create a view for that url
  // 3) Find the image with the 'image_id' variable
  // 4) Create a new comment with the request.POST, the request.user and the found image
});
