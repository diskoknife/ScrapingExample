import requests

def get_average_price(
        category: int, 
        sub_category: int, 
        operation: int, 
        state_id=-1, 
        city_id=-1, 
        district_id=-1, 
        date_from="", 
        date_to="", 
        api_token="", 
        url = "https://developers.ria.com/dom/average_price?"
        ):
    final_url = url + "category=" + str(category) + "&sub_category=" + str(sub_category) + "&operation=" + str(operation)
    if state_id >= 1:
        final_url += "&state_id="
    if city_id >= 1:
        final_url += "&city_id=" + str(city_id)
    if district_id >= 1:
        final_url += "&district_id=" + str(district_id)
    if date_from != "":
        final_url += "&date_from=" + date_from
    if date_to != "":
        final_url += "&date_to=" + date_to
    final_url += "&api_key=" + api_token
    r = requests.get(final_url)
    r.json()
    return r
