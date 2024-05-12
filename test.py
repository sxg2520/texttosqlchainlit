import time

def do_something():
    print("start task")
    time.sleep(5)
    print("task completed")
    
print("before task")
do_something()
print("after task")

import asyncio

async def do_something():
    print("start task")
    await asyncio.sleep(8)
    print("task completed")
    
async def main():
    print("before task")
    await do_something()
    print("after task")
    
asyncio.run(main())

