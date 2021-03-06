import pygame

class Joystick:
    def __init__(self):
        self.analogico = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self.botao     = [False, False, False, False, False, False]

        pygame.init()
        self._clock = pygame.time.Clock()
        pygame.joystick.init()

        # # número do joystick plugado
        self._joystick = pygame.joystick.Joystick(0)
        self._joystick.init()


    def verificar_comandos(self):
        self._verificar_botoes()
        self._verificar_analogicos()
        

    def _verificar_botoes(self):
        for event in pygame.event.get():
            # down
            if event.type == pygame.JOYBUTTONDOWN:
                for b in range(len(self.botao)):
                    if self._joystick.get_button(b):
                        self.botao[b] = True
            # up
            elif event.type == pygame.JOYBUTTONUP:
                for b in range(len(self.botao)):
                    if int(event.button) == b:
                        self.botao[b] = False


    def _verificar_analogicos(self):
        for b in range(len(self.analogico)):
            self.analogico[b] = self._joystick.get_axis(b)
        self._clock.tick(20)


    def get_botao_pressionado(self):
        # botoes
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                for n in range(15):
                   if self._joystick.get_button(n):
                       return n, 'botao'
        # analogicos
        for a in range(6):
            valor_analogico = self._joystick.get_axis(a)
            if (valor_analogico > 0.4 or valor_analogico < -0.4) and valor_analogico != -1:
                return a, 'analogico'
        return -1, ''