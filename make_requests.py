import requests
import json
# import urllib3

URL = "https://www.ncei.noaa.gov/cdo-web/api/v2/locations"
token = 'JvEHhyqQqVpFAqcmAHjcuhjNfFNjyvKV'
total_records = 38862
offset = 1
req_limit = 1000
offsetURL = URL + f"?offset=" + str(offset) + "&" + f"limit=" + str(req_limit)
offset_count = 0


# response = requests.get(URL, headers={'Token': 'JvEHhyqQqVpFAqcmAHjcuhjNfFNjyvKV'})
# temp_data = json.dumps(response)

while offset < total_records:
    response = requests.get(offsetURL, headers={'Token': token})
    temp_data = response.json()
    output_filename = f"locations_{offset_count}.json"
    output_file = open(output_filename, 'w')
    output_file.write(json.dumps(temp_data))
    offset += 1000
    offset_count += 1

# print(response.json())


# def get_record_count(url):
#     pass
#
#
# def set_offset_increment(rec_count, limit):
#     pass
#
#
# def get_response(url):
#     pass
#
#
# def write_to_json(data):
#     pass

# if __name__ == "__main__":

# will need a way to parse request limit or also pass it in
# pass a url argument
# retrieve count of entries
# set total records
# loop through requests, updating offset
