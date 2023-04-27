import numpy as np
import matplotlib.pyplot as plt

class ECGSignal:
    def __init__(self):
        #Peticion de la frecuencia cardiaca
        while 1:
            self.frecuenciaBPM = int(input("Teclee la frecuencia cardiaca entre 30 y 180 BPM: "))
            if(self.frecuenciaBPM < 30):
                print("Teclee un numero valido")
            elif(self.frecuenciaBPM > 180):
                print(print("Teclee un numero valido"))
            else:
                break

        #Peticion del tiempo en segundos para la graficacion
        while 1:
            self.segundos = int(input("Teclee el tiempo a graficar en segundos: "))
            if(self.segundos < 1):
                print("Teclee un numero valido")
            else:
                break

        #tiempos en milisegundos
        self.tiempos = np.array([180, 120, 60, 20, 40, 40, 20, 120, 200, 40, 120, 40])*(60/self.frecuenciaBPM)
        self.tiempoTotal = sum(self.tiempos)
        self.segundosTotales = (self.segundos*self.tiempoTotal)/(60/self.frecuenciaBPM)

        sumatoria = 0
        matrizTiempoSuma = []

        for i in range (0, len(self.tiempos)):
            sumatoria = sumatoria + self.tiempos[i]
            matrizTiempoSuma.append(sumatoria)

        self.tiemposSuma = np.array(matrizTiempoSuma)

        #amplitudes en milivolts
        self.amplitudes = np.array([0.1, 0.1, 0.6, 0.25, 0.25, 0.2, 0.05])

    def signalGraph(self):
        tiempoContador = 0
        contador = 0
        funcion = 0
        matrizGraficaY = []
        matrizGraficaX = []

        for i in range(0, int(self.segundosTotales)):
            if(i < (contador*self.tiempoTotal) + self.tiemposSuma[0]):
                funcion = 0
            elif(i < (contador*self.tiempoTotal) + ( self.tiemposSuma[1] )):
                funcion = self.amplitudes[0] + pow( (tiempoContador - ( self.tiempos[0] + self.tiempos[1]/2 ) ), 2)/( -4*( pow(self.tiempos[1], 2) )/( 16*self.amplitudes[0] ) )
            elif(i < (contador*self.tiempoTotal) + ( self.tiemposSuma[2] )):
                funcion = 0
            elif(i < (contador*self.tiempoTotal) + ( self.tiemposSuma[3] )):
                funcion = ( ( - self.amplitudes[1] )/( - ( - self.tiempos[3] ) ) )*( tiempoContador - (self.tiemposSuma[3]) ) - self.amplitudes[1]
            elif(i < (contador*self.tiempoTotal) + ( self.tiemposSuma[4] )):
                funcion = ( ( self.amplitudes[2] - ( - self.amplitudes[1] ) )/( - ( - self.tiempos[4] ) ) )*( tiempoContador - (self.tiemposSuma[4]) ) + self.amplitudes[2]
            elif(i < (contador*self.tiempoTotal) + ( self.tiemposSuma[5] )):
                funcion = ( ( - self.amplitudes[3] - ( self.amplitudes[2] ) )/( - ( - self.tiempos[5] ) ) )*( tiempoContador - (self.tiemposSuma[5] ) ) - self.amplitudes[3]
            elif(i < (contador*self.tiempoTotal) + ( self.tiemposSuma[6] )):
                funcion = ( ( - ( - self.amplitudes[4] ) )/( - ( - self.tiempos[6] ) ) )*( tiempoContador - (self.tiemposSuma[6]) )
            elif(i < (contador*self.tiempoTotal) + ( self.tiemposSuma[7] )):
                funcion = 0
            elif(i < (contador*self.tiempoTotal) + ( self.tiemposSuma[8] )):
                funcion = self.amplitudes[5] + pow( (tiempoContador - ( self.tiemposSuma[7] + self.tiempos[8]/2) ), 2)/( -4*( pow(self.tiempos[8], 2) )/( 16*self.amplitudes[5] ) )
            elif(i < (contador*self.tiempoTotal) + ( self.tiemposSuma[9] )):
                funcion = 0
            elif(i < (contador*self.tiempoTotal) + ( self.tiemposSuma[10] )):
                funcion = self.amplitudes[6] + pow( (tiempoContador - ( self.tiemposSuma[9] + self.tiempos[10]/2) ), 2)/( -4*( pow(self.tiempos[10], 2) )/( 16*self.amplitudes[6] ) )
            else:
                funcion = 0

            tiempoContador = tiempoContador + 1
            matrizGraficaY.append( funcion )
            matrizGraficaX.append( (tiempoContador + (contador*self.tiempoTotal)) )

            if(len(matrizGraficaX) == int((contador*self.tiempoTotal) + self.tiempoTotal)):
                contador = contador + 1
                tiempoContador = 0

        x = matrizGraficaX
        y = matrizGraficaY

        plt.plot(x, y)
        plt.xlabel('segundos')
        plt.ylabel('amplitud')
        plt.title('Grafica del ECG de ' + str(self.frecuenciaBPM) + ' BMP')
        plt.xlim(0, self.segundosTotales)
        plt.show()

signal = ECGSignal()
signal.signalGraph()