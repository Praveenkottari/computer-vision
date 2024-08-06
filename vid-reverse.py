import cv2

vid = cv2.VideoCapture('sample.mp4')

num_frame = vid.get(cv2.CAP_PROP_FRAME_COUNT)
fps = vid.get(cv2.CAP_PROP_FRAME_COUNT)

#height and width
height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('reversed.mp4', fourcc, fps , (int(0.5* width), int(height* 0.5)))

print("number of frames are: {}".format(num_frame))
print("number of fps: {}".format(fps))

frame_idx = num_frame-1

if (vid.isOpened()):
    #readaing the video

    while(frame_idx!=0):
        vid.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
        ret, frame =  vid.read()

        frame = cv2.resize(frame,(int(width * 0.5), int(height*0.5)))

        out.write(frame)

        frame_idx = frame_idx-1

        if (frame_idx% 100 == 0):
            print(frame_idx)

out.release()
vid.release()
cv2.destroyAllWindows()