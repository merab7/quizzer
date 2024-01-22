import requests

parameters = {
   "amount": 10,
   "difficulty": "medium",
   "type": "boolean"
}

data = requests.get("https://opentdb.com/api.php", params=parameters)
questions = data.json()
