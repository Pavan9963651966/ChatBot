import requests
from bs4 import BeautifulSoup

class WebAgent:
    def __init__(self, url):
        self.url = url  

    def retrieve_from_web(self, query=None):
        response = requests.get(self.url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            return soup.get_text()[:1000]  
        else:
            return "Failed to retrieve website content."
