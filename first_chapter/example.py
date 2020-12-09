import pickle 

class EmbeddedData:
	def __init__(self, data, json_file):
		self.data = data
		self.json_file = json_file


ed = EmbeddedData("", "")

sender_data = pickle.dumps(ed)


# server tier

my_recieved_obj =  pickle.loads(sender_data)
my_data = my_recieved_obj.data 
my_jon_file = my_jon_file.json_file
