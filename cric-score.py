import requests, json, time, sys, select, os, pynotify
from pprint import pprint

def display(title, msg) :
    if pynotify.init("My Application Name"):
        n = pynotify.Notification(title, msg)
        n.set_timeout(1)
        n.show()


matches = requests.get("http://cricapi.com/api/cricket/")
parsed_data = matches.json()
size = len(parsed_data["data"])

os.system('cls' if os.name == 'nt' else 'clear')
print "\nSelect the match from the options :\n\n"
for i in range(0,size):
    print( str(i+1) + " " + parsed_data["data"][i]["description"])

choice = (int)(raw_input("\n\nEnter Choice :\n"))

id = parsed_data["data"][choice-1]["unique_id"]

score = " "
details = " "

while True:
    link = "http://cricapi.com/api/cricketScore?unique_id=" + str(id)
    stats = requests.get(link)
    parsed_stats = stats.json()

    new_details = parsed_stats["innings-requirement"]
    new_score = parsed_stats["score"]
    
    if score != new_score :
	if details != new_details :
           #print new_details
	   details = new_details
        #print new_score +"\n"
        display(new_details, new_score)
        score = new_score
        
    if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        line = raw_input()
        break
    
    time.sleep(5)
