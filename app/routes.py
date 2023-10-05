from flask import render_template, request, redirect, url_for
from app import app
import os , json

# ... (โค้ดที่มีอยู่)

@app.route("/", methods=["GET"])
def index():
    file_path = os.path.join(os.getcwd(), 'data.txt')
    
    # อ่านข้อมูลจากไฟล์ data.txt และนำมาแสดง
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return render_template("home.html", content=content)

@app.route("/search", methods=["POST", "GET"])
def search_text():
    if request.method == "POST":
        search_query = request.form.get('search_query', '')
    else:
        search_query = request.args.get('search_query', '')

    file_path = os.path.join(os.getcwd(), 'data.txt')
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        search_result = [line for line in content.split('\n') if search_query in line]

    return render_template("search_result.html", search_result=search_result, search_query=search_query)


@app.route("/add_text", methods=["GET"])
def add_text():
    return render_template("add_text.html")

@app.route("/note_check", methods=["GET"])
def note_check():
    return render_template("note_check.html")

@app.route("/add_to_data", methods=["POST"])
def add_to_data():
    new_text = request.form.get('new_text', '')

    # Append the new text to the data.txt file
    file_path = os.path.join(os.getcwd(), 'data.txt')
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write('\n' + new_text)

    # Redirect to the home page to display the updated content
    return redirect(url_for('index'))

data = []  # นิยามตัวแปร data ใน global scope

@app.route('/save_note', methods=['POST'])
def save_note():
    global data  # อ้างถึงตัวแปร data ใน global scope
    note_data = request.get_json()
    data.append(note_data)
    save_to_json()
    return 'Note saved successfully.'

# ฟังก์ชันบันทึกข้อมูลลงในไฟล์ JSON
def save_to_json():
    global data
    with open('note.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)


@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404
