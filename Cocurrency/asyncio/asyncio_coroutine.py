import asyncio

async def coroutine():
    print('in coroutine')
    return

event_loop = asyncio.get_event_loop()
try:
    print('start coroutine')
    cor = coroutine()
    print('entering coroutine')
    event_loop.run_until_complete(cor)
finally:
    print('closing event loop')
    event_loop.close()