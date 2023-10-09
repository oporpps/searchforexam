from flask import jsonify, render_template, request, redirect, url_for
from app import app
import os , json

NOTE_JSON_DIRECTORY = "notes_data"
NOTE_JSON_FILE_PATH = os.path.join(os.getcwd(), NOTE_JSON_DIRECTORY, 'note.json')

@app.route("/", methods=["GET"])
def index():
    file_path = os.path.join(os.getcwd(), 'data.txt')
    print(os.getcwd())
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

@app.route("/test", methods=["GET"])
def test():
    global NOTE_JSON_FILE_PATH

    # Check if the file exists and is not empty
    if os.path.exists(NOTE_JSON_FILE_PATH) and os.path.getsize(NOTE_JSON_FILE_PATH) > 0:
        with open(NOTE_JSON_FILE_PATH, 'r', encoding="utf-8") as f:
            x = json.load(f)
    else:
        x = {}  # Provide a default empty JSON object

    return render_template("test.html", contentx=x)

@app.route("/add_to_data", methods=["POST"])
def add_to_data():
    new_text = request.form.get('new_text', '')

    # Append the new text to the data.txt file
    file_path = os.path.join(os.getcwd(), 'data.txt')
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(new_text + '\n')

    # Redirect to the home page to display the updated content
    return redirect(url_for('index'))

data = []  # นิยามตัวแปร data ใน global scope

app.route('/save_note', methods=['POST'])
def save_note():
    global data

    # Get note data from the request
    note_data = request.get_json()
    print(note_data)  # Print for debugging

    # Append note data to the global data list
    data.append(note_data)

    # Save data to note.json
    save_to_json()

    return 'Note saved successfully.'

# ฟังก์ชันบันทึกข้อมูลลงในไฟล์ JSON
def save_to_json():
    global data
    global NOTE_JSON_FILE_PATH

    # Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(NOTE_JSON_FILE_PATH), exist_ok=True)

    with open(NOTE_JSON_FILE_PATH, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)



@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404
