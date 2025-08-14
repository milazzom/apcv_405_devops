from prometheus_client import start_http_server, Counter
import time

REQUESTS = Counter('hello_requests_total', 'Total hello requests')

def process_request():
    REQUESTS.inc()
    print("Hello, monitored world!")

if __name__ == '__main__':
    start_http_server(8000)
    while True:
        process_request()
        time.sleep(5)