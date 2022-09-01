import pygame, Game, Pen , main, Color
pygame.init()
def main():
    new_color = Color.Color()
    new_pen = Pen.Pen(new_color)
    new_game = Game.Game(new_pen, new_color)
    new_pen.message(new_game)
    while (new_game.getGamestate() == True):
        new_pen.detect_movement(new_game, new_color)
        new_game.update()
if __name__ == "__main__":
    main() 