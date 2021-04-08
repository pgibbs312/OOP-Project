from flask import Flask, request, jsonify
from models.scores import Score, ScoreManager
from flask import render_template
from database_manager import DatabaseManager

app = Flask(__name__)
score_manager = ScoreManager()


@app.route('/api/list', methods=["GET"])
def list_all_scores():
    db = DatabaseManager("scores.sqlite")
    return render_template("list.html", scores= db.get_all())