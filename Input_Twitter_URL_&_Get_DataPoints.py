import urllib.request
from bs4 import BeautifulSoup
from contextlib import suppress
import requests
from datetime import datetime
import csv

page = requests.get("https://twitter.com/noob")
parsed_page = BeautifulSoup(page.content, "html.parser")

data_name = str(parsed_page.find(class_="ProfileHeaderCard-nameLink u-textInheritColor js-nav").get_text()).strip()
data_handle = str("@" + parsed_page.find(class_="u-linkComplex-target").get_text()).strip()

try:
    data_tweets = str(parsed_page.find(class_="ProfileNav-item ProfileNav-item--tweets is-active").find(
        class_="ProfileNav-value").get_text()).strip()
except:
    data_tweets = str("N/A")

try:
    data_following = str(parsed_page.find(class_="ProfileNav-item ProfileNav-item--following").find(
        class_="ProfileNav-value").get_text()).strip()
except:
    data_following = str("N/A")

try:
    data_followers = str(parsed_page.find(class_="ProfileNav-item ProfileNav-item--followers").find(
        class_="ProfileNav-value").get_text()).strip()
except:
    data_followers = str("N/A")

try:
    data_likes = str(parsed_page.find(class_="ProfileNav-item ProfileNav-item--favorites").find(
        class_="ProfileNav-value").get_text()).strip()
except:
    data_likes = str("N/A")

try:
    data_joined = str(parsed_page.find(class_="ProfileHeaderCard-joinDate").get_text()).strip()
except:
    data_joined = str("N/A")


print(data_name)
print(data_handle)
print(data_tweets)
print(data_following)
print(data_followers)
print(data_likes)
print(data_joined)


csv_file = open("test.csv", "w", encoding="utf-8")
columnTitleRow = "Name,Handle,# Of Tweets,Following,Followers,Likes,DateJoined \n"
csv_file.write(columnTitleRow)
csv_file.write(data_name + ",")
csv_file.write(data_handle + ",")
csv_file.write(data_tweets + ",")
csv_file.write(data_following + ",")
csv_file.write(data_followers + ",")
csv_file.write(data_likes + ",")
csv_file.write(data_joined + ",")
csv_file.write("\n")



