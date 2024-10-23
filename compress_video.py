import os
from moviepy import VideoFileClip

def compress_video(input_path, output_path):
    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found")
        return

    clip = VideoFileClip(input_path)

    # Get original properties
    original_size = os.path.getsize(input_path) / (1024 * 1024)  # MB
    duration = clip.duration
    fps = clip.fps
    size = clip.size

    print(f"Original: {original_size:.1f}MB, {duration:.1f}s, {size}, {fps}fps")

    # Resize if too big
    if size[0] > 1920:
        clip = clip.resize(width=1920)

    # Reasonable bitrate for background video
    clip.write_videofile(
        output_path,
        bitrate="800k",
        audio_bitrate="128k",
        codec="libx264",
        preset="medium",
        fps=fps,
    )

    new_size = os.path.getsize(output_path) / (1024 * 1024)
    print(f"Compressed: {new_size:.1f}MB")


if __name__ == "__main__":
    base_dir = r"c:\Users\pieta\Documents\GitHub\homepage"
    input_path = os.path.join(base_dir, "assets", "gfx", "bgvid.mp4")
    output_path = os.path.join(base_dir, "assets", "gfx", "bgvid_compressed.mp4")
    compress_video(input_path, output_path)
