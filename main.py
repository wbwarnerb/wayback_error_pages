import requests

dict = {}

def wayback(url):
    contents = requests.get("http://web.archive.org/cdx/search/cdx?url=" + url + "/*&output=json&collapse=urlkey")
    parser(contents.json())

def parser(input):
    for i in input[1:]:
        try:
            dict.update({i[2]: {"status":int(i[4]), "timestamp":i[1]}})
        except:
            print("Couldn't parse " + i[4])
    status_code_parser()

def status_code_parser():
    # Filtering results by 500 error codes
    for key in dict:
        status_code = dict.get(key).get("status")
        timestamp = dict.get(key).get("timestamp")
        if status_code >= 500:
            # Building URL for each 500 error timestamp
            print("https://web.archive.org/web/"+timestamp+"/"+key, "->", status_code)

if __name__ == '__main__':
    site = input("Enter Domain: ")
    wayback(site)

