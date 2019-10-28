
# import socket programming library 
import socket 
  
# import thread module 
from _thread import *
import threading 

import pickle
  
print_lock = threading.Lock() 
my_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": "1964"
}
# thread fuction 
def threaded(c): 
    while True: 
  
        # data received from client 
        data = pickle.loads(c.recv(1024))
        if not data: 
            print('ERROR: Input was not received.')
            c.send(message.encode('ascii'))
        elif (data["option"] == "1"):
            if data["word"] not in my_dict:
                my_dict[data["word"]] = data["meaning"]
                message = "Word added in dictionary."
                c.send(message.encode('ascii'))
            else:
                message = "Word already added in dictionary."
                c.send(message.encode('ascii'))
                
        elif(data["option"] == "2"):
            if data["word"] in my_dict:
                message = "Meaning: "+my_dict[data["word"]]
                c.send(message.encode('ascii'))
            else:
                message = "The word you are looking for is not present in the dictionary."
                c.send(message.encode('ascii'))
            
        elif(data["option"] == "3"):
            if data["word"] in my_dict:
                my_dict.pop(data["word"])
                message = "Word deleted from dictionary."
                c.send(message.encode('ascii'))
            else:
                message = "The word you are trying to delete is not present in the dictionary."
                c.send(message.encode('ascii'))
                
        else:
            message = "ERROR: Incorrect option."
            c.send(message.encode('ascii'))
                
        #print("Message: ",message)
        #c.send(message.encode('ascii')) 
            # lock released on exit 
        print_lock.release() 
        break
  
    # connection closed 
    c.close() 
  
  
def Main(): 
    host = "" 
  
    # reverse a port on your computer 
    # in our case it is 12345 but it 
    # can be anything 
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host, port)) 
    print("socket binded to port", port) 
  
    # put the socket into listening mode 
    s.listen(5) 
    print("socket is listening") 
  
    # a forever loop until client wants to exit 
    while True: 
  
        # establish connection with client 
        c, addr = s.accept() 
  
        # lock acquired by client 
        print_lock.acquire() 
        print('Connected to :', addr[0], ':', addr[1]) 
  
        # Start a new thread and return its identifier 
        start_new_thread(threaded, (c,)) 
    s.close() 
  
  
if __name__ == '__main__': 
    Main() 
