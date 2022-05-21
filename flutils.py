def insert_display_strs(tasks):

        from datetime import datetime
        from math import log10, floor
        current_time = datetime.now()
        round_3sf = lambda x : round(x, 2-int(floor(log10(abs(x)))))
        for task in tasks:
            datetime_end = task.get('time', {}).get('datetime_end', None)
            minleft = (datetime_end - current_time).total_seconds()/60
            hourleft = minleft/60
            daysleft = hourleft/24
            task['time']['timeleft'], task['time']['unit'] = [round_3sf(daysleft), 'D'] if abs(daysleft) > 1 else [round_3sf(hourleft), 'H'] if abs(hourleft) > 1 else [round_3sf(minleft), 'min'] 

            task['info']['assignees_str'] = None
            if task.get('assignees', None):
                if len(task['assignees'][0]) >= 6:
                    print(task['assignees'][0], len(task['assignees'][0]))
                    task['info']['assignees_str'] = f"{len(task['assignees'])} assigned"
                
                else:
                    for i in reversed(range(0, len(task['assignees'])+1)):
                        if len(''.join(task['assignees'][0:i])) < 6:
                            task['info']['assignees_str'] = ', '.join(task['assignees'][0:i]) + (' + {0} more'.format(len(task.get('assignees', [])[i:])) if len(task.get('assignees', [])[i:]) else '')    
                            break



        return tasks

def get_tasks():
    import examples
    tasks = sorted(insert_display_strs(examples.tasks), key=lambda item : item['data']['section'], reverse=True)
    taskgroups = examples.taskgroups
    return tasks, taskgroups


def sort_tasks_by_date(taskgroups, task):
    tgcategorys = {
        1:'Long-Term',
        2:'To-do',
        3:'Late',
        4:'Completed'
    }
    pass