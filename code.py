import requests
from facebook import GraphAPI

graph = GraphAPI("EAAacYxZBsn4sBAKlkiL421S4mRYwa8qgpAiXWgzVHg3K5B11KEbmJK15tb2MMjnrxTE3FA0iLXraIs0l6ZA35HdqwwQIBHAepn6QZCjB0nbhnZAZBcCvTjXVVrx3uugzZBfOgKJHAN0FHnUVu5LK2zGuvIxIZAon54YPFmcW9Tp5JI4ndiAY8tDv01ePoQVeRMZD")
# graph = GraphAPI("access_token")
try:
print graph.get('me')
except FacebookClientError:
print "failed!! :("
