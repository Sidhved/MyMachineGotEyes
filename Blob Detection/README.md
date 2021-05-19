Blob Detection<br>
OpenCV2 project #1<br>
Image used can be found at [Link](https://github.com/Sidhved/MyMachineGotEyes/blob/main/Blob%20Detection/blob1.jpg)

-> IMREAD_GRAYSCALE : If set, always convert image to the single channel grayscale image (codec internal conversion).<br>
-> SimpleBlobDetector: Extracting Blobs from an image<br>
    -> By Colour (Not used here as we convert image to grayscale first)<br>
    -> By Area : Between MinArea and MaxArea<br>
    -> By Circularity : (4*pi*area)/(peri^2) between minCerc and MaxCerc<br>
    -> By Ratio of MinInertia to MaxInertia<br>
    -> By Convexity : Area/Area of Blob convex hull<br>
-> Create detector and use it to detect key points<br>
-> Draw detected blobs as circles (use DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS to ensure)<br>
-> Display the final image<br>
OUTPUT IMAGE:<br>
    ![output_image](https://github.com/Sidhved/MyMachineGotEyes/blob/main/Blob%20Detection/OUTPUT%20IMAGE.JPG)
