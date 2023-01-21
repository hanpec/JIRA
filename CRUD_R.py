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

assignee = 'userid'
issue_key = "ABC-5"
project_team = "abc"
jql = 'Reporter = "' + assignee + '" AND project = ' + project_team + ' AND issueKey = ' + issue_key
try:
    tickets = jira.search_issues( jql )
    for ticket in tickets:
        print("KEY:" + ticket.key)
        print("タイトル:" + ticket.fields.summary)
        if (ticket.fields.description is None):
            print("説明が未設定です")
        else:
            print("説明:" + ticket.fields.description)
        try:
            print("親タスク:" + ticket.fields.parent.key)
        except:
            print("親タスクはありません")
        print("作成日:" + ticket.fields.created)
        print("更新日:" + ticket.fields.updated)
        print("タイプ:" + ticket.fields.issuetype.name)
        try: 
            print("開始日:" + ticket.fields.customfield_10029)
        except Exception as e:
            if "PropertyHolder" in e.args[0]:
                print("開始日が未設定です")
        try: 
            print("終了日:" + ticket.fields.customfield_10030)
        except Exception as e:
            if "PropertyHolder" in e.args[0]:
                print("終了日が未設定です")
        print("URL:" + "https://accountid.atlassian.net/jira/software/projects/XXX/boards/2?selectedIssue=" + ticket.key)
except Exception as e:
    print(e)
