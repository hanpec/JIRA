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
        print ("Login to JIRA failed.")
    else:
        print ("Login!!")

try:
    projects = jira.projects()
    for project in projects:
        print("KEY:" + project.key)
        print("name:" + project.name)
        print("id:" + project.id)
except Exception as e:
    print(e)
