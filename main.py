import asyncio
import aiohttp
import time

async def fetch(session, url, index):
    try:
        start_time = time.time()  # Время начала запроса
        async with session.get(url) as response:
            end_time = time.time()  # Время окончания запроса
            response_time = int((end_time - start_time) * 1000)  # Время ответа в миллисекундах
            status_code = response.status  # HTTP-код ответа
            print(f"Try {index + 1}: {response_time}ms {status_code}")
    except Exception as e:
        print(f"Try {index + 1}: Error {str(e)}")

async def main():
    url = input("Enter the URL: ")
    num_requests = int(input("Enter the number of requests: "))

    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url, i) for i in range(num_requests)]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
