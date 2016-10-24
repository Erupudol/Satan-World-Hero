import Sounds,constants

def check_colide(player,enemy):
    """checa a colisão de movimento entre o player e o inimigo"""

    if enemy.live and not constants.game_start and(player.State('move') or enemy.State('move')):
        
        if player.rect.bottom < enemy.rect.bottom and player.rect.bottom > enemy.rect.top:
            if player.rect.left < enemy.rect.left and player.rect.right > enemy.rect.left:
                player.rect.right = enemy.rect.left
            if player.rect.right > enemy.rect.right and player.rect.left < enemy.rect.right:
                player.rect.left = enemy.rect.right
        if player.rect.top > enemy.rect.top and player.rect.top < enemy.rect.bottom:
            if player.rect.left < enemy.rect.left and player.rect.right > enemy.rect.left:
                player.rect.right = enemy.rect.left
            if player.rect.right > enemy.rect.right and player.rect.left < enemy.rect.right:
                player.rect.left = enemy.rect.right
        if player.rect.top <= enemy.rect.top and player.rect.bottom >= enemy.rect.bottom:
            if player.rect.left < enemy.rect.left and player.rect.right > enemy.rect.left:
                player.rect.right = enemy.rect.left
            if player.rect.right > enemy.rect.right and player.rect.left < enemy.rect.right:
                player.rect.left = enemy.rect.right
    if player.punch and not constants.game_start and enemy.live:
        if hit(player,enemy):
            enemy.Recive_Dmg(player)
            if not enemy.live:
                Sounds.Hit_kill.play()
            else:
                Sounds.HitP.play()
    if player.kick and not constants.game_start and enemy.live:
        if hit(player,enemy):
            enemy.Recive_Dmg(player)
            if not enemy.live:
                Sounds.Hit_kill.play()
            else:
                Sounds.HitK.play()
        
    if enemy.punch and player.live:
        if hit(enemy,player):
            player.Recive_Dmg(enemy)
            if not player.live:
                Sounds.Hit_kill.play() 
            else:
                Sounds.HitP.play()
    if enemy.kick and player.live:
        if hit(enemy,player):
            player.Recive_Dmg(enemy)
            if not player.live:
                Sounds.Hit_kill.play() 
            else:
                Sounds.HitK.play()
    
def hit_box(Hit1, Hit2):
    hitbox = Hit1.rect.inflate(20,0)
    return hitbox.colliderect(Hit2.rect)
            
def hit(Hit1,Hit2):
    if hit_box(Hit1,Hit2):
        if Hit1.direction == 'R' and Hit1.rect.centerx < Hit2.rect.centerx:
            if Hit1.dealdmg == True:
                Hit2.dmg = True
                return True
        elif Hit1.direction == 'L' and Hit1.rect.centerx > Hit2.rect.centerx:
            if Hit1.dealdmg == True:
                Hit2.dmg = True
                return True
            
               