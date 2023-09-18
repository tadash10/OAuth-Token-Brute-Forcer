import requests

def send_request_with_timeout(url, data=None, timeout=5):
    try:
        # Send a request with a specified timeout
        response = requests.post(url, data=data, timeout=timeout)
        return response
    except requests.exceptions.RequestException as e:
        print(f"Request failed with an exception: {str(e)}")
        return None
