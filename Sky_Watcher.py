import requests
import datetime

def fetch_nasa_apod(api_key="DEMO_KEY"):
    """
    Fetches NASA's Astronomy Picture of the Day (APOD).
    Demonstrates API interaction and JSON data extraction.
    """
    print("\n--- NASA Astronomy Picture of the Day ---")
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status() # To  Check for HTTP errors
        data = response.json()
        
        title = data.get("title", "No Title")
        explanation = data.get("explanation", "No explanation available.")
        date = data.get("date", str(datetime.date.today()))
        
        print(f"Date: {date}")
        print(f"Title: {title}")
        print(f"\nExplanation: {explanation[:300]}...") 
        print(f"\nImage URL: {data.get('url')}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to NASA API: {e}")

def track_iss_live():
    """
    Tracks the International Space Station in real-time.
    Demonstrates handling of live telemetry data in JSON format.
    """
    print("\n--- Real-Time ISS Tracking ---")
    url = "http://api.open-notify.org/iss-now.json"
    
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        
        if data['message'] == 'success':
            pos = data['iss_position']
            lat = pos['latitude']
            lon = pos['longitude']
            timestamp = datetime.datetime.fromtimestamp(data['timestamp'])
            
            print(f"As of: {timestamp}")
            print(f"The ISS is currently at: Latitude {lat}, Longitude {lon}")
            print(f"Tracking Link: https://www.google.com/maps?q={lat},{lon}")
    except Exception as e:
        print(f"Could not retrieve ISS data: {e}")

if __name__ == "__main__":
    fetch_nasa_apod()
    track_iss_live()
