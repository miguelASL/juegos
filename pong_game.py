import pygame
import sys

# Constantes
WIDTH, HEIGHT = 600, 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BALL_RADIUS = 5
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 60
PADDLE_VELOCITY = 7

# Inicialización de Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game de Miguel Sarmiento")
clock = pygame.time.Clock()

# Función para resetear la posición del balón
def reset_ball():
    return WIDTH // 2, HEIGHT // 2, BALL_RADIUS, BALL_RADIUS

# Función para manejar la entrada del usuario
def handle_input(left_paddle_y, right_paddle_y):
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_w] and left_paddle_y > 0:
        left_paddle_y -= PADDLE_VELOCITY
    if keys[pygame.K_s] and left_paddle_y < HEIGHT - PADDLE_HEIGHT:
        left_paddle_y += PADDLE_VELOCITY
    if keys[pygame.K_UP] and right_paddle_y > 0:
        right_paddle_y -= PADDLE_VELOCITY
    if keys[pygame.K_DOWN] and right_paddle_y < HEIGHT - PADDLE_HEIGHT:
        right_paddle_y += PADDLE_VELOCITY
    
    return left_paddle_y, right_paddle_y

# Función principal del juego
def main():
    ball_x, ball_y, ball_vel_x, ball_vel_y = reset_ball()
    left_paddle_x, right_paddle_x = 10, WIDTH - 25
    left_paddle_y, right_paddle_y = HEIGHT // 2 - PADDLE_HEIGHT // 2, HEIGHT // 2 - PADDLE_HEIGHT // 2
    score_left, score_right = 0, 0

    font = pygame.font.Font("freesansbold.ttf", 32)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        left_paddle_y, right_paddle_y = handle_input(left_paddle_y, right_paddle_y)

        ball_x += ball_vel_x
        ball_y += ball_vel_y
        
        if(
            left_paddle_x < ball_x < left_paddle_x + PADDLE_WIDTH and
            left_paddle_y < ball_y < left_paddle_y + PADDLE_HEIGHT
        ) or (
            right_paddle_x < ball_x < right_paddle_x + PADDLE_WIDTH and
            right_paddle_y < ball_y < right_paddle_y + PADDLE_HEIGHT
        ):
            ball_vel_x = -ball_vel_x
            
        if ball_y <= 0 or ball_y >= HEIGHT:
            ball_vel_y = -ball_vel_y
            
        if ball_x <= 0:
            score_right += 1
            ball_x, ball_y, ball_vel_x, ball_vel_y = reset_ball()
            
        if ball_x >= WIDTH:
            score_left += 1
            ball_x, ball_y, ball_vel_x, ball_vel_y = reset_ball()
        
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, (left_paddle_x, left_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
        pygame.draw.rect(screen, WHITE, (right_paddle_x, right_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
        pygame.draw.ellipse(screen, WHITE, (int(ball_x) - 10, int(ball_y) - 10, 20, 20))
        score_display = font.render(f"{score_left} : {score_right}", True, WHITE)
        screen.blit(score_display, (WIDTH // 2 - 40, 10))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
