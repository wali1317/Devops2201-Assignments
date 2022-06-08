import base64


def encode_base64(user_name, password):
    message = user_name + ":" + password
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    print(base64_message)
    return base64_message


def decode_base64():
    base64_message = ""
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64encode(base64_bytes)
    message = message_bytes.decode('ascii')
    print(message)
