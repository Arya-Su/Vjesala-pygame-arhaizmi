import pygame
import math
import random

# Izgled displeja
pygame.init()
WIDTH, HEIGHT = 1000, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Igra vjesala")


# BiH
bosnian_alphabet = ['A', 'B', 'C', 'Č', 'Ć', 'D', 'Dž', 'Đ', 'E', 'F', 'G', 'H', 'I',
                    'J', 'K', 'L', 'Lj', 'M', 'N', 'Nj', 'O', 'P', 'R', 'S', 'Š', 'T', 'U', 'V', 'Z', 'Ž']

# Slova
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 15) / 2)
starty = 400
A = 65
for i, letter in enumerate(bosnian_alphabet):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 15))
    y = starty + ((i // 15) * (GAP + RADIUS * 2))
    letters.append([x, y, letter, True])

# Slike
images = []
for i in range(7):
    image = pygame.image.load_extended("hangman" + str(i) + ".png")
    images.append(image)
print(images)

# Font
LETTER_FONT = pygame.font.SysFont('timesnewroman', 20)
WORD_FONT = pygame.font.SysFont('timesnewroman', 30)
TITLE_FONT = pygame.font.SysFont('timesnewroman', 40)


# Promjenjive
hangman_status = 0
words = ["MINDER", "HEPEK", "HRKLJUŠ", "ĆENIFA", "AŠIKOVATI", "POĐAHKAD", "BESTILJ",
         "VAZDA", "ĆEPENEK", "HEJBET", "DIREK", "HASTA", "HASTAHANA", "JAPIJA", "HEĆIM", "ŠAMIJA"]
word = random.choice(words)
guessed = []


# Boje
SARENO = (255, 255, 255)  # bijela
BLACK = (0, 0, 0)
ROZA = (205, 16, 118)

# Igra
FPS = 60
clock = pygame.time.Clock()
run = True


def draw():
    win.fill(SARENO)
    text = TITLE_FONT.render("ARHAIZMI", 1, ROZA)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 10))


# Rijeci
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (400, 200))


# Crtanje slova
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 4)
            text = LETTER_FONT.render(ltr, 1, ROZA)
            win.blit(text, (x-text.get_width()/2, y-text.get_height()/2))

    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()


def display_message(message):
    pygame.time.delay(1000)
    win.fill(SARENO)
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (WIDTH/2-text.get_width() /
             2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)


while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                    dis = math.sqrt((x - m_x)**2 + (y-m_y)**2)
                    if dis < RADIUS:
                        letter[3] = False
                        guessed.append(ltr)
                        if ltr not in word:
                            hangman_status += 1

    draw()

    won = True
    for letter in word:
        if letter not in guessed:
            won = False
            break
    if won:
        display_message("POBJEDILI STE")
        break

    if hangman_status == 6:
        display_message(
            "IZGUBILI STE :(  Riječ koju niste pogodili je: " + word)
        break

pygame.quit()
