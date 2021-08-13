import pygame

pygame.init()

# colors
grey = (50, 50, 50)
red = (255, 64, 25)
neon = (179, 255, 25)

# board
win = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Tic-Tac-Toe")

first = pygame.draw.rect(win, grey, (25, 25, 100, 100))  # RGB -> starting positions (x, y) -> rectangle dimensions(length, width)
second = pygame.draw.rect(win, grey, (150, 25, 100, 100))
third = pygame.draw.rect(win, grey, (275, 25, 100, 100))

fourth = pygame.draw.rect(win, grey, (25, 150, 100, 100))
fifth = pygame.draw.rect(win, grey, (150, 150, 100, 100))
sixth = pygame.draw.rect(win, grey, (275, 150, 100, 100))

seventh = pygame.draw.rect(win, grey, (25, 275, 100, 100))
eighth = pygame.draw.rect(win, grey, (150, 275, 100, 100))
ninth = pygame.draw.rect(win, grey, (275, 275, 100, 100))

run = True

draw_object = 'rect'

first_open = True   # indicates that the first box is empty/available
second_open = True
third_open = True
fourth_open = True
fifth_open = True
sixth_open = True
seventh_open = True
eighth_open = True
ninth_open = True

while run:

    pygame.time.delay(100)      # refresh time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # pressing the cross quits the game
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:

                first_open = True   
                second_open = True
                third_open = True
                fourth_open = True
                fifth_open = True
                sixth_open = True
                seventh_open = True
                eighth_open = True
                ninth_open = True

                first = pygame.draw.rect(win, grey, (25, 25, 100, 100)) 
                second = pygame.draw.rect(win, grey, (150, 25, 100, 100))
                third = pygame.draw.rect(win, grey, (275, 25, 100, 100))

                fourth = pygame.draw.rect(win, grey, (25, 150, 100, 100))
                fifth = pygame.draw.rect(win, grey, (150, 150, 100, 100))
                sixth = pygame.draw.rect(win, grey, (275, 150, 100, 100))

                seventh = pygame.draw.rect(win, grey, (25, 275, 100, 100))
                eighth = pygame.draw.rect(win, grey, (150, 275, 100, 100))
                ninth = pygame.draw.rect(win, grey, (275, 275, 100, 100))

        if event.type == pygame.MOUSEBUTTONDOWN:  # looking for mouse button down event
            pos = pygame.mouse.get_pos()        # everytime mouse is clicked, it stores the position
            
            if first.collidepoint(pos) and first_open:         # if click happens inside the first box
                if draw_object == 'rect':
                    pygame.draw.rect(win, neon, (37.5, 37.5, 75, 75))
                    draw_object = 'circle'      # object switches to circle when the reactangle is drawn
                else:
                    pygame.draw.circle(win, red, (75, 75), 37.5)      # centre of the circle -> radius
                    draw_object = 'rect'        # object switches to rectangle when the circle is drawn
                first_open = False              # indicating that the box is filled/unavailable

            if second.collidepoint(pos) and second_open:
                if draw_object == 'rect':
                    pygame.draw.rect(win, neon, (162.5, 37.5, 75, 75))
                    draw_object = 'circle'
                else:
                    pygame.draw.circle(win, red, (200, 75), 37.5)
                    draw_object = 'rect'
                second_open = False

            if third.collidepoint(pos) and third_open:
                if draw_object == 'rect':
                    pygame.draw.rect(win, neon, (287.5, 37.5, 75, 75))
                    draw_object = 'circle'
                else:
                    pygame.draw.circle(win, red, (325, 75), 37.5)
                    draw_object = 'rect'
                third_open = False

            if fourth.collidepoint(pos) and fourth_open:
                if draw_object == 'rect':
                    pygame.draw.rect(win, neon, (37.5, 162.5, 75, 75))
                    draw_object = 'circle'
                else:    
                    pygame.draw.circle(win, red, (75, 200), 37.5)
                    draw_object = 'rect'
                fourth_open = False

            if fifth.collidepoint(pos) and fifth_open:
                if draw_object == 'rect':
                    pygame.draw.rect(win, neon, (162.5, 162.5, 75, 75))
                    draw_object = 'circle'
                else: 
                    pygame.draw.circle(win, red, (200, 200), 37.5)
                    draw_object = 'rect'
                fifth_open = False

            if sixth.collidepoint(pos) and sixth_open:
                if draw_object == 'rect':
                    pygame.draw.rect(win, neon, (287.5, 162.5, 75, 75))
                    draw_object = 'circle'
                else:  
                    pygame.draw.circle(win, red, (325, 200), 37.5)
                    draw_object = 'rect'
                sixth_open = False

            if seventh.collidepoint(pos) and seventh_open:
                if draw_object == 'rect':
                    pygame.draw.rect(win, neon, (37.5, 287.5, 75, 75))
                    draw_object = 'circle'
                else: 
                    pygame.draw.circle(win, red, (75, 325), 37.5)
                    draw_object = 'rect'
                seventh_open = False

            if eighth.collidepoint(pos) and eighth_open:
                if draw_object == 'rect':
                    pygame.draw.rect(win, neon, (162.5, 287.5, 75, 75))
                    draw_object = 'circle'
                else: 
                    pygame.draw.circle(win, red, (200, 325), 37.5)
                    draw_object = 'rect'
                eighth_open = False

            if ninth.collidepoint(pos) and ninth_open:
                if draw_object == 'rect':
                    pygame.draw.rect(win, neon, (287.5, 287.5, 75, 75))
                    draw_object = 'circle'
                else: 
                    pygame.draw.circle(win, red, (325, 325), 37.5)
                    draw_object = 'rect'
                ninth_open = False


    pygame.display.update()     # new things brought to the front for the users to see

pygame.quit()