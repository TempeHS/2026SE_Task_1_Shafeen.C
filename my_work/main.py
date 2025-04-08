import csv
import sys

login = []

# the register
user = input("1. Login, 2. Register, 3. Quit ")

# register
if user == "Register":
    username = input("Enter Username: ")
    password = input("Enter Password: ")

with open("storage.csv", "a") as file:
	writer = csv.DictWriter(file, fieldnames=["username", "password"])
	writer.writerow({"username": username, "password": password})

# login
if user == "Login":
    input("Username? ")
    input("Password? ")

#quit
    exit()
    


#incorrect password

#incorrect username 

# logout

