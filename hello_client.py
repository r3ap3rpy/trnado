import tornado.ioloop
from tornado.httpclient import AsyncHTTPClient
import asyncio

async def client(url):
    http_client = AsyncHTTPClient()
    response = await http_client.fetch(url)
    return response.body

async def main():
    result = await client("http://localhost:8080")
    print(result)

result = asyncio.run(client("http://localhost:8080/helloworld"))
print(result)