import os
from flask import Flask, request, render_template, redirect, url_for
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

@app.route("/add-rule", methods=["POST"])
def add_rule():
    new_rule = model.Rule()
    new_rule.id = int(request.form.get("id"))
    new_rule.title = request.form.get("title")
    new_rule.description = request.form.get("description")
    new_rule.source = request.form.get("source")
    new_rule.subject_id = int(request.form.get("subject"))
    new_rule.knowledge_level = request.form.get("knowledge_level")
    model.session.add(new_rule)
    model.session.commit()


    print new_rule

    return redirect(url_for('list_rules'))


@app.route("/add-question", methods=["GET"])
def list_questions():
    questions = model.session.query(model.Question).all()

    return render_template("question-list.html",
                           questions=questions)

@app.route("/add-question", methods=["POST"])
def add_question():
    new_question = model.Question()
    new_question.id = int(request.form.get("id"))
    new_question.rule_id = int(request.form.get("rule"))
    new_question.question = request.form.get("question")
    new_question.answer = request.form.get("answer")
    new_question.ranking = int(request.form.get("ranking"))
    new_question.question_type = request.form.get("question_type")
    model.session.add(new_question)
    model.session.commit()


    print new_question.rule

    return redirect(url_for('list_questions'))


if __name__ == "__main__":
    model.db.init_app(app)

    PORT = int(os.environ.get("PORT", 5001))
    DEBUG = "NO_DEBUG" not in os.environ
    app.run(debug=DEBUG, host="0.0.0.0", port=PORT)