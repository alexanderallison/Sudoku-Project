import pygame


class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = 0
        self.selected = False
        self.filled = None

    def cell_filled(self):  # to mark pre-filled cells
        if self.value != 0:
            self.filled = True

    def set_cell_value(self, value):  # set cell value
        if not self.filled:
            self.value = value

    def set_sketched_value(self, value):  # set cell sketched value
        if not self.filled:
            self.sketched_value = value

    def draw(self): # draws 1 specific cell, and its value
        cell_size = self.screen.get_width() // 9
        box_size = cell_size * 3
        if self.selected:
            pygame.draw.rect(self.screen, (169, 169, 169),
                             (self.col * cell_size, self.row * cell_size, cell_size, cell_size))
        else:
            pygame.draw.rect(self.screen, (255, 255, 255),
                             (self.col * cell_size, self.row * cell_size, cell_size, cell_size))
        font = pygame.font.Font(None, 36)
        value = str(self.value) if self.value != 0 else ''
        text = font.render(value, True, (0, 0, 0))
        rect_text = text.get_rect(center=((self.col * cell_size) + (cell_size // 2),
                                          (self.row * cell_size) + (cell_size // 2)))
        self.screen.blit(text, rect_text)

        if self.sketched_value != 0:  # if cell is nonzero display its value
            sketch_font = pygame.font.Font(None, 18)
            sketched_text = sketch_font.render(str(self.sketched_value), True, (0, 0, 0))
            sketched_rect = sketched_text.get_rect(topleft=(self.col * cell_size + 5, self.row * cell_size + 5))
            self.screen.blit(sketched_text, sketched_rect)
        pygame.draw.rect(self.screen, (0, 0, 0), (self.col * cell_size, self.row * cell_size, cell_size, cell_size),
                             1)
        pygame.draw.rect(self.screen, (0, 0, 0), (self.col // 3 * box_size, self.row // 3 * box_size, box_size,
                                                  box_size), 3)

       # if self.selected:  # if cell is selected outline cell red
        #    pygame.draw.rect(self.screen, (220, 20, 60), (cell_size, cell_size,
           #                                               cell_size, cell_size), 3)


