import pyphoeus

def main():
	list = [
		('https://httpbin.org/get', {}, 'foo.json'),
		('https://httpbin.org/get', {}, 'bar.json'),
		('https://httpbin.org/get', {}, 'fizz.json'),
		('https://httpbin.org/get', {}, 'buzz.json'),
	]

	hydra = pyphoeus.Hydra()

	requests = [pyphoeus.Request(url, headers=headers) for (url, headers, path) in list]

	hydra.add(*requests)
	hydra.run()

	for (request, path) in zip(requests, [path for (_, _, path) in list]):
		with open(path, 'wb') as f:
			f.write(request.response.content)
