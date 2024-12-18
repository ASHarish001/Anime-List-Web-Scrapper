from flask import Flask, url_for, redirect, render_template, request
from scrapper import fetch_episodes

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
@app.route('/anime', methods=['POST', 'GET'])
def anime():
    if request.method == "POST":
        anime_name = request.form['name']
        return redirect(url_for("episodes", name=anime_name))
    else:
        return render_template('anime.html')

@app.route("/<name>", methods=['GET'])
def episodes(name):
    episodes = fetch_episodes(name)
    word_list = name.split(' ')
    name = ''

    for word in word_list:
        name += word.capitalize() + ' '

    return  render_template('episodes.html', anime=name, episodes=episodes)

if __name__ == '__main__':
    app.run(debug=True)