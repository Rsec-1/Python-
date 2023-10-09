import requests
from bs4 import BeautifulSoup
from collections import Counter
import re

page_url = 'taget url'

def get_html_of(url):
  try:
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.content.decode()
  except requests.exceptions.RequestException as e:
    print(f'error: {e}')
    exit(1)

def get_top_words(text,n=10):
  all_words = re.findall(r'\w+',text.lower())
  word_count = Counter(all_words)
  return word_count.most_common(n)

if __name__ == '__main__':
  html = get_html_of(page_url)
  soup = BeautifulSoup(html,'html.parser')
  raw_text = soup.get_text()
  top_words = get_top_words(raw_text)

  for word,count in top_words:
    print(f'{word}:{count}')
