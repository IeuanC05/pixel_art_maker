import pygame, sys
class Pen:
    def __init__(self, Color):
        self.toggle_draw = False
        self.draw_list = []
        self.erase_toggle = False
        self.i = 0
        self.j = 0
        self.dark_mode_toggle = False
        self.light_color_list = [Color.black, Color.red, Color.orange, Color.yellow, Color.green, Color.cyan, Color.blue, Color.magenta]
        self.dark_color_list = [Color.grey, Color.dark_red, Color.dark_orange, Color.dark_yellow, Color.dark_green, Color.dark_cyan, Color.dark_blue, Color.dark_magenta]
        self.color_list = [self.light_color_list[self.i], self.dark_color_list[self.i]]
        self.current_color = self.color_list[self.j]
        self.pen_color = Color.black
    def light_mode(self, Game, Color):
        self.light_color_list = [Color.black, Color.red, Color.orange, Color.yellow, Color.green, Color.cyan, Color.blue, Color.magenta]
        self.dark_color_list = [Color.grey, Color.dark_red, Color.dark_orange, Color.dark_yellow, Color.dark_green, Color.dark_cyan, Color.dark_blue, Color.dark_magenta]
        self.color_list = [self.light_color_list[self.i], self.dark_color_list[self.i]]
        self.current_color = self.color_list[self.j]
        Game.background_color = Color.white
        self.draw(Game, Color)
    def dark_mode(self, Game, Color):
        self.light_color_list = [Color.white, Color.red, Color.orange, Color.yellow, Color.green, Color.cyan, Color.blue, Color.magenta]
        self.dark_color_list = [Color.grey, Color.dark_red, Color.dark_orange, Color.dark_yellow, Color.dark_green, Color.dark_cyan, Color.dark_blue, Color.dark_magenta]
        self.color_list = [self.light_color_list[self.i], self.dark_color_list[self.i]]
        self.current_color = self.color_list[self.j]
        Game.background_color = Color.black
        self.draw(Game, Color)
    def toggle_mode(self, Game, Color):
        self.dark_mode_toggle = not self.dark_mode_toggle
        if self.dark_mode_toggle == True:
            self.dark_mode(Game, Color)
        elif self.dark_mode_toggle == False:
            self.light_mode(Game, Color)
        self.draw(Game, Color) 
    def erase(self, Game):
        if self.erase_toggle != True:
            mouse_pos = pygame.mouse.get_pos()
            x = mouse_pos[0]
            y = mouse_pos[1]
            while (x % 8) != 0:
                x -= 1
            while (y % 8) != 0:
                y -= 1
            Game.pen_pos_x = x
            Game.pen_pos_y = y
        for x in self.draw_list:
            if Game.pen_pos_x == x[0] and Game.pen_pos_y == x[1]: 
                self.draw_list.remove(x)
    def get_pen_color(self, Game, Color):
        if Game.background_color == Color.white:
            self.pen_color = Color.black
        elif Game.background_color == Color.black:
            self.pen_color = Color.white 
    def mouse_draw(self, Game, Color):
        mouse_pos = pygame.mouse.get_pos()
        x = mouse_pos[0]
        y = mouse_pos[1]
        while (x % 8) != 0:
            x -= 1
        while (y % 8) != 0:
            y -= 1
        Game.pen_pos_x = x
        Game.pen_pos_y = y
        self.toggle_draw = True
        if x % 8 == 0 and y % 8 == 0:
            self.draw(Game, Color)
    def draw(self, Game, Color):
        Game.dis.fill(Game.background_color)
        for x in self.draw_list:
            if x[2] == Color.white and Game.background_color == Color.white:
                pygame.draw.rect(Game.dis, Color.black, [x[0], x[1], Game.pen_size, Game.pen_size])
            elif x[2] == Color.black and Game.background_color == Color.black:
                pygame.draw.rect(Game.dis, Color.white, [x[0], x[1], Game.pen_size, Game.pen_size])
            else:
                pygame.draw.rect(Game.dis, x[2], [x[0], x[1], Game.pen_size, Game.pen_size])
        if self.toggle_draw == True:
            temp_list = []
            temp_list.append(Game.pen_pos_x)
            temp_list.append(Game.pen_pos_y)
            temp_list.append(self.current_color)
            self.draw_list.append(temp_list)
        pygame.draw.rect(Game.dis, self.current_color, [Game.pen_pos_x, Game.pen_pos_y, Game.pen_size, Game.pen_size])
        self.toggle_draw = False
    def update_color(self):
        self.j += 1
        if self.j >= 2:
            self.j = 0
        self.color_list = [self.light_color_list[self.i], self.dark_color_list[self.i]]
        self.current_color = self.color_list[self.j]
    def message(self, Game):
        if Game.message == True:
            mesg = Game.font.render("Hold Esc to show controls", True, self.pen_color)
            Game.dis.blit(mesg, [0, 0])
    def detect_movement(self, Game, Color):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEMOTION:
                    if pygame.mouse.get_pressed()[0]:
                        self.mouse_draw(Game, Color)
                    if pygame.mouse.get_pressed()[2]:
                        self.erase(Game)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 2:
                        self.toggle_mode(Game, Color)
                        return False 
                    if event.button == 4:
                        if self.i >= 0:
                            self.i -= 1
                            self.color_list = [self.light_color_list[self.i], self.dark_color_list[self.i]]
                            self.current_color = self.color_list[self.j]
                        else:
                            self.i = 6
                            self.color_list = [self.light_color_list[self.i], self.dark_color_list[self.i]]
                            self.current_color = self.color_list[self.j]
                    if event.button == 5:
                        if self.i <= 6:
                            self.i += 1
                            self.color_list = [self.light_color_list[self.i], self.dark_color_list[self.i]]
                            self.current_color = self.color_list[self.j]
                        else:
                            self.i = 0
                            self.color_list = [self.light_color_list[self.i], self.dark_color_list[self.i]]
                            self.current_color = self.color_list[self.j]
                    self.toggle_draw = False
                    self.draw(Game, Color)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        self.toggle_draw = True
                        self.erase_toggle = False
                    elif event.key == pygame.K_TAB:
                        self.toggle_draw = False
                        self.draw_list.clear()
                        Game.dis.fill(Color.black)
                        self.draw(Game, Color)
                    elif event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
                        self.update_color()
                        self.toggle_draw = False
                        return False
                    elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        self.toggle_mode(Game, Color)
                        return False 
                    elif event.key == pygame.K_ESCAPE:
                        Game.controls_menu(self, Color)
                    elif event.key == pygame.K_SPACE:
                        if self.i <= 6:
                            self.i += 1
                            self.color_list = [self.light_color_list[self.i], self.dark_color_list[self.i]]
                            self.current_color = self.color_list[self.j]
                        else:
                            self.i = 0
                            self.color_list = [self.light_color_list[self.i], self.dark_color_list[self.i]]
                            self.current_color = self.color_list[self.j]
                        self.toggle_draw = False
                        self.draw(Game, Color)
                    elif event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                        self.erase_toggle = not self.erase_toggle
                        self.erase(Game)
                        self.draw(Game, Color)
                        self.toggle_draw = False
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        Game.pen_pos_x -= Game.pen_size
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        Game.pen_pos_x += Game.pen_size
                    elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        Game.pen_pos_y -= Game.pen_size
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        Game.pen_pos_y += Game.pen_size
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        self.toggle_draw = False  
                if self.erase_toggle == True:
                    self.erase(Game)
                self.draw(Game, Color)
            return False