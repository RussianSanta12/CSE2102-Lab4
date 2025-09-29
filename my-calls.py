import httpx

url = "https://shiny-space-meme-rjg6v7rwx6j25775-5000.app.github.dev/"

response = httpx.get(url)
print(response.status_code)
print(response)



response = httpx.get(url)
print(response.status_code)
print(response.text)

mydata = {
    "text": "Hello Phil!",
    "param2": "Making a POST request",
    "body": "my own value"
}

# A POST request to the API
response = httpx.post(url + "echo", data=mydata)

# Print the response
print(response.status_code)
print(response.text) 