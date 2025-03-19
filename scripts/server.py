from aiohttp import web

clients_ws = []
clients_ws_talk = []

async def ws_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    clients_ws.append(ws)
    print("Client connected to /ws")

    async for msg in ws:
        print("Received from /ws:", msg.data)
        # Example: Broadcast message to all clients
        for client in clients_ws:
            await client.send_str(f"{msg.data}")

    clients_ws.remove(ws)
    print("Client disconnected from /ws")
    return ws

async def ws_talk_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    clients_ws_talk.append(ws)
    print("Client connected to /ws_talk")

    async for msg in ws:
        print("Received from /ws_talk:", msg.data)
        # Example: Broadcast message to all clients
        for client in clients_ws_talk:
            await client.send_str(f"{msg.data}")

    clients_ws_talk.remove(ws)
    print("Client disconnected from /ws_talk")
    return ws

app = web.Application()
app.router.add_get('/ws', ws_handler)
app.router.add_get('/ws_talk', ws_talk_handler)

if __name__ == '__main__':
    web.run_app(app, host='0.0.0.0', port=8080)
