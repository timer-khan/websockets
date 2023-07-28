import asyncio
import websockets

async def chat_bot(websocket, path):
    # Greet the user when they connect
    await websocket.send("Welcome to the chat bot! Type 'exit' to leave the chat.")

    while True:
        try:
            # Receive message from the user
            message = await websocket.recv()

            # Check if the user wants to exit the chat
            if message.lower() == 'exit':
                await websocket.send("Goodbye!")
                break

            # Process the message and generate a response
            response = process_message(message)

            # Send the response to the user
            await websocket.send(response)

        except websockets.ConnectionClosed:
            print("Connection closed.")
            break

def process_message(message):
    # Add your custom logic here to process the user's message and generate a response.
    # For simplicity, let's just return a simple response.
    if message.lower() == "hello":
        return "Hello! How can I assist you?"
    elif message.lower() == "how are you?":
        return "I'm just a bot, but thanks for asking!"
    else:
        return "Sorry, I didn't understand that."

# Run the WebSocket server
start_server = websockets.serve(chat_bot, "localhost", 8765)

# Start the event loop to run the server
async def run_server():
    await start_server
    print("Chat bot is running on ws://localhost:8765")
    await asyncio.Event().wait()

# Run the event loop
asyncio.run(run_server())
