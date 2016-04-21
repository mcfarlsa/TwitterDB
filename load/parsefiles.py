import datetime, json

filedate = datetime.datetime.now().strftime ('%Y%m%d')
filename = '/media/data/daily_files/tweets_' + filedate + '.txt'


with open(filename, 'r') as filereader:
	for line in filereader:
		json_data = json.loads(line)
		try:
			print json_data["user"]["screen_name"]
		except Exception: 
			pass