#!/usr/bin/python3

import sys
import socket
from datetime import datetime

#Defing our target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Translating hostname to IPV4
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py <ip>")

# Add a preety banner
print("-" * 50)
print("Scanning target " + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)

try:
	for port in range(1, 100):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target, port)) # returns an error indicator
		if result == 0:
			print(f"Port {port} is open.")
		s.close()

except KeyboardInterrupt:
	print("\nExisting program.")
	sys.exit()

except socket.error:
	print("Couldn't connect to server.")
	sys.exit()
