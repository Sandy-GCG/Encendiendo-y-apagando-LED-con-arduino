import pyfirmata

DELAY = 1   #Tiempo de retraso

PORT = 'COM5'   #Puerto al que se conecta el arduino

board = pyfirmata.Arduino(PORT) #La placa se configura con el "pyFirmata" y su puerto correspondiente

while True:
    board.digital[13].write(1)  #La led se encendrá que esté conectado al pin 13
    board.pass_time(DELAY)  #Tardará 1 segundo encendido
    board.digital[13].write(0)  #Se apagará la led que esté conectado al pin 13
    board.pass_time(DELAY)  #Tardará 1 segundo apagado

    board.digital[12].write(1)  #La led se encendrá que esté conectado al pin 12
    board.pass_time(DELAY)  #Tardará 1 segundo encendido
    board.digital[12].write(0)  #Se apagará la led que esté conectado al pin 12
    board.pass_time(DELAY)  #Tardará 1 segundo apagado

    board.digital[11].write(1)  #La led se encendrá que esté conectado al pin 11
    board.pass_time(DELAY)  #Tardará 1 segundo encendido
    board.digital[11].write(0)  #Se apagará la led que esté conectado al pin 12
    board.pass_time(DELAY)  #Tardará 1 segundo apagado