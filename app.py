import os
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from models import*

from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))

database_file = "sqlite:///{}".format(os.path.join(project_dir, "bookdatabsae.db"))

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)

@app.route('/', methods = ["GET", "POST"])
def home():
    books = None
    if request.form:
        try:
            title = request.form.get("title")
            autor = request.form.get("autor")
            editora = request.form.get("editora")
            num_pags = request.form.get("qtd_pag")

            book = Book(title=title, autor = autor, editora = editora, num_pags = num_pags)
            db.session.add(book)
            db.session.commit()

        except Exception as e:
            print("Failed to add book")
            print(e)

    books = Book.query.all()
    return render_template("index.html", books = books)

@app.route("/update", methods = ["POST"])
def updade():
    try:
        newTitle = request.form.get("newTitle")
        oldTitle = request.form.get("oldTitle")
        book = Book.query.filter_by(title = oldTitle).first()
        book.title = newTitle
        db.session.commit()
    except Exception as e:
        print("Couldn't update book title")
        print(e)
    return redirect("/")

@app.route("/delete", methods = ["POST"])
def delete():
    title = request.form.get("title")
    book = Book.query.filter_by(title = title).first()
    db.session.delete(book)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)