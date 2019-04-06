import asyncio
import websockets

# WS server

async def server(websocket, path):
    message = await websocket.recv()

    response = handle_message.delay(message)
    #TODO: implement handle_message celery task
    await websocket.send(response)

    start_server = websockets.serve(server, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()