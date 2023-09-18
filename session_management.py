import requests

def test_session_management(token_endpoint, access_token):
    try:
        # Send a GET request to a protected resource using the access token
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get("https://api.example.com/protected/resource", headers=headers, timeout=5)

        if response.status_code == 401:
            return "Session management test passed: Access token expired"
        else:
            return "Session management test failed: Access token still valid"
    except requests.exceptions.RequestException as e:
        return f"Session management test failed with an exception: {str(e)}"
