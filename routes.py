from flask import  Flask, render_template
from models import db
from forms import SignupForm


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/find_a_place'
db.init_app(app)

app.secret_key = "development key"

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/signup")
def signup():
    form = SignupForm()
    return render_template('signup.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
