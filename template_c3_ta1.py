import pygame

pygame.init()
clock=pygame.time.Clock()
screen = pygame.display.set_mode((400,600))

pygame.display.set_caption("Shooting Spaceship")
background_image = pygame.image.load("bg2.jpg").convert()

# Load the image for the player and name it as 'player_image'


#The next line is commented as it is not required any more
#BLUE=(0,0,255)
player=pygame.Rect(200,200,30,30)

WHITE=(255,255,255)
enemy=pygame.Rect(100,100,30,30)
xvel=2
yvel=3

# Create the variables 'angle' and 'change'
# Assign the value '0' to them


while True:
  screen.blit(background_image,[0,0])
  
  # Events handling
  for event in pygame.event.get():
    # Event handling for closing the window
    if event.type == pygame.QUIT:
      pygame.quit()
    
    # Event handling if any key is pressed
    
          
    # Event handling if any key is released
    
  
  enemy.x=enemy.x + xvel
  enemy.y=enemy.y + yvel 
  
  if enemy.x < -250 or enemy.x > 650 :
    xvel = -1*xvel
  
  if enemy.y < -250 or enemy.y > 850:  
    yvel = -1*yvel
    
  # Update the new 'angle' value by incrementing it with 'change'
  
  
  # Rotating the 'player_image' to the 'angle' value
 
 
  # Displaying the new rotated image for the player
 
 
  
  #The next line is commented as it is not required any more
  #pygame.draw.rect(screen,BLUE,player)
  pygame.draw.rect(screen,WHITE,enemy)

  pygame.display.update()
  clock.tick(30)
  
  
