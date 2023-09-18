import requests

def check_captcha_challenge(token_endpoint):
    try:
        # Send a GET request to the token endpoint to check for CAPTCHA challenge
        response = requests.get(token_endpoint, timeout=5)

        if response.status_code == 200 and "captcha" in response.text.lower():
            return True  # CAPTCHA challenge detected
        else:
            return False  # No CAPTCHA challenge detected
    except requests.exceptions.RequestException as e:
        print(f"CAPTCHA check failed with an exception: {str(e)}")
        return False  # Error occurred, assume no CAPTCHA challenge
