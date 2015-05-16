import sys, random
import pygame
from pygame.locals import *
from pygame.color import *
import pymunk
import pymunk.pygame_util
import math
import slope_segments as ss

screen_w = 3033
screen_h = 720
#edit_mode = False
line_list = []


def main():
    pygame.init()
    screen = pygame.display.set_mode((screen_w, screen_h))
    clock = pygame.time.Clock()
    running = True
    edit_mode = False
    lines = False
    # img = pygame.image.load('small_circle.png')
    point_list = []
    # May need to set x and y gravity points seperately in case up and right are pressed together
    normal_grav = (0.0, -900.0)
    up_grav = (0.0, 900.0)
    down_grav = (0.0, -1500.0)
    left_grav = (-900.0, -900.0)
    right_grav = (900.0, -900.0)

    space = pymunk.Space()
    space.gravity = normal_grav

    # lines = add_line(space)
    balls = []
    lines = add_line(space)

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == K_UP:
                    space.gravity = up_grav
                elif event.key == K_DOWN:
                    space.gravity = down_grav
                elif event.key == K_LEFT:
                    space.gravity = left_grav
                elif event.key == K_RIGHT:
                    space.gravity = right_grav
                elif event.key == K_e:
                    edit_mode = True
                    pygame.display.set_caption("Edit Mode Active")
                elif event.key == K_b:
                    edit_mode = False
                    pygame.display.set_caption("Ball Mode Active")

            elif event.type == KEYUP:
                if event.key == K_UP:
                    space.gravity = normal_grav
                elif event.key == K_DOWN:
                    space.gravity = normal_grav
                elif event.key == K_LEFT:
                    space.gravity = normal_grav
                elif event.key == K_RIGHT:
                    space.gravity = normal_grav

            elif event.type == pygame.MOUSEBUTTONDOWN and edit_mode == False:
                originalMousePos = pygame.mouse.get_pos()
                #print "pygame pos:", originalMousePos
                realPos = pymunk.pygame_util.to_pygame(originalMousePos, screen)
                #print "converted:", realPos
                new_ball = create_ball(space, realPos)
                balls.append(new_ball)

            elif event.type == pygame.MOUSEBUTTONDOWN and edit_mode == True:
                originalMousePos = pygame.mouse.get_pos()
                realPos = pymunk.pygame_util.to_pygame(originalMousePos, screen)
                # print "realPos:", realPos
                point_list.append(realPos)
                # print "point list:", point_list

                if len(point_list) >= 2:  #you need a start point and stop point for line
                    lines = add_line(space, point_list)
                    point_list = []


        screen.fill(THECOLORS['black'])

        balls_to_remove = []
        for ball in balls:
            if ball.body.position.y < 10:
                balls_to_remove.append(ball)
            draw_ball(screen, ball)

        for ball in balls_to_remove:
            space.remove(ball, ball.body)
            balls.remove(ball)

        if lines:
            draw_lines(screen, lines)

        space.step(1/50.0)

        pygame.display.flip()
        clock.tick(50)



def create_ball(space, position):
    mass = 1
    radius = 20
    inertia = pymunk.moment_for_circle(mass, 0, radius, (0,0))
    body = pymunk.Body(mass, inertia)
    body.position = position
    shape = pymunk.Circle(body, radius, (0,0))
    shape.elasticity = 0.2
    shape.friction = 0.08
    space.add(body, shape)
    return shape

def draw_ball(screen, ball):
    pos = int(ball.body.position.x), screen_h-int(ball.body.position.y)
    #print "draw pos:", pos
    pygame.draw.circle(screen, THECOLORS['red'], pos, int(ball.radius), 2)
    # screen.blit(image, pos)

        ## This is a predefined set of three lines
# def add_line(space):
#     body = pymunk.Body()
#     body.position = (0, 0)
#     line_shape1 = pymunk.Segment(body, (50, 500), (300, 50), 10)
#     line_shape2 = pymunk.Segment(body, (300, 50), (550, 50), 10)
#     line_shape3 = pymunk.Segment(body, (550, 50), (600, 200), 10)
#     line_shape1.elasticity = 1
#     line_shape2.elasticity = 1
#     line_shape3.elasticity = 1
#     space.add(line_shape1, line_shape2, line_shape3)
#     return [line_shape1, line_shape2, line_shape3]

# def add_line(space, input_list):
    # ## print "input_list:", input
    # ## print "input0:", input_list[0], "input1:", input_list[1]
    # body = pymunk.Body()
    # body.position = (0, 0)
    # line = pymunk.Segment(body, input_list[0], input_list[1], 10)
    # line.elasticity = 1
    # space.add(line)
    # line_list.append(line)
    # return line_list

def add_line(space):
        ## This section works if input list is a like the line below, multiple lines in one list
    # input_list = [ [(50, 500), (300, 50)], [(300, 50), (550, 50)], [(550, 50), (600, 200)] ]
    input_list = ss.pymunk_segments
    for input in input_list:
        # print "input:", input
        # print "input0:", input[0], "input1:", input[1]
        body = pymunk.Body()
        body.position = (0, 0)
        line = pymunk.Segment(body, input[0], input[1], 10)
        line.elasticity = 1
        space.add(line)
        line_list.append(line)
    return line_list

def draw_lines(screen, lines):
    for line in lines:
        body = line.body
        p1 = to_pygame(line.a)
        p2 = to_pygame(line.b)
        pygame.draw.lines(screen, THECOLORS['blue'], False, [p1,p2], 10)

def to_pygame(p):
    """Small hack to convert pymunk to pygame coordinates"""
    return int(p.x), int(-p.y+screen_h)


if __name__ == '__main__':
    main()
    sys.exit(1)








