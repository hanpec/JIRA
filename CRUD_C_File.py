from tkinter import E
from jira import JIRA
from jira.exceptions import JIRAError
import glob

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
        summary = '添付ファイル',
        description = '添付ファイルの登録',
        issuetype = {'name':'バグ'},
        customfield_10029 = '2023-01-21T11:50:21.658+0900',
        customfield_10030 = '2023-01-31T11:50:21.658+0900',
        )
    filepath = "teams.txt"
    files =  glob.glob(filepath)
    if len(files) >= 0:
        for file in files:
            jira.add_attachment(newIssue,file)
            jira.add_comment(newIssue, 'Required files are Attached!')
except Exception as e:
    print(e)
print(newIssue.key)
