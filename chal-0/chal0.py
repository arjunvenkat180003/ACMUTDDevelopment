import requests


url = "https://us-central1-acm-core.cloudfunctions.net/challenge/tags/linux"



obj = {"name" : "linux", "contents" : "I'd just like to interject for a moment. What you're referring to as Linux is in fact, GNU/Linux, or as I've recently taken to calling it, GNU plus Linux..."}

resp = requests.post(url, json=obj)
print("Post :")
print(resp.json())

URLtoken = resp.json()["token"]


url2 = url+"/"+URLtoken


resp2 = requests.get(url2)
print("Get: ")
print(resp2.json())



obj2 = {"name": "linux", "contents": "something else"}

resp3 = requests.patch(url2, data=obj2)

print("Patch: ")

print(resp3.json())

resp4 = requests.delete(url2)

print("Delete: ")


if resp4.status_code == 200:
    print(str(resp4.status_code)+" ok")
