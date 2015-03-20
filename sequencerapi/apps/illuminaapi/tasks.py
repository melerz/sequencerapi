from __future__ import absolute_import
from celery import shared_task
from apps.illuminaapi.scripts import createfastq
import hashlib
import time
import redis

LOCK_EXPIRE = 60*60*6 #6 Hours
@shared_task
def fastq_async(data,log_level="INFO",log_file="./fastq-loq.log"):
	m = hashlib.md5()

	m.update("bla10")
	lock_id = m.digest()

	lock_obj = redis.StrictRedis().lock(name=lock_id,timeout=LOCK_EXPIRE)

	have_lock=False
	have_lock = lock_obj.acquire(blocking=False)
	if have_lock:
		print("we have the flag!")
		try:
			createfastq.run(data,log_level,log_file)
		finally:
			lock_obj.release()
	else:
		print("we need to wait...",)
		with lock_obj:
			have_lock=True
			createfastq.run(data,log_level,log_file)




