from flask import Flask, request,jsonify
from flask_cors import CORS

app = Flask (__name__)
CORS(app)

@app.route("/welcome_page", methods=["GET"])
def welcome_page():
    return """
<!DOCTYPE html>
    <html>
    <head>
        <title>Welcome...</title>
    </head>
    <body>
        <header>
            <h1 style="color: black; text-align: center;">I'm Bob, and this... is my space</h1>
        </header>
        <p>Welcome to my unique space, Alice</p>
        <section>
            <p style="background-color: orange;">Let's talk about me</p>
            <select onclick="loadPage()"></select>
        </section>
        <section>
            <p style="background-color: gold;">Now... let's talk business</p>
        </section>
        <footer>
            <p> Author: Bob</p>
            <p><a href="mailto:2507143.@leedstrinity.ac.uk">2507143.@leedstrinity.ac.uk></a></p>
            <p><ul id="fruitList"></ul></p>
        </footer>
    </body>
</html>
"""

@app.route("/api/fruits", methods=["GET"])
def get_fruits():
    fruits = ["Orange", "Strawberry", "Tangerine", "Apple"]
    return  jsonify(fruits)

@app.route('/api/data', methods=['POST']) 
def receive_data():
    data = request.json
    name = data.get("name") 
    return jsonify({"response": f"Hello {name}, data received!"}) 

@app.route("/api/profile", methods=["GET"])
def get_profile():
    profile = {
        "name": "Yam-Yam",
        "age": 20,
        "course": "Web Technologies",
        "level": "Level 3",
        "department": "Computer Science",
        "photo": "https://cdna.artstation.com/p/assets/images/images/025/032/400/large/boris-au-barbados-lupus-rex-300.jpg?1584372370"
    }
    return jsonify(profile)

@app.route("/calculate", methods=["POST"])
def calculate():
    numbers = request.json.get("numbers")
    average = sum(numbers) / len(numbers)
    return jsonify({"average": average})

if __name__ == '__main__':
    app.run(port=5000, debug=True) 
