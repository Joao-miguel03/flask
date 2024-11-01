from app import app, db

# para criar a tabela no meu banco de dados
with app.app_context():
    db.create_all() 

