#!/usr/bin/python
import os
import json
import shutil
import sys
from datetime import datetime

from os.path import join

# update papaths.py with your paths
from papaths import PA_DATA_PATH

if not os.path.isdir(PA_DATA_PATH):
  print("\nCheck your PA_DATA_PATH in papaths.py: " + PA_DATA_PATH + "\n")
  sys.exit()
  
MOD_NAME = "com.pa.legion-expansion"

SERVER_MOD_NAME = MOD_NAME + ".server"
CLIENT_MOD_NAME = MOD_NAME + ".client"

SERVER_MOD_PATH = os.path.join(PA_DATA_PATH,"server_mods",SERVER_MOD_NAME,"")
CLIENT_MOD_PATH = os.path.join(PA_DATA_PATH,"mods",CLIENT_MOD_NAME,"")

OLD_MOD_NAME = "com.pa.legionfaction"

OLD_SERVER_MOD_NAME = OLD_MOD_NAME + ".server"
OLD_CLIENT_MOD_NAME = OLD_MOD_NAME + ".client"

OLD_SERVER_MOD_PATH = os.path.join(PA_DATA_PATH,"server_mods",OLD_SERVER_MOD_NAME,"")
OLD_CLIENT_MOD_PATH = os.path.join(PA_DATA_PATH,"mods",OLD_CLIENT_MOD_NAME,"")

NOW = datetime.today()

BACKUPS_PATH = os.path.join(PA_DATA_PATH,"legion-expansion-backups")
BACKUPS_NOW_PATH = os.path.join(BACKUPS_PATH, NOW.isoformat("-") ).replace(":","-")
OLD_BACKUPS_PATH = os.path.join(PA_DATA_PATH,"legion-faction-backups")

print(BACKUPS_PATH,"\n")

if os.path.isdir(OLD_BACKUPS_PATH):
  shutil.move(OLD_BACKUPS_PATH,BACKUPS_PATH)
  
# server mod

print(SERVER_MOD_PATH)

if os.path.isdir(OLD_SERVER_MOD_PATH):
  shutil.move(OLD_SERVER_MOD_PATH,BACKUPS_NOW_PATH)
  
if os.path.isdir(SERVER_MOD_PATH):
  shutil.move(SERVER_MOD_PATH,BACKUPS_NOW_PATH)

os.mkdir(SERVER_MOD_PATH)

shutil.copy("./modinfo.json",SERVER_MOD_PATH)

shutil.copytree( "./pa", os.path.join(SERVER_MOD_PATH, "pa"))
shutil.copytree( "./ui", os.path.join(SERVER_MOD_PATH, "ui"))

# client mod

print(CLIENT_MOD_PATH)

if os.path.isdir(OLD_CLIENT_MOD_PATH):
  shutil.move(OLD_CLIENT_MOD_PATH,BACKUPS_NOW_PATH)

if os.path.isdir(CLIENT_MOD_PATH):
  shutil.move(CLIENT_MOD_PATH,BACKUPS_NOW_PATH)

print("\nREFRESH PAMM and RESTART PA\n")
