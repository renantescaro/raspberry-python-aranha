from classes.patas import Patas
from classes.joystick import Joystick

# patas    = Patas()
joystick = Joystick()

# patas.frente()

while True:
    joystick.verificar_comandos()
    print(joystick.analogico)
    print(joystick.botao)