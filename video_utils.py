import cv2
import os

def read_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []
    while True:
        ret,frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    return frames

def save_video(frames_video_frames, output_video_path):
    if not os.path.exists(os.path.dirname(output_video_path)):
        os.makedirs(os.path.dirname(output_video_path))

    # Use MP4V codec for better cross-platform compatibility
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(output_video_path, fourcc, 24.0, (frames_video_frames[0].shape[1], frames_video_frames[0].shape[0]))
    for frame in frames_video_frames:
        out.write(frame)
    out.release()

