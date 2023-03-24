import time
import numbers as np
import sys

# Imprimir con demora.
def imprimir_con_retraso(s):
#Imprimir una letra a la vez
  for c in s:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.05)

 #crear la clase
class Pokemon1:
  def __init__ (self,tipos,nombre, movimientos, puntos_de_salud, EVs='=========='):
      self.nombre= nombre
      self.tipos=tipos
      self.moviminetos=movimientos
      self.ataques=EVs['ataque']
      self.defensa=EVs['defensa']
      self.puntos_de_salud=puntos_de_salud
      self.barras=20 #Amount od puntos_de_salud barras

class Pokemon2:
    def __init__ (self,tipos,nombre, movimientos,puntos_de_salud,EVs='============='):
      self.nombre=nombre
      self.tipos=tipos
      self.moviminetos=movimientos
      self.ataques=EVs['ataque']
      self.defensa=EVs['defensa']
      self.puntos_de_salud=puntos_de_salud
      self.barras=20 #Amount od puntos_de_salud barras

def impresa(pokemon1, Pokemon2):
  '''Imprimir informacion de lucha'''
  print("-----Battalla de pokemon-----")
  print(f"\n{Pokemon1.nombre}")
  print("tipo/",Pokemon1.tipos)
  print("ataque/", Pokemon1.ataque)
  print("defensa/", Pokemon1.defensa)
  print("Nav./", 3*(1+np.mean([Pokemon1.ataque,Pokemon1.defensa])))
  print("\nVS")

  print(f"\n{Pokemon2.nombre}")
  print("tipo/" ,Pokemon2.tipos)
  print("ataque/" ,Pokemon2.araque)
  print("defensa/" ,Pokemon2.defensa)
  print("Nv./", 3*(1+np.mean([Pokemon2.ataque,Pokemon2.defensa])))
  time.sleep(2)

#crear la bentaja de cada pokemon

def ventaja(pokemon1, Pokemon2):
  '''Considerar la ventaja de tipo
  actualizada con poderes de ataque y deefensa devuelve dos cadenas de informacion
  '''
  version= ['fuego', 'agua' 'planta']
  for i,k in enumerate(version):
 
 #pokemon1

    if Pokemon1.tipos ==k:# caso 1 son del mis tipo mismo.
      if Pokemon2.tipo==k:
          cadena_1_ataque= '\nNo e muy efectivo...'
          cadena_2_ataque= '\nNo es muy efectivo..'

  #pokemon2
  #caso 2, pokemon2 ES FUERTE
    if Pokemon2.tipos== version[(i+1)%3]:
      Pokemon2.ataque*= 2
      Pokemon2.defensa*= 2
      Pokemon1.defensa/=2
      Pokemon1.defensa/=2
      cadena_1_ataque= '\nNo es muy efectivo...'
      cadena_2_ataque= '\n i Es muy eficaz'
  
  #caso 3
  #pokemon2 es debil
    if Pokemon2.tipos== version[(i+2)%3]:
        Pokemon1.ataque*= 2
        Pokemon1.defensa*= 2
        Pokemon2.ataque /= 2
        Pokemon2.defensa = 2
        cadena_1_ataque='\n i Es muy eficaz!'
        cadena_2_ataque= '\nNo es muy efectivo...'
    return cadena_1_ataque, cadena_2_ataque

#crear tunos a los pokemon
def turnos(self, Pokemon2, cadena_1_ataque, cadena_2_ataque):
  '''Empieza con Pokemon1, elige ataque y calcular los nuevos puntos de salud. Haz lo mismo con Pokemon2. Siga hasta que los puntos de salud de uno de los pokemon son < 0 Actualizar los datos'''
  while (Pokemon1.barra > 0) and (Pokemon2.barra > 0):
    #imprimir los puntos_de_salud de cada Pokemon
    print(f"\n{Pokemon1.nombre}\t\tPS\t{Pokemon1.puntos_de_salud}")
    print(f"{Pokemon2.nombre}\t\tPS\t{Pokemon2.puntos_de_salud}\n")
    
  #movimiento de cada pokemon

  #pokemon1
    print(f"¡Adelante{Pokemon1.nombre}!")
    for i, x in enumerate(Pokemon1.movimiento):
      print(f"{i+1}.",x)
      index =int(input('Elige un movimiento'))
      imprimir_con_retraso(f"\n¡{Pokemon1.nombre}uso {Pokemon1.movimiento[index-1]}!")
      time.sleep(1)
      imprimir_con_retraso(cadena_1_ataque)

#Determinar daños pokemon2
    Pokemon2.barra -= Pokemon1.ataque
    Pokemon2.puntos_de_salud=""

#Agregar barras adiccionales mas defensa boost
    for j in range(int(Pokemon2.barras+.1*Pokemon2.defensa)):
        Pokemon2.puntos_de_salud += "="
        time.sleep(1)
        print(f"\n{Pokemon1.nombre}\t\tPS\t{Pokemon1.puntos_de_salud}")
        print(f"\n{Pokemon2.nombre}\t\tPS\t{Pokemon2.puntos_de_salud}\n")
        time.sleep(5)
    #Comprobar si pokemon1 se debilito
        if Pokemon2.barras <=0:
          imprimir_con_retraso("\n..."+ Pokemon2.nombre + 'se debilito')
          break

          print(f"¡Adelante{Pokemon2.nombre}!") #pokemon2
    for i, x in enumerate(Pokemon2.movimientos):
            print(f"{i+1}.",x)
            index = int(input('Elige un movimiento'))
            imprimir_con_retraso(f"\n¡{Pokemon2.nombre}uso {Pokemon2.movimiento[index-1]}!")
            time.sleep(1)
            imprimir_con_retraso(cadena_2_ataque)

            #Determinar daños pokemon2
            Pokemon1.barra -= Pokemon2.ataque
            Pokemon1.puntos_de_salud=""

  #Agregar barras adiccionales mas defensa boost
    for j in range(int(Pokemon1.barras+.1*Pokemon1.defensa)):
            Pokemon1.puntos_de_salud +="="

            time.sleep(1)
            print(f"\n{Pokemon1.nombre}\t\tPS\t{Pokemon1.puntos_de_salud}")
            print(f"\n{Pokemon2.nombre}\t\tPS\t{Pokemon2.puntos_de_salud}\n")
            time.sleep(5)

            #Comprobar si pokemon2 se debilito
            if Pokemon1.barras <=0:
              imprimir_con_retraso("\n..."+ Pokemon1.nombre + 'se debilito')
            break   

#lucha
def lucha(self, Pokemon2):
  '''permite que dos pokemon luchen entre ellos'''
  #imprimir informacio de lucha
  Pokemon1.impresa(Pokemon2)

  #considerar la ventaja de tipo
  cadena_1_ataque, cadena_2_ataque= Pokemon1.ventaja(Pokemon2)

  #Ahora para lucha real....
  #Continua mientras Pokemon aun tenga puntos_de_vida
  Pokemon1.turno(Pokemon2, cadena_1_ataque, cadena_2_ataque)
  #recibir dinero(premio)
  money=np.random.choice(10000)
  imprimir_con_retraso(f"\nEl opente te pago $ {money}.\n")

  #crear pokemon objecto
  if __name__ == '_main_':
    
    Charizard = Pokemon('Charizard', 'fuego', ['Lanzallamas', 'Pirotecnia', 'Giro fuego', 'Ascuas'], {'ataque': 12, 'defensa': 8})

    Blastoise = Pokemon('Blastoise', 'agua', ['Pistola Agua', 'Burbuja', 'Hidropulso', 'Hidrobomba'], {'ataque': 10, 'defensa': 10})
                                              
    Venusaur = Pokemon('Venusaur', 'planta', ['LatliAdelante Cepa', 'Hoja Afilada', 'Rayo Solar','Abatidoras'], {'ataque': 8, 'defensa': 12})

    Charizard. lucha (Blastoise)
