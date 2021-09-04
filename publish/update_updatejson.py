import json
import subprocess

jsonPath = "../updatejson/update.json"

# lol
fullFormat = "updateJsonFullVersionFormat=true" in open("gradle.properties", "r", encoding="utf8").read()

data = json.load(open(jsonPath, "r", encoding="utf8"))
ver = open("version.txt", "r").read()

for gameVer in json.load(open("gameVersions.json", "r")).keys():
    modVer = "{}".format(ver) if not fullFormat else "{}-{}".format(gameVer, ver)
    
    if gameVer not in data:
        data[gameVer] = {}
    
    data[gameVer][modVer] = ""
    data["promos"]["{}-latest".format(gameVer)] = modVer

json.dump(data, open(jsonPath, "w", encoding="utf8"), indent=2)

subprocess.run(["git", "add", jsonPath])
subprocess.run(["git", "commit", "-m", "Update update json"])
subprocess.run(["git", "push"])