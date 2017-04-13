import random
from flask import Flask, session, render_template, flash, jsonify

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
            'symbol': 2,
            'weight': 2,
            'style_rank': 'rank-2'
        },
        {
            'name': 'Three',
            'rank': 3,
            'symbol': 3,
            'weight': 3,
            'style_rank': 'rank-3'
        },
        {
            'name': 'Four',
            'rank': 4,
            'symbol': 4,
            'weight': 4,
            'style_rank': 'rank-4'
        },
        {
            'name': 'Five',
            'rank': 5,
            'symbol': 5,
            'weight': 5,
            'style_rank': 'rank-5'
        },
        {
            'name': 'Six',
            'rank': 6,
            'symbol': 6,
            'weight': 6,
            'style_rank': 'rank-6'
        },
        {
            'name': 'Seven',
            'rank': 7,
            'symbol': 7,
            'weight': 7,
            'style_rank': 'rank-7'
        },
        {
            'name': 'Eight',
            'rank': 8,
            'symbol': 8,
            'weight': 8,
            'style_rank': 'rank-8'
        },
        {
            'name': 'Nine',
            'rank': 9,
            'symbol': 9,
            'weight': 9,
            'style_rank': 'rank-9'
        },
        {
            'name': 'Ten',
            'rank': 10,
            'symbol': 10,
            'weight': 10,
            'style_rank': 'rank-10'
        },
        {
            'name': 'Jack',
            'rank': 11,
            'symbol': 'J',
            'weight': 10,
            'style_rank': 'rank-j'
        },
        {
            'name': 'Queen',
            'rank': 12,
            'symbol': 'Q',
            'weight': 10,
            'style_rank': 'rank-q'
        },
        {
            'name': 'King',
            'rank': 13,
            'symbol': 'K',
            'weight': 10,
            'style_rank': 'rank-k'
        },
        {
            'name': 'Ace',
            'rank': 14,
            'symbol': 'A',
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

@app.route('/_first_step', methods=['GET', 'POST'])
def first_step():
    first_card = draw_card()
    if guess_color == first_card['suit']['color']:
        second_step(first_card)
    else:
        first_step()

@app.route('/_second_step', methods=['GET', 'POST'])
def second_step(first_card):
    second_card = draw_card()
    if guess_high_low == 'high':
        if second_card['face']['rank'] > first_card['face']['rank']:
            third_step(first_card, second_card)
        elif second_card['face']['rank'] == first_card['face']['rank']:
            first_step()
        else:
            first_step()

    elif guess_high_low == 'low':
        if second_card['face']['rank'] < first_card['face']['rank']:
            third_step(first_card, second_card)
        elif second_card['face']['rank'] == first_card['face']['rank']:
            first_step()
        else:
            first_step()



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

