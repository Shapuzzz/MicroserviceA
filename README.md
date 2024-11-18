# Microservice A - Communication Contract

## How to Programmatically REQUEST Data
To request data from Microservice A, send a **JSON object** over ZeroMQ. Each request must include the specific operation (e.g., `clear_message_log`, `delete_message_id`, etc.) and any required parameters. Example requests:
- **Clear Message Log**: `{"clear_message_log": true}`
- **Delete a Message by ID**: `{"delete_message_id": true, "message_id": 1}`
- **Edit a Message by ID**: `{"edit_message_id": true, "message_id": 2, "updated_message": {"key1": "new_value", "key2": "updated_value"}}`
- **Add a New Message**: `{"key1": "valueA", "key2": "valueB", "id": 1}`

## How to Programmatically RECEIVE Data
Microservice A sends a **JSON response** over ZeroMQ. The response includes:
- `status`: Indicates success or failure (`"success"` or `"error"`).
- `message`: Describes the result of the operation.
- `data`: (Optional) Includes the updated list of messages.. 

Example responses:
- **Successful Operation**: `{"status": "success", "message": "Message added", "data": [{"id": 1, "key1": "valueA", "key2": "valueB"}]}`
- **Error (e.g., invalid ID)**: `{"status": "error", "message": "Message ID not found"}`

## UML Sequence Diagram
Below is a UML sequence diagram that explains how requests and responses are handled by Microservice A:

![image](https://github.com/user-attachments/assets/da6a7eaa-351c-4c8c-82de-64aa40096dd8)

## Note
- Ensure that ZeroMQ is properly installed in your development environment.



