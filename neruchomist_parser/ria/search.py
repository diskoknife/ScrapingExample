"""
Module provides API for creating default search strings in dim.ria.com
"""

import requests

def get_search_result(
        category: int, 
        sub_category: int, 
        operation: int, 
        state_id=-1, 
        city_id=-1, 
        district_id=-1, 
        date_from="", 
        date_to="", 
        api_token="", 
        url = "https://developers.ria.com/dom/search?"    
        ):
    final_url = url
    