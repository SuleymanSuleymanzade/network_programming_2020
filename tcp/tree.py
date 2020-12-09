from bs4 import BeautifulSoup
import requests

class node:
	links = set()
	data = ""
	def __init__(self, links):
		self.links = links 
		self.data = None 

	def __init__(self, links, data):
		self.links = links 
		self.data = data 


class tree:
	def __init__(self, nodes):
		self.nodes = nodes
	def __init__(self):
		self.nodes = set()
	
	def get_leaf_nodes(self):
		pass 


webpage = requests.get('https://www.geeksforgeeks.org/write-a-c-program-to-get-count-of-leaf-nodes-in-a-binary-tree/')
soup = BeautifulSoup(webpage.text, "html.parser")
#print(soup.prettify())

possible_res = ['gif', 'jpg', 'gif']
c = 0
for image in soup.find_all('img'):
	source = image['src']
	print(image)
	resolution = source[-3:]
	if resolution in possible_res:
		filename = str(c)+ 'image.' + resolution
		c += 1
		with open(filename, 'wb') as file:
			file.write(requests.get(source).content)


	


