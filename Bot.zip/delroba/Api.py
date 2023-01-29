import aiohttp

async def api_text(server,type):
	async with aiohttp.ClientSession() as session:
		async with session.get(server) as response:
			if type == "json":
				Post =  await response.json()
				return Post
			elif type == "text":
				Post =  await response.text()
				return Post
			elif type == "read":
				Post =  await response.read()
				return Post