import pygame as pg
from settings import *
from board import Board

pg.init()

def draw_text(text, size, color, pos, x, y):
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    if pos == 'topleft':
        text_rect.topleft = (x, y)
    elif pos == 'midtop':
        text_rect.midtop = (x,y)
    screen.blit(text_surface, text_rect)

board = Board()

game_over = False
run = True
while run: 
    screen.fill(DIRT)
    clock.tick(FPS)

    
    all_sprites.draw(screen)
    if not game_over:
        board.update()
        all_sprites.update()
    else:
        draw_text(f'GAME OVER - SCORE: {int(board.score)}', 40, WHITE, 'midtop', WIDTH / 2, (HEIGHT / 2) - 100)

    draw_text(f'Score: {int(board.score)}', 26, WHITE, 'topleft', 0, 0)

    # sprite collision
    hits = pg.sprite.spritecollide(board.sheep, grass_group, True)
    for hit in hits:
        board.score += 100
    
    hits = pg.sprite.groupcollide(sheeps, wolves, True, False)
    if hits:
        game_over = True


    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                run = False

    pg.display.flip()

pg.quit()