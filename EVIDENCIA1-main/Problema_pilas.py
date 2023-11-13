class Stack: 
 def __init__(self): 
   self.items = [] 
 def is_empty(self): 
   return self.items == []
 def push(self, item): 
   self.items.insert(0, item)
 def pop(self): 
   return self.items.pop(0) 
 def print_stack(self): 
   print(self.items)
pila = Stack() 

pila.push('a')
pila.push('b')
pila.push('c') 
pila.push('d') 
pila.push('e') 
pila.print_stack() 
pila.pop() 
pila.print_stack() 
pila.pop() 
pila.print_stack() 


class Pila:
 def __init__(self):
   self.items = []
 def estaVacia(self): 
   return self.items == []
 
 def extraer(self): 
   return self.items.pop()
 
 def incluir(self, item): 
   self.items.append(item)
 
s = Pila() 
s.incluir('hola')
s.incluir('verdadero')
s.incluir(1)
s.incluir('falso')
print(s.extraer())

stack = [] 
SEPARA = ("-" * 20) + "\n" 
def main():
 print("1 Aplilar elemento (entero)")
 print("2 Desapilar elemento")
 print("3 Mostrar pila")
 print("4 Salir")
 print(SEPARA * 1)
 option = input("Elija una opción: ")
 if str(option)=="1":
   elemento = input(" Introduzca el numero a apilar: ")
   stack.append(elemento)
   print("**- Elemento apilado -**")
   main()
 elif str(option)=="2":
   if len(stack) == 0:
     print(" No hay elementos para desapilar ")
     main()
   else:
     print("**-El numero: ",stack.pop()," fue desapilado-**")
     main()
 elif str(option)=="3":
   for i in reversed(range(len(stack))):
     print("Pila: ",stack[i])
     main()
 elif str(option)=="4":
   exit()
 else:
   print("\Opción incorrecta.\n")
   main()
main()
