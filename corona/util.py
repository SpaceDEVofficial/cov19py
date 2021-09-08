import json

import aiohttp

async def request_api(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url) as resp:
            pr = await resp.read()
            sid = pr.decode('utf-8')
            answer = json.loads(sid)
            return answer