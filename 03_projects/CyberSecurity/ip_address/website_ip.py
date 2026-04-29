import socket

#take the severname

host = "www.google.com"
try:
  # know the ip address of a website
  addr = socket.gethostbyname(host)
  print("IP Address of the website: ", addr)
except socket.gaierror:    #if get address info not occur
  print("The website does not exist")