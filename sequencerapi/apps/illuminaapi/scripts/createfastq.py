import logging
import os
import createfastq_operations as operations
import sys

def run(data,jobModel,analyzeModel,log_level="INFO",log_file="./fastq-log.log"):
	'''
		For each expierment in the data, create a folder with the expirement name, and init it by
		calling the createRundir function.

		data is a JSON forematted data, that describe the current run (run->expierments->(configuration,samples))

		This method first calls to createRundir (links, copy the RunInfo.xml),
		and then, for each experiment it calls for runExpirement method
	'''
	try:
		#This logger object is used in the library too

		logger = configure_logging(log_level,log_file)

		logger.info(("Currently experiment:{0}".format(data['name'])))
		
		#Save the current location because createRunDir change it
		currentLocation=os.getcwd()

		logger.info("{0}: Init Directory".format(data['name']))
		#Init experiment folder (Link files, RunInfo.xml, create output directory)
		operations.createRundir(data)

		logger.info("{0}: Run bcl2fastq".format(data['name']))
		#running bcl2fastq in the current experiment folder.
		#Output folder is fastq, created by createRundir
		operations.runExpirement(data)


		#Changing back to the main folder
		os.chdir(currentLocation)

		logger.info("{0}: Finished".format(data['name']))

	except Exception as e:
		logger.exception(e)
		jobModel.description = e.message
		jobModel.status = "Failed"
		jobModel.save()
		print "main exception. See log file for further details:%s"%e
		exc_type,exc_obj,exc_tb = sys.exc_info()
		fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
		print(exc_type,fname,exc_tb.tb_lineno)

def configure_logging(log_level="INFO",log_file="./fastq-log.log"):
	loglevel = getattr(logging,log_level.upper(),None)
	if not isinstance(loglevel, int):
		raise Exception("Invalid log level: %s" %loglevel)
	#logging.basicConfig(filename=log_file,level=loglevel,foremat="%(name)s:%(levelname)s:%(message)s")
	logger=logging.getLogger(__name__) #need to change that to __name__
	logger.setLevel(loglevel)
	file_handler = logging.FileHandler(log_file)
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	file_handler.setFormatter(formatter)
	logger.addHandler(file_handler)
	return logger