import datetime
import os
import requests
import time
def feed(path="/home/sheker/",post_url="http://132.65.120.148:8080/illuminaapi/illumina/"):
	for illumina_dir in os.listdir(path):
		data={}
		raw_createdtime = os.path.getctime(os.path.join(path,illumina_dir))
		illumina_date = datetime.datetime.fromtimestamp(raw_createdtime).strftime('%Y-%M-%d')
		
		data["name"] = illumina_dir
		data["date"] = illumina_date
		print data
		#res=requests.post(post_url,data)

feed()