#!/usr/bin/python


"""
    James T.  Networking Program- SERVER.
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
    
    Please note you need the 'client.py' file to be running alongside for this 
    code to work sucessfully.    
"""


import socket                                                                                 #imports socket module
from datetime import datetime                                                                 #imports datetime from datetime module

skt = socket.socket()                                                                         #creates socket object
host = '192.168.1.6'                                                                          #sets host ip (socket.gethostname() if running on the same computer)
port = 12345                                                                                  #sets host port
skt.bind((host, port))                                                                        #bind to the port



ipaddresses = {}                                                                              #creates an empty dictionary
ipaddresses["192.168.1.184"] = "James"                                                        #hardcoded an address into the dictionary (set your own IP and name)
ipaddresses["192.168.1.29"] = "Chris"                                                         #hardcoded an address into the dictionary (set your own IP and name)



skt.listen(5)                                                                                 #Wait's for a client connection.
while True:                                                                                   #never ending loop
    cli, addr = skt.accept()                                                                  #establish connection with client
    ip = addr[0]                                                                              #defining addr to a more simple variable 
    
    f = open("ipa.txt","a+")                                                                  #opens ip text file
    
    
    usernamefromClient = cli.recv(1024).decode(encoding='UTF-8')                              #takes message (username in this case) from the client and decodes it to a string 
    message_string = f"Thank you for connecting, your username is '{usernamefromClient}'."    #puts string into a variable
    message_bytes = message_string.encode(encoding='UTF-8')                                   #encoding the string to bytes
    cli.send(message_bytes)                                                                   #sending the bytes to the client
    print(f"The user wants to use '{usernamefromClient}' as a name.")                         #prints a string
    
    
    messageFromClient_string = cli.recv(1024).decode(encoding='UTF-8')                        #decoding some bytes
    
    if messageFromClient_string == "Hello" or "hello" or "Hello!" or "hello!":                #if statement lol
        response = f"Hello there, {usernamefromClient}."                                      #splitting response up, but assigning the string to a varaible
        response_encode = response.encode(encoding='UTF-8')                                   #encoding the variable response
        cli.send(response_encode)                                                             #sending encoded messafe
        print("No message is displayed because it is a generic message.")                     #printing a string
        
        messagethreeFromClient = cli.recv(1024).decode(encoding='UTF-8')
        print(messagethreeFromClient)
        
    else:                                                                                     #else
        print(f"This is a message from '{usernamefromClient}':,"
        f"'{messageFromClient_string}'.")                                                     #printing a string
    
    
    
    ipaddresses[addr[0]] = usernamefromClient                                                 #adding the ip address and name that has just connected to the dictionary
       
    date = datetime.now()                                                                     #putting the date into a variable to make it easier to read
    datestr = date.strftime("%d-%b-%Y (%H:%M:%S.%f)")                                         #converting the date to a string.
    
    
    textfile = (f"The user, '{usernamefromClient}', with the ipaddress: '{ip}', "             #so this was long so i split it into 2 messages to keep it all neat
                f"connected sucessfully at: {datestr}. \n")                                   #basically this is a long string
    
    f.write(textfile)                                                                         #writes a string to a text file on a new line
    print (textfile)                                                                          #printing the string to make sure it works properly
    
    print(ipaddresses)                                                                        #printing the ipaddresses dictionary
    f.close()                                                                                 #closing the file or it won't write to it lol.... ha noobs
    cli.close()                                                                               #closing the client connection BYE LOL