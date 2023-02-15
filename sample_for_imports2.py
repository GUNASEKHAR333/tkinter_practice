# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 16:17:50 2023

@author: gundar9t
"""
"""
def fun():
    return "this content is from function fun"

def fun2():
    if __name__ == "__main__":
        print("program is running in main module")
    else:
        print("program is running in other module")
    print("the value of __name__ is ",__name__)
    return "this content is from function fun2"

print(fun)
print(fun())"""
def get_admin_password():
    global get_admin_pasword
    print("called ",get_admin_password)
    return "1234"

get_admin_password()

def secure_function(func):
    def wrapper_():
        pass
        #if user["access level"] == "admin" : 
        #    print("something")
            #print(func)
            #return func()
    #rint(wrapper_)
    return wrapper_
#abc=secure_function(get_admin_password)

get_admin_pasword = secure_function(get_admin_password)
user={"username":"guna","access level":"guest"}
 
#print(abc())
print(get_admin_pasword)
print(get_admin_password())

