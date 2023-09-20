import pygame
from pygame.locals import *
from sys import exit
import datetime

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Aplicación de Dibujo")

# Definir colores
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)  # Azul
border_radius = 15  # Radio para esquinas redondeadas

# Variables para el dibujo
drawing = False
last_pos = None

# Área de dibujo (ajustar coordenadas y tamaño según tus necesidades)
drawing_area_x = 10
drawing_area_y = 60
drawing_area_width = 480
drawing_area_height = 430
drawing_area = None

# Área para el botón de "Borrar"
button_rect_clear = pygame.Rect(10, 10, 100, 40)

# Área para el botón de "Guardar"
button_rect_save = pygame.Rect(120, 10, 100, 40)

# Crear una fuente de texto
font = pygame.font.Font(None, 36)

# Texto para el botón de "Borrar"
text_surface_clear = font.render("Borrar", True, white)  # Crear la superficie de texto

# Texto para el botón de "Guardar"
text_surface_save = font.render("Guardar", True, white)  # Crear la superficie de texto

# Lista para almacenar los trazos
drawing_list = []  # Definir la lista de dibujos

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == MOUSEBUTTONDOWN:
            if button_rect_clear.collidepoint(event.pos):  # Verificar si se hizo clic en el botón de "Borrar"
                drawing_list = []  # Borrar todos los dibujos
            elif button_rect_save.collidepoint(event.pos):  # Verificar si se hizo clic en el botón de "Guardar"
                # Obtener la fecha y hora actual como parte del nombre del archivo
                now = datetime.datetime.now()
                date_time_str = now.strftime("%Y%m%d%H%M%S")
                file_name = f"src/images/drawing_{date_time_str}.png"
                pygame.image.save(drawing_area, file_name)  # Guardar el dibujo como una imagen
                print(f"Dibujo guardado como {file_name}")
            else:
                drawing = True
                last_pos = event.pos
        elif event.type == MOUSEMOTION:
            if drawing:
                drawing_list.append(event.pos)  # Agregar el trazo a la lista
                last_pos = event.pos
        elif event.type == MOUSEBUTTONUP:
            drawing = False

    # Limpiar la pantalla
    screen.fill(white)

    # Dibujar el marco alrededor del área de dibujo
    pygame.draw.rect(screen, black, (drawing_area_x - 2, drawing_area_y - 2, drawing_area_width + 4, drawing_area_height + 4), 2)

    # Capturar el área de dibujo
    drawing_area = screen.subsurface(pygame.Rect(drawing_area_x, drawing_area_y, drawing_area_width, drawing_area_height))

    # Dibujar todos los trazos
    for line in drawing_list:
        start_x, start_y = line[0] - drawing_area_x, line[1] - drawing_area_y
        pygame.draw.circle(drawing_area, black, (start_x, start_y), 15)

    # Dibujar el botón de "Borrar" con curvas suaves
    pygame.draw.rect(screen, blue, button_rect_clear, border_radius=border_radius)  # Relleno azul con esquinas redondeadas
    pygame.draw.rect(screen, black, button_rect_clear, 3, border_radius=border_radius)  # Contorno negro con esquinas redondeadas

    # Dibujar el botón de "Guardar" con curvas suaves
    pygame.draw.rect(screen, blue, button_rect_save, border_radius=border_radius)  # Relleno azul con esquinas redondeadas
    pygame.draw.rect(screen, black, button_rect_save, 3, border_radius=border_radius)  # Contorno negro con esquinas redondeadas

    # Posicionar el texto en el botón de "Borrar"
    text_rect_clear = text_surface_clear.get_rect(center=button_rect_clear.center)

    # Posicionar el texto en el botón de "Guardar"
    text_rect_save = text_surface_save.get_rect(center=button_rect_save.center)

    # Dibujar el texto en los botones
    screen.blit(text_surface_clear, text_rect_clear)
    screen.blit(text_surface_save, text_rect_save)

    # Actualizar la pantalla
    pygame.display.update()
