Task 3
We want to test your research ability.

We have 20 pictures of motherboards with memory.
We have 20 pictures of motherboards without memory.

We want to make a simple flask api where we upload image or choose a hardcode image and can draw a box around the different memory. So if there 2 memory, we draw 2 boxes. If only 1 memory, draw 1 box only.

Which algorithm you will use? Why you choose this? Does CPU or GPU have an impact on your decision?
YOLOv5 (You Only Look Once version 5) is a popular and widely used object detection algorithm for real-time object detection tasks. It is known for its speed and accuracy, making it suitable for applications where real-time processing is important.

There are several reasons why YOLOv5 could be a good choice for detecting memory on motherboards in images or videos:

Speed: YOLOv5 is designed to be fast and efficient, making it suitable for real-time or near real-time applications. It can process images or videos quickly, which can be beneficial for detecting memory on motherboards in real-time scenarios, such as in a production line or during system testing.

Accuracy: YOLOv5 has shown good accuracy in object detection tasks, with the ability to detect objects with high precision and recall rates. This can be important for accurately detecting memory modules on motherboards, even in challenging conditions such as varying lighting or orientations.

Flexibility: YOLOv5 allows for the detection of multiple objects in a single image or video frame, which can be useful for detecting multiple memory modules on motherboards in a single image or video frame. It can also be easily trained on custom datasets, allowing for customization and adaptation to specific tasks or domains.

As for CPU or GPU, YOLOv5 can be run on both CPU and GPU, but it is generally recommended to use GPU for better performance. YOLOv5 utilizes convolutional neural networks (CNNs) which are computationally intensive, and GPU's parallel processing capabilities can significantly speed up the inference process. However, if GPU resources are not available or the scale of the task is small, CPU can also be used, although it may be slower compared to GPU in terms of inference speed. The choice between CPU and GPU would depend on the computational resources available and the performance requirements of the specific application. 


What if given a video instead of images? Does your approach change?
If you are given a video instead of images, the overall approach would be similar, but there would be some differences in implementation.

Video frame extraction: Instead of processing individual images, you would need to extract frames from the video and process them one by one. Most computer vision libraries provide APIs to extract frames from videos, which can be used to input frames into the YOLOv5 model for object detection.

Frame-by-frame object detection: Once you have extracted frames from the video, you can pass each frame through the YOLOv5 model for object detection. The model would analyze each frame separately and detect memory modules in each frame based on the model's predictions.

Real-time considerations: In the case of video, real-time considerations become important, as the video is processed in real-time or near real-time. Depending on the frame rate of the video and the processing speed of the YOLOv5 model, you may need to optimize the implementation to ensure real-time performance, such as using hardware acceleration, frame skipping, or other optimization techniques.

Video-specific challenges: Videos may present additional challenges, such as motion blur, lighting changes, and object occlusions, which may impact the accuracy of object detection. Techniques like temporal consistency, object tracking, or incorporating temporal information into the model can be used to address these challenges.

Output visualization: In addition to drawing bounding boxes around detected memory modules, you may need to visualize the results in a video format, such as drawing boxes on each frame or creating a new video with annotated memory modules.

In summary, while the overall approach of using YOLOv5 for object detection can remain similar for videos, there would be some differences in implementation, such as video frame extraction, real-time considerations, addressing video-specific challenges, and output visualization.


We suggest using https://www.makesense.ai/ to annotate.
