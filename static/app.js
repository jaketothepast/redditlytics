var socket = io.connect('http://localhost:' + location.port);

socket.on('comment', function(comment) {
  console.log('got comment: ' + comment.data);
  var comments = document.getElementById('comments');
  var newElem = document.createElement('li');
  newElem.innerHTML = comment.data;
  comments.append(newElem);
});

function commentStream() {
  console.log('Getting comment');
  socket.emit('start-stream', 'starting');
  setTimeout(commentStream, 1000);
}

commentStream();
