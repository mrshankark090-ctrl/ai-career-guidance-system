
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

careers = {
    "python": {
        "career": "Python Developer",
        "skills": ["Python", "SQL", "Git"]
    },
    "web": {
        "career": "Web Developer",
        "skills": ["HTML", "CSS", "JavaScript"]
    },
    "ai": {
        "career": "AI/ML Engineer",
        "skills": ["Python", "Mathematics", "Machine Learning"]
    },
    "data": {
        "career": "Data Analyst",
        "skills": ["Python", "SQL", "Data Visualization"]
    }
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json(silent=True) or {}

    name = data.get("name", "").strip()
    interest = data.get("interest", "")

    if not name or interest not in careers:
        return jsonify({
            "error": "Enter a valid name and interest"
        }), 400

    return jsonify({
        "name": name,
        "career": careers[interest]["career"],
        "skills": careers[interest]["skills"]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
