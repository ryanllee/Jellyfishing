# I got the idea and help learning pygame from here
# http://programarcadegames.com/index.php?lang=en

import pygame
import random
import time
black =0,0,0
white =255,255,255
blue=0,0,255
red=255,0,0
green=50,205,50
#JellyNet class, inherits from Sprite
class JellyNet(pygame.sprite.Sprite):
    change_x=0
    change_y=0
    # Constructor takes in self and name of file image
    def __init__(self, filename):
        # Calls parent Sprite constructor
        pygame.sprite.Sprite.__init__(self)
	# Loads image of jellyfish
        # if pygame.image.get_extended():
        self.image = pygame.image.load(filename).convert()
	# Gets rid of the black background around the net picture
        self.image.set_colorkey(black)
        self.rect=self.image.get_rect()
    # Changes the speed of the player
    def changespeed(self,x,y):
        self.change_x+=x
        self.change_y+=y
    # Finds a new position for the player
    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
# JellyFish class for making the jellyfish
class JellyFish(pygame.sprite.Sprite):
    # Constructor for jellyfish sprites
    def __init__(self, filename):
        # Calls parent Sprte constructor
        pygame.sprite.Sprite.__init__(self)
	# Loads net image
        # if pygame.image.get_extended():
        self.image = pygame.image.load(filename).convert()
	# Gets rid of white background around the jellyfish
        self.image.set_colorkey(white)
        self.rect=self.image.get_rect()
# Initializes Pygame
pygame.init()
# Sets height and width of screen
screen_width=900
screen_height=500
screen=pygame.display.set_mode([screen_width,screen_height])
# Sets name on top of the bar thing
pygame.display.set_caption("Jellyfish Game")
# Makes list of jellyfish from Group class (makes it easier to manage them)
jellyfish_list = pygame.sprite.Group()
# Makes list of all sprites from Group class
all_sprites_list = pygame.sprite.Group()
# Creates player's net
player = JellyNet("Jellyfish.png")
all_sprites_list.add(player)
# Makes it loop until the user clicks the close button.
done=False
clock=pygame.time.Clock()
timer = pygame.font.Font(None, 30)
# For the timer clock thing, not the Clock() thing but an actual timer
frame_count = 0
frame_rate = 50
start_time = 30
# Manages how fast the screen updates
clock=pygame.time.Clock()
# Collects score
score = 0
# Hides mouse
# pygame.mouse.set_visible(0)
# Will be used to diplay "Game Over"
font=pygame.font.Font(None, 200)
# Checks if game is over
# For all the fonts I display
instruction_font=pygame.font.Font(None, 60)
title_font=pygame.font.Font(None, 130)
other_instructions=pygame.font.Font(None, 60)
score_font=pygame.font.Font(None, 30)
or_font=pygame.font.Font(None, 80)
game_over=False
level=1
display_instructions=True
instruction_page=1
# For background use
# if pygame.image.get_extended():
background=pygame.image.load("water.png").convert()
# I'm going to use these later to make the jellyfish move faster as the level increases
range_for_jelly=-2
check_level_raise=0
empty=0
# Loop to print instructions
while done==False and display_instructions:
    for event in pygame.event.get(): # General loop for the instructions page
        if event.type == pygame.QUIT:
            done=True
        if event.type == pygame.MOUSEBUTTONDOWN:
            instruction_page += 1
            if instruction_page == 3:
                display_instructions = False
        # Gives player an endless option to the game so it lasts forever
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                start_time=9999999
            if event.key == pygame.K_RIGHT:
                start_time=9999999
            if event.key == pygame.K_UP:
                start_time=9999999
            if event.key == pygame.K_DOWN:
                start_time=9999999
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                start_time=9999999
            if event.key == pygame.K_RIGHT:
                start_time=9999999
            if event.key == pygame.K_UP:
                start_time=9999999
            if event.key == pygame.K_DOWN:
                start_time=9999999

    screen.fill(green)
    # Prints out the starter screen and instruction screen
    if instruction_page == 1:
        text=title_font.render("Jellyfishing", True, blue)
        text_rect = text.get_rect()
        text_x = screen.get_width()/2 - text_rect.width/2
        text_y = screen.get_height()/2 - text_rect.height/2
        screen.blit(text, [text_x, text_y-70])
        text=instruction_font.render("1. Click on the screen to begin normal", True, red)
        text_rect = text.get_rect()
        text_x = screen.get_width()/2 - text_rect.width/2
        text_y = screen.get_height()/2 - text_rect.height/2
        screen.blit(text, [text_x, text_y+10])
        text=instruction_font.render("2. Press on arrow key to play endless", True, red)
        text_rect = text.get_rect()
        text_x = screen.get_width()/2 - text_rect.width/2
        text_y = screen.get_height()/2 - text_rect.height/2
        screen.blit(text, [text_x, text_y+125])
        text=instruction_font.render("then click on screen", True, red)
        text_rect = text.get_rect()
        text_x = screen.get_width()/2 - text_rect.width/2
        text_y = screen.get_height()/2 - text_rect.height/2
        screen.blit(text, [text_x, text_y+165])
        text=or_font.render("OR", True, black)
        text_rect = text.get_rect()
        text_x = screen.get_width()/2 - text_rect.width/2
        text_y = screen.get_height()/2 - text_rect.height/2
        screen.blit(text, [text_x, text_y+70])
    if instruction_page%2==0:
        text=other_instructions.render("Collect all the jellyfish in 30 seconds", True, black)
        text_rect = text.get_rect()
        text_x = screen.get_width()/2 - text_rect.width/2
        text_y = screen.get_height()/2 - text_rect.height/2
        screen.blit(text, [text_x, text_y])
    clock.tick(20)
    pygame.display.flip()

# Main loop
while done==False:
    for event in pygame.event.get(): # General loop to run the program and runs until someone presses the exit button
        if event.type == pygame.QUIT:
            done=True
        # Person pressed down on a key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed=-6
            if event.key == pygame.K_RIGHT:
                x_speed=6
            if event.key == pygame.K_UP:
                y_speed=-6
            if event.key == pygame.K_DOWN:
                y_speed=6
        # Person lets up on a key
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_speed=0
            if event.key == pygame.K_RIGHT:
                x_speed=0
            if event.key == pygame.K_UP:
                y_speed=0
            if event.key == pygame.K_DOWN:
                y_speed=0

    # Changes position of net using keyboard
    # Set the speed based on the key pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3,0)
            if event.key == pygame.K_RIGHT:
                player.changespeed(3,0)
            if event.key == pygame.K_UP:
                player.changespeed(0,-3)
            if event.key == pygame.K_DOWN:
                player.changespeed(0,3)
        # Reset speed when key goes up
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3,0)
            if event.key == pygame.K_RIGHT:
                player.changespeed(-3,0)
            if event.key == pygame.K_UP:
                player.changespeed(0,3)
            if event.key == pygame.K_DOWN:
                player.changespeed(0,-3)
    # Moves the player block based on the current speed
    player.update()

    # Puts up background image
    screen.blit(background, [0,0])

    # Checks if net went off screen
    if player.rect.x>screen_width:
        player.rect.x=screen_width-20
    elif player.rect.y>screen_height:
        player.rect.y=screen_height-10
    elif player.rect.x<0:
        player.rect.x=0
    elif player.rect.y<0:
        player.rect.y=0
    # Sees if player hit anything
    for jellyfish in jellyfish_list:
        jellyfish.rect.x+=random.randrange(range_for_jelly)
        if jellyfish.rect.x>screen_width:
            jellyfish.rect.x=screen_width-20
        jellyfish.rect.x-=random.randrange(range_for_jelly)
        if jellyfish.rect.x<0:
            jellyfish.rect.x=0
        jellyfish.rect.y-=random.randrange(range_for_jelly)
        if jellyfish.rect.y>screen_height:
            jellyfish.rect.y=screen_height-15
        jellyfish.rect.y+=random.randrange(range_for_jelly)
        if jellyfish.rect.y<0:
            jellyfish.rect.y=0
    jellyfish_hit_list = pygame.sprite.spritecollide(player, jellyfish_list, True)
    # Checks the list of collisions
    for jellyfish in jellyfish_hit_list:
        score +=1
        print(score)
    if len(jellyfish_list)==0:
        level+=1
        for i in range(level * 10):
            # This represents a block
            jellyfish = JellyFish("jelly.png")
            # Set a random location for the block
            jellyfish.rect.x = random.randrange(screen_width)
            jellyfish.rect.y = random.randrange(screen_height)
            # Add the block to the list of objects
            jellyfish_list.add(jellyfish)
            all_sprites_list.add(jellyfish)
            check_level_raise+=1
            frame_count=0
    # The jellyfish move faster as the level increases
    if check_level_raise>empty:
        empty=check_level_raise
        range_for_jelly+=5
	# Adds 2 seconds to time each level
        start_time+=2
    # Draw all the sprites
    all_sprites_list.draw(screen)
    # The double backslash gives an int value unlike the single backslash
    total_seconds = frame_count // frame_rate
    # Divides by 60 to get total minutes
    minutes = total_seconds // 60
    # Uses mod to get seconds
    seconds = total_seconds % 60
    # Use python string formatting to format in leading zeros
    # I dont know what the next part does, it doesnt make sense to me
    output_string = "Time: {0:02}:{1:02}".format(minutes,seconds)
    # Makes the text
    text = timer.render(output_string,True,black)
    # Puts text on screen below "Time left"
    screen.blit(text, [0,30])
    # Calculates total seconds
    text=score_font.render("Score: "+str(score), True, black)
    screen.blit(text, [0, 60])
    total_seconds = start_time - (frame_count // frame_rate)
    if total_seconds < 0:
        total_seconds = 0
    # Gets total minutes
    minutes = total_seconds // 60
    # Gets seconds
    seconds = total_seconds % 60
    # Use python string formatting to format in leading zeros
    output_string = "Time left: {0:02}:{1:02}".format(minutes,seconds)
    # Makes the text
    text = timer.render(output_string,True,black)
    # Puts text on screen starting at 0,0
    screen.blit(text, [0,0])
    frame_count +=1
#5000=100 seconds
#2500=50 seconds
#1500=30 seconds frame_count if start_time=15:00
#500=10 seconds
#250=5 seconds
    if frame_count>start_time*50:#1500+(level*250):
        game_over=True
    if game_over:
        # If game over is true, puts game over on the screen
        screen.fill(black)
        text=font.render("Game Over", True, white)
        text_rect = text.get_rect()
        # Centers the text to the middle
        text_x = screen.get_width()/2 - text_rect.width/2
        text_y = screen.get_height()/2 - text_rect.height/2
        screen.blit(text, [text_x, text_y])
    # 50 frames per second
    clock.tick(frame_rate)
    # Updates screen, puts the picture on there
    pygame.display.flip()
#Lets player quit game easily or safely
pygame.quit()
