import requests

s = requests.Session()
r = s.get("http://120.24.86.145:8002/post/")
values = {'what': 'flag'}
r = s.post("http://120.24.86.145:8002/post/", values)
print(r.text)