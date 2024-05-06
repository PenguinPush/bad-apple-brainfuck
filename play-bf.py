import brainfuck
import numpy
import time

fps = 30
video_frames_x4 = numpy.load("assets/video_frames_x4.npy")

for i in range(video_frames_x4.shape[0]):
    with open(f"bf/{i}.txt", "r") as file:
        print(file.read())
        # brainfuck.evaluate(file.read())
        time.sleep(1/fps)

