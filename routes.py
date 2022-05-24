from json.tool import main
from app import app
from flask import render_template, redirect, request, url_for
from flutils import get_tasks, group_tasks_by_date


@app.route('/')
@app.route('/theseus')
def redir():
    return redirect(url_for('mainpage', projectname = 'internal'))

@app.route('/theseus/<projectname>', methods=['GET', 'POST'])
def mainpage(projectname):
    if request.method == 'POST':
        print(request.data)
    tasks, taskgroups = get_tasks(projectname=projectname)
    return render_template('theseus/projectmain.html', num_cols=12//len(taskgroups), tasks=tasks, taskgroups=taskgroups, len=len, projectname=projectname)

@app.route('/theseus/<projectname>/<mode>')
def tgview(projectname, mode):
    # taskgroups_desired = request.args.get('tgs').split(';')
    taskgroups_desired = request.args.getlist('tgs')
    tasks, taskgroups = get_tasks(projectname=projectname)

    if len(taskgroups_desired) != 1 or 'all' not in taskgroups_desired:
        taskgroups = {i:taskgroups[i] for i in taskgroups if taskgroups[i] in taskgroups_desired}
    tasks = [task for task in tasks if task['data']['group'] in taskgroups.values()]

    if mode == 'date':
        tasks, tgcategorys  = group_tasks_by_date(tasks)
    return render_template('theseus/taskgroupview.html', num_cols=12//len(tgcategorys), tasks=tasks, tgcategorys=tgcategorys, taskgroups=taskgroups, len=len)