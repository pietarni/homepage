import cv2
import os

def extract_frames(video_path, output_dir, num_frames=3):
    if not os.path.exists(video_path):
        print(f"Error: Video file not found at {video_path}")
        return

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    duration = total_frames / fps
    
    print(f"Video duration: {duration} seconds, Total frames: {total_frames}")

    # Extract frames at 25%, 50%, and 75% of the video
    percentages = [0.25, 0.50, 0.75, 0.90]
    
    # Only extract as many as requested (up to 4 in this list)
    targets = percentages[:num_frames]

    for i, p in enumerate(targets):
        frame_no = int(total_frames * p)
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_no)
        ret, frame = cap.read()
        
        if ret:
            output_path = os.path.join(output_dir, f"helsinki_shot_{i+1}.webp")
            # Save as WebP, quality 85
            cv2.imwrite(output_path, frame, [cv2.IMWRITE_WEBP_QUALITY, 85])
            print(f"Saved {output_path}")
        else:
            print(f"Failed to extract frame at {p*100}%")

    cap.release()

if __name__ == "__main__":
    base_dir = r"c:\Users\pieta\Documents\GitHub\homepage"
    video_path = os.path.join(base_dir, "assets", "gfx", "bgvid.mp4")
    output_dir = os.path.join(base_dir, "assets", "gfx")
    extract_frames(video_path, output_dir, num_frames=3)
