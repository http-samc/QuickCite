import requests
import json

# TODO Improve of citations, not currently consistent (better parsing in the _cite() method)
# TODO More error logging

class Citation:
    """
    Create citations with ease!
    """

    def __init__(self, URL, type: str = "MLA") -> None:
        """
            Creates Citation object

            :param: URL (str) (req) - the URL for your citation
            :param: type (str) (opt) - the default output type on __str__()
                - "MLA" -> (default) MLA citation 
                - "APA" -> APA citation
                - "CHI" -> Chicago citation
        """

        self.data = {"url" : str(URL)} # Formatting POST data to API
        self.BASE = "https://formatically.com/api/website" # API Base
        self.response = None 
        self.type = type.upper() 

        self._cite() # Creating citation

    def _cite(self) -> None:
        """
            Gets raw citation data from API
        """

        r = requests.post(url = self.BASE, data = self.data) # Making request
        self.response = dict(json.loads(r.text)) # Converting response -> dict
        self._format() # Formatting response

    def _format(self) -> None:
        """
            Formats raw citation date
        """

        # Getting data from response
        self.firstName = self.response["creators"][0]["firstName"]
        self.lastName = self.response["creators"][0]["lastName"]
        self.title = self.response["title"]
        self.date = self.response["date"]
        self.accessed = self.response["accessDate"]
        self.publication = self.response["websiteTitle"]
        self.url = self.response["url"]

        #Getting year
        self.split_date = self.date.split('-')
        self.year = None
        for _ in self.split_date:
            if len(_) == 4:
                self.year = _
        if self.year == None:
            self.year = self.split_date[2]
        
        # Getting day-month
        self.day_month = ""
        for _ in self.split_date:
            if _ != self.year:
                self.day_month += _ + "-"
        self.day_month = self.day_month[:-1]

    def MLA(self) -> str:
        """
            Returns an MLA 8 citation
        """

        return f'{self.lastName}, {self.firstName}. "{self.title}" {self.publication}, {self.date}, {self.url}. Accessed {self.accessed}.'
    
    def APA(self) -> str:
        """
            Returns an APA 7 Citation
        """

        return f'{self.lastName}, {self.firstName[0:1]}. ({self.year}, {self.day_month}) {self.title}. {self.publication}.\n{self.url}'
    
    def CHI(self) -> str:
        """
            Returns a Chicago Citation
        """

        return f'{self.firstName} {self.lastName}, "{self.title}," {self.publication}, last modified {self.date}, {self.url}.'

    def __str__(self) -> str:
        
        if self.type == "APA":
            return self.APA()

        elif self.type == "CHI":
            return self.CHI()
            
        else:
            return self.MLA()
