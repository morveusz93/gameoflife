import pygame

(width, height) = (1500, 800)
cell_size = 8
cells_x = width//cell_size
cells_y = height//cell_size

pygame.init()
pygame.display.set_caption("GameOfLife by Morvy")
screen = pygame.display.set_mode((width, height))
'''color of background'''
screen.fill((61,61,61))

gameboard = [0] * cells_x
for i in range(cells_x):
    gameboard[i] = [0] * cells_y


def draw_gameboard():
    for i in range(cells_x):
        for j in range(cells_y):
            if gameboard[i][j] == 0:
                pygame.draw.rect(screen, (70,70,70), (i*cell_size, j*cell_size, cell_size, cell_size))
            else:
                pygame.draw.rect(screen, (255, 196, 0), (i*cell_size, j*cell_size, cell_size, cell_size))

def draw_starting(pos):
    mx, my = pos
    mx, my = mx//cell_size, my//cell_size
    gameboard[mx][my] = 1

def draw_starting_erase(pos):
    mx, my = pos
    mx, my = mx//cell_size, my//cell_size
    gameboard[mx][my] = 0

def count_pop(pop, x, y):
    try:
        if gameboard[x][y] == 1:
            pop += 1
    except IndexError:
        pass
    return pop


def life_is_on(board):
    next = [0] * cells_x
    for i in range(cells_x):
        next[i] = [0] * cells_y
    if board == 0:
        return next
    # lets check population around cell:
    for x in range(cells_x):
        for y in range(cells_y):
            pop = 0
            pop = count_pop(pop, x-1, y-1)
            pop = count_pop(pop, x, y-1)
            pop = count_pop(pop, x+1, y-1)
            pop = count_pop(pop, x-1, y)
            pop = count_pop(pop, x+1, y)
            pop = count_pop(pop, x-1, y+1)
            pop = count_pop(pop, x, y+1)
            pop = count_pop(pop, x+1, y+1)
            # for life cells:
            if board[x][y] == 1:
                if pop == 2 or pop == 3:
                    next[x][y] = 1
            else:
                if pop == 3:
                    next[x][y] = 1
    return next

def run_game():

    life = False
    key_down = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    key_down = True
                if event.button == 3:
                    draw_starting_erase(event.pos)
            if event.type == pygame.MOUSEBUTTONUP:
                key_down = False
            if key_down:
                draw_starting(pygame.mouse.get_pos())
            if event.type == pygame.KEYDOWN:
                if event.key == 13 or event.key == 32:
                    life = True
                if event.key == 27:
                    life = False
                
        if life:
            global gameboard
            gameboard = life_is_on(gameboard)

        draw_gameboard()
        pygame.display.update()
        pygame.time.delay(40)


if __name__ == '__main__':
    run_game()