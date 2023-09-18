def interactive_login():
    # Create an interactive mode where the penetration tester can manually input credentials
    username = input("Enter username: ")
    password = input("Enter password: ")

    # You can customize this part to send the provided credentials to the authentication endpoint
    # and check the response
    return username, password
