from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Pratyu$1rao@localhost:3306/LangLearn'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Import your models here
from models import Lesson, Vocabulary, GrammarRule, Exercise, UserProgress, Achievement

# Routes
@app.route('/api/lessons', methods=['GET'])
def get_lessons():
    lessons = Lesson.query.all()
    lessons_list = [{'lss_id': lesson.lss_id, 'lang_id': lesson.lang_id, 'title': lesson.title, 'content': lesson.content} for lesson in lessons]
    return jsonify(lessons_list)

@app.route('/api/vocabulary/<int:lang_id>', methods=['GET'])
def get_vocabulary(lang_id):
    vocabulary = Vocabulary.query.filter_by(lang_id=lang_id).all()
    vocabulary_list = [{'word_id': word.word_id, 'lang_id': word.lang_id, 'word': word.word, 'definition': word.definition, 'example': word.example} for word in vocabulary]
    return jsonify(vocabulary_list)

@app.route('/api/grammarrules/<int:lang_id>', methods=['GET'])
def get_grammar_rules(lang_id):
    grammar_rules = GrammarRule.query.filter_by(lang_id=lang_id).all()
    grammar_rules_list = [{'rule_id': rule.rule_id, 'lang_id': rule.lang_id, 'rule': rule.rule, 'example': rule.example} for rule in grammar_rules]
    return jsonify(grammar_rules_list)

@app.route('/api/exercises/<int:lang_id>', methods=['GET'])
def get_exercises(lang_id):
    exercises = Exercise.query.filter_by(lang_id=lang_id).all()
    exercises_list = [{'excs_id': exc.excs_id, 'lang_id': exc.lang_id, 'lss_id': exc.lss_id, 'title': exc.title, 'question': exc.question, 'options': exc.options, 'crct_optn': exc.crct_optn} for exc in exercises]
    return jsonify(exercises_list)

@app.route('/api/userprogress/<int:user_id>', methods=['GET'])
def get_user_progress(user_id):
    user_progress = UserProgress.query.filter_by(user_id=user_id).all()
    user_progress_list = [{'pgs_id': progress.pgs_id, 'user_id': progress.user_id, 'lss_id': progress.lss_id, 'completed': progress.completed, 'score': progress.score, 'timestamp': progress.timestamp} for progress in user_progress]
    return jsonify(user_progress_list)

@app.route('/api/achievements/<int:user_id>', methods=['GET'])
def get_achievements(user_id):
    achievements = Achievement.query.filter_by(user_id=user_id).all()
    achievements_list = [{'ach_id': achievement.ach_id, 'user_id': achievement.user_id, 'name': achievement.name, 'description': achievement.description, 'timestamp': achievement.timestamp} for achievement in achievements]
    return jsonify(achievements_list)

if __name__ == '__main__':
    app.run(debug=True)
