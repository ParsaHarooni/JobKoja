from .make_request import Request
from bs4 import BeautifulSoup
from unidecode import unidecode

class Search:

    def __init__(self, query: str, location: str = '', page=1) -> None:
        """
        This initializes the Search class

        Parameters;
        query: string query of your job search
        location: location of where you wanna search in

        Returns: None
        """
        self.query = query
        self.location = location
        self.page = page
        self.requester = Request()
        self.response = self.get_response()

    def get_response(self, page=None):
        """
        This helper function returns the raw response of search

        Parameter:
        page: Which page of responses do you want to get?
        """
        page = page or self.page
        url = f'/jobs?filters[job_categories][]=&filters[keywords][0]={self.query}&filters[locations][]={self.location}&sort_by=relevance_desc&page={page}'
        status_code, resp = self.requester.get_request(url)
        if status_code == 200:
            return resp
        else:
            raise Exception(
                "The request was not sent, Please try again or check your connection.")

    def get_html_parser(self):
        return BeautifulSoup(self.response, 'html.parser')

    def get_json(self):
        pass

    def get_count(self) -> int:
        """
        This function returns count of the all of job applications
        """
        parser = self.get_html_parser()
        count_str = parser.find(
            "span", {"class": "c-jobSearchState__numberOfResultsEcho"}).get_text().strip()
        count_str_normalized = unidecode(count_str)
        count = ''.join(filter(str.isdigit, count_str_normalized))
        return int(count)
    
    def get_page_count(self) -> int:
        """
        This page returns pages count of this query
        """
        return self.get_count() / 20 + 1
