import pygame
import random

# Inicializando o Pygame
pygame.init()

# Configurações da tela
screen_width = 400
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird Fictício")

# Definindo as cores
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 255)
  
# Configurações do jogo
bird_width = 40
bird_height = 30
bird_x = 50
bird_y = screen_height // 2
bird_velocity = 0
gravity = 0.5
jump = -10

pipe_width = 70
pipe_gap = 200
pipe_velocity = 3
pipe_frequency = 1500  # em milissegundos

# Inicializando o relógio
clock = pygame.time.Clock()

# Função para desenhar o pássaro
def draw_bird(x, y):
    pygame.draw.rect(screen, blue, [x, y, bird_width, bird_height])

# Função para criar e gerenciar os canos
def create_pipe():
    height = random.randint(150, 450)
    pipe = {'x': screen_width, 'height': height}
    return pipe

def draw_pipes(pipes):
    for pipe in pipes:
        pygame.draw.rect(screen, green, [pipe['x'], 0, pipe_width, pipe['height']])
        pygame.draw.rect(screen, green, [pipe['x'], pipe['height'] + pipe_gap, pipe_width, screen_height])

# Função para verificar colisão
def check_collision(pipes, bird_y):
    for pipe in pipes:
        if pipe['x'] < bird_x + bird_width and pipe['x'] + pipe_width > bird_x:
            if bird_y < pipe['height'] or bird_y + bird_height > pipe['height'] + pipe_gap:
                return True
    if bird_y < 0 or bird_y > screen_height:
        return True
    return False

# Inicializando variáveis do jogo
running = True
pipes = []
last_pipe = pygame.time.get_ticks() - pipe_frequency
score = 0

# Loop principal do jogo
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = jump

    # Atualizando a posição do pássaro
    bird_velocity += gravity
    bird_y += bird_velocity

    # Gerenciando os canos
    time_now = pygame.time.get_ticks()
    if time_now - last_pipe > pipe_frequency:
        pipes.append(create_pipe())
        last_pipe = time_now

    for pipe in pipes:
        pipe['x'] -= pipe_velocity

    # Removendo canos fora da tela
    pipes = [pipe for pipe in pipes if pipe['x'] + pipe_width > 0]

    # Verificando colisão
    if check_collision(pipes, bird_y):
        running = False

    # Atualizando a tela
    screen.fill(white)
    draw_bird(bird_x, bird_y)
    draw_pipes(pipes)

    # Atualizando o display e controlando o FPS
    pygame.display.update()
    clock.tick(60)

pygame.quit()