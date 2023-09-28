#include <opencv2/opencv.hpp>

int main()
{
    cv::Mat image = cv::imread("example.jpg");

    if (image.empty())
    {
        std::cerr << "Error: Could not open or find the image" << std::endl;
        return -1;
    }

    cv::imshow("Image", image);
    cv::waitKey(0);

    return 0;
}