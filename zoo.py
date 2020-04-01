    
class animal: 
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo   = tipo
       
    
    def set_nombre(self,nombre): 
        self.nombre = nombre
    def set_tipo(self,tipo): 
        self.tipo = tipo
          
    def get_nombre(self):
        print(self.nombre)
        self.get_miprueba()
    def get_tipo(self):
        print(self.nombre)
        self.get_miprueba()
            
       
        
def main():
    
    nanimales = int(input("¿Cuántos animales son?: "))
    listanimales = [nanimales]
    for i in range(nanimales):
        anombre = input("¿Cuál es su nombre?")
        atipo = input("¿Qué tipo es?")
        if i<(nanimales - 1):
            listanimales[i] = animal(anombre,atipo)
        print('Los animales agregados son %s' % listaanimales[:])
    animbusc=int(input("Dame un id, 0 es el primeroen la lista"))
    
    posicion=listanimales.index(animbusc)
    print(posicion)
    nuevo=(input("nueva categoría"))
    listanimales.extend(posicion,nuevo)
    
    if __name__ == "__main__":
    main()