

Fora do "while" do jogo:

# Inicializa o joystick
pygame.joystick.init()
joystick = pygame.joystick.Joystick(1)
joystick.init()

Dentro do "while" do jogo:

# Recebe valor real entre (-1) e (1) para o analógico esquerdo no eixo horizontal, onde (0) é parado
axis_lh = joystick.get_axis(0)
# Recebe valor real entre (-1) e (1) para o analógico esquerdo no eixo vertical, onde (0) é parado
axis_lv = joystick.get_axis(1)
        
# Recebe valor inteiro de (-1) e (1) para os botões direcionais, onde (0) é parado
hat = joystick.get_hat(0)
        
# Mapa de botões, recebem valor booleano quando pressionados
button_square = joystick.get_button(0)
button_x = joystick.get_button(1)
button_circle = joystick.get_button(2)
button_triangle = joystick.get_button(3)
button_L1 = joystick.get_button(4)
button_R1 = joystick.get_button(5)
button_L2 = joystick.get_button(6)
button_R2 = joystick.get_button(7)
button_start = joystick.get_button(9)

for event in pygame.event.get():
    if (hat == ((-1,0) or (-1,1) or (-1,-1))) or axis_lh <= -0.5:
        # Direcional ou  Analógico esquerdo para a esquerda
            
    if (hat == ((1,0) or (1,1) or (1,-1))) or axis_lh >= 0.5:
        # Direcional ou  Analógico esquerdo para a direita
            
    if (hat == ((0,0) or (0,1) or (0,-1)) and (-0.5 < axis_lh < 0.5)) and (player1.change_x != 0):
        # Direcional ou  Analógico esquerdo parados
        
    if button_x:
        # Botão X pressionado
            
    if button_circle:
        # Botão CIRCULO pressionado
            
    if button_square:
        # Botão QUADRADO pressionado
            
    if button_L1:
        # Botão L1 pressionado
    else:
        # Botão L1 solto
        
    if button_L2:
        # Botão L2 pressionado
            
    if button_R1:
        # Botão R1 pressionado
            
    if button_R2:
        # Botão R2 pressionado
            
    if button_start:
        # Botão START pressionado