import pygame, sys

pygame.init()

width = 960
height = 560

dis = pygame.display.set_mode((width, height))
pygame.display.set_caption('pixel art maker')

white = (255, 255, 255)
grey = (128, 128, 128)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
magenta = (255, 0, 255)
cyan = (0, 255, 255)
dark_red = (128, 0, 0)
dark_green = (0, 128, 0)
dark_blue = (0, 0, 128)
dark_yellow = (128, 128, 0)
dark_magenta = (128, 0, 128)
dark_cyan = (0, 128, 128)

block_size = 8
block_pos = [width // 2, height // 2]
clock = pygame.time.Clock()
block_list = []
back_color = [black, white]
i = 0
j = 0
current_pen_color = white
color = [current_pen_color, red, green, blue, cyan, yellow, magenta]
dark_colors = [grey, dark_red, dark_green, dark_blue, dark_cyan, dark_yellow, dark_magenta]
current_color = color[i]
current_back_color = black

font1 = pygame.font.SysFont("calibri", 25)

class game:
    def __init__():
        dis.fill(black)
        pygame.draw.rect(dis, white, [width // 2, height // 2, block_size, block_size])
        pygame.display.update()

    def update_page(self, block_list):
        dis.fill(current_back_color)
        for x in block_list:
            pygame.draw.rect(dis, x[2], [x[0], x[1], block_size, block_size]) 
        pygame.display.update()

    def controls_menu():
        dis.fill(current_back_color)
        mesg = font1.render("Ctrl: dark/light colors toggle", True, current_pen_color)
        dis.blit(mesg, [100, 100])
        mesg = font1.render("WASD or arrow keys: move pen", True, current_pen_color)
        dis.blit(mesg, [100, 130])
        mesg = font1.render("Hold Shift or left mouse click and drag: draw to page", True, current_pen_color)
        dis.blit(mesg, [100, 160])
        mesg = font1.render("Esc: shows controls menu", True, current_pen_color)
        dis.blit(mesg, [100, 190])
        mesg = font1.render("Delete or BackSpace or right mouse click and drag: toggle erases block", True, current_pen_color)
        dis.blit(mesg, [100, 220])
        mesg = font1.render("Enter or middle mouse button click: inverts colors(black and white only)", True, current_pen_color)
        dis.blit(mesg, [100, 250])
        mesg = font1.render("Tab: Clears page", True, current_pen_color)
        dis.blit(mesg, [100, 280])
        mesg = font1.render("Space or mouse wheel: Swaps through list of colors", True, current_pen_color)
        dis.blit(mesg, [100, 310])
        pygame.display.update()

class pen:
    def draw(self, pos_x, pos_y):
        pygame.draw.rect(dis, current_color, [pos_x, pos_y, block_size, block_size])
        pygame.display.update()

    def erase():
        for x in block_list:
            if x[0] == block_pos[0] and x[1] == block_pos[1]:
                block_list.remove(x)

    def movement():
        for event in pygame.get():
            if event.type == pygame.QUIT:
                pass
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    pass
                elif event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                    pass
                elif event.key == pygame.K_ESCAPE:
                    pass
                elif event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
                    pass
                elif event.key == pygame.K_TAB:
                    pass
                elif event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                    pass
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    pass
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    pass
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    pass
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    pass
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    pass
            elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEWHEEL:
                if event.button == 1:
                    pass
                if event.button == 2:
                    pass
                if event.button == 3:
                    pass
                if event.button == 4:
                    pass
                if event.button == 5:
                    pass
        
def drawing():
    global current_color
    dis.fill(current_back_color)
    for x in block_list:
        if x[2] == black or x[2] == white:
            x[2] = current_pen_color
        pygame.draw.rect(dis, x[2], [x[0], x[1], block_size, block_size])  
    pygame.display.update()

def erase(pos):
    global current_color
    for x in block_list:
        if x[0] == pos[0] and x[1] == pos[1]:
            block_list.remove(x)
            erase(pos)
    drawing()

def controls_menu():
    global current_color
    dont_exit = True
    while dont_exit:
        dis.fill(current_back_color)
        mesg = font1.render("Ctrl: dark/light colors toggle", True, current_pen_color)
        dis.blit(mesg, [100, 100])
        mesg = font1.render("WASD or arrow keys: move pen", True, current_pen_color)
        dis.blit(mesg, [100, 130])
        mesg = font1.render("Hold Shift or left mouse click and drag: draw to page", True, current_pen_color)
        dis.blit(mesg, [100, 160])
        mesg = font1.render("Esc: shows controls menu", True, current_pen_color)
        dis.blit(mesg, [100, 190])
        mesg = font1.render("Delete or BackSpace or right mouse click and drag: toggle erases block", True, current_pen_color)
        dis.blit(mesg, [100, 220])
        mesg = font1.render("Enter or middle mouse button click: inverts colors(black and white only)", True, current_pen_color)
        dis.blit(mesg, [100, 250])
        mesg = font1.render("Tab: Clears page", True, current_pen_color)
        dis.blit(mesg, [100, 280])
        mesg = font1.render("Space or mouse wheel: Swaps through list of colors", True, current_pen_color)
        dis.blit(mesg, [100, 310])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    dont_exit = False

def mouse_draw():
    Draw = True
    global block_pos
    mouse_pos = pygame.mouse.get_pos()
    mouse_x = mouse_pos[0]
    mouse_y = mouse_pos[1]
    while (mouse_x % 8) != 0:
        mouse_x -= 1
    while (mouse_y % 8) != 0:
        mouse_y -= 1
    if current_color == black or current_color == white:
        pygame.draw.rect(dis, current_pen_color, [mouse_x, mouse_y, block_size, block_size])
    else:
        pygame.draw.rect(dis, current_color, [mouse_x, mouse_y, block_size, block_size])
    pygame.display.update()
    if Draw == True:
        temp_array = []
        temp_array.append(mouse_x)
        temp_array.append(mouse_y)
        temp_array.append(current_color)
        block_list.append(temp_array)
    block_pos = [mouse_x, mouse_y]

def mouse_erase():
    global block_pos
    mouse_pos = pygame.mouse.get_pos()
    mouse_x = mouse_pos[0]
    mouse_y = mouse_pos[1]
    while (mouse_x % 8) != 0:
        mouse_x -= 1
    while (mouse_y % 8) != 0:
        mouse_y -= 1
    block_pos = [mouse_x, mouse_y]
    erase(block_pos)

def main():
    global block_pos
    global i
    global current_color
    global color
    global j
    global current_back_color
    global current_pen_color
    global color
    color = [current_pen_color, red, green, blue, cyan, yellow, magenta]
    _erase = False
    clock.tick(120)
    Draw = False
    dis.fill(current_back_color)
    dark_mode = False
    while True:
        if current_color == black or current_color == white:
            pygame.draw.rect(dis, current_pen_color, [block_pos[0], block_pos[1], block_size, block_size])
        else:
            pygame.draw.rect(dis, current_color, [block_pos[0], block_pos[1], block_size, block_size])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]:
                    mouse_draw()
                if pygame.mouse.get_pressed()[1]:
                    j += 1
                    if j >= 2:
                        j = 0
                    back_color = [black, white]
                    current_back_color = back_color[j]
                    dis.fill(current_back_color)
                    if j == 0:
                        current_pen_color = back_color[1]
                    elif j == 1:
                        current_pen_color = back_color[0]
                    if current_color == black or current_color == white:
                        pygame.draw.rect(dis, current_pen_color, [block_pos[0], block_pos[1], block_size, block_size])
                    else:
                        pygame.draw.rect(dis, current_color, [block_pos[0], block_pos[1], block_size, block_size])
                    pygame.display.update()
                elif pygame.mouse.get_pressed()[2]:
                    mouse_erase()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 5:
                    if i >= 6:
                        i = 0
                    else:
                        i += 1
                    if dark_mode == True:
                        current_color = dark_colors[i]
                    else:
                        current_color = color[i]
                if event.button == 4:
                    if i <= 0:
                        i = 6
                    else:
                        i -= 1
                    if dark_mode == True:
                        current_color = dark_colors[i]
                    else:
                        current_color = color[i]
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    Draw = not Draw
                    _erase = False
                if event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                    _erase = not _erase
                    Draw = False
                if event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
                    dark_mode = not dark_mode
                    if dark_mode == True:
                        current_color = dark_colors[i]
                    else:
                        current_color = color[i]
                if event.key == pygame.K_ESCAPE:
                    controls_menu()
                if event.key == pygame.K_TAB:
                    dis.fill(current_back_color)
                    block_list.clear()
                    i = 0
                    j = 0
                    main()
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    j += 1
                    if j >= 2:
                        j = 0
                    back_color = [black, white]
                    current_back_color = back_color[j]
                    dis.fill(current_back_color)
                    if j == 0:
                        current_pen_color = back_color[1]
                    elif j == 1:
                        current_pen_color = back_color[0]
                    if current_color == black or current_color == white:
                        pygame.draw.rect(dis, current_pen_color, [block_pos[0], block_pos[1], block_size, block_size])
                    else:
                        pygame.draw.rect(dis, current_color, [block_pos[0], block_pos[1], block_size, block_size])
                    pygame.display.update()
                if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and block_pos[0] > 0:
                    block_pos[0] -= block_size
                elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and block_pos[0] < width - block_size:
                    block_pos[0] += block_size
                elif (event.key == pygame.K_UP or event.key == pygame.K_w) and block_pos[1] > 0:
                    block_pos[1] -= block_size
                elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and block_pos[1] < height - block_size:
                    block_pos[1] += block_size
                elif event.key == pygame.K_SPACE:
                    if i >= 6:
                        i = 0
                    else:
                        i += 1
                    if dark_mode == True:
                        current_color = dark_colors[i]
                    else:
                        current_color = color[i]
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    Draw = False 
            if Draw == True:
                temp_array = []
                temp_array.append(block_pos[0])
                temp_array.append(block_pos[1])
                temp_array.append(current_color)
                block_list.append(temp_array)
            if _erase == True:
                erase(block_pos)
            drawing()
main()