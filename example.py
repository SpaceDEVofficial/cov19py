import corona
import asyncio


async def run():
    crn = corona.Client(
        '2rVxc96OKnB%2BFzDfQgVjSNuYgpEHXCnfJ%2B8WRbtKI1R0Gao%2BCUEJNfe1kr5S3OxYR2qbhpkUDdLN0XAmZDbIiA%3D%3D')
    print(await crn.todayCorona())


asyncio.run(run())
