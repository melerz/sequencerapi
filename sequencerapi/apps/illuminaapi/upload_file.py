from django.core.files.storage import default_storage
import json
import subprocess
def handle_upload_file(f):
	#file is UploadedFile object
	path=default_storage.save(f.name, f)
	res = []
	configuration = extractCsv_information(path)	
	result = {}
	result['name']=f.name
	result['type'] = f.content_type
	result['size'] = f.size
	result['url'] = "http://kernel"

	res.append(result)
	return res


def extractCsv_information(path):

	#Reads#
 	cmd_reads = "cat %s | grep -A2 '\[Reads\]' | tail -n +2 | cut -d',' -f1" %path

	p = subprocess.Popen(['/bin/sh','-c',cmd_reads],stderr=subprocess.PIPE,stdout=subprocess.PIPE)
	out_reads,err=p.communicate() #communicate() returns (stdout,stderr) tuple
	if (p.returncode != 0):
		 out_reads = "Error in parsing csv file: %s"%err


	#Indexes#
	#cmd_index_location will take index2 too if we have it
	cmd_index_location = "columns=`cat %s | grep 'index' | tr ',' '\\n' | grep -n 'index' | cut -d ':' -f1`" %path 
 	cmd_indexes = "for index in $columns; do cat %s | grep -A1 'index' | tail -n +2 | cut -d ',' -f$index;done" %path
 	cmd = "%s;%s"%(cmd_index_location,cmd_indexes)

	p = subprocess.Popen(['/bin/sh','-c',cmd],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	out_indexes,err=p.communicate() #communicate() returns (stdout,stderr) tuple
	if (p.returncode != 0):
		 out_indexes = "Error in parsing csv file: %s"%err
		

	#Clean empty lines from reads and indexes
	out_reads=out_reads.replace('\r', '') #it appears the cmd_reads return '\r' in output
	reads = [read for read in out_reads.split("\n") if read]
	indexes = [index for index in out_indexes.split("\n") if index]