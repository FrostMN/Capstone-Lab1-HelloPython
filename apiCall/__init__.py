import requests
import json
import os
api_key = os.environ["ZIP_KEY"]
del os
api_url = "https://www.zipcodeapi.com/rest/<api_key>/distance.json/<zip_code1>/<zip_code2>/mile"
api_url = api_url.replace("<api_key>", api_key)


if __name__ == '__main__':
    first_zip = input("please enter the first zipcode: ")
    second_zip = input("please enter the second zipcode: ")
    # first_zip = str(55414)
    # second_zip = str(55418)

    api_url = api_url.replace("<zip_code1>", first_zip)
    api_url = api_url.replace("<zip_code2>", second_zip)

    print(api_url)

    json_data = requests.get(api_url).text
    data = json.loads(json_data)
    distance = data["distance"]

    print( str(first_zip) + " is " + str(distance) + " miles from " + str(second_zip))
