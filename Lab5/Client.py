
# Import socket module 
import socket 
import pickle
  
def Main(): 
    # local host IP '127.0.0.1' 
    host = '127.0.0.1'
  
    # Define the port on which you want to connect 
    port = 12345
  
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
  
    # connect to server on local computer 
    s.connect((host,port)) 
  
    # message you send to server
    message_dict = {}

    
    while True: 
        option = input("\nPlease select an option. \nEnter 1 to add a new word to the dictionary.\nEnter 2 to search for a word.\nEnter 3 to delete a word.\nOption No: ")
        if(option == "1"):
            print("\nAdding new word to dictionary\n")
            message_dict["option"] = "1"
            message_dict["word"] = input("Enter word: ")
            message_dict["meaning"] = input("Enter meaning: ")
            s.send(pickle.dumps(message_dict,-1))
            
        elif(option == "2"):
            print("\nSearch word from dictionary\n")
            message_dict["option"] = "2"
            message_dict["word"] = input("Enter word: ")
            s.send(pickle.dumps(message_dict,-1))
            
        elif(option == "3"):
            print("\nDelete word from dictionary\n")
            message_dict["option"] = "3"
            message_dict["word"] = input("Enter word: ")
            s.send(pickle.dumps(message_dict,-1))
            
        else:
            print("ERROR: The option you entered is not valid. Please try again.\n")
            continue
  
        # messaga received from server 
        data = s.recv(1024) 
  
        # print the received message 
        print('Received from the server :',str(data.decode('ascii'))) 
  
        # ask the client whether he wants to continue 
        ans = input('\nDo you want to continue(y/n) :') 
        if ans == 'y': 
            continue
        else: 
            break
    # close the connection 
    s.close() 
  
if __name__ == '__main__': 
    Main() 
