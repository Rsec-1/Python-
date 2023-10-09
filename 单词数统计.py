import requests
from bs4 import BeautifulSoup
from collections import Counter

def get_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content.decode()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def get_top_words(html, min_length=0, top_n=10):
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    words = [word.lower() for word in text.split() if len(word) >= min_length]
    word_count = Counter(words)
    return word_count.most_common(top_n)

if __name__ == '__main__':
    url = input("Enter the URL: ")
    html = get_html(url)

    if html is not None:
        top_words = get_top_words(html, min_length=4, top_n=10)

        for word, count in top_words:
            print(f'{word}: {count}')
