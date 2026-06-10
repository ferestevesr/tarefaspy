from projetoti102 import database, app
from projetoti102.models import Usuario, Foto

with app.app_context():
    database.create_all()