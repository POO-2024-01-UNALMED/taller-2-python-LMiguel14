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
    pass
  def verificarIntegridad(self):
    pass
        

class Motor():
  def __init__(self, cilindros, tipo, registro):
    self.cilindros = cilindros
    self.tipo = tipo
    self.registro = registro
  def cambiarRegistros(self, numero):
    self.registro = numero
  def asignarTipo(self, nuevoTipo):
    if (nuevoTipo == "gasolina") or (nuevoTipo== "electrico"):
      self.tipo= nuevoTipo


class Asiento():
  def _init_ (self, color , precio , registro):
    self.color =    color
    self.precio =   precio
    self.registro = registro
  def cambiarColor(self,  nuevo_color):
    colores = ["verde", "amarillo", "blanco", "negro" , "rojo",]
    if nuevo_color in colores:
      self.color = nuevo_color
