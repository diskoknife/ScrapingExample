"""
This is python API that can help you to interact with current ria.com API
"""

import requests

class AveragePrice:
    
    def __init__(
            self, 
            category: int, 
            sub_category: int, 
            operation: int, 
            state_id=-1, 
            city_id=-1, 
            district_id=-1, 
            date_from=-1, 
            date_to=-1, 
            api_token="", 
            url = "https://developers.ria.com/dom/average_price?") -> None:
        """
        category -> int, list of categories you can get in categories.json file
        sub_category -> int, list of sub-categories you can get in sub-categories.json file
        operation -> int, same
        state_id -> int, same
        city_id -> int, same
        district_id -> int, same
        date_from -> format YYYY-MM
        date_to -> format YYYY-MM
        """
        self.category = category
        self.sub_category = sub_category
        self.operation = operation
        self.state_id = state_id
        self.city_id = city_id
        self.district_id = district_id
        self.date_from = date_from
        self.date_to = date_to
        self.api_token = api_token
        self.url = url

    # @property
    # def category(self):
    #     return self._category
    # @property
    # def sub_category(self):
    #     return self._sub_category
    # @property
    # def operation(self):
    #     return self._operation
    # @property
    # def state_id(self):
    #     return self._state_id
    # @property
    # def city_id(self):
    #     return self._city.id
    # @property
        
    def average_price_request(self):
        final_url = self.url + "category=" + str(self.category) + "&sub_category=" + str(self.sub_category) + "&operation=" + str(self.operation)
        if self.state_id >= 1:
            final_url += "&state_id="
        if self.city_id >= 1:
            final_url += "&city_id=" + str(self.city_id)
        if self.district_id >= 1:
            final_url += "&district_id=" + str(self.district_id)
        if self.date_from != "":
            final_url += "&date_from=" + self.date_from
        if self.date_to != "":
            final_url += "&date_to=" + self.date_to
        final_url += "&api_key=" + self.api_token
        r = requests.get(final_url)
        r.json()

        

