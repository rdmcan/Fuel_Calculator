
# FUNCIÓN CALIFICADA calcular_costo_gasolina

def calcular_costo_gasolina(num_litros, precio_galon):
  """
  Calcula el costo de n litros de gasolina a partir del precio del galón
  de gasolina.

  :param num_litros: número de litros a adquirir.
  :param precio_galon: precio de 1 galón de gasolina.

  :return: costo total de los 'num_litros' de gasolina.
  """
  ###### ESCRIBA SU CÓDIGO AQUÍ ######

  galones = num_litros / 3.79
  costo_gasolina = galones * precio_galon

  ###### FIN DEL CÓDIGO ######

  return round(costo_gasolina,4)


# FUNCIÓN CALIFICADA calcular_consumo_vehiculo

def calcular_consumo_vehiculo(distancia, consumo):
  """
  Calcula cuántos litros de gasolinas se consumen para recurrer una distancia
  dada en un vehiculo con un consumo dado.

  :param distancia: distancia de la cual se quiere saber cuantos litros
  van a ser consumidos.
  :param consumo: número de litros que se consumen por cada 100 km.

  :return: número de litros que consumirá el trayecto
  """
  ###### ESCRIBA SU CÓDIGO AQUÍ ######

  cantidad_de_litros = (distancia * consumo) / 100

  ###### FIN DEL CÓDIGO ######

  return cantidad_de_litros

# FUNCIÓN CALIFICADA reportar_gasto_viaje

def reportar_gasto_viaje(distancia, precio_galon,
                         consumo_vehiculo = 10):
  """
  Calcula cuanto dinero se debe gastar en gasolina para realizar el viaje con
  las condiciones ingresadas.

  :param distancia: número de kilometros a recorrer.
  :param precio_galon: costo que tiene 1 galón de gasolina.
  :param consumo: número de litros que consume el vehículo cada 100 km.

  :return: costo que se realizará en gasolina para completar el viaje
  """
  ###### ESCRIBA SU CÓDIGO AQUÍ ######

  consumo = calcular_consumo_vehiculo(distancia, consumo_vehiculo)
  costo = calcular_costo_gasolina(consumo, precio_galon)
  # costo  = float("{:.4f}".format(costo))
  mensaje_costo = f'El viaje ({round(distancia,4)} km) tiene un costo de {costo:.4f}$'

  ###### FIN DEL CÓDIGO ######

  return mensaje_costo
