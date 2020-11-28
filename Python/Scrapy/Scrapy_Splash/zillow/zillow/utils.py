from http.cookies import SimpleCookie
from urllib.parse import urlparse, parse_qs, urlencode
import json

URL = 'https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState=%7B%22usersSearchTerm%22%3A%22Miami%2C%20FL%22%2C%22mapBounds%22%3A%7B%22west%22%3A-80.375570048584%2C%22east%22%3A-80.11910795141603%2C%22south%22%3A25.637793410033606%2C%22north%22%3A25.90739047439762%7D%2C%22mapZoom%22%3A12%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A12700%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%7D%2C%22isListVisible%22%3Atrue%7D&includeMap=false&includeList=true'

def cookie_parser():
    cookie_string = 'zjs_user_id=null; JSESSIONID=E483F7F3668C823BFBA48FE61C246322; zguid=23|%24ad88a4cd-0c95-4ce1-bc8f-edbf5f8982b6; zgsession=1|8b867ef9-2f0f-43d5-a375-a651fe1bdbef; _ga=GA1.2.1557043503.1577088979; _gid=GA1.2.2089774889.1577088979; _gcl_au=1.1.531585927.1577088980; KruxPixel=true; DoubleClickSession=true; KruxAddition=true; zjs_anonymous_id=%22ad88a4cd-0c95-4ce1-bc8f-edbf5f8982b6%22; __gads=ID=52ce9267f7761af4:T=1577089037:S=ALNI_MZvBpyX8aWP-DZ_Z8YXgUGANb8naA; _px3=0559af8100dba3370bf5eb72ac298d804e6b8d3747d628a0b7aefd4cddd65431:7I7sMIfcI9bi41SXMj81o7OGq4v0Rtu0JPVJMvJJA4fOKaqciU8kXlhb4cZ8i9/S0SPNHEybOu5B4G4Z8FVqeg==:1000:D+DjBwmPRjnJDJ+clxurN/9Mx1oR1BkuSJCdStveFqVBk/wjOJ1hjiLc6zvMIRmXrF6C6C7XXna2/AbdA0h1wNdqg8ougkxtg6GW/tSYRl/dKNERzv4jPEaKdBUjtfJ9kdv4wsxN3uZUEXn/zixnMsAuE68vDHmpwkr8zgFOvyQ=; AWSALB=DOjDyXQ40x12ppl7bwQR9Vn0pdo7+YZ1ox8oRfhul6QwoPPSjWyspPOnxVxOy3Mve/onoA+nWbfs3WwQD7jtltOzhvOLtl1XPCtZ0kDwQdYV43qAGEfRQ/DDrAag; search=6|1579681353249%7Crect%3D25.90739047439762%252C-80.11910795141603%252C25.637793410033606%252C-80.375570048584%26rid%3D12700%26disp%3Dmap%26mdm%3Dauto%26p%3D2%26z%3D0%26pt%3Dpmf%252Cpf%26fs%3D1%26fr%3D0%26mmm%3D1%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%09%01%0912700%09%09%09%090%09US_%09; _gat=1'
    cookie = SimpleCookie()
    cookie.load(cookie_string)

    cookies = {}

    for key, morsel in cookie.items():
        cookies[key] = morsel.value
    
    return cookies

def parse_new_url(url, page_number):
    url_parsed = urlparse(url)
    query_string = parse_qs(url_parsed.query)
    search_query_state = json.loads(query_string.get('searchQueryState')[0])
    search_query_state['pagination'] = {"currentPage": page_number}
    query_string.get('searchQueryState')[0] = search_query_state
    encoded_qs = urlencode(query_string, doseq=1)
    new_url = f"https://www.zillow.com/search/GetSearchPageState.htm?{encoded_qs}"
    return new_url

