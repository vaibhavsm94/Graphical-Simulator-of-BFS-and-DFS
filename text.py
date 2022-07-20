import pygame

def text(screen, text, x, y, size=20, color=(255, 255, 255), fonttype="monospace"):
    text=str(text)
    font=pygame.font.SysFont(fonttype, size)
    text=font.render(text, True, color)
    screen.blit(text, (x, y))
