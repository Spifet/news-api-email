import requests
from send_email import send_email

api_key = "65f072179cd343d185c797cd1e20d09c"
url = "https://newsapi.org/v2/everything?q=tesla&from=" \
      "2023-02-14&sortBy=publishedAt&language=en&apiKey=65f072179cd3" \
      "43d185c797cd1e20d09c"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
email = ''
for article in content["articles"]:
    if article['title'] or article['description'] is not None:
        email += f"\n {article['title']} \n {article['description']} \n\n"

email = email.encode("utf-8")
send_email(message=email)

