import pygame as pg
import os 
import constants, enemy, personagens, collide, random , player
import levels , pygame.locals 

 
def main():
    """ Main Program """
    pg.init()
 
#==============================================================================
    """Define o Tamano da Janela do Game:"""
    icon = pg.image.load("Fotos\SatanIcon.png")
    pg.display.set_caption("Satan's Wolrd Hero")
    pg.display.set_icon(icon)
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT] 
    screen = pg.display.set_mode(size)
    """Coloca a tela na posiçao desejada do monitor"""
    os.environ["SDL_VIDEO_WINDOW_POS"] = '100,30'
    screen = pg.display.set_mode((1, 1))
#==============================================================================
    pg.mouse.set_visible(0) #Deixa o mouse imvisivel 
#==============================================================================
    """Define o icone e nome do Jogo"""
    
#==============================================================================
    """Carrega o Jogar, Inimigos e Fases"""
    player1 = personagens.MrSatan()
    boss1 = enemy.Cell()
#==============================================================================
#    Enemys
#==============================================================================
    enemys_list =[[enemy.Cell_Jr(),random.choice(range(-200,2400)),constants.SCREEN_HEIGHT, random.choice(range(0,100))],
[enemy.Cell_Jr(),random.choice(range(-200,2400)),constants.SCREEN_HEIGHT, random.choice(range(0,100))],
[enemy.Cell_Jr(),random.choice(range(-200,2400)),constants.SCREEN_HEIGHT, random.choice(range(0,100))],
[enemy.Cell_Jr(),random.choice(range(-200,2400)),constants.SCREEN_HEIGHT, random.choice(range(0,100))],
[enemy.Cell_Jr(),random.choice(range(-200,2400)),constants.SCREEN_HEIGHT, random.choice(range(0,100))], 
[enemy.Cell_Jr(),random.choice(range(-200,2400)),constants.SCREEN_HEIGHT, random.choice(range(0,100))],
[enemy.Cell_Jr(),random.choice(range(-200,2400)),constants.SCREEN_HEIGHT, random.choice(range(0,100))],
[enemy.Cell_Jr(),random.choice(range(-200,2400)),constants.SCREEN_HEIGHT, random.choice(range(0,100))],
[enemy.Cell_Jr(),random.choice(range(-200,2400)),constants.SCREEN_HEIGHT, random.choice(range(0,100))],
[enemy.Cell_Jr(),random.choice(range(-200,2400)),constants.SCREEN_HEIGHT, random.choice(range(0,100))],
[enemy.Cell_Jr(),random.choice(range(-200,2400)),constants.SCREEN_HEIGHT, random.choice(range(0,100))], 
[enemy.Cell_Jr(),random.choice(range(-200,2400)),constants.SCREEN_HEIGHT, random.choice(range(0,100))],
[enemy.Cell_Jr(),random.choice(range(-200,2400)),constants.SCREEN_HEIGHT, random.choice(range(0,100))],
[enemy.Cell_Jr(),random.choice(range(-200,2400)),constants.SCREEN_HEIGHT, random.choice(range(0,100))],
[enemy.Cell_Jr(),random.choice(range(-200,2400)),constants.SCREEN_HEIGHT, random.choice(range(0,100))],
[enemy.Cell_Jr(),random.choice(range(-200,2400)),constants.SCREEN_HEIGHT, random.choice(range(0,100))],
[enemy.Cell_Jr(),random.choice(range(-200,2400)),constants.SCREEN_HEIGHT, random.choice(range(0,100))], 
[enemy.Cell_Jr(),random.choice(range(-200,2400)),constants.SCREEN_HEIGHT, random.choice(range(0,100))],
[enemy.Cell_Jr(),random.choice(range(-200,2400)),constants.SCREEN_HEIGHT, random.choice(range(0,100))],
[enemy.Cell_Jr(),random.choice(range(-200,2400)),constants.SCREEN_HEIGHT, random.choice(range(0,100))],
[enemy.Cell_Jr(),random.choice(range(-200,2400)),constants.SCREEN_HEIGHT, random.choice(range(0,100))],
[enemy.Cell_Jr(),random.choice(range(-200,2400)),constants.SCREEN_HEIGHT, random.choice(range(0,100))],
[enemy.Cell_Jr(),random.choice(range(-200,2400)),constants.SCREEN_HEIGHT, random.choice(range(0,100))], 
[enemy.Cell_Jr(),random.choice(range(-200,2400)),constants.SCREEN_HEIGHT, random.choice(range(0,100))],
[enemy.Cell_Jr(),random.choice(range(-200,2400)),constants.SCREEN_HEIGHT, random.choice(range(0,100))],
[enemy.Cell_Jr(),random.choice(range(-200,2400)),constants.SCREEN_HEIGHT, random.choice(range(0,100))],
[enemy.Cell_Jr(),random.choice(range(-200,2400)),constants.SCREEN_HEIGHT, random.choice(range(0,100))],
[enemy.Cell_Jr(),random.choice(range(-200,2400)),constants.SCREEN_HEIGHT, random.choice(range(0,100))],
[enemy.Cell_Jr(),random.choice(range(-200,2400)),constants.SCREEN_HEIGHT, random.choice(range(0,100))], 
[enemy.Cell_Jr(),random.choice(range(-200,2400)),constants.SCREEN_HEIGHT, random.choice(range(0,100))],
[enemy.Cell_Jr(),random.choice(range(-200,2400)),constants.SCREEN_HEIGHT, random.choice(range(0,100))],
[enemy.Cell_Jr(),random.choice(range(-200,2400)),constants.SCREEN_HEIGHT, random.choice(range(0,100))],
[enemy.Cell_Jr(),random.choice(range(-200,2400)),constants.SCREEN_HEIGHT, random.choice(range(0,100))],
[enemy.Cell_Jr(),random.choice(range(-200,2400)),constants.SCREEN_HEIGHT, random.choice(range(0,100))],
[enemy.Cell_Jr(),random.choice(range(-200,2400)),constants.SCREEN_HEIGHT, random.choice(range(0,100))], 
[enemy.Cell_Jr(),random.choice(range(-200,2400)),constants.SCREEN_HEIGHT, random.choice(range(0,100))],
[enemy.Cell_Jr(),random.choice(range(-200,2400)),constants.SCREEN_HEIGHT, random.choice(range(0,100))]] 
    backup_enemys_list = enemys_list[:]      
    level_list = []
    enemy_l=[]
    backup_enemy_l = []
    backup_enemy  = []
    backup_boss = []
    for inimigo in enemys_list:
        Enemy = inimigo[0]
        Enemy.rect.x = inimigo[1]
        Enemy.Muda_Rota = inimigo[3]
        Enemy.rect.y = inimigo[2] - Enemy.rect.height - Enemy.Muda_Rota
        level_list.append(levels.Level_01(player1,Enemy,boss1))
        enemy_l.append(Enemy)
    backup_enemy_l = enemy_l[:]
        
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
#==============================================================================
# Cria as listas de Sprites 
#==============================================================================
    player1_list = pg.sprite.Group()
    enemy_list = pg.sprite.Group()  
    boss_list = pg.sprite.Group()
#==============================================================================
# Define a Posiçao inicial    
#==============================================================================
    """Player"""
    player1.level = current_level
    player1.rect.x = -200
    player1.Muda_Rota = 20
    player1.rect.y = constants.SCREEN_HEIGHT - player1.rect.height - player1.Muda_Rota 
    player1_list.add(player1)
    """Boss"""
    boss1.level = current_level
    boss1.rect.x = constants.SCREEN_WIDTH+100
    boss1.rect.y = constants.SCREEN_HEIGHT - boss1.rect.height - player1.Muda_Rota 
    boss_list.add(boss1)
    backup_boss = boss_list.copy()
    """Enemy"""
    for Enemy in enemy_l:
        Enemy.level = current_level
        enemy_list.add(Enemy)
    backup_enemy = enemy_list.copy()
#==============================================================================
    # Used to manage how fast the screen updates
    clock = pg.time.Clock()
    Regen = pygame.USEREVENT + 1 
    Boss_Action = pygame.USEREVENT + 2
    Boss_Sub_Action = pygame.USEREVENT + 3
    pg.time.set_timer(Regen,50)
    pg.time.set_timer(Boss_Action,1000)
    pg.time.set_timer(Boss_Sub_Action,500)
    pg.time.set_timer(pygame.USEREVENT + 4,5000)
    levels.Start_Screen()
    
    levels.Music_play(0)
#==============================================================================
    """Main Loop"""
    while not constants.Game_loop:
#==============================================================================
        #==============================================================================
        """Joystck Configuration"""
        #==============================================================================
        # Recebe valor real entre (-1) e (1) para o analógico esquerdo no eixo horizontal, onde (0) é parado
        if pg.joystick.get_count() >0:
            axis_lh = joystick.get_axis(0)
            # Recebe valor real entre (-1) e (1) para o analógico esquerdo no eixo vertical, onde (0) é parado
            axis_lv = joystick.get_axis(1)
              
            # Recebe valor inteiro de (-1) e (1) para os botões direcionais, onde (0) é parado
            hat = joystick.get_hat(0)
        #==============================================================================
#==============================================================================
#      Comfiguraçoes teclado:       
#==============================================================================
        for event in pg.event.get():
            if event.type == pg.QUIT:
                constants.Game_loop = True 
                
            pressed = pg.key.get_pressed()
            if (pressed[pg.K_LALT] and pressed[pg.K_F4]) or (pressed[pg.K_RALT] and pressed[pg.K_F4]):
                pg.quit()
            pg.key.set_repeat(10,20)
            if pressed[pg.K_UP]: player1.Muda_Rota_Sup()
            if pressed[pg.K_DOWN]: player1.Muda_Rota_Inf()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    if player1.State('move') and not constants.game_start:
                        player1.go_left()
                if event.key == pg.K_RIGHT:
                    if player1.State('move') and not constants.game_start:
                        player1.go_right()
                if event.key == pg.K_z:
                    if player1.State('punch') and not constants.game_start:
                        player1.Soco_1()
                if event.key == pg.K_x:
                    if player1.State('kick') and not constants.game_start:
                        player1.Chute_1()
                if event.key == pg.K_c:
                    if player1.State('jump') and not constants.game_start:
                        player1.Jump()
                if event.key == pg.K_v:
                     if player1.State('defending') and not constants.game_start:
                        player1.Defesa()                    
                if event.key == pg.K_RETURN:
                    if not  player1.com and not constants.reset:
                        pygame.mixer.music.pause()
                        levels.Pause()
                    
            if event.type == pg.KEYUP:
                if event.key == pg.K_LEFT and player1.change_x < 0:
                    player1.stop()
                if event.key == pg.K_RIGHT and player1.change_x > 0:
                    player1.stop()
                if event.key == pg.K_v:
                   player1.stop()
                
            if event.type == Regen:
                player1.healt_regen()
                player1.Mp_regen()
#==============================================================================
            #Enemy:
#==============================================================================
            for Enemy in enemy_l:
                
                if event.type == pygame.USEREVENT + 4:
                    Enemy.ml = False
                    
                if event.type == Boss_Action:
                    Enemy.boss_action()
                    
                if event.type == Boss_Sub_Action:
                    Enemy.sub_action()
                    
                if not Enemy.live:
                    if constants.delay_dead > 85:
                        constants.delay_dead =  0
                        enemy_list.remove(Enemy)
                        enemy_l.remove(Enemy)
                    else:
                        constants.delay_dead += 1
#==============================================================================
#           Boss:
#==============================================================================
            if event.type == Boss_Action:
                boss1.boss_action()
                
            if event.type == Boss_Sub_Action:
                boss1.sub_action()
                
            if not boss1.live:
                if constants.delay_dead > 85:
                    constants.delay_dead =  0
                    boss_list.remove(boss1)
                else:
                    constants.delay_dead += 1
        
#==============================================================================
        #==============================================================================
            """Configuraçoes dos botoes do controle"""
        #==============================================================================
            if pg.joystick.get_count()>0:
                    # Direcional ou  Analógico esquerdo para a esquerda
                    if (hat == ((-1,0) or (-1,1) or (-1,-1))) or axis_lh <= -0.5:
                        if player1.State('move') and not constants.game_start:
                            player1.go_left()
                    # Direcional ou  Analógico esquerdo para a direita
                    if (hat == ((1,0) or (1,1) or (1,-1))) or axis_lh >= 0.5:
                        if player1.State('move') and not constants.game_start:
                            player1.go_right()
                            
                    if (hat == ((0,1) or (1,1) or (-1,1))) or axis_lv <= -0.5:
                        if player1.State('move') and not constants.game_start:
                            player1.Muda_Rota_Sup()
                    if (hat == ((0,-1) or (1,-1) or (-1,-1))) or axis_lv >= 0.5:
                        if player1.State('move') and not constants.game_start:
                            player1.Muda_Rota_Inf()
                     # Direcional ou  Analógico esquerdo parados   
                    if (hat == ((0,0) or (0,1) or (0,-1)) and (-0.5 < axis_lh < 0.5)) and (player1.change_x != 0):       
                        player1.stop()
                        
                    if event.type == pg.JOYBUTTONDOWN:
                        if event.button == 2: # Botão X pressionado
                            if player1.State('jump') and not constants.game_start:
                                player1.Jump()
                            
                        if event.button == 1: # Botão CIRCULO pressionado
                            if player1.State('kick') and not constants.game_start:
                                player1.Chute_1()
                        if event.button == 3: # Botão QUADRADO pressionado
                             if player1.State('punch') and not constants.game_start:
                                player1.Soco_1()
                                
                        if event.button == 5: # Botão R1 pressionado
                            if player1.State('defending') and not constants.game_start:
                                player1.Defesa()
                        
                        if event.button == 9:
                            if not  player1.com and not constants.reset  and not constants.game_start:
                                pygame.mixer.music.pause()
                                levels.Pause()
                            
                                
                    if event.type == pg.JOYBUTTONUP:
                            if event.button == 5:
                                player1.stop()
                    
                        # Botao R1
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
        """ Realiza af funçoes necessarias para relizar ad achoes no game"""
#==============================================================================
        
                     
        for Enemy in enemy_l:
            if not constants.game_start:
                collide.check_colide(player1,Enemy)        
                Enemy.ai(player1)
            
        
        if len(enemy_list)<10:
            collide.check_colide(player1,boss1)
            boss1.ai(player1)
            
        if constants.Pause:
            pygame.mixer.music.unpause()
            
        if constants.reset:
            levels.Music_play(0)
            constants.i = 0
            constants.d = 0
            constants.s = 0
            constants.teste = 0
            player1.rect.x +=1
            player1.com = False
            enemys_list = backup_enemys_list [:]
            enemy_l = backup_enemy_l[:]
            enemy_list.remove()
            enemy_list = backup_enemy.copy()
            boss_list.remove()
            boss_list = backup_boss.copy()
            for i,Enemy in enumerate(enemy_l):
                Enemy.Re_life(enemys_list[i][1],enemys_list[i][2],enemys_list[i][3])
            constants.reset = False

        player1_list.update()
        enemy_list.update()
        if len(enemy_list)<10:
            boss_list.update()
        current_level.update()
#==============================================================================
        """Define a posiçao da tela em relaçao ao cenario"""
        current_position = player1.rect.x + abs(current_level.world_shift)
        if current_position > 200 and  current_position < 2000 and current_level_no != 1:
            if player1.rect.right >= 800:
                diff = player1.rect.right - 800
                player1.rect.right = 800
                boss1.rect.left -= diff
                for Enemy in enemy_l:
                    Enemy.rect.right -= diff 
                current_level.shift_world(-diff)
  
            
            if player1.rect.left <= 200:
                diff = 200 - player1.rect.left
                player1.rect.left = 200
                boss1.rect.left += diff
                for Enemy in enemy_l:
                    Enemy.rect.left += diff
                current_level.shift_world(diff)
                
#==============================================================================
        """Desenha tudo o que aparece na tela"""
#==============================================================================
        current_level.draw(screen)                                             #Desenha a fase
        
        #Desenha os Inimigo
        enemy_list.draw(screen)                                               
        for Enemy in enemy_l:
            if Enemy.ml:
                Enemy.enemy_hud(screen)
                
        #Desenha o boss        
        if len(enemy_list)<10:
            boss_list.draw(screen)
            boss1.boss_hud(screen)
            if constants.i==0:
                pygame.mixer.music.stop()
                constants.i = 1
            if constants.d == 0:
                levels.Music_play(1)
                constants.d = 1
        #Desenha o Player        
        player1_list.draw(screen)                                              
        player1.player_hud(screen)
        if not player1.live and player1.Lives == 0:
            player.dead_screen(screen,player1,current_position)
            pygame.mixer.music.stop()
            
        if len(enemy_l) == 0 and not  boss_list.has(boss1):
            player.Stage_Clear(screen,player1)
            player1.stop()
            player1.Vitoria()
        if constants.game_clear:
            player.Game_Clear(screen,player1,current_position)
        if constants.game_start:
            player.Game_Start(screen,player1)
#==============================================================================     
        clock.tick(constants.FPS) 
        pg.display.flip()
 
 
    pg.quit()
 
if __name__ == "__main__":
    main()