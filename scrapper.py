import requests, os
from bs4 import BeautifulSoup
from dotenv import load_dotenv

def fetch_episodes(anime_name):
    """
    Fetches the list of episodes for a given anime from animefillerlist.com.
    """
    url_name = anime_name.lower().replace(" ", "-")
    
    load_dotenv()
    base_url = os.getenv('BASE_URL')
    url = base_url + url_name
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to access episode list for '{anime_name}'. Please check the anime name.")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    episodes = soup.find_all("td", class_="Title")
    
    if not episodes:
        print(f"No episodes found for '{anime_name}'. Please check the anime name.")
        return []

    return [ep.get_text(strip=True) for ep in episodes]

if __name__ == "__main__":
    pass