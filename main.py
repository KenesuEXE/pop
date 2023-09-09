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
    image_url, song_url = library.get_stats(artist_name, song_name)
    return render_template("song.html",
                           artist_name=artist_name,
                           song_name=song_name,
                           image_url=image_url,
                           song_url=song_url)


@app.route('/discover', methods=['POST'])
def discover():
    artist_name, song_name = library.discover()
    return redirect(url_for('song', artist_name=artist_name, song_name=song_name))


if __name__ == "__main__":
    app.run(debug = True)


"""
TODO:
fix page not founds
for you


This can be a webdev portfolio
"""