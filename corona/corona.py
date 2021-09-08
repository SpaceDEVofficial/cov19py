from .util import request_api

class root_api:
    main_api = ""

class client():

    def __init__(self):
        self.main_api = root_api.main_api

    async def getTodayCount(self):
        res = await request_api(url=self.main_api)
        return res

    
