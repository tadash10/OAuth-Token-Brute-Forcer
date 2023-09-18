import time

def throttle_requests(rate_limit, total_requests):
    # Throttle the rate of login attempts
    # rate_limit: number of requests per second
    # total_requests: total number of requests to send

    interval = 1 / rate_limit
    for _ in range(total_requests):
        response = send_request_with_timeout(url, data=data)

        if response:
            print(analyze_http_status(response))

        time.sleep(interval)
