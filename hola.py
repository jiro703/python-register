from os import system
system("cls")

# e=int(input(": "))
# num=int(input(": "))
# for i in range(10):
#     print("--------------------------")
#     for j in range(10):
#         print(f"{j+1} x {i+1} = {(i+1)*(j+1)}")
    
# for i in range(2):
#     t=0 
#     for i in range(2):
#         g =int(input("agrege gasto: "))
#         t = t+g
#     print(t)

# p=0
# e= int(input(":"))
# for i in range(e):
#     n=int(input(": "))
#     p=(p+n)
# print(f"su promedio es = {(p/e)}")   

# t = 0 
# for i in range(3):
#     print("agrege nota: ")
#     n = float(input(": "))
#     t = t+n
# print(f"su promedio es = {round(t/(i+1))}")

# num=int(input(":"))
# if num%2==0:
#     print("es par")
# else:
#     print("es impar")

num=int(input(":"))
for i in range((num)+1):
    if i%2!=0:
        print("es impar",i)
    if i%2==0:
        print("es par",i)