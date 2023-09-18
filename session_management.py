import requests

def test_session_management(token_endpoint, access_token):
    try:
        # Send a GET request to a protected resource using the access token
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get("https://api.example.com/protected/resource", headers=headers, timeout=5)

        if response.status_code == 401:
            return "Session management test passed: Access token expired"
        elif response.status_code == 200:
            return "Session management test passed: Access token is valid"
        else:
            return f"Session management test failed: Unexpected status code {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Session management test failed with an exception: {str(e)}"
