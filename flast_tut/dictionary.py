users = [
    (0, "Suresh", "password"),
    (0, "Misha", "num123"),
    (0, "Joshua", "karadin23"),
    (0, "Anand", "password"),

]

# Map Comprehension
username_mapping = {user[1]: user for user in users}
print(username_mapping)

print(username_mapping["Misha"])

username_input = input("Enter your username: \n")
password_input = input("Enter your password: \n")

_, username, password = username_mapping[username_input]

if password_input == password:
    print("Your details are correct")
else:
    print("Yourt details are incorect")
