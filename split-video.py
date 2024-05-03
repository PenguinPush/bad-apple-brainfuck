import ffmpeg
import numpy as np

source_video = 'assets/bad apple.mp4'
video_frames = []
video_frames_lowres = []

probe = ffmpeg.probe(source_video)
video_info = next(s for s in probe['streams'] if s['codec_type'] == 'video')

width = video_info['width']
height = video_info['height']

process = (
    ffmpeg.input(source_video, r=30)
    .output('pipe:', format='rawvideo', pix_fmt='gray', vf='transpose=2')
    .run_async(pipe_stdout=True)
)

process_lowres = (
    ffmpeg.input(source_video, r=30)
    .output('pipe:', format='rawvideo', pix_fmt='gray', vf='transpose=2, scale=iw/4:ih/4')
    .run_async(pipe_stdout=True)
)

while True:
    in_bytes = process.stdout.read(width * height)
    if not in_bytes:
        break
    frame_array = np.frombuffer(in_bytes, np.uint8).reshape([width, height])
    video_frames.append(frame_array)

while True:
    in_bytes = process_lowres.stdout.read(width//4 * height//4)
    if not in_bytes:
        break
    frame_array_lowres = np.frombuffer(in_bytes, np.uint8).reshape([width//4, height//4])
    video_frames_lowres.append(frame_array_lowres)

process.wait()

video_frames = np.array(video_frames)
video_frames_lowres = np.array(video_frames_lowres)
ffmpeg.input(source_video).output("assets/video_audio.wav", format='wav').run()

print("Video converted to numpy array with shape:", video_frames.shape)
print("Video converted to numpy array with shape:", video_frames_lowres.shape)

np.save("assets/video_frames.npy", video_frames)
np.save("assets/video_frames_lowres.npy", video_frames_lowres)
