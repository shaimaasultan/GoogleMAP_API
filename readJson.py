import os
import json

def prase_source_data(Query):
    folderNAme = "C:\\map\\Files\\"
    sourceFolder = folderNAme+"Source data\\"+Query+"\\"
    ParsedFolder = folderNAme+"Parsed data\\"

    if not os.path.exists(sourceFolder):
        print("this Query is not executed Yet")
        return

    try:
        path = ParsedFolder+Query+".txt"
        final = open(path,"w" , encoding='utf-8')
    except FileNotFoundError:
        print("please check your parsed Data path")


    for filename in os.listdir(sourceFolder):
        try:
            path = sourceFolder+filename
            print(path)
            response = open(path , "r")
        except FileNotFoundError:
            print("please check your source Data path")
        st=''
        try:
            st = json.loads(response.read())
            for ListItem in st["results"]:
                final.write("Name : {} |  FormattedAddress : {} ".format( ListItem["name"] ,  dict(ListItem.items()).get("formatted_address")))
        except:
            pass

Query ="bowling_alley" #"drugstore"        
prase_source_data(Query)