import os
from time import sleep

import requests
import documentcloud

from documentcloud.addon import CronAddOn

# We will create a Python script that uploads a document into documentcloud, and then monitors to see that the document has been uploaded successfully.
# Once it has been uploaded successfully, we can proceed to process the docment with the search term.

DC_USERNAME = os.getenv('DC_USERNAME')
DC_PASSWORD = os.getenv('DC_PASSWORD')

DOCUMENT_PATH = os.path.join(os.getcwd(), 'output.pdf')
DOCUMENT_URL = os.getenv('DOCUMENT_URL')
SEARCH_TERM = "page"

def main(): 
	client = documentcloud.DocumentCloud(DC_USERNAME, DC_PASSWORD)
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
			break	
	
	# Examine the full text of the PDF to see if our term can be found. 
	# If so, send an email.
	if SEARCH_TERM.upper() in obj.full_text.upper():
		print("Sending email to user.")
		CronAddOn().send_mail("TERM MATCHED", f"""Hi there, \n We're writing to let you know that we've discovered the following match: \n\n TERM: {SEARCH_TERM} \n DOCUMENT URL:  {DOCUMENT_URL} \n\n Thanks.""")

	# Finally, delete our PDF which has been stored Document Cloud.
	obj.delete()

if __name__ == "__main__":
	main()
