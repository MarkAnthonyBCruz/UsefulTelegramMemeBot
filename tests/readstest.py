import requests
import json
from udpy import UrbanClient
"""goodweedskey = 'BITG2oRAnefsoqrs4VT21Q'
goodweeds = 'eBUSUEE6rZWGnearzpO6m5lKMOjzqStTutX1MLXIA0'
myid = '45546009'
#url = 'https://www.goodreads.com/review/list?v=2&key={}&id={}&shelf=to-read&sort=random&per_page=1'.format(goodweedskey, myid)

url = 'https://www.goodreads.com/book/title.json?author=Arthur+Conan+Doyle&key=BITG2oRAnefsoqrs4VT21Q&title=Hound+of+the+Baskervilles'

book = requests.get(url).json()
print(book)"""

client = UrbanClient()

defs = client.get_random_definition()
for index, d in enumerate(defs):
    print(str(index) + "). " + d.definition + "\n")
    print(d.word)
