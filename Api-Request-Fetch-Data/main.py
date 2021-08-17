import requests

# we can make request to remote application like gitlab. We can request to get existing application, we can also make
# request to change something. For example, we can write python application that will create project on my gitlab
# account.
# Here we will only fetch info from gitlab.

# requests.get() will take one url and tell python where to find that remote application to talk to it.
# https://gitlab.example.com/api/v4/projects list all the projects however we want only for specific user

response = requests.get("https://gitlab.com/api/v4/users/nanuchi/projects")

# With response.text we are getting a whole single string but we want type of list of dict with type dict
# print(response.text)

# when 2 applications written in different languages communicate with each other then generally we use json
# which all languages understand

# requests json() function converts the data from json into python data type
# json() function will read the json response sent from gitlab and turn it into one of the python datatype

print(type(response.json()))

# since response was a list so json() converted the response to list

my_projects = response.json()

for project in my_projects:
    print(f"Project Name: {project['name']}\nProject Url: {project['web_url']}\n")
