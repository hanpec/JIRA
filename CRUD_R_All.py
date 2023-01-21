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
# ticket.id
# ticket.key
# ticket.self
# ticket.fields.created
# ticket.fields.customfield_10029
# ticket.fields.customfield_10030
# ticket.fields.customfield_10031
# ticket.fields.customfield_10032
# ticket.fields.description
# ticket.fields.issuetype.subtask
# ticket.fields.issuetype.avatarId
# ticket.fields.issuetype.name
# ticket.fields.parent.key
# ticket.fields.summary
# ticket.fields.updated
# ticket.fields.status.name
# ticket.fields.assignee.displayName
# ticket.fields.assignee.emailAddress
# ticket.fields.assignee.active
# ticket.fields.priority.name
# ticket.fields.progress.progress
# ticket.fields.progress.total
# ticket.fields.project.name
# ticket.fields.project.key

# ticket.fields.customfield_10020[0].name
# ticket.fields.customfield_10020[0].startDate
# ticket.fields.customfield_10020[0].endDate
# ticket.fields.customfield_10020[0].state
# ticket.fields.customfield_10020[0].id
# ticket.fields.customfield_10020[0].boardId
# ticket.fields.creator.displayName
# ticket.fields.creator.emailAddress

# len(ticket.fields.subtasks)
# ticket.fields.subtasks[0].key
# ticket.fields.subtasks[0].fields.summary

# ticket.fields.customfield_10015 startDate wbs
# ticket.fields.duedate 期日 wbs

# ticket.fields.labels[0] ラベル
# ticket.fields.customfield_10046 text

try:
    tickets = jira.search_issues( "Reporter = 'name' AND project = 'ABC' ORDER BY key")
    for ticket in tickets:
        try:
            print("KEY:" + ticket.key)
            if (ticket.key == "ABC-2"):
                print("a")
            print("タイトル:" + ticket.fields.summary)
            if (ticket.fields.description is None):
                print("説明が未設定です")
            else:
                print("説明:" + ticket.fields.description)
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
except Exception as e:
    print(e)
