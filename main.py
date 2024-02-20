class Auto():
  cantidadCreados = 0

  def __init__(self, modelo, precio, asientos, marca, motor, registro):
    self.modelo = modelo                                                              
    self.precio = precio
    self.asientos = asientos
    self.marca = marca
    self.motor= motor
    self.registro = registro

  def  cantidadAsientos(self):
    asientos=0
    for i in self.asientos:
      if isinstance(i, Asiento) == True:
        asientos += 1
    return asientos

  def verificarIntegridad(self):
    registrosAsientos = []
    registros= [self.registro, self.motor.registro]
    for i in self.asientos:
      if isinstance(i, Asiento) == True:
        registrosAsientos.append(i.registro)
    if registrosAsientos == registros :
      print("Auto original")
    else:
      print("Las piezas no son originales")  


class Motor():

  def __init__(self, cilindros, tipo, registro):
    self.cilindros = cilindros
    self.tipo = tipo
    self.registro = registro

  def cambiarRegistro(self, numero):
    self.registro = numero

  def asignarTipo(self, nuevoTipo):
    if (nuevoTipo == "gasolina") or (nuevoTipo== "electrico"):
      self.tipo= nuevoTipo


class Asiento():

  def __init__ (self, color , precio , registro):
    self.color =    color
    self.precio =   precio
    self.registro = registro

  def cambiarColor(self,  nuevo_color):
    colores = ["verde", "amarillo", "blanco", "negro" , "rojo",]
    if nuevo_color in colores:
      self.color = nuevo_color