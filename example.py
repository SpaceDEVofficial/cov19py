import cov19py
import asyncio


async def run():
    crn = cov19py.Client('Your API Key')
    data = await crn.todayCorona()
    print(data['response'])


asyncio.run(run())
