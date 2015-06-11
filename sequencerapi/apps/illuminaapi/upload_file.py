from django.core.files.storage import default_storage
from django.conf import settings
import json
import subprocess
import os

def handle_upload_file(experiment_name,f):
	try:
		path = None
		if(f.content_type in ['application/vnd.ms-excel','text/csv','text/plain']):
			#file is UploadedFile object
			experiment_upload_dir = os.path.join(ssettings.MEDIA_ROOT,experiment_name)
			if not os.path.isdir(experiment_upload_dir):
				os.mkdir(experiment_upload_dir)
			default_storage.save(f.name, f)
			path = os.path.join(settings.MEDIA_ROOT,f.name)
			res = []
			configuration = extractCsv_information(path)
			result = {}
			result['name']=f.name
			result['type'] = f.content_type
			result['size'] = f.size
			result['url'] = "http://kernel"
			result['configuration'] = configuration
			res.append(result)
			return res
		else:
			raise Exception("Uploaded file is not a csv file, but: %s" % f.content_type)
		except Exception, e:
			raise Exception(e.message)

def extractCsv_information(path):
	try:
		#Reads#
	 	cmd_reads = "cat %s | grep -A2 '\[Reads\]' | tail -n +2 | cut -d',' -f1" %path

		p = subprocess.Popen(['/bin/sh','-c',cmd_reads],stderr=subprocess.PIPE,stdout=subprocess.PIPE)
		out_reads,err=p.communicate() #communicate() returns (stdout,stderr) tuple
		if (p.returncode != 0 or (not out_reads)):
			 raise Exception("Error in parsing csv file: Couldn't find reads")


		#Indexes#
		#cmd_index_location will take index2 too if we have it
		cmd_index_location = "columns=`cat %s | grep 'index' | tr ',' '\\n' | grep -n 'index' | cut -d ':' -f1`" %path 
	 	cmd_indexes = "for index in $columns; do cat %s | grep -A1 'index' | tail -n +2 | cut -d ',' -f$index;done" %path
	 	cmd = "%s;%s"%(cmd_index_location,cmd_indexes)

		p = subprocess.Popen(['/bin/sh','-c',cmd],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		out_indexes,err=p.communicate() #communicate() returns (stdout,stderr) tuple
		if (p.returncode != 0 or (not out_indexes)):
			 raise Exception("Error in parsing csv file:  Couldn't find indexes")
			

		#Clean empty lines from reads and indexes
		out_reads=out_reads.replace('\r', '') #it appears the cmd_reads return '\r' in output
		reads = [read for read in out_reads.split("\n") if read]
		indexes = [str(len(index)) for index in out_indexes.split("\n") if index]

		conf_hash={}

		conf_hash['reads']=reads
		conf_hash['indexes'] = indexes
		return conf_hash
	except Exception as e:
		raise Exception(e.message)