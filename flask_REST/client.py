import requests 
HEADER = "http://127.0.0.1:5000/"

def get_data(id):
	resp = requests.get(HEADER + f"game/{id}")
	print(resp.json()['name'])

def post_data(id, name, release_date):
	resp = requests.post(HEADER + f"game/{id}", {'name': name, 'release_date': release_date})
	print(resp)
	return resp


res = post_data(3, 'SpiderMan', '2020')

print(res)
