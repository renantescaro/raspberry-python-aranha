import time
from classes.servo_motor import ServoMotor

class Patas:
    def __init__(self):
        self._superior_1 = ServoMotor(21)
        self._inferior_1 = ServoMotor(20)
        self._iniciar_angulos()


    def _iniciar_angulos(self):
        self._superior_1.set_angulo(0)
        self._inferior_1.set_angulo(0)

    
    def frente(self):
        time.sleep(2)

        self._inferior_1.set_angulo(10)
        self._superior_1.set_angulo(10)
        time.sleep(2)

        self._inferior_1.set_angulo(20)
        self._superior_1.set_angulo(20)
        time.sleep(2)

        self._inferior_1.set_angulo(30)
        self._superior_1.set_angulo(30)
        time.sleep(2)

        self._inferior_1.set_angulo(40)
        self._superior_1.set_angulo(40)
        time.sleep(2)