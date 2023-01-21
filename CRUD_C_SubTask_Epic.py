from multiprocessing import parent_process
from tkinter import E
from jira import JIRA
from jira.exceptions import JIRAError

options = {'server': 'https://accountid.atlassian.net/'}
usr = 'userid'
api = "apikey"

try:
    jira = JIRA(options=options, basic_auth=(usr, api))
except JIRAError as e:
    if e.status_code == 401:
        raise ValueError("Login to JIRA failed.")
    else:
        raise ValueError(e)

issue = "XXX-24"
project_key = "XXX"
start_item = "2022-01-03T11:50:21.658+0900"
end_item = "2022-02-31T11:50:21.658+0900"
try:
    subtask_one = {
        'project' : { 'key' : project_key },
        'summary' : 'Subtask 1',
        'description' : 'サブタスク１',
        'issuetype' : { 'name' : 'バグ' },
        'parent' : { 'key' : issue},
        'assignee' : { 'name' : 'user.name'},
        'customfield_10029' : '2022-03-07T11:50:21.658+0900',
        'customfield_10030' : '2022-05-10T11:50:21.658+0900',
    }
    subtask_two = {
        'project' : { 'key' : project_key },
        'summary' : 'Subtask 2',
        'description' : 'サブタスク２',
        'issuetype' : { 'name' : 'ストーリー' },
        'parent' : { 'key' : issue},
        'assignee' : { 'name' : 'user.name'},
        'customfield_10029' : '2022-03-04T11:50:21.658+0900',
        'customfield_10030' : '2022-05-31T11:50:21.658+0900',
    }
    subtask_three = {
        'project' : { 'key' : project_key },
        'summary' : 'Subtask 3',
        'description' : 'サブタスク３',
        'issuetype' : { 'name' : 'バグ' },
        'parent' : { 'key' : issue},
        'assignee' : { 'name' : 'user.name'},
        'customfield_10029' : '2022-03-10T11:50:21.658+0900',
        'customfield_10030' : '2022-03-21T11:50:21.658+0900',
    }

    if len(issue) > 0 and len(issue) <= 7:
        subtasks = [subtask_one, subtask_two, subtask_three]
        for task in subtasks:
            child = jira.create_issue(fields=task)
            print("created child: " + child.key)
    elif len(issue) == 0:
        pass
    else:
        print(issue)

except Exception as e:
    print(e)
