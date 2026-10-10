# write  program to encode a message into nonlinear codeword
message="101"
encoded=""
i=0
while i< len(message):
    if message[i]=='1':
        encoded=encoded+"11"
    else:
        encoded=encoded+"00"
    i=i+1
print("Message :",message)
print("Encoded codeword :",encoded)
