import numpy

video_frames_x2 = numpy.load("assets/video_frames_x2.npy")
video_frames_x4 = numpy.load("assets/video_frames_x4.npy")
threshold = 128

for i in range(video_frames_x4.shape[0]):
    bf = "--------------------------------->"
    shaped = ""
    bf_shaped = ""
    shape_index = 0
    l = 0

    for k in range(video_frames_x4.shape[2]):
        for j in range(video_frames_x4.shape[1]):
            if video_frames_x4[i][j][k] > threshold + 42:
                bf += "+++>"
            elif video_frames_x4[i][j][k] > threshold - 42:
                bf += "+>"
            else:
                bf += ">"

            if j == video_frames_x4.shape[1] - 1 or j == video_frames_x4.shape[1] // 2 - 1:
                bf += "---------------------->"

    bf += "+[<+++++++++++++++++++++++++++++++++]>[-.>]"

    l = 0
    for k in range(video_frames_x2.shape[2]):
        for j in range(video_frames_x2.shape[1]):
            if video_frames_x2[i][j][k] > threshold + 84:
                shaped += "#"
            elif video_frames_x2[i][j][k] > threshold - 84:
                if j % 2 == k % 2:
                    shaped += " "
                else:
                    shaped += "#"
            else:
                shaped += " "

            if k == video_frames_x2.shape[1] - 1 or k == video_frames_x2.shape[1]//2 - 1:
                shaped += "\n"

    l = 0
    for j in range(len(shaped)):
        if shape_index >= len(bf):
            bf_shaped += "#"
        else:
            if shaped[j] == " ":
                bf_shaped += " "
            elif shaped[j] == "#":
                bf_shaped += bf[shape_index]
                shape_index += 1
            if (j + 1) % video_frames_x2.shape[1] == 0:
                bf_shaped += "\n"

    if shape_index < len(bf):
        bf_shaped += "\n" + bf[shape_index:-1] + bf[-1]

    print(i, video_frames_x4[i].shape)
    # print(shaped)

    with open(f"bf/{i}.txt", "w") as file:
        file.write(bf_shaped)

print("finished")
