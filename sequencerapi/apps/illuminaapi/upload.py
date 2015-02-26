from django.core.files.storage import default_storage

def handle_upload_file(file):
	path = default_storage.save('tahat.html', file)