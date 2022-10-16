#la liste de tous les nombres premiers jusqu'a un certains nombre...


def Nombre_Premier(nombre: int):

  for i in range(2, nombre):
    if nombre % i == 0:
     return False

  return True 

def Nombre_diviseurs(nombre: int):
  nombre_diviseurs = 0
  for i in range(2, nombre-1):
    if nombre %i == 0:
      nombre_diviseurs += 1
  
  return nombre_diviseurs    



if __name__ == "__main__":

  for i in range(1, 7):
    print(i, "==> ", Nombre_diviseurs(i))
    