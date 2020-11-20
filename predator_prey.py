import os
from PIL import Image
import random

image = Image.new("RGB", (50, 50))

directory = os.getcwd()

colors = ["green", "green", "green", "green", "green", "white", "red"]

for x in range(image.width):
    for y in range(image.height):
        color = random.choice(colors)
        if color == "green":
            image.putpixel((x,y), (0, 255, 0))
        elif color == "red":
            image.putpixel((x,y), (255, 0, 0))
        elif color == "white":
            image.putpixel((x,y), (255, 255, 255))
        
        if x == 0:
            image.putpixel((x,y), (125,125,125))
        elif x == image.width - 1:
            image.putpixel((x,y), (125,125,125))
        elif y == 0:
            image.putpixel((x,y), (125,125,125))
        elif y == image.height - 1:
            image.putpixel((x,y), (125,125,125))
        


### Rules:
    #        
    # If there are at least 2 predators (red) near a prey (green),
    # then it has a 25% chance of dying (change to white = empty)
    # due to being eating
    #
    # If there are not at least 3 prey next to a predator, then
    # there is a 20% chance of dying (change to white = empty)
    # due to starvation
    #
    # If there are at least 5 prey next to another prey, then it
    # has a 10% chance of dying (change to white = empty) due to
    # lack of food
    #
    # If there is an empty cell, than whichever species has a higher
    # count surrounding it will have a chance to repopulate it,
    # 70% for prey and 30% for predators (tie goes to predators)
    #
    
image.show()

count = 0
for _ in range(100):
    count += 1
    thirty_percent = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
    ten_percent = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    seventy_percent = [0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
    twenty_percent = [0, 0, 0, 0, 1]
    twenty_five_percent = [0, 0, 0, 1]
    
    for x in range(1, image.width - 1):
        for y in range(1, image.height - 1):
            group = [(x-1,y-1), (x-1,y), (x-1, y+1), (x,y-1), (x, y+1), (x+1,y-1), (x+1,y), (x+1, y+1)]
            
            pixel = image.getpixel((x,y))
            
            if pixel == (0,255,0):
                green = 0
                red = 0
                for space in group:
                    location = image.getpixel(space)
                    if location == (0,255,0):
                        green += 1
                    if location == (255,0,0):
                        red += 1
                if red >= 2:
                    chance = random.choice(twenty_five_percent)
                    if chance == 1:
                        image.putpixel((x,y), (255, 0, 0))
                        for space in group:
                            pred = image.getpixel(space)
                            if pred == (255,0,0):
                                image.putpixel(space, (255, 255, 255))
                                break
                elif green >= 5:
                    chance = random.choice(ten_percent)
                    if chance == 1:
                        image.putpixel((x,y), (255, 255, 255))
            
            elif pixel == (255, 0, 0):
                green = 0
                red = 0
                for space in group:
                    location = image.getpixel(space)
                    if location == (0,255,0):
                        green += 1
                    if location == (255,0,0):
                        red += 1
                if green < 3:
                    chance = random.choice(twenty_percent)
                    if chance == 1:
                        image.putpixel((x,y), (255, 255, 255))
            
            elif pixel == (255, 255, 255):
                green = 0
                red = 0
                for space in group:
                    location = image.getpixel(space)
                    if location == (0,255,0):
                        green += 1
                    if location == (255,0,0):
                        red += 1
                if red >= green:
                    chance = random.choice(thirty_percent)
                    if chance == 1:
                        image.putpixel((x,y), (255, 0, 0))
                else:
                    chance = random.choice(seventy_percent)
                    if chance == 1:
                        image.putpixel((x,y), (0, 255, 0))
                        
    if count == 1:
        image.show()
        
    elif count == 2:
        image.show()
        
    elif count == 5:
        image.show()
        
    elif count == 10:
        image.show()
        
    elif count == 20:
        image.show()
        
    elif count == 30:
        image.show()
        
    elif count == 40:
        image.show()
        
    elif count == 50:
        image.show()
        
                             
image.show()
           
                    
                
    




