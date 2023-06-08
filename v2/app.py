import os
from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

import forms

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config["SECRET_KEY"] = "dfgsfdgsdfgsdfgsdf"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "data.sqlite"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Father(db.Model):
    __tablename__ = "father"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column("name", db.String)
    surname = db.Column("surname", db.String)
    child_id = db.Column(db.Integer, db.ForeignKey("child.id"))
    child = db.relationship("Child")


class Child(db.Model):
    __tablename__ = "child"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column("name", db.String)
    surname = db.Column("surname", db.String)
    fathers = db.relationship("Father")


@app.route("/new_child", methods=["GET", "POST"])
def new_child():
    db.create_all()
    form = forms.ChildForm()
    if form.validate_on_submit():
        new_child = Child(name=form.name.data, surname=form.surname.data)
        db.session.add(new_child)
        db.session.commit()
        return redirect(url_for("get_all_children"))
    return render_template("add_child.html", form=form)


@app.route("/all_childs", methods=["GET", "POST"])
def get_all_children():
    db.create_all()
    children = Child.query.all()
    return render_template(
        "children.html",
        children=children,
    )


@app.route("/new_father", methods=["GET", "POST"])
def new_parent():
    db.create_all()
    form = forms.FatherForm()
    if form.validate_on_submit():
        print(form.surname.data)
        new_father = Father(
            name=form.name.data, surname=form.surname.data, child_id=form.child.data
        )
        db.session.add(new_father)
        db.session.commit()
        return redirect(url_for("get_all_fathers"))
    return render_template("add_father.html", form=form)


@app.route("/all_fathers", methods=["GET", "POST"])
def get_all_fathers():
    db.create_all()
    fathers = Father.query.all()
    return render_template("all_fathers.html", fathers=fathers)


if __name__ == "__main__":
    app.run(debug=True, port=9000, host="0.0.0.0")
    db.create_all()
