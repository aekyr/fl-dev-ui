from json.tool import main
from app import app
from flask import render_template, redirect, request, url_for
from flutils import get_tasks, group_tasks_by_date


@app.route('/')
def redir():
    return redirect(url_for('mainpage'))

@app.route('/theseus', methods=['GET', 'POST'])
def mainpage():
    if request.method == 'POST':
        print(request.data)
    tasks, taskgroups = get_tasks()
    return render_template('projectmain.html', num_cols=12//len(taskgroups), tasks=tasks, taskgroups=taskgroups, len=len)

@app.route('/theseusgroups')
def tgview():
    # taskgroups_desired = request.args.get('tgs').split(';')
    taskgroups_desired = request.args.getlist('tgs')
    print(taskgroups_desired)
    tasks, taskgroups = get_tasks()
    taskgroups = {i:taskgroups[i] for i in taskgroups if taskgroups[i] in taskgroups_desired}
    tasks = [task for task in tasks if task['data']['group'] in taskgroups.keys()]

    tasks, tgcategorys  = group_tasks_by_date(tasks)
    return render_template('taskgroupview.html', num_cols=12//len(tgcategorys), tasks=tasks, tgcategorys=tgcategorys, taskgroups=taskgroups, len=len)