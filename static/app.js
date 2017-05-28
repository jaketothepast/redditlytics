var socket = io.connect('http://localhost:' + location.port);

socket.on('comment', function(comment) {
  console.log('got comment: ' + comment.data);
  var comments = document.getElementById('comments');
  var l = comments.getElementsByTagName('li');

  if (l.length > 1 && l[l.length - 1].innerHTML == comment.data) {
    console.log("Same comment, doing nothing");
  }
  else {
    var newElem = document.createElement('li');
    newElem.innerHTML = comment.data;
    comments.append(newElem);
  }
});

function commentStream() {
  console.log('Getting comment');
  socket.emit('start-stream', subreddit);
  setTimeout(commentStream, 1000);
}

commentStream();
