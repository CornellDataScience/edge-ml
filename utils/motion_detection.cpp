#include <opencv2/opencv.hpp>
#include <iostream>

const double MIN_CONTOUR_SIZE = 3000; // Adjust this threshold as needed

bool detect_motion(std::string im_path1, std::string im_path2)
{
    // load images
    cv::Mat image1 = cv::imread(im_path1);
    cv::Mat image2 = cv::imread(im_path2);

    // preprocess
    cv::Mat gray1, gray2;
    cv::cvtColor(image1, gray1, cv::COLOR_BGR2GRAY);
    cv::cvtColor(image2, gray2, cv::COLOR_BGR2GRAY);
    cv::GaussianBlur(gray1, gray1, cv::Size(21, 21), 0);
    cv::GaussianBlur(gray2, gray2, cv::Size(21, 21), 0);

    cv::Mat diff;
    cv::absdiff(gray1, gray2, diff);

    cv::Mat thresh;
    cv::threshold(diff, thresh, 25, 255, cv::THRESH_BINARY);

    std::vector<std::vector<cv::Point>> contours;
    cv::findContours(thresh, contours, cv::RETR_EXTERNAL, cv::CHAIN_APPROX_SIMPLE);

    for (int i = 0; i < contours.size(); i++)
    {
        cv::drawContours(image2, contours, i, cv::Scalar(0, 255, 0), 2);
    }

    bool motionDetected = false;
    for (int i = 0; i < contours.size(); i++)
    {
        if (cv::contourArea(contours[i]) > MIN_CONTOUR_SIZE)
        {
            motionDetected = true;
            break;
        }
    }
    return motionDetected;
}