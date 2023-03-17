import requests

api_endpoint = "https://api.openai.com/v1/completions"
api_key_file = open("apikey.txt", "r")
api_key = api_key_file.readline()
api_key_file.close()

def process_request(prompt : str):
    request_headers = {
        "Content-Type" : "application/json",
        "Authorization" : "Bearer " + api_key
    }

    request_data = {
        "model": "text-davinci-003",
        "prompt": prompt,
        "max_tokens": 1000,
        "temperature": 0.5
    }
    response = requests.post(api_endpoint, headers=request_headers, json=request_data)

    if response.status_code == 200:
        return response.json()["choices"][0]["text"]
    else:
        return "Request failed with status code " + str(response.status_code)

while True:
    prompt = input("Please enter your prompt or type ABORT to stop execution:\n")
    if prompt == "ABORT":
        break
    print(process_request(prompt))