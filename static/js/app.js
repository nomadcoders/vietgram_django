$(document).ready(function() {
  var $heart = $(".feedHeart"),
    $commentInput = $(".comment-input");
  $heart.click(function() {
    var imageId = $(this).attr("data-id");
    var heart = $(this);
    $.ajax({
      url: "/images/" + imageId + "/like/",
      statusCode: {
        204: function(data) {
          console.log(data);
          heart.toggleClass("fa-heart-o fa-frown-o");
        },
        200: function() {
          console.log(data);
          heart.toggleClass("fa-heart-o fa-frown-o fa-heart clickedHeart");
        }
      }
    });
  });
  $commentInput.keypress(function(event) {
    var keyCode = event.keyCode;
    var textArea = $(this);
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
        data: {
          comment: commentToSend
        }
      }).done(function(data) {
        var photoComments = textArea
          .parent()
          .parent()
          .children(".photo__comments");
        photoComments.append(
          '<li class="photo__comment"><span class="photo__comment-author ">' +
            data.user +
            "</span> " +
            data.comment +
            "</li>"
        );
      });
    }
  });
  // TODO:
  // 5) Put the new comment on the comment list (<ul>)
});
