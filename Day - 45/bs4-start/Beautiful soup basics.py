from bs4 import BeautifulSoup

with open("website.html") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")

# print(soup.title)
# print(soup.p) # Seaches only for the first paragraph.

all_para_tags = soup.find_all(name="p")
# print(all_para_tags)

filter_by_id = soup.find(name="h1", id="name")
# print(filter_by_id)

filter_by_class = soup.find(name="h3", class_="heading")
# print(filter_by_class)
# print(filter_by_class.get("class")) # Getting some specific part.

# Using CSS selectors.
company_url = soup.select_one("p a")
name = soup.select("#name") # Selecting by id.
headings = soup.select(".heading") # Selecting by classs.
print(headings)
