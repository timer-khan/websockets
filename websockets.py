import asyncio
import websockets

async def echo(websocket, path):
    try:
        async for message in websocket:
            # Просто отправляем обратно полученное сообщение
            await websocket.send(message)
    except websockets.exceptions.ConnectionClosedError:
        print("Соединение закрыто")

async def main():
    # Запускаем сервер на localhost, порт 8765
    server = await websockets.serve(echo, "localhost", 8765)
    print("Сервер WebSocket запущен на ws://localhost:8765")

    # Ожидаем завершения сервера
    await server.wait_closed()

# Запускаем асинхронный цикл
asyncio.get_event_loop().run_until_complete(main())
