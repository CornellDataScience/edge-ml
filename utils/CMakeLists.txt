cmake_minimum_required(VERSION 3.12)
project(OpenCVExample)

find_package(OpenCV REQUIRED)

add_executable(motion_detection motion_detection.cpp)
include_directories(${OpenCV_INCLUDE_DIRS})

target_link_libraries(motion_detection PRIVATE ${OpenCV_LIBS})