#include <opencv2/opencv.hpp>
#include <iostream>
#include <string>
#include <vector>
#include <filesystem>
#include <chrono>
#include <iomanip>
#include <sstream>

namespace fs = std::filesystem;
using namespace cv;
using namespace std;

int main()
{
    string img_folder = "images";
    string output_folder = "cropped";

    // Create output directory if it doesn't exist
    fs::create_directories(output_folder);

    // Load Haar Cascade
    CascadeClassifier haar_cascade;
    haar_cascade.load("haarcascade_frontalface_default.xml");

    // Iterate over images in the folder
    for (const auto &entry : fs::directory_iterator(img_folder))
    {
        string filename = entry.path().string();
        if (filename.find(".jpeg") != string::npos || filename.find(".jpg") != string::npos || filename.find(".png") != string::npos)
        {
            // Load image
            Mat img = imread(filename);
            Mat g_img;
            cvtColor(img, g_img, COLOR_BGR2GRAY);

            // Detect faces
            vector<Rect> faces_rect;
            haar_cascade.detectMultiScale(g_img, faces_rect, 1.1, 6);

            // Get current time for folder naming
            auto now = chrono::system_clock::now();
            auto in_time_t = chrono::system_clock::to_time_t(now);
            stringstream ss;
            ss << put_time(localtime(&in_time_t), "%Y-%m-%d-%H-%M-%S");
            string time = ss.str();

            // Create output directory for current image
            string curr_output_dir = output_folder + "/" + time;
            fs::create_directories(curr_output_dir);

            // Process faces
            int image_idx = 0;
            for (auto &rect : faces_rect)
            {
                rectangle(img, rect, Scalar(255, 0, 0), 3);
                Mat face = img(rect);
                string face_filename = curr_output_dir + "/face" + to_string(image_idx) + ".jpg";
                imwrite(face_filename, face);
                image_idx++;
            }

            // Display the processed image
            imshow("bounding-boxes", img);
            waitKey(0);
        }
    }
    return 0;
}
