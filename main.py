import ast
import pygame
import ctypes

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
sx, sy = screensize
screen_middle = (sx / 2, sy / 2)

win = pygame.display.set_mode((screensize))
pygame.display.set_caption("Thawing")


class World():
    def __init__(self, data):
        self.tile_list = []

        # load images

        # Grass
        grass = pygame.image.load("GameData/img/grass.png")

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:

                if tile == 0:
                    pass


                elif tile == 1:
                    img = pygame.transform.scale(grass, (50, 50))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * 50
                    img_rect.y = row_count * 50
                    tile = (img, img_rect)
                    self.tile_list.append(tile)



                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            win.blit(tile[0], tile[1])





class Player():
    def __init__(self):
        # Vars
        self.vel_y = 0
        self.vel_x = 0

        # Settings

        self.x = 100
        self.y = 800

        # Images
        leg = pygame.image.load("GameData/img/Player/leg.png")
        leg45 = pygame.image.load("GameData/img/Player/leg_45.png")
        body = pygame.image.load("GameData/img/Player/body.png")

        # Rotate
        leg135 = pygame.transform.flip(leg45, True, False)



        # Set Images
        self.left_leg = [[leg, leg.get_rect()], [leg45, leg45.get_rect()]]
        self.right_leg = [[leg, leg.get_rect()], [leg135, leg135.get_rect()]]

        self.body = [body, body.get_rect()]

        # Player Hit Box / Player Data
        self.CanUse = ["leg1"] # leg2, arms1, arms2




    def Update(self):
        # Gravity
        T_y = 0
        T_x = 0

        downforce = 0.1
        self.vel_y += downforce
        if self.vel_y > 8:
            self.vel_y = 8

        T_y += self.vel_y

        # Check For Collisions
        for tile in world.tile_list:
            if tile[1].colliderect(self.x, self.y + 75.5 + T_y, 10, 10):
                T_y = 0




        self.y += T_y




    def Display(self):
        win.blit(self.left_leg[1][0], self.left_leg[1][1].move(self.x + 20, self.y + 45))
        win.blit(self.right_leg[1][0], self.right_leg[1][1].move(self.x + 1, self.y + 45))

        win.blit(self.right_leg[0][0], self.right_leg[0][1].move(self.x + 1, self.y + 65))
        win.blit(self.left_leg[0][0], self.left_leg[0][1].move(self.x + 28, self.y + 65))


        win.blit(self.body[0], self.body[1].move(self.x, self.y))


f = open("GameData/levels/0.txt")
world_data = f.read()
f.close()

world = World(ast.literal_eval(world_data))
player = Player()

background = pygame.image.load("GameData/img/background.png")

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break


    win.blit(background, (0,0))
    world.draw()
    player.Update()
    player.Display()
    pygame.display.flip()

pygame.quit()