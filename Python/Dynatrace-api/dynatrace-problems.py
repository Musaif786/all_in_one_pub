import requests
import json
import pandas as pd
from datetime import datetime
from datetime import timedelta


#token = "dt0c01.24char.TECWGFROZEXGAOFI2D5IJ2KT3AUWOBJUKYK7TGDUHJLFJSXGS5CS33AILL23ZK4Z"

dyna_url = "https://rjt123.live.dynatrace.com"
api_token = "dt0c01.24.TECWGFROZEXGAOFI2D5IJ2KT3AUWOBJUKYK7TGDUHJLFJSXGS5CS33AILL23ZK4Z"


#https://rjt123.live.dynatrace.com/api/v2/apiTokens
def get_problems():
 

  headers = {"Authorization": f"Api-Token {api_token}",
             "totalCount": '10'}
  params = {
    "pageSize": 10, 
    #"from": "2023-12-07T03:05:00Z",  # start date_time
    #"to": "2023-12-07T03:20:00Z",  #  end date_time
    }
  url = f"{dyna_url}/api/v2/problems?status=open"

  try:
    resp = requests.get(url, headers=headers, params=params)
    resp.raise_for_status()
  except Exception as error:
    print(f"Error retrieving problems: {error}")
    return

  data = resp.json()
  
  if not data["problems"]:
    print("No open problems found.")
    return
  prb = data['problems']
  print(f"Found {len(data['problems'])} open problems:")
  #print(prb)

  #Using pandas
  data_list = []
  for problem in data["problems"]:
    # print(problem["displayId"]+"\n")
    # print(problem["title"])
    displayid = problem["displayId"]
    title = problem["title"]
    status = problem['status']
    severityLevel = problem['severityLevel']
    affectedEntities = problem.get('affectedEntities', [{}])[0].get('entityId', {}).get('id', None)
    host = problem.get('affectedEntities', [{}])[0].get('name', {})

    #below for to get data into txt
    # storing = [{
    #   "DisplayId": displayid,
    #   "Title": title
    # }]

    storing = [displayid, title,status,severityLevel,affectedEntities,host]
    data_list.append(storing)
   
  print(data_list)
  #storing data into csv
  df = pd.DataFrame(data_list,columns=["Problem_Number", "Title", "Status","SeverityLevel","EntityId","Host_name"])
  df.to_csv("problems_.csv",index=False)

  #storing data into json file
  for problem in data["problems"]:
    #print(f"- {problem['entityId']} ({problem['entityType']}): {problem['title']}")
    #print(problem)
    with open("problmes.json", "w") as file:
       json.dump(problem,file, indent=4)
    # pass

if __name__ == "__main__":
  get_problems()
