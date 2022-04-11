import tkinter as tk
from graphics import *
import turtle
from pygame.locals import *
import random
import sys
import pygame

root = tk.Tk()
root.title("Menu")
root.geometry('300x300')
def rysunek():


    t = turtle.Turtle()

    screen = turtle.Screen()
    screen.bgcolor("springgreen1")
    t.speed(0)
    t.color("black")
    t.shape("turtle")

    # niebo
    t.fillcolor('blue')
    t.begin_fill()
    t.penup()
    t.goto(-5000, -200)
    t.pendown()
    t.fillcolor('blue')
    t.begin_fill()
    t.goto(5000, -200)
    t.goto(5000, 5000)
    t.goto(-5000, 5000)
    t.goto(-5000, -200)
    t.end_fill()

    # dom
    t.penup()
    t.goto(-200, -200)
    t.pendown()
    t.fillcolor('pale goldenrod')
    t.begin_fill()
    t.goto(400, -200)
    t.goto(400, 200)
    t.goto(-200, 200)
    t.goto(-200, -200)
    t.end_fill()

    # dach
    t.penup()
    t.goto(-200, 200)
    t.pendown()
    t.fillcolor('firebrick')
    t.begin_fill()
    t.goto(100, 350)
    t.goto(400, 200)
    t.end_fill()

    # drzwi
    t.penup()
    t.goto(100, -200)
    t.pendown()
    t.fillcolor('sienna')
    t.begin_fill()
    t.goto(100, -100)
    t.goto(50, -100)
    t.goto(50, -200)
    t.end_fill()

    # okno1
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.fillcolor('light gray')
    t.begin_fill()
    t.goto(-100, 0)
    t.goto(-100, 100)
    t.goto(0, 100)
    t.goto(0, 0)
    t.end_fill()

    # okno2
    t.penup()
    t.goto(300, 0)
    t.pendown()
    t.fillcolor('light gray')
    t.begin_fill()
    t.goto(200, 0)
    t.goto(200, 100)
    t.goto(300, 100)
    t.goto(300, 0)
    t.end_fill()

    # komin
    t.penup()
    t.goto(300, 200)
    t.pendown()
    t.fillcolor('firebrick')
    t.begin_fill()
    t.goto(300, 300)
    t.goto(250, 300)
    t.goto(250, 200)
    t.end_fill()

    # promienie
    def promienie(t, length, radius):
        for i in range(4):
            t.penup()
            t.forward(radius)
            t.pendown()
            t.forward(length)
            t.penup()
            t.backward(length + radius)
            t.left(90)

    # slonce
    t.penup()
    t.goto(-300, 300)
    t.pendown()
    t.fillcolor('yellow')
    t.begin_fill()
    t.pencolor('yellow')
    t.circle(30)
    t.end_fill()
    t.penup()
    t.pensize(3)
    t.goto(-300, 330)
    promienie(t, 40, 54)
    t.right(45)
    promienie(t, 40, 54)
    t.left(45)

    # chmura
    t.penup()
    t.goto(500, 300)
    t.fillcolor('white')
    t.begin_fill()
    t.circle(40)
    t.end_fill()
    t.goto(540, 280)
    t.fillcolor('white')
    t.begin_fill()
    t.circle(40)
    t.end_fill()
    t.goto(580, 300)
    t.fillcolor('white')
    t.begin_fill()
    t.circle(40)
    t.end_fill()
    t.goto(620, 280)
    t.fillcolor('white')
    t.begin_fill()
    t.circle(40)
    t.end_fill()
    t.goto(660, 300)
    t.fillcolor('white')
    t.begin_fill()
    t.circle(40)
    t.end_fill()

    # drzewo
    t.goto(-500, -200)
    t.pendown()
    t.pencolor('brown')
    t.fillcolor('brown')
    t.begin_fill()
    t.goto(-500, -100)
    t.goto(-475, -100)
    t.goto(-475, -200)
    t.end_fill()
    t.pencolor('springgreen4')
    t.penup()
    t.goto(-650, -100)
    t.pendown()
    t.fillcolor('springgreen4')
    t.begin_fill()
    t.goto(-350, -100)
    t.goto(-500, 200)
    t.goto(-650, -100)
    t.end_fill()

    t.hideturtle()
    turtle.exitonclick()


def inicjaly():


    win = GraphWin('Bezier Inicjały', 800, 500)

    class Line():

        def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
            self.x1 = x1
            self.x2 = x2
            self.x3 = x3
            self.x4 = x4
            self.y1 = y1
            self.y2 = y2
            self.y3 = y3
            self.y4 = y4

        def draw_Line(self, win):
            t = 0
            for i in range(0, 1000):
                t += 0.001
                self.xt = pow(1 - t, 3) * self.x1 + 3 * t * pow(1 - t, 2) * self.x2 + 3 * pow(t, 2) * (
                        1 - t) * self.x3 + pow(t, 3) * self.x4
                self.yt = pow(1 - t, 3) * self.y1 + 3 * t * pow(1 - t, 2) * self.y2 + 3 * pow(t, 2) * (
                        1 - t) * self.y3 + pow(t, 3) * self.y4
                punkt = Point(self.xt, self.yt)
                punkt.draw(win)

    def draw_Bezier():
        linie = [
            # LITERA L
            Line(99, 85, 99, 70, 92, 318, 105, 326),
            Line(105, 326, 124, 338, 251, 328, 266, 331),
            Line(266, 331, 285, 335, 294, 294, 273, 289),
            Line(273, 289, 258, 286, 180, 275, 168, 284),
            Line(168, 284, 152, 296, 176, 110, 160, 89),
            Line(160, 89, 151, 77, 96, 72, 98, 86),

            # LITERA Z
            Line(376, 76, 361, 75, 507, 70, 521, 83),
            Line(521, 83, 532, 93, 391, 260, 395, 274),
            Line(395, 274, 400, 292, 494, 280, 509, 282),
            Line(509, 282, 527, 285, 528, 328, 508, 328),
            Line(508, 328, 493, 328, 356, 314, 341, 313),
            Line(341, 313, 321, 312, 336, 287, 342, 273),
            Line(342, 273, 353, 248, 443, 137, 443, 122),
            Line(443, 122, 443, 107, 388, 115, 373, 113),
            Line(373, 113, 354, 111, 355, 80, 376, 76),

        ]

        for linia in linie:
            linia.draw_Line(win)

    draw_Bezier()
    win.getMouse()
    win.close()

def gra():


    FPS = 32
    scr_width = 289
    scr_height = 511
    display_screen_window = pygame.display.set_mode((scr_width, scr_height))
    play_ground = scr_height * 0.8
    game_image = {}
    game_audio_sound = {}
    player = 'images/bird.png'
    bcg_image = 'images/background.png'
    pipe_image = 'images/pipe.png'

    def welcome_main_screen():
        p_x = int(scr_width / 5)
        p_y = int((scr_height - game_image['player'].get_height()) / 2)
        msgx = int((scr_width - game_image['message'].get_width()) / 2)
        msgy = int(scr_height * 0.13)
        b_x = 0
        while True:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    #sys.exit()

                elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                    return
                else:
                    display_screen_window.blit(game_image['background'], (0, 0))
                    display_screen_window.blit(game_image['player'], (p_x, p_y))
                    display_screen_window.blit(game_image['message'], (msgx, msgy))
                    display_screen_window.blit(game_image['base'], (b_x, play_ground))
                    pygame.display.update()
                    time_clock.tick(FPS)

    def main_gameplay():
        score = 0
        p_x = int(scr_width / 5)
        p_y = int(scr_width / 2)
        b_x = 0

        n_pip1 = get_Random_Pipes()
        n_pip2 = get_Random_Pipes()

        up_pips = [
            {'x': scr_width + 200, 'y': n_pip1[0]['y']},
            {'x': scr_width + 200 + (scr_width / 2), 'y': n_pip2[0]['y']},
        ]

        low_pips = [
            {'x': scr_width + 200, 'y': n_pip1[1]['y']},
            {'x': scr_width + 200 + (scr_width / 2), 'y': n_pip2[1]['y']},
        ]

        pip_Vx = -4

        p_vx = -9
        p_mvx = 10
        p_mvy = -8
        p_accuracy = 1

        p_flap_accuracy = -8
        p_flap = False

        while True:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                    if p_y > 0:
                        p_vx = p_flap_accuracy
                        p_flap = True
                        game_audio_sound['wing'].play()

            cr_tst = is_Colliding(p_x, p_y, up_pips,
                                  low_pips)
            if cr_tst:
                return

            p_middle_positions = p_x + game_image['player'].get_width() / 2
            for pipe in up_pips:
                pip_middle_positions = pipe['x'] + game_image['pipe'][0].get_width() / 2
                if pip_middle_positions <= p_middle_positions < pip_middle_positions + 4:
                    score += 1
                    print(f"Your score is {score}")
                    game_audio_sound['point'].play()

            if p_vx < p_mvx and not p_flap:
                p_vx += p_accuracy

            if p_flap:
                p_flap = False
            p_height = game_image['player'].get_height()
            p_y = p_y + min(p_vx, play_ground - p_y - p_height)

            for pip_upper, pip_lower in zip(up_pips, low_pips):
                pip_upper['x'] += pip_Vx
                pip_lower['x'] += pip_Vx

            if 0 < up_pips[0]['x'] < 5:
                new_pip = get_Random_Pipes()
                up_pips.append(new_pip[0])
                low_pips.append(new_pip[1])

            if up_pips[0]['x'] < -game_image['pipe'][0].get_width():
                up_pips.pop(0)
                low_pips.pop(0)

            display_screen_window.blit(game_image['background'], (0, 0))
            for pip_upper, pip_lower in zip(up_pips, low_pips):
                display_screen_window.blit(game_image['pipe'][0], (pip_upper['x'], pip_upper['y']))
                display_screen_window.blit(game_image['pipe'][1], (pip_lower['x'], pip_lower['y']))

            display_screen_window.blit(game_image['base'], (b_x, play_ground))
            display_screen_window.blit(game_image['player'], (p_x, p_y))
            d = [int(x) for x in list(str(score))]
            w = 0
            for digit in d:
                w += game_image['numbers'][digit].get_width()
            Xoffset = (scr_width - w) / 2

            for digit in d:
                display_screen_window.blit(game_image['numbers'][digit], (Xoffset, scr_height * 0.12))
                Xoffset += game_image['numbers'][digit].get_width()
            pygame.display.update()
            time_clock.tick(FPS)

    def is_Colliding(p_x, p_y, up_pipes, low_pipes):
        if p_y > play_ground - 25 or p_y < 0:
            game_audio_sound['hit'].play()
            return True

        for pipe in up_pipes:
            pip_h = game_image['pipe'][0].get_height()
            if (p_y < pip_h + pipe['y'] and abs(p_x - pipe['x']) < game_image['pipe'][0].get_width()):
                game_audio_sound['hit'].play()
                return True

        for pipe in low_pipes:
            if (p_y + game_image['player'].get_height() > pipe['y']) and abs(p_x - pipe['x']) < \
                    game_image['pipe'][0].get_width():
                game_audio_sound['hit'].play()
                return True

        return False

    def get_Random_Pipes():
        pip_h = game_image['pipe'][0].get_height()
        off_s = scr_height / 3
        yes2 = off_s + random.randrange(0, int(scr_height - game_image['base'].get_height() - 1.2 * off_s))
        pipeX = scr_width + 10
        y1 = pip_h - yes2 + off_s
        pipe = [
            {'x': pipeX, 'y': -y1},  # upper Pipe
            {'x': pipeX, 'y': yes2}  # lower Pipe
        ]
        return pipe

    if __name__ == "__main__":

        pygame.init()
        time_clock = pygame.time.Clock()
        pygame.display.set_caption('Gra')
        game_image['numbers'] = (
            pygame.image.load('images/0.png').convert_alpha(),
            pygame.image.load('images/1.png').convert_alpha(),
            pygame.image.load('images/2.png').convert_alpha(),
            pygame.image.load('images/3.png').convert_alpha(),
            pygame.image.load('images/4.png').convert_alpha(),
            pygame.image.load('images/5.png').convert_alpha(),
            pygame.image.load('images/6.png').convert_alpha(),
            pygame.image.load('images/7.png').convert_alpha(),
            pygame.image.load('images/8.png').convert_alpha(),
            pygame.image.load('images/9.png').convert_alpha(),
        )

        game_image['message'] = pygame.image.load('images/message.png').convert_alpha()
        game_image['base'] = pygame.image.load('images/base.png').convert_alpha()
        game_image['pipe'] = (pygame.transform.rotate(pygame.image.load(pipe_image).convert_alpha(), 180),
                              pygame.image.load(pipe_image).convert_alpha()
                              )

        game_audio_sound['die'] = pygame.mixer.Sound('sounds/die.wav')
        game_audio_sound['hit'] = pygame.mixer.Sound('sounds/hit.wav')
        game_audio_sound['point'] = pygame.mixer.Sound('sounds/point.wav')
        game_audio_sound['swoosh'] = pygame.mixer.Sound('sounds/swoosh.wav')
        game_audio_sound['wing'] = pygame.mixer.Sound('sounds/wing.wav')

        game_image['background'] = pygame.image.load(bcg_image).convert()
        game_image['player'] = pygame.image.load(player).convert_alpha()

        while True:
            welcome_main_screen()
            main_gameplay()


btn1 = tk.Button(root, text="1. Rysunek",command=rysunek)
btn1.pack(ipadx=1, ipady=1, expand=True)
btn2 = tk.Button(root, text="2. Gra",command=gra)
btn2.pack(ipadx=1, ipady=1, expand=True)
btn3 = tk.Button(root, text="3. Inicjały",command=inicjaly)
btn3.pack(ipadx=1, ipady=1, expand=True)
btn4 = tk.Button(root, text= 'Exit', command=exit)
btn4.pack(ipadx=1, ipady=1, expand=True)
root.mainloop()