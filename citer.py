import requests
import json

class cite:
    """
    create MLA citations with ease!
    """

    def __init__(self, URL):
        """
        @Param: URL (str) - the website URL of your article
        @Desc: creates citation
        """

        self.data = {"url" : str(URL)}
        self.BASE = "https://formatically.com/api/website"
        self.response = None

    def get_citation(self):
        """
        @Desc: gets raw citation data from API
        """

        r = requests.post(url = self.BASE, data = self.data)
        self.response = dict(json.loads(r.text))
        self.format()

    def format(self):
        """
        @Desc: formats raw citation date
        """

        self.firstName = self.response["creators"][0]["firstName"]
        self.lastName = self.response["creators"][0]["lastName"]
        self.title = self.response["title"]
        self.published_date = self.response["date"]
        self.accessed_date = self.response["accessDate"]
        self.publication = self.response["websiteTitle"]
        self.url = self.response["url"]

    def mla(self):
        """
        @Desc: Returns an MLA 8 citation
        """
        
        self.get_citation()
        return f'{self.lastName}, {self.firstName}. "{self.title}" {self.publication}, {self.published_date}, {self.url}. Accessed {self.accessed_date}.'
    