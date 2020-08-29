#!/usr/bin/python           # This is client.py file

"""
    James T.  Networking Program- CLIENT.
    Copyright (C) 2020 James T

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    If you want a copy of this source code: https://github.com/xftransformers

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

    Please note you need the 'server.py' file to be running alongside for this 
    code to work sucessfully.
"""



import socket                                                                            #Import socket module
import time                                                                              #Import time module 

usernameToServer = input("Please input a username you wish to use while connected. ")    #Taking a string and storing it in a variable
messageToServer = input("Please input a message. ")                                      #Taking a string and storing it in a variable
s = socket.socket()                                                                      #Create a socket object
host = '192.168.1.6'                                                                     #Sets host ip (socket.gethostname() if running on the same computer)
port = 12345                                                                             #Sets host port

s.connect((host, port))                                                                  #connecting to the server!
s.send(usernameToServer.encode(encoding='UTF-8'))                                        #sending the username to the server
s.send(messageToServer.encode(encoding='UTF-8'))                                         #sending the message to the server

recvfromserver1 = s.recv(1024).decode(encoding='UTF-8')                                  #taking a message recieved from a server and storing it in a variable
recvfromserver2 = s.recv(1024).decode(encoding='UTF-8')                                  #taking a message recieved from a server and storing it in a variable

if recvfromserver2 == f"Hello there, {usernameToServer}.":                               #if statement, scary
    text2server = "Hey server, how is it going?"                                         #storing a string in a variable
    text2server_encoded = text2server.encode(encoding='UTF-8')                           #encoding the string
    s.send(text2server_encoded)                                                          #sending the encoded string


print(recvfromserver1)                                                                   #printing the name
print(recvfromserver2)                                                                   #printing the message from the server
s.close()                                                                                #closing the server connection
