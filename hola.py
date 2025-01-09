
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

# num=int(input(":"))
# for i in range((num)+1):
#     if i%2!=0:
#         print("es impar",i)
#     if i%2==0:
#         print("es par",i)
        
pal=input("ingrese nombre: ")
print(len(pal))
t=0
for i in range(len(pal)):
    t=t+(i+1)
print(f"total = {t}")
    
# for i in pal:
#     print(i)
    
# n = int(input(":"))
# m = int(input(":"))  
# while True:
#     if m == 0:
#         print("error")
#         n = int(input(":"))
#         m = int(input(":"))
#     else:
#         print(n/m)
#         break