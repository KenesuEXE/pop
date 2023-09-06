from flask import Flask, render_template, url_for, request, redirect
import library

app = Flask(__name__)


@app.route('/')
def home():
    #if request.method == "POST":
    #    return redirect(url_for("song", artist_name="Random Artist", song_name="Random Song"))
    return render_template("index.html")


@app.route('/song/<artist_name>/<song_name>')
def song(artist_name, song_name):
    # Get other stats here
    image_url = library.get_stats(artist_name, song_name)
    return render_template("song.html", artist_name=artist_name, song_name=song_name, image_url=image_url)


@app.route('/discover', methods=['POST'])
def discover():
    artist_name, song_name = library.discover()
    return redirect(url_for('song', artist_name=artist_name, song_name=song_name))


if __name__ == "__main__":
    app.run(debug = True)


"""
IDEA DUMP
# Song recommendor AI
# Random button play!
# Make song pic placeholder


https://chat.openai.com/share/7cc49bda-112e-4e85-96ec-d5ff35b9af77
ai gen personal playlist
shared playlist
lyrics and karaoke
music discovery, random track but still personalized
interactive podcasts
accessability features
music education
virtual concerts, live streaming, radio station
user gen content, forums
music visualization
mood and activity recognition


This can be a webdev portfolio
"""