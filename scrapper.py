import requests
from bs4 import BeautifulSoup

def fetch_episodes(anime_name):
    """
    Fetches the list of episodes for a given anime from animefillerlist.com.
    """
    url_name = anime_name.lower().replace(" ", "-")
    
    base_url = "https://www.animefillerlist.com/shows/"
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

def main():
    anime_name = input("Enter Anime Name = ")
    episodes = fetch_episodes(anime_name)

    if episodes:
        print(f"{anime_name.capitalize()} episodes are listed :- ")
        for idx, name in enumerate(episodes):
            print(f"{idx+1} - {name}")

if __name__ == "__main__":
    main()