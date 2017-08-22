import random

from flask_login import (LoginManager, login_user, logout_user, login_required, current_user)

from flask import (Flask, session, render_template, flash, jsonify,
                   escape, redirect, url_for, request, g, abort)

import forms
import models

from flask_bcrypt import check_password_hash

DEBUG = True
PORT = 8000
HOST = '0.0.0.0'

app = Flask(__name__)
app.secret_key = 'sadgfiowASDGFAHI357%^&2gakjH$DSD'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except models.DoesNotExist:
        return None


@app.before_request
def before_request():
    """Connect to the database before each request"""
    g.db = models.DATABASE
    g.db.connect()
    g.user = current_user


@app.after_request
def after_request(response):
    """Close the database connection after each request."""
    g.db.close()
    return response


@app.route('/register', methods=('GET', 'POST'))
def register():
    form = forms.RegisterForm()
    if form.validate_on_submit():
        flash("Congrats, you have registered!", "success")
        models.User.create_user(
            username=form.username.data,
            password=form.password.data
        )
        return redirect(url_for('index'))
    return render_template('register.html', form=form)


@app.route('/login', methods=('GET', 'POST'))
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        try:
            user = models.User.get(models.User.username == form.username.data)
        except models.DoesNotExist:
            flash("Your username or password doesn't match!", "error")
        else:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                flash("You've been logged in!", "success")
                return redirect(url_for('index'))
            else:
                flash("Your username or password doesn't match!", "error")
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "success")
    return redirect(url_for('index'))


@app.route('/', methods=['GET', 'POST'])
def index():
    stream = models.Post.select().limit(100)
    return render_template("stream.html", stream=stream)


@app.route('/new_post', methods=('GET', 'POST'))
@login_required
def post():
    form = forms.PostForm()
    if form.validate_on_submit():
        models.Post.create(user=g.user._get_current_object(),
                           content=form.content.data.strip())
        flash("Message posted! Thanks!", "success")
        return redirect(url_for('index'))
    return render_template('post.html', form=form)


@app.route('/stream')
@app.route('/stream/<username>')
def stream(username=None):
    template = 'stream.html'
    if username and username != current_user.username:
        try:
            user = models.User.select().where(models.User.username**username).get()
        except models.DoesNotExist:
            abort(404)
        else:
            stream = user.posts.limit(100)
    else:
        stream = current_user.get_stream().limit(100)
        user = current_user
    if username:
        template = 'user_stream.html'
    return render_template(template, stream=stream, user=user)


@app.route('/post/<int:post_id>')
def view_post(post_id):
    posts = models.Post.select().where(models.Post.id == post_id)
    if posts.count() == 0:
        abort(404)
    else:
        return render_template('stream.html', stream=posts)


@app.route('/follow/<username>')
@login_required
def follow(username):
    try:
        to_user = models.User.get(models.User.username**username)
    except models.DoesNotExist:
        abort(404)
    else:
        try:
            models.Relationship.create(
                from_user=g.user._get_current_object(),
                to_user=to_user
            )
        except models.IntegrityError:
            pass
        else:
            flash("You're now following {}!".format(to_user.username), "success")
    return redirect(url_for('stream', username=to_user.username))


@app.route('/unfollow/<username>')
@login_required
def unfollow(username):
    try:
        to_user = models.User.get(models.User.username**username)
    except models.DoesNotExist:
        abort(404)
    else:
        try:
            models.Relationship.get(
                from_user=g.user._get_current_object(),
                to_user=to_user
            ).delete_instance()
        except models.IntegrityError:
            pass
        else:
            flash("You've unfollowed {}".format(to_user.username), "success")
    return redirect(url_for('stream', username=to_user.username))


@app.route('/view', methods=['GET', 'POST'])
def resume():
    return render_template('view.html')


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
    return card


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


@app.route('/test_route', methods=['POST'])
def test():
    userdata = request.get_json()
    first_card = draw_card()
    if 'guess_color' in userdata:
        if userdata['guess_color'] == first_card['suit']['color']:
            return 'Correct, Your guess was {} and the card was a {} of {}'.format(userdata['guess_color'], first_card['face']['name'], first_card['suit']['name'])
        else:
            return 'Wrong, Your guess was {} and the card was a {} of {}'.format(userdata['guess_color'], first_card['face']['name'], first_card['suit']['name'])
    return "Bad request you dummy"


@app.route('/first_step', methods=['GET', 'POST'])
def first_step():
    userdata = request.get_json()
    first_card = draw_card()
    session['first_card'] = first_card
    if 'guess' in userdata:
        if userdata['guess'] == first_card['suit']['color']:
            score_card = {'value': 'True', 'card': first_card}
            return jsonify(score_card)
        else:
            score_card = {'value': 'False', 'card': first_card}
            return jsonify(score_card)
    return "Bad request you dummy"


@app.route('/second_step', methods=['GET', 'POST'])
def second_step():
    userdata = request.get_json()
    second_card = draw_card()
    session['second_card'] = second_card
    if 'first_card' in session:
        first_card = session.get('first_card')
        if 'guess' in userdata:
            if userdata['guess'] == 'high':
                if second_card['face']['rank'] > first_card['face']['rank']:
                    score_card = {'value': 'True', 'card': second_card}
                    return jsonify(score_card)
                else:
                    score_card = {'value': 'False', 'card': first_card}
                    return jsonify(score_card)
            elif userdata['guess'] == 'low':
                if second_card['face']['rank'] < first_card['face']['rank']:
                    score_card = {'value': 'True', 'card': second_card}
                    return jsonify(score_card)
                else:
                    score_card = {'value': 'False', 'card': first_card}
                    return jsonify(score_card)
            else:
                return "Error with the guess"
        return "Bad request, the seven kingdoms are disappointed."
    return "First card not in session"


@app.route('/third_step', methods=['GET', 'POST'])
def third_step():
    userdata = request.get_json()
    third_card = draw_card()
    session['third_card'] = third_card
    if 'second_card' in session:
        second_card = session.get('second_card')
        first_card = session.get('first_card')
        top = max(first_card['face']['rank'], second_card['face']['rank'])
        bottom = min(first_card['face']['rank'], second_card['face']['rank'])
        if 'guess' in userdata:
            if userdata['guess'] == 'inside':
                if top > third_card['face']['rank'] > bottom:
                    score_card = {'value': 'True', 'card': third_card}
                    return jsonify(score_card)
                else:
                    score_card = {'value': 'True', 'card': third_card}
                    return jsonify(score_card)
            elif userdata['guess'] == 'outside':
                if top < third_card['face']['rank'] or third_card['face']['rank'] < bottom:
                    score_card = {'value': 'True', 'card': third_card}
                    return jsonify(score_card)
                else:
                    score_card = {'value': 'True', 'card': third_card}
                    return jsonify(score_card)
            else:
                return 'False'
        return "Bad request, the seven kingdoms are disappointed."
    return "Second card not in session"


@app.route('/fourth_step', methods=['GET', 'POST'])
def fourth_step():
    userdata = request.get_json()
    fourth_card = draw_card()
    session['fourth_card'] = fourth_card
    if 'guess' in userdata:
        if userdata['guess'] == fourth_card['suit']['name']:
            score_card = {'value': 'True', 'card': fourth_card}
            return jsonify(score_card)
        else:
            score_card = {'value': 'True', 'card': fourth_card}
            return jsonify(score_card)
    return "Bad request, the seven kingdoms are disappointed."


@app.route('/view_card', methods=['GET', 'POST'])
def view_card():
    return render_template('view.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    models.initialize()
    try:
        models.User.create_user(
            username='jmeyer',
            password='password',
            admin=True
        )
    except ValueError:
        pass
    app.run(debug=DEBUG, host=HOST, port=PORT)
