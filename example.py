import corona
import asyncio


async def run():
    crn = corona.Client('Your API Key')
    print(await crn.todayCorona())


asyncio.run(run())
