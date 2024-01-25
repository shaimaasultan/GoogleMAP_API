import requests
import json
import time
import os

key = "{MAP_API_KEY}"
Query = "bowling_alley" #"drugstore" #"cafe"#"gym"#"hospital" #"doctor"#,Postal_code,health"

relative_path = "C:\\map\\Files\\"
sourceFolder = relative_path+"Source data\\"
filepath =  sourceFolder+Query+"\\"
if not os.path.exists(filepath):
    os.mkdir(filepath)

i = 1
filename = "{}{}.txt".format( filepath+Query , i )

url = "https://maps.googleapis.com/maps/api/place/textsearch/json?type={}&key={}".format(Query , key)
payload={}
headers = {}
response = requests.request("GET", url, headers=headers, data=payload)
print(response.status_code)
res= json.loads(response.text)
sourcefiles = open(filename , "w")
sourcefiles.write(response.text)
time.sleep(1)
while("next_page_token" in res):
    if len(res["next_page_token"]) > 0 :
        Token = res["next_page_token"]
        next_page = url + "&pagetoken="+Token
        payload={}
        headers = {}
        status = 0
        j = 1
        while ( status != 200 and j <= 2):
            time.sleep(2)
            response = requests.request("GET", next_page, headers=headers, data=payload)
            status = response.status_code
            j = j + 1
        i = i + 1
        filename = "{}{}.txt".format( filepath+Query , i )
        file = open(filename, "w+")
        file.write(response.text)
        res= json.loads(response.text)
        if "next_page_token" not in res or ("next_page_token" in res and len(res["next_page_token"]) == 0)  or  i > 4 : 
            break


        