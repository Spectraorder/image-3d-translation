import cv2
import numpy as np

input_filename = input("Enter input filename: ")
output_filename = input("Enter output filename: ")

# Load the pre-trained YOLOv3 model
net = cv2.dnn.readNet("models/yolov3.weights", "models/yolov3.cfg")

# Load the list of object classes
with open("data/coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Load the input image
img = cv2.imread(input_filename)

# Get the image dimensions
height, width, channels = img.shape

# Create a blob from the image
blob = cv2.dnn.blobFromImage(img, 1/255.0, (416, 416), swapRB=True, crop=False)

# Set the input blob for the network
net.setInput(blob)

# Get the output layers
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers().tolist()]

# Run the forward pass to get the network output
outputs = net.forward(output_layers)

# Get detected objects
class_ids = []
confidences = []
boxes = []
labels = []
for out in outputs:
    for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.5:
            center_x = int(detection[0] * img.shape[1])
            center_y = int(detection[1] * img.shape[0])
            w = int(detection[2] * img.shape[1])
            h = int(detection[3] * img.shape[0])
            x = int(center_x - w / 2)
            y = int(center_y - h / 2)
            class_ids.append(class_id)
            label = classes[class_id]
            labels.append(label)
            confidences.append(float(confidence))
            boxes.append([x, y, w, h])

# Print the list of detected objects and their labels
print("Detected Objects:", boxes)
print("Labels:", labels)

# Apply non-maximum suppression
indices = cv2.dnn.NMSBoxes(boxes, confidences, score_threshold=0.5, nms_threshold=0.4)
new_boxes = []
new_class_ids = []
new_confidences = []
if len(indices) > 0:
    for i in indices.flatten():
        new_boxes.append(boxes[i])
        new_class_ids.append(class_ids[i])
        new_confidences.append(confidences[i])

# Draw bounding boxes
for i in range(len(new_boxes)):
    x, y, w, h = new_boxes[i]
    label = f'{classes[new_class_ids[i]]}: {new_confidences[i]:.2f}'
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(img, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Save output image
cv2.imwrite(output_filename, img)
