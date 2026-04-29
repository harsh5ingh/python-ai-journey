import socket

# take the IP Address of the device

hostName = socket.gethostname()
ip_address = socket.gethostbyname(hostName)
print("Your IP Address: ", ip_address)

