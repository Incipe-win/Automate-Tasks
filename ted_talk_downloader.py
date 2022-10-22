from unittest import result
from matplotlib.font_manager import json_load
import requests
from bs4 import BeautifulSoup
import re
import sys
import json

if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    sys.exit("Error: Please enter the TED Talk URL")

# url = "https://www.ted.com/talks/jia_jiang_what_i_learned_from_100_days_of_rejection"
# url = "https://www.ted.com/talks/ken_robinson_says_schools_kill_creativity"

r = requests.get(url)
print("Download about to start")
soup = BeautifulSoup(r.content, features="lxml")

for val in soup.findAll("script"):
    relu = r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>'
    result = re.findall(relu, str(val), re.M | re.S)
    if result:
        break

result_json = json.loads(json.loads(result[0])[
                         "props"]["pageProps"]["videoData"]["playerData"])
mp4_url = result_json["resources"]["h264"][0]["file"]
print("Downloading video from ..... " + mp4_url)
file_name = mp4_url.split("/")[len(mp4_url.split("/")) - 1]
print("Storing video in ..... " + file_name)

r = requests.get(mp4_url)

with open(file_name, "wb") as f:
    f.write(r.content)

# Alternate mthod
# urlretrieve(mp4_url, file_name)

print("Download Process finished")
