import os
from flask import Flask, request, render_template, redirect
import model
import random

SECRET_KEY = os.environ.get('FLASK_SECRET_KEY', "abcdefg")

app = Flask(__name__)
# DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql:///carolineorsi")
DATABASE_URL = "postgres://dafjsxehbywvux:hmaDRyyu8As6uTU9t1lCahEm5X@ec2-54-204-45-196.compute-1.amazonaws.com:5432/d4qboj00bqn958"
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SECRET_KEY'] = SECRET_KEY


@app.route("/")
def index():
    """ This is the 'cover' page of the site """

    return render_template("index.html")

@app.route("/question")
def get_question():
    rand_key = random.randrange(1, model.session.query(model.Question).count())
    question = model.session.query(model.Question)[rand_key].question
    answer = model.session.query(model.Question)[rand_key].answer

    return render_template("question.html", 
                           question=question,
                           answer=answer)

@app.route("/add-rule", methods=["GET"])
def list_rules():
    rules = model.session.query(model.Rule).all()
    
    return render_template("rule-list.html",
                           rules=rules)


@app.route("/add-question", methods=["GET"])
def list_questions():
    questions = model.session.query(model.Question).all()

    return render_template("question-list.html",
                           questions=questions)

@app.route("/add-question", methods=["POST"])
def add_question():
    # new_question = model.Question()
    # new_question.rule = request.form.get("to") # Need to figure this out
    # new_question.question = request.form.get("question")
    # new_question.answer = request.form.get("answer")
    # new_question.ranking = int(request.form.get("ranking"))
    # new_question.question_type = request.form.get("question-type")


    print request.form
    questions = model.session.query(model.Question).all()

    return render_template("question-list.html",
                           questions=questions)


if __name__ == "__main__":
    model.db.init_app(app)

    PORT = int(os.environ.get("PORT", 5001))
    DEBUG = "NO_DEBUG" not in os.environ
    app.run(debug=DEBUG, host="0.0.0.0", port=PORT)