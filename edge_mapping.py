import pygame
import sys

image_w = 3033
image_h = 1000
image = 'slope.jpg'
detail = 50  #how many pixels do I want to increment by 1 pixel 5 pixels, etc.

def main():
    pygame.init()
    screen = pygame.display.set_mode((image_w, image_h))
    running = True
    clock = pygame.time.Clock()

    img = pygame.image.load(image)
    screen.blit(img, (0, 0))  # had (0, 200) for a while, not sure why, might be reason game is 200 off up/down axis
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
                #if screen.get_at((x, y)) == (0, 0, 0, 255) or screen.get_at((x,y)) == (8, 8 , 6, 255):
                if r < 10 and g < 10 and b < 10:
                    y += detail
                else:
                    edge_list.append((x,y))
                    print "RGB:", screen.get_at((x,y))
                    print "added to list:", x, y
                    x += detail
                    y = 0

                if x >= image_w-5:
                    print edge_list
                    detecting = False
            except IndexError:
                print "Index Error at", x, y
                detecting = False
            break


        # screen.blit(img, (100, 100))

        # pygame.display.flip()
        #clock.tick(50)

if __name__ == "__main__":
    main()
    sys.exit(1)

