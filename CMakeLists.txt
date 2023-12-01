cmake_minimum_required(VERSION 3.12)
project(edge-ml)

find_package(OpenCV REQUIRED)

# Add subdirectories
add_subdirectory(src)
add_subdirectory(utils)

# Define your executable and link libraries if needed
add_executable(camera src/simple_camera.cpp)

include_directories(${OpenCV_INCLUDE_DIRS})

target_link_libraries(camera PRIVATE ${OpenCV_LIBS} UtilityLib)
