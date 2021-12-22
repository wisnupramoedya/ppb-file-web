from app import app, db
from models.presence import Presence

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Presence': Presence}