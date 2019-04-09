import asyncio
import websockets
import logging 

# WS server

async def server(websocket, path):
    message = await websocket.recv()

    response = handle_message.delay(message)
    #TODO: implement handle_message celery task
    await websocket.send(response)


start_server = websockets.serve(server, '0.0.0.0', 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()








# async def hello(websocket, path):
#     name = await websocket.recv()
#     print(f"< {name}")

#     greeting = f"Hello {name}!"

#     await websocket.send(greeting)
#     print(f"> {greeting}")

# ws_logger = logging.getLogger('websockets')
# ws_logger.setLevel(logging.INFO)
# ws_logger.addHandler(logging.StreamHandler())

# start_server = websockets.serve(hello, '0.0.0.0', 8765)

# asyncio.get_event_loop().run_until_complete(start_server)
# asyncio.get_event_loop().run_forever()