import subprocess
import xml.etree.ElementTree as ET
import datetime
import os
import sys
import csv
import json
import shutil
import logging
import time
from django.conf import settings

logger = logging.getLogger(__name__) #need to change that to __name__

def createRundir(experiment,WEBSITE_PATH="/home/sheker/website/",BASE_ILLUMINA_PATH="/home/sheker/"):
	try:
		logger.debug("start createRundir: {0}".format(experiment))
		#Creating dir_name if not exists
		dir_name = experiment['job_id']+"-"+experiment['name']
		if not (os.path.isdir(dir_name)):
			os.mkdir(dir_name)
		#enter into dir.
		#From now on, our location will be ./dir_name
		os.chdir(dir_name)

		#create output folder in the WEBSITE_PATH global variable
		output_folder = WEBSITE_PATH+str(datetime.date.today())+"-%s" % dir_name
		if not (os.path.isdir(output_folder)):
			os.mkdir(output_folder)


		destination_path=BASE_ILLUMINA_PATH + experiment['illumina_name']

		#check for destination_path trailing slash
		if destination_path[-1:] == "/":
			print "removing trailing slash"
			destination_path = destination_path[:-1]
		cmd = "ln -s %s/* .;cp ./RunInfo.xml RunInfo_original.xml;rm -f RunInfo.xml;mv RunInfo_original.xml RunInfo.xml;ln -s %s fastq" %(destination_path,output_folder)
		p = subprocess.Popen(cmd,shell=True,stderr=subprocess.PIPE)
		out,err=p.communicate() #communicate() returns (stdout,stderr) tuple
		if (p.returncode != 0):
			raise Exception("Error in running bash commands: %s" %err)
		logger.debug("End createRundir successfully")
	except Exception, e:
		raise Exception("Exception in createRundir : %s" %e)


def runExpirement(experiment_data,xml_path="./RunInfo.xml"):
	'''
		This function should be run **after** createRundir function
		We assume we have RunInfo.xml (unlinked with destination folder) with clean reads
		fastq folder should be a link to a website home directory.
	'''
	try:
		logger.debug("start runExpirement: {0},{1}".format(experiment_data,xml_path))
		#clean xml from reads
		cleanXML(xml_path)

		#modify xml reads settings based on configuration setting
		configureXML(experiment_data['configuration'],xml_path)

		#create SampleSheet.csv based on samples settings
		createSampleSheet(experiment_data['csv'],"./SampleSheet.csv")

		#run the bcl2fastq
		#p = subprocess.Popen("/usr/local/bcl2fastq/2.15.0.4/bin/bcl2fastq -o fastq -p 8 -d 6 -r 4 -w 4")
		time.sleep(30)
		#create download link - mayb we don't need that!

		logger.debug("End runExpirement successfully")
	except Exception, e:
		raise Exception("Exception in runExpirement : %s" %e)


def cleanXML(path="./RunInfo.xml"):
	'''
		This method clear the previous XML reads settings in the <Reads> element
	'''
	try:
		logger.debug("start cleanXML: {0}".format(path))
		tree = ET.parse(path)
		root = tree.getroot()
		readsElement=root.find(".//Reads")
		for read in root.findall(".//Reads/Read"):
			readsElement.remove(read)

		tree.write(path)
		logger.debug("Finished cleanXML")
	except Exception, e:
		raise Exception("Exception in cleanXML : %s" %e)



def configureXML(configuration,path="./RunInfo.xml"):
	'''
		We assume we have RunInfo.xml (unlinked with destination folder) with clean reads
	'''

	try:
		logger.debug("start configureXML: {0},{1}".format(configuration,path))
		print 'begiining configure xml'
		tree = ET.parse(path)
		root = tree.getroot()
		readsElement=root.find(".//Reads")
		#Creates new reads based on configuration
		for readIndex in configuration.keys():
			print readIndex
			ET.SubElement(readsElement,'Read',dict(Number=readIndex,NumCycles=configuration[readIndex]['NumCycles'],IsIndexedRead=configuration[readIndex]['IsIndexedRead']))

		tree.write(path)
		logger.debug("End configureXML successfully")

	except Exception, e:
		raise Exception("Exception in configureXML : %s" %e)

def createSampleSheet(csv_file_name,csv_dest="./SampleSheet.csv"):
	'''
		This function copies the uploaded csv file from the website to the experiment folder
		We assume we are in the experiment folder already
	'''

	try:
		logger.debug("Start createSampleSheet: csv filename: {0}, destinationl: {1}".format(csv_file_name,csv_dest))
		src = os.path.join(settings.MEDIA_ROOT,csv_file_name + ".csv")
		shutil.copyfile(src,csv_dest)
		logger.debug("End createSampleSheet")

	except Exception, e:
		raise Exception("error in createSampleSheet %s" % e)
