# # # function and module

# # # A file containing multiple module is called function
# # # function - function is a block of code which we use when we want 
# # # Types of function
# # 1. pre defined ex- print,input,int,float
# # 2. user defined function 
# # there will be 4 way to  declare a user define function
# # 1. No return no argument 
# # 2. no return with argument 
# # 3. return with no argument
# # 4. return with argument 
# # in python one more single line function which is annonmus function named lambda function 
# # in python three more functions which is map , filter , reduce . 
# # Local and global variable
# # when we declare any variable inside the functions then scope of this variable are only present inside the function  
# # when we declare any variable outside the functions then scope of this variable are outside the function as well as inside the function  

# # Syntax of a function 
# # Def = define function 
  


# #   def function_name():
# #       statement 1
# #       statement 2
# #  function_name()
# # 1. No return no argument 
# # argument and parameter
# def noreturn_noargument():
#     a=10
#     b=10
#     c=a+b
#     print("addition = ",c)
# noreturn_noargument()
# # def noreturn_noargument( here parameter is store):
# #     a=10
# #     b=10
# #     c=a+b
# #     print("addition = ",c)
# # noreturn_noargument(here argument isstore )

# # 2. Not return with argument 
def noreturn_withargument(n):
    for i in range(1,n+1,1):
        for j in range(1,i+1,1):
            print(i,end=" ")
        print()    
          
    
noreturn_withargument(5)        

# # 2. Default argument 
def noreturn_withargument(n=10):
    for i in range(n,0,-1):
        for j in range(1,i+1,1):
            print(i,end=" ")
        print()    
          
    
noreturn_withargument()      