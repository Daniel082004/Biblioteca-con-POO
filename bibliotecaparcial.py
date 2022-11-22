import datetime

libro1 = []
libro2 = []
libro3 = []

class usuario:
    
    def datos(self, nombre = "", cedula= ""):
        
        self.nombre_usuario = nombre
        self.cedula_usuario = cedula
        
    def set_nombre(self, nombre):
        self.nombre_usuario = nombre
    def get_nombre(self):
        return self.nombre_usuario
    def set_cedula(self, cedula):
        self.cedula_usuario = cedula
    def get_cedula(self):
        return self.cedula_usuario
    
class autor:
    
    def autor_libro(self, autor = ""):
        
        self.autor = autor
        
    def set_autor(self, nombre):
        self.autor = autor
    def get_autor(self):
        return self.autor
        

class libro:
    
    def libros(self):
        print ("===========================================")
        print ("[/************LIBROS PARA VER\************]")
        print(self.libroN1())
        print(self.libroN2())
        print(self.libroN3())
        self.mostrar()
    
    def libroN1(Self):
        print ("===========================================")
        print ("******************LIBRO 1******************")
        print ("Titulo: Caperucita Roja ")
        print ("Autor: Charles perrout y los hermanos green")
        print ("ISBN: 23435-X-34800 ")
        print ("Paginas: 34 pag ")
        print ("Genero: Cuento ")
        print ("Fecha de publicacion: 1697")
        print ("Pais: Alemania ")
        print ("===========================================")
        
         
    def libroN2(Self):
        print ("===========================================")
        print ("******************LIBRO 2******************")
        print ("Titulo: Alicia en el pais de las maravillas ")
        print ("Autor: Lewiss Carroll ")
        print ("ISBN: 978-84-9044-159-6 ")
        print ("Paginas: 784 pag ")
        print ("Genero: Novela ")
        print ("Fecha de publicacion: 26 de Noviembre de 1865 ")
        print ("Pais: Reino Unido ")
        print ("===========================================")
        
    
    def libroN3(self):
        print ("===========================================")
        print ("******************LIBRO 3******************")
        print ("Titulo: Cronica de una muerte anunciada ")
        print ("Autor: Gabriel Garcia Marquez ")
        print ("ISBN: 978-84-397-0386-0 ")
        print ("Paginas: 156 pag ")
        print ("Genero: Narrativo ")
        print ("Fecha de publicacion: 1981 ")
        print ("Pais: Colombia ")
        print ("===========================================")
        
        
class mostrar_informacion(usuario,autor,libro):
    
    def mostrar(self):
        import datetime
        print()
        print ("===========================================")
        print("Bienvenido a la biblioteca virtual de Daniel ")
        tiempo =datetime.datetime.now()
        fecha= datetime.datetime.strftime(tiempo,"%B/%d/%Y")
        print("Fecha:",fecha)
        hora=datetime.datetime.strftime(tiempo,"%I:%M:%S") 
        print("Hora:",hora)
        print()
        print ("¿Que deseas hacer en nuestra biblioteca virtual?: ")
        print ("1) Ver libros ")
        print ("2) Pedir prestado un libro ")
        print ("3) Salir ")
        print()
        elija = int(input("Escoga la opcion deseada: "))
        if elija == 1:
            super(mostrar_informacion,self).libros()
        if elija == 2:
            l = usuario()
            print("DATOS PARA SOLICITAR UN LIBRO ")
            l.set_nombre(input("Nombre del Usuario: "))
            l.set_cedula(input("TI/CC: "))
            print ("=======================================")
            print ("1) CAPERUCITA ROJA ")
            print ("2) ALICIA EN EL PAIS DE LAS MARAVILLAS ")
            print ("3) CRONICA DE UNA MUERTE ANUNCIADA " )
            print ("=======================================") 
            print() 
            opcion = int(input("¿Que libro desea prestar?: "))
            print()
            if opcion == 1:
                if 1 in libro1:
                    print("Libro ocupado ")
                    self.mostrar()
                else: 
                    print("[Prestamo Exitoso, disfrutalo]")
                    libro1.append(1)
                    self.mostrar()
            
            if opcion == 2:
                if 2 in libro2:
                    print("Libro ocupado ")
                    self.mostrar()
                else: 
                    print("[Prestamo Exitoso, disfrutalo]")
                    libro2.append(2)
                    self.mostrar()
                    
            if opcion == 3:
                if 3 in libro3:
                    print("Libro ocupado ")
                    self.mostrar()
                else: 
                    print("[Prestamo Exitoso, disfrutalo]")
                    libro3.append(3)
                    self.mostrar()
          
        if elija == 3:
            exit()
            
biblioteca = mostrar_informacion()
biblioteca.mostrar()
            