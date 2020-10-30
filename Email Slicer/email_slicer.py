# Get the user's email address
email = input("what is your email address?:").strip()

# Slice out the user name
username = email[:email.index("@")]

# Slice out the domain name
domain_name = email[email.index("@")+1]

# Format message
result = "Your username is '{}' and your domain name of the email is '{}'".format(username, domain_name)

# Display the result message
print(result)