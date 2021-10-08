import requests as re
import json
url = "http://127.0.0.1:5000/"
route = "api/auth/email_signup"


data={"email":"example@mail.com", "password":"examplepassword", "display_name":"John Doe", "photo_url":"url of a photo"}
act = re.post(url+route, json=json.dumps(data) )
print(act)
print(type(data))