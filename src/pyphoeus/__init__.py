import pycurl

class Pyphoeus:
    def __init__(self, url):
        self.url = url
        self.c = pycurl.Curl()
        self.c.setopt(pycurl.URL, self.url)
        self.response = None
        self.error_code = None

class Hydra:
	def __init__(self):
		self.requests = []
		self.multi = pycurl.CurlMulti()

	def queue(self, request):
		self.requests.append(request)
		self.multi.add_handle(request.c)

	def run(self):
		for request in self.requests:
    		self.multi.add_handle(request.c)

		num_handles = len(self.requests)
		while num_handles:
		    ret = self.multi.select(1.0)
		    if ret == -1: continue
		    while True:
		        ret, num_handles = self.multi.perform()
		        if ret != pycurl.E_CALL_MULTI_PERFORM:
		            break

		for request in self.requests:
		    request.response = request.c.getinfo(pycurl.RESPONSE_CODE)
		    request.error_code = request.c.getinfo(pycurl.OS_ERRNO)
		    self.multi.remove_handle(request.c)
