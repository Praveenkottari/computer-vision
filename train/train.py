import cv2
import os

def extract_images_from_video(video_path, output_dir, frame_rate=0.0):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    video_capture = cv2.VideoCapture(video_path)
    
    if not video_capture.isOpened():
        print("Error: Could not open video.")
        return

    frame_count = 0
    saved_count = 0

    while True:
        success, frame = video_capture.read()
        
        if not success:
            break
        
        if frame_count % frame_rate == 0:
            image_filename = os.path.join(output_dir, f"frame_{saved_count:04d}.jpg")
            cv2.imwrite(image_filename, frame)
            saved_count += 1
        
        frame_count += 1
    video_capture.release()
    print(f"Extracted {saved_count} images from the video.")

video_file_path = 'train.mp4'  # Replace with your video file path
output_directory = 'images'     # Replace with your desired output directory
extract_images_from_video(video_file_path, output_directory, frame_rate=5)  # Change frame_rate as needed
