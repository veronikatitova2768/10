from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Список задач
task_list = []

@app.route('/')
def index():
    return redirect(url_for('show_tasks'))

@app.route('/tasks')
def show_tasks():
    return render_template('tasks.html', tasks=task_list)

@app.route('/add_task', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        task = request.form.get('task')
        if task:
            task_list.append(task)
        return redirect(url_for('show_tasks'))
    return render_template('add_task.html')

if __name__ == '__main__':
    app.run(debug=True)
