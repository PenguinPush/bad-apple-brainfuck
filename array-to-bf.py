import numpy as np

video_frames = np.load("assets/video_frames_lowres.npy")
threshold = 128

print(video_frames.shape)

for i in range(video_frames.shape[0]):
    bf = ""

    for j in range(video_frames.shape[1]):
        for k in range(video_frames.shape[2]):
            if video_frames[i][j][k] > threshold:
                bf += "+>"
            else:
                bf += ">"

    print(i, video_frames[i].shape)

    with open(f"bf/{i}.txt", "w") as file:
        file.write(bf)

print("finished")