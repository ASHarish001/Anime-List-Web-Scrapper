from flask import Flask, render_template
from scrapper import fetch_episodes

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')    

@app.route("/<name>")
def display_episodes(name):
    episodes = fetch_episodes(name)
    name = name.split('-')
    s = ''
    for word in name:
        s += word.capitalize() + ' '

    name = s   
    return render_template('episodes.html', episodes=episodes, anime=name)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)