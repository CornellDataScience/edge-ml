# Create a library from motion_detection.cpp
add_library(UtilityLib motion_detection.cpp)

# Link OpenCV libraries if needed
target_link_libraries(UtilityLib ${OpenCV_LIBS})
