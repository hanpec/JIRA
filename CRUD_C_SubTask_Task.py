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

issue = "ABC-19"
project_key = "ABC"

data = {
    "project":
    {
        "key": project_key
    },
    "parent":
    {
        "key": issue
    },
    "summary": "どうなる？",
    "description": "サブタスクの中にサブサブタスク",
    'issuetype' : { 'name' : 'サブタスク' },
}

try:

    if len(issue) > 0 and len(issue) <= 7:
        subtasks = [data]
        for task in subtasks:
            child = jira.create_issue(fields=task)
            print("created child: " + child.key)
    elif len(issue) == 0:
        pass
    else:
        print(issue)

except Exception as e:
    print(e)
