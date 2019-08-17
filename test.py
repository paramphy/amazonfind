import requests
from bs4 import BeautifulSoup

def get_reviews(s,url):
    s.headers['User-Agent'] = 'Mozilla/5.0'
    response = s.get(url)
    soup = BeautifulSoup(response.text,"html.parser")
    return soup.find_all(id="productTitle")

if __name__ == '__main__':
    link = 'https://www.amazon.in/XOLO-ZX-Midnight-Blue-Storage/dp/B07NR79B1X/ref=br_msw_pdt-4?_encoding=UTF8&smid=A14CZOWI0VEHLG&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=&pf_rd_r=B54B9R1SSYRTHC3BQ1DJ&pf_rd_t=36701&pf_rd_p=cc9b62a5-2189-486a-89b4-4eda80243fbe&pf_rd_i=desktop'    
    with requests.Session() as s:
        for review in get_reviews(s,link):
            print(f'{review.text}\n')