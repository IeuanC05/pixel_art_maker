import pygame, sys
class Game:
    def __init__(self, Pen, Color):
        self.width = 960
        self.height = 560
        self.dis = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.clock.tick(120)
        self.background_color = Color.white
        self.pen_size = 8
        self.pen_pos_x = self.width // 2
        self.pen_pos_y = self.height // 2
        self.gameState = True
        self.font = pygame.font.SysFont("arial", 30)
        Pen.draw(self, Color)
        self.update()
        self.message = True
    def controls_menu(self, Pen, Color):
        Pen.get_pen_color(self, Color)
        while True:
            self.dis.fill(self.background_color)
            mesg = self.font.render("Ctrl: dark/light colors toggle", True, Pen.pen_color)
            self.dis.blit(mesg, [50, 100])
            mesg = self.font.render("WASD or arrow keys: move pen", True, Pen.pen_color)
            self.dis.blit(mesg, [50, 130])
            mesg = self.font.render("Hold Shift and arrow keys(or WASD) or left mouse click and drag: draw to page", True, Pen.pen_color)
            self.dis.blit(mesg, [50, 160])
            mesg = self.font.render("Hold Esc: shows controls menu", True, Pen.pen_color)
            self.dis.blit(mesg, [50, 190])
            mesg = self.font.render("Delete or BackSpace to toggle or right mouse click and drag: toggle erases block", True, Pen.pen_color)
            self.dis.blit(mesg, [50, 220])
            mesg = self.font.render("Enter or middle mouse button click: inverts colors(Color.black and Color.white only)", True, Pen.pen_color)
            self.dis.blit(mesg, [50, 250])
            mesg = self.font.render("Tab: Clears page", True, Pen.pen_color)
            self.dis.blit(mesg, [50, 280])
            mesg = self.font.render("Space or mouse wheel: Swaps through list of colors", True, Pen.pen_color)
            self.dis.blit(mesg, [50, 310])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 2:
                        Pen.toggle_mode(self)
                        Pen.get_pen_color(self)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        Pen.toggle_mode(self)
                        Pen.get_pen_color(self)
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        self.message = False
                        return False
    def update(self):
        pygame.display.update()
    def getGamestate(self): 
        return self.gameState