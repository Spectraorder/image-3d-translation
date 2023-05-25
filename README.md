# image-3d-translation
<<<<<<< HEAD
3D photo translation development
=======
## OpenCV Image Recognition

### Packages

[`opencv-python`](https://pypi.org/project/opencv-python/)

[`numpy`](https://pypi.org/project/numpy/)

### Foundamental

**Note that the use of trained model of [YOLO: Real-Time Object Detection](https://pjreddie.com/darknet/yolo/) is begin used in this program and the `yolov3.weights` file need to be put under the `model` folder**

You may download the `.weight` file [here](https://pjreddie.com/media/files/yolov3.weights).

YOLO is supporting the following input image formats

- JPEG (.jpg, .jpeg)
- PNG (.png)
- BMP (.bmp)
- TIFF (.tiff, .tif)
- GIF (.gif)

### Results

By inputting a image with real (**not animated**) object contained, OpenCV's package will detect the object and decide what it is.

For example, using an image of a zebra would be easy to detect.

<img src="imgs\zebra_output.jpg" alt="zebra_output" style="zoom: 40%;" />

### Limitation

However, YOLO's training data is very limited. It can only detect at most 100 objects from a image. It would take a large amount of time to train the data and correct them properly. An simple defect that YOLO has is not able to distinguish objects with resemble properties. 

For example, it may detect fox as dog.

<img src="imgs\fox_output.png" alt="fox_output" style="zoom: 80%;" />
>>>>>>> 8bac8ea (opencv image translation)
