import zmq

# Message log
message_log = []

def handle_request(request):
    global message_log

    # a list with a JSON object
    if isinstance(request, list) and len(request) > 0:
        operation = request[0] 

        # clearing the message log
        if "clear_message_log" in operation and operation["clear_message_log"]:
            message_log.clear()
            return message_log

        # deleting a specific message by ID
        elif "delete_message_id" in operation and operation["delete_message_id"]:
            message_id = operation.get("message_id")
            message_log = [msg for msg in message_log if msg.get("id") != message_id]
            return message_log

        # editing a specific message by ID
        elif "edit_message_id" in operation and operation["edit_message_id"]:
            message_id = operation.get("message_id")
            updated_message = operation.get("updated_message")
            for msg in message_log:
                if msg.get("id") == message_id:
                    msg.update(updated_message)
                    return message_log
            return [{'Error': 'Could not load messages'}]

        # add the message to the log
        else:
            message_log.append(operation)
            return message_log

    # invalid request 
    return [{'Error': 'Could not load messages'}]

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
