#!/bin/bash

curl -X GET "https://developers.ria.com/dom/options?category=13&realty_type=0&operation_type=1&api_key="INPUT API KEY" -H "accept: application/json" |
jq '.' > ../json/commerce.json
