class Name:
 
    # Constructor
    def __init__(self,name):
        self.name = name
 
    # For call to repr(). Prints object's information
    def __repr__(self):
        return self.name+"repr"  
 
    # For call to str(). Prints readable form
    def __str__(self):
        return self.name+"str"
 
 
# Driver program to test above
t = Name("nandani")
 
# Same as "print t"
print (t)
# print (str(t))