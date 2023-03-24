import requests

API_KEY = "AIzaSyAIWEFdwoFLxi7zzBtgBP_7-HldO2UvjP8"
SEARCH_ENGINE_ID = "43290867be9fa42f8"
QUERY = "python"

url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={QUERY}"

#response = requests.get(url, verify="Corp-Prj-Root-CA.crt")
response = requests.get(url)
results = response.json()["items"]

for result in results:
    print(result["title"])
    print(result["link"])
    print(result["snippet"])
    print()