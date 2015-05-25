import pygame
import pymunk
import pymunk.pygame_util
import sys
import random

white = (255,255,255)
black = (0,0,0)
blue = (0,0,255)
green = (0, 255, 0)
red = (255,0,0)


pygame.init()
clock = pygame.time.Clock()

windowSize = (800, 600)
screen = pygame.display.set_mode(windowSize)

running = True

rad = 14
ball_elasticity = 0.8
friction = .08
space = pymunk.Space()
space.gravity = (0.0, -900.0)
circles = []

def random_color():
    r = random.choice(range(255))
    g = random.choice(range(255))
    b = random.choice(range(255))    
    color = (r,g,b)
    return color

def create_circle(position):
    mass = 1
    inertia = pymunk.moment_for_circle(mass, 0, rad)
    body = pymunk.Body(mass, inertia)
    body.position = position
    shape = pymunk.Circle(body, rad)
    shape.elasticity = ball_elasticity
    shape.friction = friction
    space.add(body, shape)
    return shape

def create_line():
    body = pymunk.Body()
    body.position = (400, 600)
    line_shape = pymunk.Segment(body, (-400, -500), (400, -500), 5)
    line_shape.elasticity = 1
    space.add(line_shape)
    return line_shape

def add_poly():
    body = pymunk.Body()
    body.position = (200, 400)
    vertices = [(-100,-100), (100,-100), (100,100), (-100, 100) ]
    poly = pymunk.Poly(body, vertices, (0,0), 2)
    space.add(poly)
    return poly

line = create_line()
line.color = blue

poly = add_poly()
poly.color = red



while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            originalMousePos = pygame.mouse.get_pos()
            realPos = pymunk.pygame_util.to_pygame(originalMousePos, screen)
            newCircle = create_circle(realPos)
            circles.append(newCircle)

    screen.fill(black)

    for circle in circles:
        circlePosition = int(circle.body.position.x), 600 - int(circle.body.position.y)
        pygame.draw.circle(screen, red, circlePosition, int(circle.radius),0)

    pymunk.pygame_util.draw(screen, line)
    pymunk.pygame_util.draw(screen, poly)

    pygame.display.flip()
    space.step(1/60.0)

sys.exit()
