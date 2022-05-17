import ast
import pygame
import ctypes

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
sx, sy = screensize
screen_middle = (sx / 2, sy / 2)

win = pygame.display.set_mode((screensize))
pygame.display.set_caption("Deep Dive")


class World():
    def __init__(self, data):
        self.tile_list = []

        # load images

        # Walls
        wall = pygame.image.load("GameData/img/coral/wall.png")
        wall_rt = pygame.image.load("GameData/img/coral/wall_rt.png")
        wall_lt = pygame.image.load("GameData/img/coral/wall_lt.png")
        wall_rb = pygame.image.load("GameData/img/coral/wall_rb.png")
        wall_lb = pygame.image.load("GameData/img/coral/wall_lb.png")


        # Items
        shell = pygame.image.load("GameData/img/items/shell.png")



        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:

                if tile == 0:
                    pass


                elif tile == 1:
                    img = pygame.transform.scale(wall, (50, 50)) # Coral Wall
                    img_rect = img.get_rect()
                    img_rect.x = col_count * 50
                    img_rect.y = row_count * 50
                    self.tile_list.append((img, img_rect, 0))

                elif tile == 2:
                    img = pygame.transform.scale(wall_rt, (50, 50)) # Coral Wall
                    img_rect = img.get_rect()
                    img_rect.x = col_count * 50
                    img_rect.y = row_count * 50
                    self.tile_list.append((img, img_rect, 0))

                elif tile == 3:
                    img = pygame.transform.scale(wall_lt, (50, 50)) # Coral Wall
                    img_rect = img.get_rect()
                    img_rect.x = col_count * 50
                    img_rect.y = row_count * 50
                    self.tile_list.append((img, img_rect, 0))

                elif tile == 4:
                    img = pygame.transform.scale(wall_rb, (50, 50)) # Coral Wall
                    img_rect = img.get_rect()
                    img_rect.x = col_count * 50
                    img_rect.y = row_count * 50
                    self.tile_list.append((img, img_rect, 0))

                elif tile == 5:
                    img = pygame.transform.scale(wall_lb, (50, 50)) # Coral Wall
                    img_rect = img.get_rect()
                    img_rect.x = col_count * 50
                    img_rect.y = row_count * 50
                    self.tile_list.append((img, img_rect, 0))


                # Collectables Always Start with 1 something aka 1 3 or 13

                elif tile == 10:
                    img = pygame.transform.scale(shell, (30, 30)) # Coral Wall
                    img_rect = img.get_rect()
                    img_rect.x = (col_count * 50) + 10
                    img_rect.y = (row_count * 50) + 10
                    self.tile_list.append((img, img_rect, 1))



                col_count += 1
            row_count += 1

    def RemoveTile(self, index):
        self.tile_list.pop(index)

    def draw(self):
        for tile in self.tile_list:
            win.blit(tile[0], tile[1])

class Player():
    def __init__(self):
        # Images
        self.player = [pygame.image.load("GameData/img/player/test.png"), pygame.image.load("GameData/img/player/test.png").get_rect()]

        # Starting Possition
        self.x = 100
        self.y = 100

        # Velocity
        self.vel_x = 0
        self.vel_y = 0

        # Player Score
        self.collected = 0


    def Update(self):
        # Event Handling
        events = pygame.event.get()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.vel_x += 1
        elif keys[pygame.K_a]:
            self.vel_x += -1

        if keys[pygame.K_w]:
            self.vel_y += -1
        elif keys[pygame.K_s]:
            self.vel_y += 1

        # Movement
        T_y = 0.5
        T_x = 0


        friction = 0.5
        if self.vel_x > 0:
            self.vel_x += (friction * -1)
        elif self.vel_x < 0:
            self.vel_x += friction

        if self.vel_y > 0:
            self.vel_y += (friction * -1)
        elif self.vel_y < 0:
            self.vel_y += friction

        # Cap Velocity
        if self.vel_x > 6:
            self.vel_x = 6
        elif self.vel_x < -6:
            self.vel_x = -6

        if self.vel_y > 6:
            self.vel_y = 6
        elif self.vel_y < -6:
            self.vel_y = -6

        T_y += self.vel_y
        T_x += self.vel_x

        # Check For Collisions
        tile_number = 0
        for tile in world.tile_list:
            collected = False
            if tile[1].colliderect(self.x, self.y + T_y, 50, 100):  # 50 by 100 is the player size
                if tile[2] == 0:
                    T_y = 0
                    self.vel_y = 0
                elif tile[2] == 1:
                    world.RemoveTile(tile_number)
                    collected = True

            if tile[1].colliderect(self.x + T_x, self.y, 50, 100):
                if tile[2] == 0:
                    T_x = 0
                    self.vel_x = 0
                elif tile[2] == 1:
                    world.RemoveTile(tile_number)
                    collected = True

            if collected:
                self.collected += 1
            tile_number += 1

        self.y += T_y
        self.x += T_x

    def Draw(self):
        win.blit(self.player[0], self.player[1].move(self.x, self.y))


f = open("GameData/level/data.txt")
world_data = f.read()
f.close()

world = World(ast.literal_eval(world_data))
player = Player()

background = pygame.image.load("GameData/img/background.png")

# Pygame Clock and Stuff
clock = pygame.time.Clock()
pygame.mouse.set_visible(True)
# Game Loop
Pressing = False
GameLoop = True

# Make It land When Game First Starts
stage = "water"

while GameLoop:
    Clicking = False



    if stage == "water":
        win.blit(background, (0,0))
        world.draw()
        player.Update()
        player.Draw()

    pygame.display.update()
    clock.tick(30) # 30 is the fps

pygame.quit()