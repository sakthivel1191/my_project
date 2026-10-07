import requests
def greet(name):
    return f"hello,{name}!"

if __name__ =="__main__":
    print(greet("python...."))

r=requests.get("http://api.github.com")
print("GitHub Status:",r.status_code)
