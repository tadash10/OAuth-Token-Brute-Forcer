def analyze_http_status(response):
    # Analyze the HTTP status code and response content for more nuanced feedback
    if response.status_code == 200:
        if "access_token" in response.text:
            return "Login successful: Access token obtained"
        else:
            return "Login successful: Check response content for access token"
    elif response.status_code == 401:
        return "Login failed: Unauthorized (401)"
    elif response.status_code == 403:
        return "Login failed: Forbidden (403)"
    else:
        return f"Login failed with status code: {response.status_code}"
