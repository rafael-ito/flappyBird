import pygame

from entities.Background import Background
from entities.Bird import Bird
from entities.Floor import Floor
from entities.Pipe import Pipe

WIDTH_SCREEN = 500
HEIGHT_SCREEN = 800

pygame.font.init()
FONT_SCORE = pygame.font.SysFont('arial', 50)


def draw_screen(screen, background, birds, pipes, floor, score):
    background.draw(screen)
    for bird in birds:
        bird.draw(screen)
    for pipe in pipes:
        pipe.draw(screen)

    text = FONT_SCORE.render(f"Score: {score}", 1, (255, 255, 255))
    screen.blit(text, (WIDTH_SCREEN - 10 - text.get_width(), 10))
    floor.draw(screen)
    pygame.display.update()


def main():
    background = Background()
    birds = [Bird(230, 350)]
    floor = Floor(730)
    pipes = [Pipe(700)]
    screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
    score = 0
    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    for bird in birds:
                        bird.jump()

        for bird in birds:
            bird.move()

        background.move()
        floor.move()

        add_pipe = False
        for pipe in pipes:
            for i, bird in enumerate(birds):
                if pipe.collide(bird):
                    birds.pop(i)
                if not pipe.passed and bird.x > pipe.x:
                    pipe.passed = True
                    add_pipe = True

            pipe.move()
            if pipe.x + pipe.pipe_top.get_width() < 0:
                pipes.remove(pipe)

        if add_pipe:
            score += 1
            pipes.append(Pipe(600))

        for i, bird in enumerate(birds):
            if (bird.y + bird.image.get_height() > floor.y) or (bird.y < 0):
                birds.pop(i)

        draw_screen(screen, background, birds, pipes, floor, score)

        if len(birds) < 1:
            running = False

    print(score)
    pygame.quit()
    quit()


if __name__ == '__main__':
    main()
