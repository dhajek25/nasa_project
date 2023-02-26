import datetime as dt
import requests
import credentials

# creates variables with current date and date minus 7 days
today = dt.date.today()
week_ago = today - dt.timedelta(days=7)

def nasa_neows():
    """The function that connects to the Nasa NeoWs API and returns data for the latest 7 days"""
    URL_NeoFeed = "https://api.nasa.gov/neo/rest/v1/feed"
    params = {
        'api_key': credentials.api_key,
        'start_date':today,
        'end_date':week_ago
    }
    try:
        response = requests.get(URL_NeoFeed, params=params).json()
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    return response