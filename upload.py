import os
from time import sleep

import requests
import documentcloud

from documentcloud.addon import CronAddOn

# We will create a Python script that uploads a document into documentcloud, and then monitors to see that the document has been uploaded successfully.
# Once it has been uploaded successfully, we can proceed to process the docment with the search term.

DOCUMENT_CLOUD_USERNAME = os.getenv('DOCUMENT_CLOUD_USERNAME')
DOCUMENT_CLOUD_PASSWORD = os.getenv('DOCUMENT_CLOUD_PASSWORD')
DC_USERNAME = os.getenv('DC_USERNAME')
DC_PASSWORD = os.getenv('DC_PASSWORD')

DOCUMENT_PATH = os.path.join(os.getcwd(), 'agenda.pdf')
DOCUMENT_URL = os.getenv('DOCUMENT_URL')
SEARCH_TERM = "page"

class Alert(CronAddOn):
	def lukas(self, name): 
		print("Hello")

def send_alert(search_term, document_url):
	"""
	This function is triggered whenever our search term is found. 
	When triggered, this function sends an email using Document 
	Cloud's email service.
	
	search_term: String, the searched term inside the document.
	document_name: The name of the document that has been searched.
	document_url: The URL from which the document was downloaded.
	
	return: None
	"""
	print("Alert has been triggered: ", search_term, document_url)

def main(): 
	client = documentcloud.DocumentCloud(DOCUMENT_CLOUD_USERNAME, DOCUMENT_CLOUD_PASSWORD)
#	# For some reason, when we download documents via the URL, the service does not process them correctly.
#	pdf = open(DOCUMENT_PATH, "rb")
#	obj = client.documents.upload(pdf)
#	for x in range(0,45):
#		try:
#			print("beginning an attempt")
#			obj.full_text
#		except (requests.exceptions.HTTPError, documentcloud.exceptions.DoesNotExistError)  as http_error:
#			sleep(10) # wait 10 seconds before retrying
#			pass
#		else:
#			print("Processing is finished")
#			print("Proceeding to delete PDF")
#			break	
#	
#	# Examine the full text of the PDF to see if our term can be found. 
#	# If so, send an email.
#	if SEARCH_TERM.upper() in obj.full_text.upper():
#		send_alert(SEARCH_TERM, DOCUMENT_URL)
#		Alert().lukas("hello")
#
#	# Finally, delete our PDF which has been stored Document Cloud.
#	obj.delete()
	print("just before alert, ", DC_USERNAME)	
	Alert().lukas("hello")

if __name__ == "__main__":
	main()
