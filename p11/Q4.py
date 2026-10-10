# write a program to detect wheater error occured durring transmission
syndrome=[5,6]
error=False
i=0
while i< len(syndrome):
    if syndrome[i] != 0:
        error=True
    i=i+1
    
if error:
    print("Error detected in recived word ")
else: 
    print("No error detected")
    