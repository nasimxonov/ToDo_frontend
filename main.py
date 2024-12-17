from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)

tasks = []


@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add_task():
    task = request.form.get("task")
    if task:
        tasks.append(task)
    return redirect(url_for("index"))


@app.route("/delete/<int:id>")
def delete_task(id):
    if 0 <= id < len(tasks):
        tasks.pop(id)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)


