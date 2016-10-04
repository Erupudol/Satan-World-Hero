
 
import pygame as pg
import os 
import constants, enemy, personagens, collide
import levels
from pygame.locals import *

 
def main():
    """ Main Program """
    pg.init()
 
#==============================================================================
    """Define o Tamano da Janela do Game:"""
    
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT] 
    screen = pg.display.set_mode(size)
    """Coloca a tela na posiçao desejada do monitor"""
    os.environ["SDL_VIDEO_WINDOW_POS"] = '100,30'
    screen = pg.display.set_mode((1, 1))
#==============================================================================
    pg.mouse.set_visible(0) #Deixa o mouse imvisivel 
#==============================================================================
    """Define o icone e nome do Jogo"""
    icon = pg.image.load("Fotos\SatanIcon.png")
    pg.display.set_caption("Satan's Wolrd Hero")
    pg.display.set_icon(icon)
#==============================================================================
    """Carrega o Jogar, Inimigos e Fases"""
    player = personagens.MrSatan()
    Enemy = enemy.Boss_Satan()
    level_list = []
    level_list.append(levels.Level_01(player,enemy))
#==============================================================================
    """Iniciaiza o Joystick"""
    pg.joystick.init()
    if pg.joystick.get_count()> 0:
        joystick = pg.joystick.Joystick(0)
        joystick.init()
#==============================================================================
    """Seleciona o level Inicial e Define a Posiçao o player e dos inimigos na
    tela"""
    current_level_no = 0
    current_level = level_list[current_level_no]
     
    player_sprite_list = pg.sprite.Group()
    enemy_sprite_list = pg.sprite.Group()
    player.level = current_level
    Enemy.level = current_level
    player.rect.x = 200
    player.rect.y = constants.SCREEN_HEIGHT - player.rect.height
    Enemy.rect.x = 2000
    Enemy.rect.y = constants.SCREEN_HEIGHT - Enemy.rect.height
    player_sprite_list.add(player)
    enemy_sprite_list.add(Enemy)
#==============================================================================
    # Used to manage how fast the screen updates
    clock = pg.time.Clock()
    Regen = USEREVENT + 1 
    pg.time.set_timer(Regen,50)
    pg.time.set_timer(USEREVENT + 2,1000)
    levels.Start_Screen()
#==============================================================================
    """Main Loop"""
    while not constants.Game_loop:
#==============================================================================
        #==============================================================================
        """Joystck Configuration"""
        # Recebe valor real entre (-1) e (1) para o analógico esquerdo no eixo horizontal, onde (0) é parado
        if pg.joystick.get_count() >0:
            axis_lh = joystick.get_axis(0)
            # Recebe valor real entre (-1) e (1) para o analógico esquerdo no eixo vertical, onde (0) é parado
            axis_lv = joystick.get_axis(1)
              
            # Recebe valor inteiro de (-1) e (1) para os botões direcionais, onde (0) é parado
            hat = joystick.get_hat(0)
              
            # Mapa de botões, recebem valor booleano quando pressionados
            button_square = joystick.get_button(3)
            button_x = joystick.get_button(2)
            button_circle = joystick.get_button(1)
            button_triangle = joystick.get_button(0)
            button_L1 = joystick.get_button(4)
            button_R1 = joystick.get_button(5)
            button_L2 = joystick.get_button(6)
            button_R2 = joystick.get_button(7)
            button_start = joystick.get_button(9)
        #==============================================================================
#==============================================================================
        for event in pg.event.get():
            if event.type == pg.QUIT:
                constants.Game_loop = True 
                
            pressed = pg.key.get_pressed()
            if (pressed[pg.K_LALT] and pressed[pg.K_F4]) or (pressed[pg.K_RALT] and pressed[pg.K_F4]):
                pg.quit()
            pg.key.set_repeat(10,20)
            if pressed[pg.K_UP]: player.Muda_Rota_Sup()
            if pressed[pg.K_DOWN]: player.Muda_Rota_Inf()
            if pressed[pg.K_DOWN]: 
                if player.State('move'):
                    player.go_left()    
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    if player.State('move'):
                        player.go_left()
                if event.key == pg.K_RIGHT:
                    if player.State('move'):
                        player.go_right()
                if event.key == pg.K_z:
                    if player.State('punch'):
                        player.Soco_1()
                if event.key == pg.K_x:
                    if player.State('kick'):
                        player.Chute_1()
                if event.key == pg.K_c:
                    if player.State('jump'):
                        player.Jump()
                if event.key == pg.K_v:
                     if player.State('defending'):
                        player.Defesa()
                    
                if event.key == pg.K_b:
                    player.Recive_Dmg()
                if event.key == pg.K_RETURN:
                    levels.Pause()
                   
 
            if event.type == pg.KEYUP:
                if event.key == pg.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pg.K_RIGHT and player.change_x > 0:
                    player.stop()
                if event.key == pg.K_v:
                   player.stop()
                
            if event.type == Regen:
                player.healt_regen()
                player.Mp_regen()
                
            if event.type == USEREVENT+2 :
                print (Enemy.hp)
#==============================================================================
        #==============================================================================
        """Configuraçoes dos botoes do controle"""
        if pg.joystick.get_count()>0:
                # Direcional ou  Analógico esquerdo para a esquerda
                if (hat == ((-1,0) or (-1,1) or (-1,-1))) or axis_lh <= -0.5:
                    if player.State('move'):
                        player.go_left()
                # Direcional ou  Analógico esquerdo para a direita
                if (hat == ((1,0) or (1,1) or (1,-1))) or axis_lh >= 0.5:
                    if player.State('move'):
                        player.go_right()
                        
                if (hat == ((0,1) or (1,1) or (-1,1))) or axis_lv <= -0.5:
                    if player.State('move'):
                        player.Muda_Rota_Sup()
                if (hat == ((0,-1) or (1,-1) or (-1,-1))) or axis_lv >= 0.5:
                    if player.State('move'):
                        player.Muda_Rota_Inf()
                 # Direcional ou  Analógico esquerdo parados   
                if (hat == ((0,0) or (0,1) or (0,-1)) and (-0.5 < axis_lh < 0.5)) and (player.change_x != 0):       
                    player.stop()
                
                if button_x: # Botão X pressionado
                    if player.State('jump'):
                        player.Jump()
                    
                if button_circle: # Botão CIRCULO pressionado
                    if player.State('kick'):
                        player.Chute_1()
                if button_square: # Botão QUADRADO pressionado
                     if player.State('punch'):
                        player.Soco_1()
        #        if button_L1: # Botão L1 pressionado
        #        
        #        else: # Botão L1 solto
        #        
        #        if button_L2: # Botão L2 pressionado
        #            
        #        if button_R1: # Botão R1 pressionado
        #                
        #        if button_R2: # Botão R2 pressionado
        #            
        #        if button_start: # Botão START pressionado
        #==============================================================================
#==============================================================================
            
        

        
        collide.check_colide(player,Enemy)
                
                
        player_sprite_list.update()
        Enemy.ai(player) 
        enemy_sprite_list.update()
        current_level.update()
        
       
        if player.rect.right >= 1000:
            diff = player.rect.right - 1000
            player.rect.right = 1000
            current_level.shift_world(-diff)
  
        
        if player.rect.left <= 0:
            diff = 0 - player.rect.left
            if diff > 0:
                diff = 0
            player.rect.left = 0
            current_level.shift_world(diff)
 
        
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 100
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level
       
 
    
        current_level.draw(screen)
        player_sprite_list.draw(screen)
        enemy_sprite_list.draw(screen)
        player.player_hud(screen)
 
        
      
        clock.tick(constants.FPS)
 
       
        pg.display.flip()
 
 
    pg.quit()
 
if __name__ == "__main__":
    main()