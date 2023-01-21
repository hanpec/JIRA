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
    newIssue = jira.create_issue(
        project = 'XXX',
        summary = 'あいうえお',
        description = 'あーーーーー',
        issuetype = {'name':'バグ'}
    )
except Exception as e:
    print(e)
print(newIssue.key)
