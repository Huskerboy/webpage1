from flask import Flask, render_template

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


@app.route('/user/<name>', methods=['GET', 'POST'])
def user(name):
    return render_template(user.html, name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == ("__main__"):
    app.run(debug=True)

