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

try:
    sprints = jira.sprints(7)
    for sprint in sprints:
        try:
            print("id:" + str(sprint.id))
            print("name:" + sprint.name)
            print("startDate:" + sprint.startDate)
            print("endDate:" + sprint.endDate)
            print("state:" + sprint.state)
            print("originBoardId:" + str(sprint.originBoardId))
        except Exception as e:
            print(e)
except Exception as e:
    print(e)
