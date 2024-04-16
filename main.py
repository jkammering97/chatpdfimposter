
#%%
import requests
from dotenv import load_dotenv
import os
load_dotenv()
#%%
class ChatPDF:
    """
    A class to handle uploading PDF files to a specified API and managing the resulting source ID.

    :param api_url: The URL of the API endpoint for uploading PDF files.
    :param api_token: The authentication token required for API access.
    """
    def __init__(self, api_key):
        self.api_key = api_key
        self.source_id = None
        
    def add_file(self, file_path: str):
        """
        Adds a PDF file to the API and updates the source_id attribute of the class instance.

        :param file_path: Your system path to the file.
        :returns: A dictionary representing the JSON response from the API.
        :raises Exception: An exception is raised if the upload fails, with an error message included.
        """
        files = [
            ('file', ('file', open(file_path, 'rb'), 'application/octet-stream'))
        ]
        headers = {
            'x-api-key': self.api_key
        }

        response = requests.post(
            'https://api.chatpdf.com/v1/sources/add-file', headers=headers, files=files)

        if response.status_code == 200:
            self.source_id = response.json()['sourceId']
            print('Source ID:', response.json()['sourceId'])
        else:
            print('Status:', response.status_code)
            print('Error:', response.text)

    def ask_question(self, question: str):
        """
        Asks a question to the uploaded PDF
        You can include up to 6 messages in one request. If the total number of OpenAI tokens in the these messages exceed 2,500, older messages are ignored until that limit is no longer exceeded.
        This method assumes that the source_id is already set. It uses this ID to perform further operations as defined by the API.

        :returns: A dictionary representing the JSON response from the API operation.
        :raises ValueError: If the source_id is not set, a ValueError is raised.
        """
        headers = {
            'x-api-key': self.api_key,
            "Content-Type": "application/json",
        }

        data = {
            'sourceId': self.source_id,
            'messages': [
                {
                    'role': "user",
                    'content': question,
                }
            ]
        }
        response = requests.post(
            'https://api.chatpdf.com/v1/chats/message', headers=headers, json=data)

        if response.status_code == 200:
            print('Result:', response.json()['content'])
        else:
            print('Status:', response.status_code)
            print('Error:', response.text)

