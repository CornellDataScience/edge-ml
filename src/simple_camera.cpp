#include "../utils/motion_detection.cpp"
#include <chrono>
#include <iomanip>
#include <opencv2/opencv.hpp>
#include <sstream>

int WAIT_TIME = 5.0; // seconds

// function to get the current time formatted
std::string current_time_formatted() {
  auto now = std::chrono::system_clock::now();
  auto in_time_t = std::chrono::system_clock::to_time_t(now);

  std::stringstream ss;
  ss << std::put_time(std::localtime(&in_time_t), "%Y-%m-%d_%H-%M-%S");
  return ss.str();
}

int main() {
  // default webcam caputre - change for jetson
  int webcam_index = 0;

  // open the default camera
  cv::VideoCapture cap(webcam_index);
  // error handling
  if (!cap.isOpened()) {
    std::cout << "Failed to open camera." << std::endl;
    return -1;
  }

  // load the face cascade
  cv::CascadeClassifier face_cascade;
  if (!face_cascade.load(
          "../utils/haarcascade_frontalface_default.xml")) // Update with
                                                           // correct path
  {
    // error handling
    std::cout << "Error loading face cascade\n";
    return -1;
  }

  // create a window
  cv::namedWindow("Webcam", cv::WINDOW_AUTOSIZE);
  cv::Mat img;                      // create a matrix to hold the image
  std::cout << "Hit ESC to exit\n"; // print to console
  auto start = std::chrono::steady_clock::now(); // start the timer
  int img_count = 0;                             // image counter
  int bb_count = 0;                              // bounding box counter

  // main loops
  while (true) {
    // read the image
    if (!cap.read(img)) {
      std::cout << "Capture read error" << std::endl;
      break;
    }

    // fix paths when using jetson
    std::string prevImPath =
        "../Images/image" + std::to_string(img_count - 1) + ".jpg";
    std::string currImPath =
        "../Images/image" + std::to_string(img_count) + ".jpg";

    // display realtime webcam feed
    cv::imshow("Webcam", img);

    auto end = std::chrono::steady_clock::now();
    // calculate the elapsed time
    std::chrono::duration<double> elapsed = end - start;

    if (elapsed.count() >= WAIT_TIME) {
      // save the image
      cv::imwrite(currImPath, img);

      if (img_count > 0 && detect_motion(prevImPath, currImPath)) {
        std::cout << "Motion detected!" << std::endl;

        // detect faces
        std::vector<cv::Rect> faces;
        cv::Mat gray; // create a matrix to hold the gray image
        cvtColor(img, gray, cv::COLOR_BGR2GRAY);    // convert to gray
        face_cascade.detectMultiScale(gray, faces); // detect faces

        // draw the faces
        for (const auto &face : faces) {
          // draw a rectangle around the face
          cv::rectangle(img, face, cv::Scalar(255, 0, 0), 2);
        }
        // save the image
        for (const auto &face : faces) {
          // crop the face
          cv::Mat face_img = img(face);
          // save the image
          std::string filename = "../Images/bounding_boxes/image" +
                                 std::to_string(bb_count) + ".jpg";
          cv::imwrite(filename, face_img);
          bb_count++;
        }
      }
      img_count++;
      start = std::chrono::steady_clock::now(); // reset the timer
    }

    // exit on ESC
    int keycode = cv::waitKey(1) & 0xff;
    if (keycode == 27) // ESC key
      break;
  }

  // release the camera
  cap.release();
  cv::destroyAllWindows();
  return EXIT_SUCCESS;
}