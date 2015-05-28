import pygame
import sys

# manually input image dimensions and filename
image_w = 3033
image_h = 1000
image = 'slope.jpg'
screen_h = 720  #height of display screen for final game
detail = 10  #how many pixels do I want to increment by 1 pixel 5 pixels, etc.

def map():
    pygame.init()
    screen = pygame.display.set_mode((image_w, image_h))
    running = True
    clock = pygame.time.Clock()

    img = pygame.image.load(image)
    screen.blit(img, (0, 0))
    pygame.display.flip()

    x = 0
    y = 0
    edge_list = []
    detecting = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print "Position:", pos
                rgba = screen.get_at(pos)
                print "RGBA:", rgba

        while detecting:
            r = screen.get_at((x,y))[0]
            g = screen.get_at((x,y))[1]
            b = screen.get_at((x,y))[2]
            try:
                if r < 10 and g < 10 and b < 10:
                    y += 1
                else:
                    edge_list.append((x,y))
                    #print "RGB:", screen.get_at((x,y))
                    #print "added to list:", x, y
                    x += detail
                    y = 0

                if x >= image_w-5:
                    #print edge_list
                    return edge_list
                    detecting = False
            except IndexError:
                print "Index Error at", x, y
                detecting = False
            break

def points_to_segments(points):
    p = points
    slope_segments = []
    for i in range(len(p)):
        #print i, slope_points[i]
        if i < len(p)-2:
            slope_segments.append([p[i], p[i+1]])

    #print slope_segments
    return slope_segments

def segment_to_pymunkseg(segments):
    pymunk_segments = []
    for segment in segments:
        first_pair = segment[0]
        second_pair = segment[1]
        pymunk_segments.append([(first_pair[0], screen_h-first_pair[1]), (second_pair[0], screen_h-second_pair[1])])
    return pymunk_segments

def write_file(data):
    with open('pymunk_slope_segments.py', 'w') as outfile:
        outfile.write("pymunk_slope_segments = {}".format(str(data)))



if __name__ == "__main__":
    points = map()
    segments = points_to_segments(points)
    pymunk_segments = segment_to_pymunkseg(segments)
    write_file(pymunk_segments)

    sys.exit(1)

