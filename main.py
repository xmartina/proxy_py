import csv
import requests

CSV_FILENAME = 'proxy_list.csv'
URL_TO_CHECK = 'https://ip.oxylabs.io/ip'
TIMEOUT_IN_SECONDS = 10
scheme_proxy_map = {
  'http://203.243.63.16:80',
'http://3.24.58.156:3128'
}

with open(CSV_FILENAME) as open_file:
    reader = csv.reader(open_file)
    for csv_row in reader:
        scheme_proxy_map = {
            'https': csv_row[0],
        }
        
        # Access the website via proxy
        try:
             response = requests.get('https://ip.oxylabs.io/ip', proxies=scheme_proxy_map, timeout=TIMEOUT_IN_SECONDS)
        except (ProxyError, ReadTimeout, ConnectTimeout) as error:
            pass
        else:
            print(response.text)
            break  # notice the break here
