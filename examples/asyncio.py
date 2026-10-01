import asyncio
import aiohttp

async def download(
	url: str,
	headers: dict[str, str],
	output_path: str, session: aiohttp.ClientSession
) -> None:
	async with session.get(url, headers=headers) as response:
		with open(output_path, 'wb') as f:
			while True:
				chunk = await response.content.read(1024)
				if not chunk:
					break
				f.write(chunk)


async def main():
	list = [
		('https://httpbin.org/get', {}, 'foo.json'),
		('https://httpbin.org/get', {}, 'bar.json'),
		('https://httpbin.org/get', {}, 'fizz.json'),
		('https://httpbin.org/get', {}, 'buzz.json'),
	]

	# Run every download from the lists concurrently using aiohttp gather
	async with aiohttp.ClientSession() as session:
		await asyncio.gather(*[download(url, headers, path, session) for (url, headers, path) in list])

asyncio.run(main())
