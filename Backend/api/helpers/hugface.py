import requests

API_URL = "https://api-inference.huggingface.co/models/sagorsarker/mbert-bengali-tydiqa-qa"
headers = {"Authorization": f"Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

result = {
    'location': '',
    'time': '',
	'vehicle': '',
	'dead': '',
	'injured': ''
}


location = "কোথায় দুর্ঘটনা ঘটেছে?"
time = "কখন দুর্ঘটনা ঘটেছিলো?"
vehicle = "কোন যানবাহন দুর্ঘটনায় জড়িত ছিল?"
dead = "কে মারা গেছে?"
injured = "দুর্ঘটনায় আহত কারা?"



async def find_params(news):
	result = {
		'location': find_location(news)['answer'],
		'time': find_time(news)['answer'],
		'vehicle': find_vehicle(news)['answer'],
		'dead': find_dead(news)['answer'],
		'injured': find_injured(news)['answer']
	}

	return result


def find_location(news):
	output = query({
		"inputs": {
			"question": location,
			"context": news
		},
	})
	return output



def find_time(news):
	output = query({
		"inputs": {
			"question": time,
			"context": news
		},
	})
	return output

# result["time"] = output['answer']

def find_vehicle(news):
	output = query({
		"inputs": {
			"question": vehicle,
			"context": news
		},
	})
	return output

# result["vehicle"] = output['answer']

def find_dead(news):
	output = query({
		"inputs": {
			"question": dead,
			"context": news
		},
	})
	return output

# result["dead"] = output['answer']

def find_injured(news):
	output = query({
		"inputs": {
			"question": injured,
			"context": news
		},
	})
	return output
