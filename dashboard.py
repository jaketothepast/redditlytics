"""
Flask application to run endpoints for the Reddit analytics application
"""
import time
import asyncio

from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

from reddit import get_reddit

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('start-stream')
def handle_stream(message):
    print("Got the stream connection")
    print("starting stream")
    reddit = get_reddit()
    c = next(reddit.subreddit('aww').stream.comments())
    emit('comment', {'data': c.body})

@app.route('/')
@app.route('/r/<subreddit>')
def index(subreddit=None):
    reddit_client = get_reddit()
    top_titles = None
    message = None
    if subreddit:
        try:
            top_posts = reddit_client.subreddit(subreddit).hot(limit=10)
            top_titles = [post.title for post in top_posts]
        except:
            message = 'Could not get top posts for {0}'.format(subreddit)
    else:
        message = 'Welcome'

    return render_template('index.html', top_titles=top_titles, message=message)

@app.route('/r/<subreddit>/comments')
def comments(subreddit=None):
    """Stream comments to the flask application"""
    return render_template('comments.html')

if __name__ == '__main__':
    socketio.run(app)
