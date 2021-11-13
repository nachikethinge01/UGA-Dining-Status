from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import date
import calendar
import requests
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog


gui = Tk()
gui.withdraw()
user_dining = simpledialog.askstring(title="Test",prompt="What dining's status do you want?")
user_dining = user_dining.replace(" ", "")


my_date = date.today()
weekday = calendar.day_name[my_date.weekday()]
#messagebox.showinfo('information', weekday)




url = "https://apps.auxiliary.uga.edu/Dining/OccupancyCounter/api/occupancy.php"
try:
    page = urlopen(url)
except:
    print("Error opening the URL")

soup = BeautifulSoup(page, 'html.parser')

content = soup.find('\"Bolton\"')

#print(soup)

r = requests.get(url)
data = r.json()
lst = list(data.values())

dining_halls = lst[3]

dining_halls_keys = list(dining_halls)

availability = list(dining_halls.values())


bolton = availability[0]
village_summit = availability[1]
o_house = availability[2]
snelling = availability[3]
niche = availability[4]




bolton_list = list(bolton.values())
bolton_num = bolton_list[0]

village_summit_list = list(village_summit.values())
village_summit_num = village_summit_list[0]

o_house_list = list(o_house.values())
o_house_num = o_house_list[0]

snelling_list = list(snelling.values())
snelling_num = snelling_list[0]

niche_list = list(niche.values())
niche_num = niche_list[0]

bolton_open = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
village_open = bolton_open
ohouse_open = bolton_open[0:5]
snelling_open = bolton_open[0:5]
niche_open = bolton_open[0:5]







if(user_dining.lower() == "bolton" and weekday in bolton_open):
    print(100 - bolton_num)
    messagebox.showinfo('information', "Bolton has " + str(100 - bolton_num) + "% occupacy left")

elif(user_dining.lower() == "villagesummit" and weekday in village_open):
    print(100 - village_summit_num)
    messagebox.showinfo('information', "Village Summit has " + str(100 - village_summit_num) + "% occupacy left")

elif(user_dining.lower() == "ohouse" and weekday in ohouse_open):
    print(100 - o_house_num)
    messagebox.showinfo('information', "O House has " + str(100 - o_house_num) + "% occupacy left")

elif(user_dining.lower() == "snelling" and weekday in snelling_open):
    print(100 - snelling_num)
    messagebox.showinfo('information', "Snelling has " + str(100 - snelling_num) + "% occupacy left")

elif(user_dining.lower() == "niche" and weekday in niche_open):
    print(100 - niche_num)
    messagebox.showinfo('information', "Niche has " + str(100 - niche_num) + "% occupacy left")
else:
    
    messagebox.showinfo('information', "This Dining is closed today. Try Bolton or Village Summit")





