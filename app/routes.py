from flask import render_template, request, redirect, url_for
from app import app, STORE_PATH
from app.JsonManager import JsonManager



@app.route("/", methods=["GET"])
def index():
    with open(STORE_PATH + "data.txt", 'r', encoding='utf-8') as file:
        content = file.read()
    return render_template("home.html", content=content)



@app.route("/add_text", methods=["GET", "POST"])
def add_text():
    if request.method != "POST":
        return render_template("add_text.html")
    with open(STORE_PATH + "data.txt", 'a', encoding='utf-8') as file:
        file.write(request.form.get('new_text', '') + '\n')
    return redirect(url_for('index'))



@app.route("/add_note", methods=["GET", "POST"])
def add_note():
    if request.method != "POST":
        return render_template("add_note.html")
    data = { "title": request.form["title"], "choice": request.form["choice"], "answer": request.form["answer"] }
    JsonManager("note.json").setData(data)
    return redirect(url_for('add_note'))



@app.route("/show_note", methods=["GET"])
def show_note():
    return render_template("show_note.html", data=JsonManager("note.json").getData())



@app.errorhandler(404)
def page_not_found(error):
    return 'Request not found. <a href="/">back to home</a>', 404
