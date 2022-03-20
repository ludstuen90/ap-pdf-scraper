import os
from time import sleep

import requests
import documentcloud


# We will create a Python script that uploads a document into documentcloud, and then monitors to see that the document has been uploaded successfully.
# Once it has been uploaded successfully, we can proceed to process the docment with the search term.

DOCUMENT_CLOUD_USERNAME = os.getenv('DOCUMENT_CLOUD_USERNAME')
DOCUMENT_CLOUD_PASSWORD = os.getenv('DOCUMENT_CLOUD_PASSWORD')
DOCUMENT_PATH = os.path.join(os.getcwd(), 'agenda.pdf')

def main(): 
	client = documentcloud.DocumentCloud(DOCUMENT_CLOUD_USERNAME, DOCUMENT_CLOUD_PASSWORD)
	# For some reason, when we download documents via the URL, the service does not process them correctly.
	pdf = open(DOCUMENT_PATH, "rb")
	obj = client.documents.upload(pdf)
	for x in range(0,45):
		try:
			print("beginning an attempt")
			obj.full_text
		except (requests.exceptions.HTTPError, documentcloud.exceptions.DoesNotExistError)  as http_error:
			sleep(10) # wait 10 seconds before retrying
			pass
		else:
			print("Processing is finished")
			print("Proceeding to delete PDF")
			obj.delete()
			break

if __name__ == "__main__":
	main()
