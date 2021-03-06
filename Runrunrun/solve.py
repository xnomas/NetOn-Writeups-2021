import requests
import selenium
import hashlib

from bs4 import BeautifulSoup

url = 'http://167.99.129.209:7777/'
post_url = url + '/index.php' 

s = requests.Session()
r = s.get(url).text 
soup = BeautifulSoup(r,'html.parser')

to_hash = soup.find_all('h3')[0]
to_hash = str(to_hash)[4:-5] # slice of the <h3> tags
to_hash = eval(to_hash)

to_hash = str(to_hash).encode('ascii')
hashed = hashlib.md5(to_hash).hexdigest()

data = { 'md5' : str(hashed) }

post = s.post(post_url, data=data)

print(post.text)