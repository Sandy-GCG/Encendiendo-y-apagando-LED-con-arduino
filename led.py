import pyfirmata

DELAY = 1

PORT = 'COM5'

board = pyfirmata.Arduino(PORT)

while True:
    board.digital[13].write(1)
    board.pass_time(DELAY)
    board.digital[13].write(0)
    board.pass_time(DELAY)

    board.digital[12].write(1)
    board.pass_time(DELAY)
    board.digital[12].write(0)
    board.pass_time(DELAY)

    board.digital[11].write(1)
    board.pass_time(DELAY)
    board.digital[11].write(0)
    board.pass_time(DELAY)