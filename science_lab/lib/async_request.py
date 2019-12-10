
from tornado import httpclient
from tornado.httputil import url_concat
import json

httpclient.AsyncHTTPClient.configure('tornado.simple_httpclient.SimpleAsyncHTTPClient', max_clients=300)


async def async_fetch(url, params=None, timeout=20):
    http_client = httpclient.AsyncHTTPClient()
    url = url_concat(url, params)
    request = httpclient.HTTPRequest(url=url, method='GET', request_timeout=timeout)
    response = await http_client.fetch(request)
    response = json.loads(response.body.decode())
    return response


async def http_post_async(url, params=None):
    http_client = httpclient.AsyncHTTPClient()
    request = httpclient.HTTPRequest(url, method='POST', body=json.dumps(params).encode())
    response = await http_client.fetch(request)
    response = json.loads(response.body.decode())
    return response

