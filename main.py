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


@app.route("/edit/<int:id>")
def edit(id):
    if 0 <= id < len(tasks):
        task = tasks[id]
    return render_template("edit.html", id=id, task=task)


@app.route("/delete/<int:id>")
def delete_task(id):
    if 0 <= id < len(tasks):
        tasks.pop(id)
    return redirect(url_for("index"))


@app.route("/update/<int:id>", methods=["POST"])
def update(id):
    if id > -1 and id < len(tasks):
        tasks[id] = request.form.get("new_tasks")

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
