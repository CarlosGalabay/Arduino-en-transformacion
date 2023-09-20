import pygame

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mi Aplicación Pygame")

# Definir colores
white = (255, 255, 255)

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Lógica del juego (aquí, no hay lógica adicional)

    # Limpiar la pantalla
    screen.fill(white)

    # Dibujar objetos (en este caso, no se dibuja nada)

    # Actualizar la pantalla
    pygame.display.update()

# Salir de Pygame
pygame.quit()
