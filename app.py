from flask import Flask, request, render_template, redirect, url_for
from pytube import YouTube
import os

app = Flask(__name__)

def download_video_yt(url, path):
    try:
        yt = YouTube(url)
        yt.streams.get_highest_resolution().download(output_path=path)
        return "Download complete!"
    except Exception as e:
        return f"ERROR: {e}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        path = request.form.get('path', 'C:/Users/Gonzalo/Desktop/musica descargada')
        message = download_video_yt(url, path)
        return render_template('index.html', message=message)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
