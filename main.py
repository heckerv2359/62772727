import requests
import json
import random
import threading
import sys
import os
import colorama
from colorama import Fore, init
sys.tracebacklimit = 0
os.system("title adv roblox gen")

def has_repeated_letters(s):
  for i in range(len(s)-1):
    if s[i] == s[i+1]:
      return True
  return False

def gen():
  try:
    id = random.randint(11900000, 13100000)
    r = requests.get(f"https://rblx.trade/api/v2/users/{id}/last-online", data={'excludeBannedUsers': True})
    data = r.json()
    if "error" in data or r.status_code != 200:
      #print(f"Invalid UID {id}")
      1+1
    else:
      last = data["lastOnline"][:4]
      username = requests.get(f"https://users.roblox.com/v1/users/{id}").json()["name"]
      if (int(last) == 2010) or (int(last) == 2010):
        if (len(username) == 20) and not has_repeated_letters(username):
          print(Fore.GREEN+f"2010 USER FOUND!  {last}    {username}  {id}  ")
          open('usernames.txt', 'a').write(f"{username}\n")
          open('login.txt', 'a').write(f"{username}:l0l0l0l:{id}\n")
      else:
        if not username.startswith("roblox_user") and (len(username) == 20) and not has_repeated_letters(username):
          print(Fore.RED + f"user {username} lastonline {last} {id}")
  except KeyError:
    pass
    
x = 0;
while (x < 1):
  if threading.active_count() <= int("500"):
    threading.Thread(target=gen).start()