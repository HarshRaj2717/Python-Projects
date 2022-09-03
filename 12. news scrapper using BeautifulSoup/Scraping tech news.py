# scraping from https://news.ycombinator.com/ and printing the story title and link to the most upvoted story.

import requests
from bs4 import BeautifulSoup

site_response = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(site_response.text, "html.parser")

scores = {}
for i in soup.findAll(class_="score"):
    # <span class="score" id="score_32384653">800 points</span>
    scores[i.get("id")[6:]] = int(i.get_text().strip("points"))

scores_list = list(scores.values())
scores_list.sort()
max_score = scores_list[-1]
for i in scores:
    if scores[i] == max_score:
        max_score_id = i

max_score_id_content =  soup.find(id=max_score_id).find(class_="titlelink")
story_name = max_score_id_content.get_text()
print(f"Story with highest no. of votes : {story_name}")
story_link = max_score_id_content.get("href")
print(f"Link : {story_link}")
print(f"Points : {max_score}")
