# Secret De-coder 

# save a message to a file

# encrypt the message to a separate file

# option to decrypt a file

def main():
	message = raw_input("Enter your message: ")
	plain_message = open("plain_message.txt" , "w")
	plain_message.write(message)
	plain_message.close()
	
	

main()