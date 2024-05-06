import ffmpeg
import numpy

source_video = "assets/bad apple.mp4"

probe = ffmpeg.probe(source_video)
video_info = next(s for s in probe["streams"] if s["codec_type"] == "video")

width = video_info["width"] * 2
height = video_info["height"]

print(width, height)

# width = 480
# height = 360


def process_frames(scale):
    video_frames = []

    process = (
        ffmpeg.input(source_video, r=30)
        .output('pipe:', format="rawvideo", pix_fmt="gray",
                vf=f"transpose=1, scale={height//scale}:{width//scale}:flags=lanczos:param0=1, setsar=1:1, hflip")
        .run_async(pipe_stdout=True)
    )

    while True:
        in_bytes = process.stdout.read(width // scale * height // scale)
        if not in_bytes:
            break
        frame_array = numpy.frombuffer(in_bytes, numpy.uint8).reshape(
            [width // scale, height // scale])
        video_frames.append(frame_array)

    process.wait()

    video_frames = numpy.array(video_frames)
    return video_frames


# ffmpeg.input(source_video).output("assets/video audio.wav", format="wav").run()

video_frames_x1 = process_frames(1)
video_frames_x2 = process_frames(2)
video_frames_x4 = process_frames(4)

print("Video converted to numpy array with shape:", video_frames_x1.shape)
print("Video converted to numpy array with shape:", video_frames_x2.shape)
print("Video converted to numpy array with shape:", video_frames_x4.shape)

numpy.save("assets/video_frames_x1.npy", video_frames_x1)
numpy.save("assets/video_frames_x2.npy", video_frames_x2)
numpy.save("assets/video_frames_x4.npy", video_frames_x4)
