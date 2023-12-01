cmake_minimum_required(VERSION 3.12)
project(OpenCVExample)

find_package(OpenCV REQUIRED)

add_executable(simple_camera simple_camera.cpp)

target_link_libraries(simple_camera PRIVATE ${OpenCV_LIBS})
