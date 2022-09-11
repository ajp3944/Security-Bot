import requests

def file_info(user_input):
    url = "https://url-shortener-service.p.rapidapi.com/shorten"
    payload = f'url={user_input}'
    print(user_input)
    headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "2efad7f699msh835311fb7809de6p1bc0dajsn915f78e41a14",
	"X-RapidAPI-Host": "url-shortener-service.p.rapidapi.com"
}

    response = requests.request("POST", url, data=payload, headers=headers).json()

    return "Here your shorten link " + response.get("result_url")

#file_info('https://google.com')