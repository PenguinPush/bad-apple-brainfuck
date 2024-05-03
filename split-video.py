import ffmpeg
import numpy as np

source_video = 'assets/bad apple.mp4'
video_frames = []

probe = ffmpeg.probe(source_video)
video_info = next(s for s in probe['streams'] if s['codec_type'] == 'video')

width = video_info['width']
height = video_info['height']

process = (
    ffmpeg.input(source_video, r=30)
    .output('pipe:', format='rawvideo', pix_fmt='gray', vf='transpose=2')
    .run_async(pipe_stdout=True)
)

while True:
    in_bytes = process.stdout.read(width * height)
    if not in_bytes:
        break
    frame_array = np.frombuffer(in_bytes, np.uint8).reshape([width, height])
    video_frames.append(frame_array)

process.wait()

video_frames = np.array(video_frames)
ffmpeg.input(source_video).output("assets/video_audio.wav", format='wav').run()

print("Video converted to numpy array with shape:", video_frames.shape)
np.save("assets/video_frames.npy", video_frames)
