import os
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))

database_file = "sqlite:///{}".format(os.path.join(project_dir, "bookdatabsae.db"))

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(80),unique = True, nullable = False)
    autor = db.Column(db.String(80), nullable = False)
    num_pags = db.Column(db.Integer, nullable = False)
    editora = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return "<Title: {}>".format(self.title)
    

@app.route('/', methods = ["GET", "POST"])
def home():
    books = None
    if request.form:
        try:
            book = Book(title=request.form.get("title"))
            db.session.add(book)
            db.session.commit()
        except Exception as e:
            print("Failed ro add book")
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