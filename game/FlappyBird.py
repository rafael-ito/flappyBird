import pygame
import neat

from entities.Background import Background
from entities.Bird import Bird
from entities.Floor import Floor
from entities.Pipe import Pipe

AI_PLAYING = True
GENERATION = 0

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

    if AI_PLAYING:
        text = FONT_SCORE.render(f"Gen: {GENERATION}", 1, (255, 255, 255))
        screen.blit(text, (10, 10))

    floor.draw(screen)
    pygame.display.update()


def main(genomes, config):
    global GENERATION
    GENERATION += 1

    if AI_PLAYING:
        networks = []
        genomes_list = []
        birds = []
        for _, genome in genomes:
            network = neat.nn.FeedForwardNetwork.create(genome, config)
            networks.append(network)
            genome.fitness = 0
            genomes_list.append(genome)
            birds.append(Bird(230, 350))
    else:
        birds = [Bird(230, 350)]

    background = Background()
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
                pygame.quit()
                quit()
            if not AI_PLAYING and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    for bird in birds:
                        bird.jump()

        index_pipe = 0
        if len(birds) < 1:
            running = False
            break

        if len(pipes) > 1 and birds[0].x > (pipes[0].x + pipes[0].pipe_top.get_width()):
            index_pipe = 1

        for i, bird in enumerate(birds):
            bird.move()
            if AI_PLAYING:
                genomes_list[i].fitness += 0.1
                output = networks[i].activate((bird.y, abs(bird.y - pipes[index_pipe].height), abs(bird.y - pipes[index_pipe].pos_bottom)))
                if output[0] > 0.5:
                    bird.jump()

        background.move()
        floor.move()

        add_pipe = False
        for pipe in pipes:
            for i, bird in enumerate(birds):
                if pipe.collide(bird):
                    birds.pop(i)
                    if AI_PLAYING:
                        genomes_list[i].fitness -= 1
                        genomes_list.pop(i)
                        networks.pop(i)
                if not pipe.passed and bird.x > pipe.x:
                    pipe.passed = True
                    add_pipe = True

            pipe.move()
            if pipe.x + pipe.pipe_top.get_width() < 0:
                pipes.remove(pipe)

        if add_pipe:
            score += 1
            pipes.append(Pipe(600))
            if AI_PLAYING:
                for genome in genomes_list:
                    genome.fitness += 5

        for i, bird in enumerate(birds):
            if (bird.y + bird.image.get_height() > floor.y) or (bird.y < 0):
                birds.pop(i)
                if AI_PLAYING:
                    genomes_list[i].fitness -= 1
                    genomes_list.pop(i)
                    networks.pop(i)

        draw_screen(screen, background, birds, pipes, floor, score)

    print(score)


def run(path_ai_config):
    if AI_PLAYING:
        config = neat.config.Config(neat.DefaultGenome,
                                    neat.DefaultReproduction,
                                    neat.DefaultSpeciesSet,
                                    neat.DefaultStagnation,
                                    path_ai_config)

        population = neat.Population(config)
        population.add_reporter(neat.StdOutReporter(True))
        population.add_reporter(neat.StatisticsReporter())
        population.run(main, 50)
    else:
        main(None, None)


if __name__ == '__main__':
    run('config.txt')
