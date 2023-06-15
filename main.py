import pygame
from pygame import surface

import button
from sys import exit


def Chara_name(name):
    n_font = pygame.font.Font(None, 50)
    n_surface = n_font.render(name, True, ("White"))
    screen.blit(n_surface, (255, 520))

def Speech(text, name, f_size, x, y):
    s_font = pygame.font.Font(None, f_size)
    s_surface = s_font.render(text, True, ("Black"))
    screen.blit(speech_bubble, speech_rect)
    screen.blit(s_surface, (x, y))
    Chara_name(name)


def Chara_blit(img, x, y):
    img_rect = img.get_rect(center=(x, y))
    screen.blit(img, img_rect)


def scene0():

    into_font = pygame.font.Font(None, 130)
    intro_surf = into_font.render('Welcome to the group!', False, 'Black').convert()
    intro_rect = intro_surf.get_rect(center=(600, 300))
    txt_font = pygame.font.Font(None, 90)
    text_surf = txt_font.render('Press Space to Start', False, "Black").convert()
    text_rect = text_surf.get_rect(center=(600,420))

    screen.blit(intro_surf, intro_rect)
    screen.blit(text_surf, text_rect)

    for event in pygame.event.get():

        if exit_button.draw(screen):
            run = exit()


    pygame.display.update()

def scene1():
    global current_scene
    screen.fill("White")
    screen.blit(class_img, (0,0))
    Chara_blit(miho_img, 600, 550)
    Speech("Hello! my name is Miho!", "Miho", 50, 250, 640)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            current_scene = scene2()

    pygame.display.update()


def scene2():
    global current_scene
    screen.fill("White")
    screen.blit(class_img, (0,0))
    Chara_blit(mihos_img, 600, 550)
    Speech('Ms. Lee put you with me and my friends for the final project!', "Miho", 37, 220, 640)

    pygame.display.update()

def scene3():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(class_img, (0,0))
    Chara_blit(mihos_img, 600, 550)
    Speech('You and my other 2 friends to be exact!', "Miho", 40, 220, 640)

    pygame.display.update()

def scene4():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(class_img, (0,0))
    Chara_blit(mihos_img, 600, 550)
    Speech("Well! Let's try to get to know each other", "Miho", 40, 220, 640)

    pygame.display.update()

def scene5():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(class_img, (0,0))
    Chara_blit(mihos_img, 600, 550)
    Speech("My name is Miho, we're probably the same age...", "Miho", 40, 220, 640)

    pygame.display.update()

def scene6():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(class_img, (0,0))
    Chara_blit(miho_img, 600, 550)
    Speech("My favorite food is pudding!!", "Miho", 40, 220, 640)

    pygame.display.update()

def scene7():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(class_img, (0,0))
    Chara_blit(miho_b_img, 600, 550)
    Speech("Well I guess you didn't have to know that for the project", "Miho", 40, 220, 640)

    pygame.display.update()

def scene8():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(class_img, (0,0))
    Chara_blit(miho_img, 600, 550)
    Speech("Let me introduce you to the other members!!", "Miho", 40, 220, 640)

    pygame.display.update()

def scene9():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(class_img, (0,0))
    Chara_blit(miho_img, 300, 550)
    Chara_blit(kanas_img, 900, 550)
    Speech("This is Kana", "Miho", 40, 220, 640)

    pygame.display.update()

def scene10():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(class_img, (0,0))
    Chara_blit(mihos_img, 300, 550)
    Chara_blit(kanas_img, 900, 550)
    Speech("We've been friends since elementary!!", "Miho", 40, 220, 640)

    pygame.display.update()

def scene11():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(class_img, (0,0))
    Chara_blit(mihos_img, 300, 550)
    Chara_blit(kanas_img, 900, 550)
    Speech("Shes the student council president!", "Miho", 40, 220, 640)

    pygame.display.update()

def scene12():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(class_img, (0,0))
    Chara_blit(miho_img, 300, 550)
    Chara_blit(kanas_b_img, 900, 550)
    Speech("Yup!! Shes that genius typa gurl!", "Miho", 40, 220, 640)

    pygame.display.update()

def scene13():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(class_img, (0,0))
    Chara_blit(mihos_img, 300, 550)
    Chara_blit(kanas_b_img, 900, 550)
    Speech("I've spent my life being jealous of her brain!", "Miho", 40, 220, 640)

    pygame.display.update()

def scene14():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(class_img, (0,0))
    Chara_blit(mihos_img, 300, 550)
    Chara_blit(kana_b_img, 900, 550)
    Speech("Don't Listen to her!", "Kana", 40, 220, 640)

    pygame.display.update()

def scene15():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(class_img, (0,0))
    Chara_blit(mihos_img, 300, 550)
    Chara_blit(kanas_b_img, 900, 550)
    Speech("She is so exaggerating.", "Kana", 40, 220, 640)

    pygame.display.update()

def scene16():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(class_img, (0,0))
    Chara_blit(mihos_img, 300, 550)
    Chara_blit(seikos_img, 900, 550)
    Speech("This here is Seiko", "Miho", 40, 220, 640)

    pygame.display.update()

def scene17():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(class_img, (0,0))
    Chara_blit(miho_img, 300, 550)
    Chara_blit(seikos_img, 900, 550)
    Speech("She just transfered here last year", "Miho", 40, 220, 640)

    pygame.display.update()

def scene18():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(class_img, (0,0))
    Chara_blit(mihos_img, 300, 550)
    Chara_blit(seikos_img, 900, 550)
    Speech("But we became instantly attached", "Miho", 40, 220, 640)

    pygame.display.update()

def scene19():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(class_img, (0,0))
    Chara_blit(mihos_img, 300, 550)
    Chara_blit(seikos_img, 900, 550)
    Speech("Now school feels imcomplete without her presence!", "Miho", 40, 220, 640)

    pygame.display.update()

def scene20():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(class_img, (0,0))
    Chara_blit(mihos_img, 300, 550)
    Chara_blit(seikos_img, 900, 550)
    Speech("Shes the typical kinda girl type that loves animals!", "Miho", 40, 220, 640)

    pygame.display.update()

def scene21():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(class_img, (0,0))
    Chara_blit(mihos_img, 300, 550)
    Chara_blit(seikos_img, 900, 550)
    Speech("Nice to meet you, looking forward to working with you!", "Seiko", 40, 220, 640)

    pygame.display.update()

def scene22():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(class_img, (0,0))
    Chara_blit(miho_img, 600, 550)
    Speech("Well these are my friends", "Miho", 40, 220, 640)

    pygame.display.update()

def scene23():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(class_img, (0,0))
    Chara_blit(miho_img, 600, 550)
    Speech("Hope you find yourself able to get along with us!!", "Miho", 40, 220, 640)

    pygame.display.update()

def scene24():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(class_img, (0,0))
    Chara_blit(mihos_img, 600, 550)
    Speech("Let's meet up next Friday for our project", "Miho", 40, 220, 640)

    pygame.display.update()

def scene25():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(class_img, (0,0))
    Chara_blit(miho_img, 600, 550)
    Speech("Until next time then, byebye!", "Miho", 40, 220, 640)

    pygame.display.update()


#General
pygame.init()
clock = pygame.time.Clock()
#game_scene = GameScene()
nbase_font = pygame.font.Font(None, 50)
lbase_font = pygame.font.Font(None, 40)

#Screen
s_width = 1200
s_height = 800
screen = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption("Freya's Game Trial")
screen.fill("Pink")
pygame.display.flip()

# start and exit button
start_btn = pygame.image.load('Graphics/Basics/start.png').convert_alpha()
exit_btn = pygame.image.load('Graphics/Basics/exit.png').convert_alpha()
start_button = button.Button(225, 400, start_btn, 0.6)
exit_button = button.Button(800, 483, exit_btn, 0.7)

# Miho
miho_im = pygame.image.load('Graphics/Miho_base/Miho_SummerUni_Open.png').convert_alpha()
miho_img = pygame.transform.scale(miho_im, (380, 950))

mihos_im = pygame.image.load('Graphics/Miho_base/Miho_SummerUni_Smile.png').convert_alpha()
mihos_img = pygame.transform.scale(mihos_im, (380, 950))

miho_b_im = pygame.image.load('Graphics/Miho_base/Miho_SummerUni_Open_Blush.png').convert_alpha()
miho_b_img = pygame.transform.scale(miho_b_im, (380, 950))

# Kana
kana_im = pygame.image.load("Graphics/Kana_base/Kana_Wintersei_Open.png")
kana_img = pygame.transform.scale(kana_im, (420, 950))

kanas_im = pygame.image.load("Graphics/Kana_base/Kana_Wintersei_Smile.png")
kanas_img = pygame.transform.scale(kanas_im, (420, 950))

kanas_b_im = pygame.image.load("Graphics/Kana_base/Kana_Wintersei_Smile_Blush.png")
kanas_b_img = pygame.transform.scale(kanas_b_im, (420, 950))

kana_b_im = pygame.image.load("Graphics/Kana_base/Kana_Wintersei_Open_Blush.png")
kana_b_img = pygame.transform.scale(kana_b_im, (420, 950))

#Seiko
seiko_im = pygame.image.load("Graphics/Seiko_base/Seiko_SummerUni_Open.png")
seiko_img = pygame.transform.scale(seiko_im, (310, 920))

seikos_im = pygame.image.load("Graphics/Seiko_base/Seiko_SummerUni_Smile.png")
seikos_img = pygame.transform.scale(seikos_im, (310, 920))

seikos_b_im = pygame.image.load("Graphics/Seiko_base/Seiko_SummerUni_Smile_Blush.png")
seikos_b_img = pygame.transform.scale(seikos_b_im, (310, 920))

seiko_b_im = pygame.image.load("Graphics/Seiko_base/Seiko_SummerUni_Open_Blush.png")
seiko_b_img = pygame.transform.scale(seiko_b_im, (310, 920))

# Backgrounds
class_im = pygame.image.load('Graphics/Background/school.jpeg')
class_img = pygame.transform.scale(class_im, (1200, 800))


speech_bubbl = pygame.image.load("Graphics/Basics/speech.png")
speech_bubble = pygame.transform.scale(speech_bubbl, (850, 300))
speech_rect = speech_bubble.get_rect(center=(600, 650))

#scenes_list = [scene0(), scene1(), scene2(), scene3(), scene4(), scene5(), scene6(), scene7(),
            #   scene8(), scene9(), scene10(), scene11(), scene12(), scene13(), scene14(),
            #   scene15(), scene16()]

#current_scene: scenes_list[0]



# Start the game loop

current_scene = scene0

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if current_scene == scene0:
                current_scene = scene1
            elif current_scene == scene1:
                current_scene = scene2
            elif current_scene == scene1:
                current_scene = scene2
            elif current_scene == scene2:
                current_scene = scene3
            elif current_scene == scene3:
                current_scene = scene4
            elif current_scene == scene4:
                current_scene = scene5
            elif current_scene == scene5:
                current_scene = scene6
            elif current_scene == scene6:
                current_scene = scene7
            elif current_scene == scene7:
                current_scene = scene8
            elif current_scene == scene8:
                current_scene = scene9
            elif current_scene == scene9:
                current_scene = scene10
            elif current_scene == scene10:
                current_scene = scene11
            elif current_scene == scene11:
                current_scene = scene12
            elif current_scene == scene12:
                current_scene = scene13
            elif current_scene == scene13:
                current_scene = scene14
            elif current_scene == scene14:
                current_scene = scene15
            elif current_scene == scene15:
                current_scene = scene16
            elif current_scene == scene16:
                current_scene = scene17
            elif current_scene == scene17:
                current_scene = scene18
            elif current_scene == scene18:
                current_scene = scene19
            elif current_scene == scene19:
                current_scene = scene20
            elif current_scene == scene20:
                current_scene = scene21
            elif current_scene == scene21:
                current_scene = scene22
            elif current_scene == scene22:
                current_scene = scene23
            elif current_scene == scene23:
                current_scene = scene24
            elif current_scene == scene24:
                current_scene = scene25

    current_scene()

    clock.tick(40)







