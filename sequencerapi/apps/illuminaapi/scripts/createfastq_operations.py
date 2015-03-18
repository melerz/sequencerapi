import subprocess
import xml.etree.ElementTree as ET
import datetime
import os
import sys
import csv
import json
import shutil
import logging
from django.conf import settings
def createRundir(experiment,WEBSITE_PATH="/home/sheker/website/",BASE__ILLUMINA_PATH="/home/sheker/"):
	try:
		#Creating dir_name if not exists
		dir_name = experiment['name']
		if not (os.path.isdir(dir_name)):
			os.mkdir(dir_name)
		#enter into dir.
		#From now on, our location will be ./dir_name
		os.chdir(dir_name)

		#create output folder in the WEBSITE_PATH global variable
		output_folder = WEBSITE_PATH+str(datetime.date.today())+"-%s" % dir_name
		if not (os.path.isdir(output_folder)):
			os.mkdir(output_folder)


		destination_path=BASE__ILLUMINA_PATH + experiment['illumina_name']

		#check for destination_path trailing slash
		if destination_path[-1:] == "/":
			print "removing trailing slash"
			destination_path = destination_path[:-1]
		cmd = "ln -s %s/* .;cp ./RunInfo.xml RunInfo_original.xml;rm -f RunInfo.xml;mv RunInfo_original.xml RunInfo.xml;ln -s %s fastq" %(destination_path,output_folder)
		p = subprocess.Popen(cmd,shell=True,stderr=subprocess.PIPE)
		out,err=p.communicate() #communicate() returns (stdout,stderr) tuple
		if (p.returncode != 0):
			raise Exception("Error in running bash commands: %s" %err)
	except Exception, e:
		raise Exception("Exception in createRundir : %s" %e)


def runExpirement(experiment_data,xml_path="./RunInfo.xml"):
	'''
		This function should be run **after** createRundir function
		We assume we have RunInfo.xml (unlinked with destination folder) with clean reads
		fastq folder should be a link to a website home directory.
	'''
	try:
		#clean xml from reads
		cleanXML(xml_path)
		print "finished cleanning xml"
		#modify xml reads settings based on configuration setting
		configureXML(experiment_data['configuration'],xml_path)
		print "finished configurig xml"

		#create SampleSheet.csv based on samples settings
		createSampleSheet(experiment_data['csv'],"./SampleSheet.csv")
		print "finished creating csv"

		#run the bcl2fastq
		#p = subprocess.Popen("/usr/local/bcl2fastq/2.15.0.4/bin/bcl2fastq -o fastq -p 8 -d 6 -r 4 -w 4")

		#create download link - mayb we don't need that!
		# url=createDownloadLink(full_directory_name)
		# print "finished create download link"
	except Exception, e:
		raise Exception("Exception in runExpirement : %s" %e)


def cleanXML(path="./RunInfo.xml"):
	'''
		This method clear the previous XML reads settings in the <Reads> element
	'''
	try:

		print "im in cleanXML"
		tree = ET.parse(path)
		root = tree.getroot()
		readsElement=root.find(".//Reads")
		for read in root.findall(".//Reads/Read"):
			readsElement.remove(read)

		tree.write(path)

	except Exception, e:
		raise Exception("Exception in cleanXML : %s" %e)



def configureXML(configuration,path="./RunInfo.xml"):
	'''
		We assume we have RunInfo.xml (unlinked with destination folder) with clean reads
	'''

	try:

		print 'begiining configure xml'
		tree = ET.parse(path)
		root = tree.getroot()
		readsElement=root.find(".//Reads")
		#Creates new reads based on configuration
		for readIndex in configuration.keys():
			print readIndex
			ET.SubElement(readsElement,'Read',dict(Number=readIndex,NumCycles=configuration[readIndex]['NumCycles'],IsIndexedRead=configuration[readIndex]['IsIndexedRead']))

		tree.write(path)

	except Exception, e:
		raise Exception("Exception in configureXML : %s" %e)

def createSampleSheet(csv_file_name,csv_dest="./SampleSheet.csv"):
	'''
		This function copies the uploaded csv file from the website to the experiment folder
	'''

	try:
		src = os.path.join(settings.MEDIA_ROOT,csv_file_name + ".csv")
		copyfile(src,csv_dest)

	except Exception, e:
		raise Exception("error in createSampleSheet %s" % e)


def createDownloadLink(folder_name):
	print "im in create download link"
	return None