// simple_camera.cpp
// MIT License
// Copyright (c) 2019-2022 JetsonHacks
// See LICENSE for OpenCV license and additional information
// Using a CSI camera (such as the Raspberry Pi Version 2) connected to a
// NVIDIA Jetson Nano Developer Kit using OpenCV
// Drivers for the camera and OpenCV are included in the base image

#include <opencv2/opencv.hpp>
#include "../utils/motion_detection.cpp"

std::string gstreamer_pipeline(int capture_width, int capture_height, int display_width, int display_height, int framerate, int flip_method)
{
    return "nvarguscamerasrc ! video/x-raw(memory:NVMM), width=(int)" + std::to_string(capture_width) + ", height=(int)" +
           std::to_string(capture_height) + ", framerate=(fraction)" + std::to_string(framerate) +
           "/1 ! nvvidconv flip-method=" + std::to_string(flip_method) + " ! video/x-raw, width=(int)" + std::to_string(display_width) + ", height=(int)" +
           std::to_string(display_height) + ", format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink";
}

int main()
{
    int capture_width = 1280;
    int capture_height = 720;
    int display_width = 1280;
    int display_height = 720;
    int default_framerate = 4;
    int motion_framerate = 2;
    int flip_method = 0;

    std::string pipeline = gstreamer_pipeline(capture_width,
                                              capture_height,
                                              display_width,
                                              display_height,
                                              default_framerate,
                                              flip_method);
    std::cout << "Using pipeline: \n\t" << pipeline << "\n";

    cv::VideoCapture cap(pipeline, cv::CAP_GSTREAMER); // nano
    // cv::VideoCapture cap(0); // macbook

    if (!cap.isOpened())
    {
        std::cout << "Failed to open camera." << std::endl;
        return (-1);
    }

    cv::namedWindow("CSI Camera", cv::WINDOW_AUTOSIZE);
    cv::Mat img;

    std::cout << "Hit ESC to exit"
              << "\n";

    int i = 0;
    while (true)
    {
        if (!cap.read(img))
        {
            std::cout << "Capture read error" << std::endl;
            break;
        }

        std::string prevImPath = "../Images/image" + std::to_string(i - 1) + ".jpg";
        std::string currImPath = "../Images/image" + std::to_string(i) + ".jpg";

        cv::imshow("CSI Camera", img);
        cv::imwrite(currImPath, img);

        int keycode = cv::waitKey(10) & 0xff;
        if (keycode == 27) // esc
            break;

        if ((i > 0) && (detect_motion(prevImPath, currImPath))) // if prev img and motion detected
        {
            cap.set(cv::CAP_PROP_FPS, motion_framerate);
        }
        else
        {
            cap.set(cv::CAP_PROP_FPS, default_framerate);
        }

        double frameRate = cap.get(cv::CAP_PROP_FPS);
        std::cout << "Current Frame Rate: " << frameRate << std::endl;

        i++;
    }

    cap.release();
    cv::destroyAllWindows();
    return 0;
}
