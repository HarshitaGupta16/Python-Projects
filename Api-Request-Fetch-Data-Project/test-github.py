import requests

# response = requests.get("https://api.github.com/v3/users/HarshitaGupta16/projects")
response = requests.get("https://api.github.com/users/HarshitaGupta16/repos")

my_projects = response.json()

#print(dir(response))

for project in my_projects:
    print(f"Project Name: {project['name']}\nProject Url: {project['html_url']}\n")
