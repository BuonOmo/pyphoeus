from '../src/pyphoeus' import Hydra, Pyphoeus

hydra = Hydra()
requests = []

for i in range(10):
	request = Pyphoeus('https://httpbin.org/get')
	requests.append(request)
	hydra.queue(request)

hydra.run()

for request in requests:
	print(request.response.body)
