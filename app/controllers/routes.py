from app import app, database
from flask import render_template, request, redirect, url_for
from app.models.db_models import Tasks


@app.route('/tasks')
@app.route('/')
def home():
    all_tasks = Tasks.query.all()
    return render_template("index.html", tasks_list=all_tasks)


@app.route('/create-task', methods=['POST'])
def create():
    task = Tasks(content=request.form['task-content'], done=False)
    database.session.add(task)
    database.session.commit()
    return redirect(url_for('home'))


@app.route('/delete-task/<id>')
def delete(id):
    deleting_task = Tasks.query.filter_by(id=int(id)).delete()
    database.session.commit()
    return redirect(url_for('home'))


@app.route('/task-done/<id>')
def done(id):
    done_task = Tasks.query.filter_by(id=int(id)).first()
    done_task.done = True
    database.session.commit()
    return redirect(url_for('home'))
