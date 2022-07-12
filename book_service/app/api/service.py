import os
import httpx

PUBLISHER_HOST_URL = 'http://localhost:8002/api/v1/publishers/'
url = os.environ.get('PUBLISHER_HOST_URL') or PUBLISHER_HOST_URL

def is_publisher_present(publisher_id: int):
    r = httpx.get(f'{url}{publisher_id}')
    return True if r.status_code == 200 else False