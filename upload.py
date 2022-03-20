import os 

from documentcloud import DocumentCloud

# We will create a Python script that uploads a document into documentcloud, and then monitors to see that the document has been uploaded successfully.
# Once it has been uploaded successfully, we can proceed to process the docment with the search term.

DOCUMENT_CLOUD_USERNAME = os.getenv('DOCUMENT_CLOUD_USERNAME')
DOCUMENT_CLOUD_PASSWORD = os.getenv('DOCUMENT_CLOUD_PASSWORD')
DOCUMENT_URL = os.getenv('PDF_URL')

def main(): 
	print("helloworld") 
	print("We have username: ", DOCUMENT_CLOUD_USERNAME)
	print("WE HAVE URL: ", DOCUMENT_URL)
	client = DocumentCloud(DOCUMENT_CLOUD_USERNAME, DOCUMENT_CLOUD_PASSWORD)
	# For some reason, when we download documents via the URL, the service does not process them correctly.
	pdf_path = os.path.join(os.getcwd(), 'output.pdf')
	pdf = open(pdf_path, "rb")
	obj = client.documents.upload(pdf)

if __name__ == "__main__":
	main()
