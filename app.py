from app import App, db
from app.models import Form, Question, Submission, User, Answer

@App.shell_context_processor
def make_shell_context():
    return {'db': db, 'Answer': Answer, 'Form': Form, 'Question': Question, \
    'Submission': Submission, 'User': User}
