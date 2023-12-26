import pygame

pygame.init()
screen = pygame.display.set_mode((810, 950))
clock = pygame.time.Clock()

color_active = pygame.Color((63, 63, 63))
color_passive = pygame.Color((26, 26, 26))
font = pygame.font.Font(None, 90)
font_buttons = pygame.font.Font(None, 60)
user_text = ""

rect = pygame.Rect(0, 0, 90, 90)

square_list = []
button_list = []


def draw_lines():
    pygame.draw.line(screen, 'white', [0, 810], [810, 810], 7)
    pygame.draw.lines(screen, 'white', False, [[270, 0], [270, 810], [540, 810], [540, 0]], 7)
    pygame.draw.line(screen, 'white', [0, 270], [810, 270], 7)
    pygame.draw.line(screen, 'white', [0, 540], [810, 540], 7)

    pygame.draw.line(screen, 'white', [90, 0], [90, 810], 1)
    pygame.draw.line(screen, 'white', [180, 0], [180, 810], 1)
    pygame.draw.line(screen, 'white', [360, 0], [360, 810], 1)
    pygame.draw.line(screen, 'white', [450, 0], [450, 810], 1)
    pygame.draw.line(screen, 'white', [630, 0], [630, 810], 1)
    pygame.draw.line(screen, 'white', [720, 0], [720, 810], 1)

    pygame.draw.line(screen, 'white', [0, 90], [810, 90], 2)
    pygame.draw.line(screen, 'white', [0, 180], [810, 180], 2)
    pygame.draw.line(screen, 'white', [0, 360], [810, 360], 2)
    pygame.draw.line(screen, 'white', [0, 450], [810, 450], 2)
    pygame.draw.line(screen, 'white', [0, 630], [810, 630], 2)
    pygame.draw.line(screen, 'white', [0, 720], [810, 720], 2)


def initialize_squares():
    if True:
        square11 = Square(0, 0, 90, 90)
        square12 = Square(90, 0, 90, 90)
        square13 = Square(180, 0, 90, 90)
        square14 = Square(270, 0, 90, 90)
        square15 = Square(360, 0, 90, 90)
        square16 = Square(450, 0, 90, 90)
        square17 = Square(540, 0, 90, 90)
        square18 = Square(630, 0, 90, 90)
        square19 = Square(720, 0, 90, 90)
        square21 = Square(0, 90, 90, 90)
        square22 = Square(90, 90, 90, 90)
        square23 = Square(180, 90, 90, 90)
        square24 = Square(270, 90, 90, 90)
        square25 = Square(360, 90, 90, 90)
        square26 = Square(450, 90, 90, 90)
        square27 = Square(540, 90, 90, 90)
        square28 = Square(630, 90, 90, 90)
        square29 = Square(720, 90, 90, 90)
        square31 = Square(0, 180, 90, 90)
        square32 = Square(90, 180, 90, 90)
        square33 = Square(180, 180, 90, 90)
        square34 = Square(270, 180, 90, 90)
        square35 = Square(360, 180, 90, 90)
        square36 = Square(450, 180, 90, 90)
        square37 = Square(540, 180, 90, 90)
        square38 = Square(630, 180, 90, 90)
        square39 = Square(720, 180, 90, 90)
        square41 = Square(0, 270, 90, 90)
        square42 = Square(90, 270, 90, 90)
        square43 = Square(180, 270, 90, 90)
        square44 = Square(270, 270, 90, 90)
        square45 = Square(360, 270, 90, 90)
        square46 = Square(450, 270, 90, 90)
        square47 = Square(540, 270, 90, 90)
        square48 = Square(630, 270, 90, 90)
        square49 = Square(720, 270, 90, 90)
        square51 = Square(0, 360, 90, 90)
        square52 = Square(90, 360, 90, 90)
        square53 = Square(180, 360, 90, 90)
        square54 = Square(270, 360, 90, 90)
        square55 = Square(360, 360, 90, 90)
        square56 = Square(450, 360, 90, 90)
        square57 = Square(540, 360, 90, 90)
        square58 = Square(630, 360, 90, 90)
        square59 = Square(720, 360, 90, 90)
        square61 = Square(0, 450, 90, 90)
        square62 = Square(90, 450, 90, 90)
        square63 = Square(180, 450, 90, 90)
        square64 = Square(270, 450, 90, 90)
        square65 = Square(360, 450, 90, 90)
        square66 = Square(450, 450, 90, 90)
        square67 = Square(540, 450, 90, 90)
        square68 = Square(630, 450, 90, 90)
        square69 = Square(720, 450, 90, 90)
        square71 = Square(0, 540, 90, 90)
        square72 = Square(90, 540, 90, 90)
        square73 = Square(180, 540, 90, 90)
        square74 = Square(270, 540, 90, 90)
        square75 = Square(360, 540, 90, 90)
        square76 = Square(450, 540, 90, 90)
        square77 = Square(540, 540, 90, 90)
        square78 = Square(630, 540, 90, 90)
        square79 = Square(720, 540, 90, 90)
        square81 = Square(0, 630, 90, 90)
        square82 = Square(90, 630, 90, 90)
        square83 = Square(180, 630, 90, 90)
        square84 = Square(270, 630, 90, 90)
        square85 = Square(360, 630, 90, 90)
        square86 = Square(450, 630, 90, 90)
        square87 = Square(540, 630, 90, 90)
        square88 = Square(630, 630, 90, 90)
        square89 = Square(720, 630, 90, 90)
        square91 = Square(0, 720, 90, 90)
        square92 = Square(90, 720, 90, 90)
        square93 = Square(180, 720, 90, 90)
        square94 = Square(270, 720, 90, 90)
        square95 = Square(360, 720, 90, 90)
        square96 = Square(450, 720, 90, 90)
        square97 = Square(540, 720, 90, 90)
        square98 = Square(630, 720, 90, 90)
        square99 = Square(720, 720, 90, 90)


def initialize_buttons():
    solve_button = Button(315, 840, 180, 60, 'Solve', False, solve_sukodu)
    reset_button = Button(45, 840, 180, 60, 'Reset', False, reset)
    quit_button = Button(585, 840, 180, 60, 'Quit', False, quit)


def print_grid():
    for row in range(9):
        for col in range(9):
            print(grid[row][col], end=' ')
        print()


def find_empty_square(rc):
    for row in range(9):
        for col in range(9):
            if (grid[row][col] == 0):
                rc[0] = row
                rc[1] = col
                return True
    return False


def used_in_row(row, number):
    nr = 0
    for col in range(9):
        if grid[row][col] == number:
            nr += 1
    return nr


def used_in_col(col, number):
    nr = 0
    for row in range(9):
        if grid[row][col] == number:
            nr += 1
    return nr


def used_in_box(row, col, number):
    nr = 0
    for x in range(3):
        for y in range(3):
            if grid[x + row][y + col] == number:
                nr += 1
    return nr


def verify_safe_square(row, col, number):
    return (not used_in_row(row, number) and
            (not used_in_col(col, number) and
             (not used_in_box(row - row % 3, col - col % 3, number))))


def valid_sudoku():
    for row in range(9):
        for col in range(9):
            if grid[row][col]:
                if used_in_box(row - row % 3, col - col % 3, grid[row][col]) > 1 or \
                        used_in_row(row, grid[row][col]) > 1 or \
                        used_in_col(col, grid[row][col]) > 1:
                    return False
    return True


def solve():
    rc = [0, 0]
    if not find_empty_square(rc):
        return True

    row = rc[0]
    col = rc[1]

    for number in range(1, 10):
        if verify_safe_square(row, col, number):

            grid[row][col] = number
            if solve():
                return True

            grid[row][col] = 0
    return False


grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]


def solve_sukodu():
    i, j = 0, 0
    for square in square_list:
        if len(square.text):
            grid[i][j] = int(square.text)
        j += 1
        if j > 8:
            j = 0
            i += 1
    if valid_sudoku():
        if solve():
            return True
        else:
            return False
    else:
        return False


def reset():
    i, j = 0, 0
    for square in square_list:
        grid[i][j] = 0
        j += 1
        if j > 8:
            j = 0
            i += 1
        square.text = ''
        square.text_surface = font.render(square.text, True, 'white')

def quit():
    pygame.quit()
    exit()


class Button:
    def __init__(self, x, y, w, h, text, start=False, function=None):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.function = function
        self.start = start
        self.colors = {
            'normal': 'white',
            'hover': 'black'
        }
        self.button_surface = font.render(text, True, 'white')
        button_list.append(self)

    def process(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.start = self.function()

    def draw(self, screen):
         pygame.draw.rect(screen, self.colors['normal'], self.rect)
         self.button_surface = font_buttons.render(self.text, True, (63, 63, 63))
         screen.blit(self.button_surface, (self.rect.x + 35, self.rect.y + 10))


class Square:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = pygame.Color(color_passive)
        self.text = text
        self.text_surface = font.render(text, True, self.color)
        self.active = False
        square_list.append(self)

    def handle_event(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = color_active if self.active else color_passive

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif event.key == pygame.K_RIGHT:
                    self.skip = 1
                else:
                    if '1' <= event.unicode <= '9':
                        self.text = event.unicode


                self.text_surface = font.render(self.text, True, 'white')

    def update(self):
        width = max(90, self.text_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.text_surface, (self.rect.x + 29, self.rect.y + 20))


def main():
    initialize_squares()
    initialize_buttons()
    running = True

    start = False
    counter = 0
    i, j = 0, 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            for square in square_list:
                square.handle_event(event)

            for button in button_list:
                button.process(event)
                if button.start:
                    start = button.start
        if start:
            if not len(square_list[counter].text):
                square_list[counter].text = str(grid[i][j])
                square_list[counter].text_surface = font.render(square_list[counter].text, True, '#7A4988')

            counter += 1
            j += 1
            if j > 8:
                j = 0
                i += 1
            if counter > 80:
                start = False
                for button in button_list:
                    button.start = False
                counter, i, j = 0, 0, 0

        for square in square_list:
            square.update()

        screen.fill((26, 26, 26))

        for square in square_list:
            square.draw(screen)

        for button in button_list:
            button.draw(screen)

        draw_lines()

        clock.tick(30)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
