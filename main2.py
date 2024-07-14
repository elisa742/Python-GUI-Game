from graphics import *
from enemy3 import *
from projectile import *
from player1 import *
import time
import random

window = GraphWin("Final", 400, 400)

keys = {"w": False, "a": False, "s": False, "d": False, "q": False, " ": False}
#Background Picture Setting
myimage=Image(Point(200,200),"game.gif")
myimage.draw(window)

start_time = time.time()
last_time = start_time
quit = False
frames = 0
enemies = []
enemy_spawn_rate = 2
enemy_spawn_timer = 2
player = Player(window, 30, window.getHeight()/2)
projectiles=[]
count=0
count1=0
healths=[]
#Create 3 health: color in green, on top right of the screen
class Health:
	def __init__(self,i,window):
		self.health=Circle(Point(250+i*40,30),15)
		self.health.setFill(color_rgb(40,190,160))
		self.health.draw(window)
	            
for i in range (0,3):
	health_player=Health(i,window)
	healths.append(health_player)
#Score setting : color in red, on the top left of the screen
class Score:
    def __init__(self,win):
        self.mytext=Text(Point(80,20),"score ")
        self.mytext.setSize(20)
        self.mytext.setTextColor(color_rgb(178,34,34))
        self.mytext.draw(win)
    def update(self,score,win):
        self.mytext.setText(score)
        self.mytext.getText()
        self.mytext.draw(win)
score=Score(window)

def keypress_callback(event):
    if event.char in "wasdq ":
        keys[event.char] = True


def keyrelease_callback(event):
    if event.char in "wasdq ":
        keys[event.char] = False

window.bind_all("<Key>", keypress_callback)
window.bind_all("<KeyRelease>", keyrelease_callback)

while not quit:
    current_time = time.time()
    delta_time = current_time - last_time

    # Update the player based on input
    player.update(keys, delta_time)

    enemy_spawn_timer -= delta_time
    # Make a new enemy at a random y location if enemy_spawn_rate seconds has passed
    if enemy_spawn_timer < 0:
        #normal enemy:color in purple
        enemy = Enemy(window, window.getWidth(), random.randint(0, window.getHeight()))
        enemies.append(enemy)
        #chasing-player enemy: color in blue
        enemy_chase=Chase(window,window.getWidth(), random.randint(0, window.getHeight()))
        enemies.append(enemy_chase)
        #SIN wave enemy: color in yellow
        enemy_wave=Third_enemy(window,window.getWidth(), random.randint(0, window.getHeight()))
        enemies.append(enemy_wave)
        # Reset the enemy spawn timer
        enemy_spawn_timer = enemy_spawn_rate
    for enemy in enemies:
        x=player.circle.getCenter().getX()
        y=player.circle.getCenter().getY()
        enemy.update(x,y,delta_time)
        # Remove the enemy from the screen and the list of enemies if it gets to the screen's far left
        if enemy.circle.getCenter().getX() < 0:
            enemy.circle.undraw()
            enemies.remove(enemy)
    #Projectile        
    if keys[" "]:
        x=player.circle.getCenter().getX()
        y=player.circle.getCenter().getY()
        projectile_player=Projectile(window,x,y)
        projectiles.append(projectile_player)
    for projectile_player in projectiles:
        projectile_player.update(delta_time)
        if projectile_player.circle.getCenter().getX()>400:
            projectiles.remove(projectile_player)
            projectile_player.circle.undraw()
    #Score Mechanism: killing 1 enemy, get 1 point
    for projectile_player in projectiles:            
        for enemy in enemies:
            if projectile_player.circle_collision(enemy.circle):
                score.mytext.undraw()
                enemies.remove(enemy)
                enemy.circle.undraw()
                projectiles.remove(projectile_player)
                projectile_player.circle.undraw()
                count1+=1
                score.update("score "+str(count1),window)
                
    #Enemies collide with each other            
    for enemy in enemies:
        for z in enemies:
            if enemy is not z:
                if enemy.circle_collision(z.circle):
                    enemies.remove(enemy)
                    enemy.circle.undraw()
                    enemies.remove(z)
                    z.circle.undraw()
    #Health Update
    for enemy in enemies:
    	if player.circle_collision(enemy.circle) and count<3:
    		healths[count].health.undraw()
    		enemy.circle.undraw()
    		enemies.remove(enemy)
    		count+=1
    		
    	if player.circle_collision(enemy.circle) and count>=3:
    		quit=True
    		player.collision_with_enemy()
    		game_over_text=Text(Point(window.getWidth()/2.0, window.getHeight()/2.0), "Game Over!\nClick to exit.")
    		game_over_text.draw(window)

    if keys["q"]:
        quit = True

    last_time=current_time
    frames+=1


window.getMouse()
window.close()
exit()             


           
	