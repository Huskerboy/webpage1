import random
from flask import Flask, render_template, flash, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def homepage():
    return render_template("main.html")


@app.route('/ride_bus', methods=['GET', 'POST'])
def ridebus():
    return render_template('ride.html')


@app.route('/gwent', methods=['GET', 'POST'])
def gwent():
    return render_template('gwent.html')


@app.route('/resume', methods=['GET', 'POST'])
def resume():
    return render_template('resume.html')


@app.route('/user/<name>', methods=['GET', 'POST'])
def user(name):
    return render_template(user.html, name=name)


@app.route('/_draw_card', methods=['GET', 'POST'])
def draw_card():
    suits = _get_suits()
    faces = _get_faces()

    face = random.choice(faces)
    suit = random.choice(suits)

    card = {
        'face': face,
        'suit': suit,
        'style_name': suit,
        'style_rank': face,
    }
    return jsonify(card)


def _get_suits():
    suits = [
        {
            'name': 'Clubs',
            'color': 'black',
            'style_name': 'clubs'
        },
        {
            'name': 'Spades',
            'color': 'black',
            'style_name': 'spades'
        },
        {
            'name': 'Diamonds',
            'color': 'red',
            'style_name': 'diams'
        },
        {
            'name': 'Hearts',
            'color': 'red',
            'style_name': 'hearts'
        },
    ]

    return suits


def _get_faces():
    faces = [
        {
            'name': 'Two',
            'rank': 2,
            'weight': 2,
            'style_rank': 'rank-2'
        },
        {
            'name': 'Three',
            'rank': 3,
            'weight': 3,
            'style_rank': 'rank-3'
        },
        {
            'name': 'Four',
            'rank': 4,
            'weight': 4,
            'style_rank': 'rank-4'
        },
        {
            'name': 'Five',
            'rank': 5,
            'weight': 5,
            'style_rank': 'rank-5'
        },
        {
            'name': 'Six',
            'rank': 6,
            'weight': 6,
            'style_rank': 'rank-6'
        },
        {
            'name': 'Seven',
            'rank': 7,
            'weight': 7,
            'style_rank': 'rank-7'
        },
        {
            'name': 'Eight',
            'rank': 8,
            'weight': 8,
            'style_rank': 'rank-8'
        },
        {
            'name': 'Nine',
            'rank': 9,
            'weight': 9,
            'style_rank': 'rank-9'
        },
        {
            'name': 'Ten',
            'rank': 10,
            'weight': 10,
            'style_rank': 'rank-10'
        },
        {
            'name': 'Jack',
            'rank': 11,
            'weight': 10,
            'style_rank': 'rank-j'
        },
        {
            'name': 'Queen',
            'rank': 12,
            'weight': 10,
            'style_rank': 'rank-q'
        },
        {
            'name': 'King',
            'rank': 13,
            'weight': 10,
            'style_rank': 'rank-k'
        },
        {
            'name': 'Ace',
            'rank': 14,
            'weight': 11,
            'style_rank': 'rank-a'
        },
    ]

    return faces

"""
def draw_card():
    card = {
        "face": "ace",
        "suit": "spades"
    }
    return jsonify(card)
"""

@app.route('/view_card', methods=['GET', 'POST'])
def view_card():
    return render_template('view.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == ("__main__"):
    app.run(debug=True)

