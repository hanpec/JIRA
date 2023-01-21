import requests
import json
from jira import JIRA
from jira.exceptions import JIRAError
from jira.resources import GreenHopperResource

options = {'server': 'https://accountid.atlassian.net/',
"agile_rest_path": GreenHopperResource.AGILE_BASE_REST_PATH
}
usr = 'userid'
api = "apikey"

try:
    jira = JIRA(options=options, basic_auth=(usr, api))
except JIRAError as e:
    if e.status_code == 401:
        raise ValueError("Login to JIRA failed.")
    else:
        raise ValueError(e)

SprintName = "Sprint test" # 名前が一緒ならIDのみが加算され、内容は置き換わらない（つまり、何処にできたのか不明）
SprintBoardProjID = 7 # この値が意味不明（現在、ＰＪ＝XXXは1と2が有効で、どっちも作成できる）
SprintStartDay = "2023-01-21T11:50:21.658+0900"
SprintEndDate = "2023-01-31T11:50:21.658+0900"
res = jira.create_sprint(SprintName, SprintBoardProjID, SprintStartDay, SprintEndDate)
print(res)
