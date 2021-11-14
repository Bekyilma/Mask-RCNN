import pixellib
from pixellib.instance import instance_segmentation
import cv2



def main():
    segmentation_model = instance_segmentation()
    segmentation_model.load_model('mask_rcnn_coco.h5')

    capture = cv2.VideoCapture("/users/path-to_file")
    while capture.isOpened():
        ret, frame = capture.read()

        # Apply instance segmentation
        res = segmentation_model.segmentFrame(frame, show_bboxes=True)
        image = res[1]

        cv2.imshow('Instance Segmentation', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()




if __name__ == '__main__':
    main()