import zmq
import json

# Message log
message_log = []

# Function to handle operations
def handle_request(request):
    global message_log

    if "clear_message_log" in request and request["clear_message_log"]:
        message_log.clear()
        return {"status": "success", "message": "Message log cleared", "data": message_log}

    elif "delete_message_id" in request and request["delete_message_id"]:
        message_id = request["message_id"]
        message_log = [msg for msg in message_log if msg.get("id") != message_id]
        return {"status": "success", "message": f"Message with ID {message_id} deleted", "data": message_log}

    elif "edit_message_id" in request and request["edit_message_id"]:
        message_id = request["message_id"]
        updated_message = request["updated_message"]
        for msg in message_log:
            if msg.get("id") == message_id:
                msg.update(updated_message)
                return {"status": "success", "message": f"Message with ID {message_id} updated", "data": message_log}
        return {"status": "error", "message": "Message ID not found"}

    elif "key1" in request:
        # Add a new message to the log
        message_log.append(request)
        return {"status": "success", "message": "Message added", "data": message_log}

    else:
        return {"status": "error", "message": "Invalid request"}

# ZeroMQ server setup
def main():
    print("Starting microservice setup...")
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")  # Bind to port 5555
    print("Microservice is running...")


    while True:
        # Receive request
        message = socket.recv_json()
        print(f"Received request: {message}")

        # Handle the request
        response = handle_request(message)

        # Send response
        socket.send_json(response)

if __name__ == "__main__":
    main()
