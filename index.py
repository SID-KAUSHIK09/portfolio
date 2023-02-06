from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def about():
    return render_template('about.html')
@app.route("/education")
def education():
    return render_template('education.html')
@app.route("/skills")
def skills():
    return render_template('skills.html')
@app.route("/projects")
def projects():
    return render_template('projects.html')
@app.route("/designs")
def designs():
    return render_template('designs.html')
@app.route("/accomplishments")
def accomplishments():
    return render_template('accomplishments.html')
@app.route("/certifications")
def certifications():
    return render_template('certifications.html')
@app.route("/experience")
def experience():
    return render_template('experience.html')
if __name__=='__main__':
    app.run(debug=True)