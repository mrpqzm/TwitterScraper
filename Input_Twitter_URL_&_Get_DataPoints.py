import urllib.request
from bs4 import BeautifulSoup
from contextlib import suppress
import requests
from datetime import datetime
import csv

page = requests.get("https://twitter.com/tonevays")

with suppress(Exception): parsed_page = BeautifulSoup(page.content, "html.parser")

with suppress(Exception): data_name = str(parsed_page.find(class_="ProfileHeaderCard-nameLink u-textInheritColor js-nav").get_text()).strip()
with suppress(Exception): data_handle = str("@" + parsed_page.find(class_="u-linkComplex-target").get_text()).strip()

with suppress(Exception): data_tweets = str(parsed_page.find(class_="ProfileNav-item ProfileNav-item--tweets is-active").find(class_="ProfileNav-value").get_text()).strip()
with suppress(Exception): data_following = str(parsed_page.find(class_="ProfileNav-item ProfileNav-item--following").find(class_="ProfileNav-value").get_text()).strip()
with suppress(Exception): data_followers = str(parsed_page.find(class_="ProfileNav-item ProfileNav-item--followers").find(class_="ProfileNav-value").get_text()).strip()
with suppress(Exception): data_likes = str(parsed_page.find(class_="ProfileNav-item ProfileNav-item--favorites").find(class_="ProfileNav-value").get_text()).strip()

with suppress(Exception): data_location = str(parsed_page.find(class_="ProfileHeaderCard-locationText u-dir").get_text()).strip().replace(",","")
with suppress(Exception): data_website = str(parsed_page.find(class_="ProfileHeaderCard-urlText u-dir").get_text()).strip()
with suppress(Exception): data_website_link = str(parsed_page.find(class_="ProfileHeaderCard-urlText u-dir").find("a").get("href")).strip()
with suppress(Exception): data_joined = str(parsed_page.find(class_="ProfileHeaderCard-joinDate").get_text()).strip()



''' #This checks if all data points are stored correctly.
with suppress(Exception): print(data_name)
with suppress(Exception): print(data_handle)
with suppress(Exception): print(data_tweets)
with suppress(Exception): print(data_following)
with suppress(Exception): print(data_followers)
with suppress(Exception): print(data_likes)
with suppress(Exception): print(data_location)
with suppress(Exception): print(data_website)
with suppress(Exception): print(data_website_link)
with suppress(Exception): print(data_joined)
'''

csv_file = open("test.csv", "w")
columnTitleRow = "Name,Handle,# Of Tweets,Following,Followers,Likes,Location,Website,Link,DateJoined \n"
csv_file.write(columnTitleRow)
csv_file.write(data_name + ",")
csv_file.write(data_handle + ",")
csv_file.write(data_tweets + ",")
csv_file.write(data_following + ",")
csv_file.write(data_followers + ",")
csv_file.write(data_likes + ",")
csv_file.write(data_location + ",")
csv_file.write(data_website + ",")
csv_file.write(data_website_link + ",")
csv_file.write(data_joined + ",")
csv_file.write("\n")



