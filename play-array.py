import numpy
import pygame

video_frames = numpy.load("assets/video_frames_x1.npy")
video_frames = numpy.repeat(video_frames[:, :, :, numpy.newaxis], 3, axis=3)

pygame.mixer.init()
pygame.mixer.music.load("assets/video audio.wav")

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

    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.play()

    surface = pygame.surfarray.make_surface(video_frames[i])

    screen.blit(surface, (0, 0))
    pygame.display.flip()

    i += 1
    if i >= video_frames.shape[0]:
        i = 0