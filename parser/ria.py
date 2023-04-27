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
            state_id: int, 
            city_id: int, 
            district_id: int, 
            date_from: str, 
            date_to: str, 
            token: str, 
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
        self.api_token = token

    @property
    def category(self):
        return self._category
    @property
    def sub_category(self):
        return self._sub_category
    @property
    def operation(self):
        return self._operation
    @property
    def state_id(self):
        return self._state_id
    @property
    def city_id(self):
        return self._city.id
    @property
    def city_id(self):
        return self._city.id
    def average_price_request(self):
        r = requests.get()
        r.json()

        

