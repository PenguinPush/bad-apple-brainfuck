import numpy as np
import pygame

video_frames = np.load("assets/video_frames.npy")
video_frames = np.repeat(video_frames[:, :, :, np.newaxis], 3, axis=3)

pygame.init()
screen = pygame.display.set_mode((480, 360))
clock = pygame.time.Clock()


running = True
i = 0

while running:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    surface = pygame.surfarray.make_surface(video_frames[i])

    screen.blit(surface, (0, 0))
    pygame.display.flip()

    i += 1
    if i >= video_frames.shape[0]:
        i = 0