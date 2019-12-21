customer={"frist_name":"Kamran","Last_name":"Ayoub","adress":"Umerkot"}
def checkKey(customer, key): 
      
    if key in customer.keys(): 
        print("Already exists, ", end =" ") 
        print("value =", customer[key]) 
    else: 
        print("Not Already exists")
key = 'frist_name'
checkKey(customer, key) 