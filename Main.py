"""This application should scrape HTML from behind a logged in page of the internet."""
import requests


def scrape() -> None:

    # Login page URL
    post_login_url = '%LOGIN URL%'
    # Scraped URL
    request_url = '%TARGET URL%'
    # Login payload
    payload = {
        'UserName': '%USERNAME%',
        'Password': '%PASSWORD%'
    }
    with requests.Session() as session:
        post = session.post(post_login_url, data=payload)
        r = session.get(request_url)
        print(r.text)


scrape()

