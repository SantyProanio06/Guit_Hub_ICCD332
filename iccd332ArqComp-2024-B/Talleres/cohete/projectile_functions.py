import argparse
def obtenerParametros():
    """
    Esta función captura todos los parametros necesarios para la resolución de las ecuaciones desde la linea de comandos 
    """
    parser = argparse.ArgumentParser(description='Calculadora gráfica del alcance de un cohete')
    parser.add_argument('-V', '--velocidad', type = float, default = 0.0, help = "Parametro de la velocidad inicial, de tipo flotante")

    parser.add_argument('-B', '--coeficiente', type = float, default = 0.0, help = "Coeficiente de resistencia del viento, de tipo flotante")

    parser.add_argument('-t', '--tmax', type = float, default = 0.0, help = "Tiempo maximo, en segundos, de vuelo, de tipo flotante")

    parser.add_argument('-a', '--angulos', type = float, nargs = '+', help = "Angulos de lanzamiento, estan en lista de flotantes")

    return parser.parse_args()




    
    

 
