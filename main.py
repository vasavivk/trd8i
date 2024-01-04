import yt_dlp, subprocess 
from flask import Flask, render_template, request


app = Flask(__name__)
import re

def get_video_id(url):
    regex = r"(?<=v=)[\w-]+|(?<=be/)[\w-]+"
    match = re.search(regex, url)
    if match:
        return match.group(0)
    else:
        return None
      
@app.route('/')
def home():
    return render_template('input.html')

@app.route("/download", methods=["POST"])
def download():
    # Get the YouTube link from the form
    link = request.form.get("link")

    # Download the video using yt-dlp
    command = ["yt-dlp", "-f", "140,18,22", "--get-url", link]
    result = subprocess.run(command, capture_output=True, text=True)
    urls = result.stdout.strip().split("\n")
    print (urls)
    tcmd = ["yt-dlp", "-e", link]
    rtit = subprocess.run(tcmd, capture_output=True, text=True)
    tt = rtit.stdout.strip().split("\n")[0]
    title = str(tt)
    print(title)
    x = ["audio m4a", "Video 360p", "Video 720p"]
    n = [".m4a", ".mp4",".mp4"]
    vid = get_video_id(link)
    print(vid) 
    t_url = f"https://i.ytimg.com/vi/{vid}/maxresdefault.jpg"

    print(t_url)
    # Render the output page and pass the download links to it
    return render_template("output.html", urls=urls,x =x,t_url = t_url,n=n,title=title)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get(
        "PORT", 5000), use_reloader=True, threaded=True)
