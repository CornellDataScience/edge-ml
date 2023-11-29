# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.13

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/local/bin/cmake

# The command to remove a file.
RM = /usr/local/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/cds-nano-3/edge-ml/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/cds-nano-3/edge-ml/build

# Include any dependencies generated for this target.
include CMakeFiles/simple_camera.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/simple_camera.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/simple_camera.dir/flags.make

CMakeFiles/simple_camera.dir/simple_camera.cpp.o: CMakeFiles/simple_camera.dir/flags.make
CMakeFiles/simple_camera.dir/simple_camera.cpp.o: /home/cds-nano-3/edge-ml/src/simple_camera.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/cds-nano-3/edge-ml/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/simple_camera.dir/simple_camera.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/simple_camera.dir/simple_camera.cpp.o -c /home/cds-nano-3/edge-ml/src/simple_camera.cpp

CMakeFiles/simple_camera.dir/simple_camera.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/simple_camera.dir/simple_camera.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/cds-nano-3/edge-ml/src/simple_camera.cpp > CMakeFiles/simple_camera.dir/simple_camera.cpp.i

CMakeFiles/simple_camera.dir/simple_camera.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/simple_camera.dir/simple_camera.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/cds-nano-3/edge-ml/src/simple_camera.cpp -o CMakeFiles/simple_camera.dir/simple_camera.cpp.s

# Object files for target simple_camera
simple_camera_OBJECTS = \
"CMakeFiles/simple_camera.dir/simple_camera.cpp.o"

# External object files for target simple_camera
simple_camera_EXTERNAL_OBJECTS =

simple_camera: CMakeFiles/simple_camera.dir/simple_camera.cpp.o
simple_camera: CMakeFiles/simple_camera.dir/build.make
simple_camera: /usr/lib/aarch64-linux-gnu/libopencv_dnn.so.4.1.1
simple_camera: /usr/lib/aarch64-linux-gnu/libopencv_gapi.so.4.1.1
simple_camera: /usr/lib/aarch64-linux-gnu/libopencv_highgui.so.4.1.1
simple_camera: /usr/lib/aarch64-linux-gnu/libopencv_ml.so.4.1.1
simple_camera: /usr/lib/aarch64-linux-gnu/libopencv_objdetect.so.4.1.1
simple_camera: /usr/lib/aarch64-linux-gnu/libopencv_photo.so.4.1.1
simple_camera: /usr/lib/aarch64-linux-gnu/libopencv_stitching.so.4.1.1
simple_camera: /usr/lib/aarch64-linux-gnu/libopencv_video.so.4.1.1
simple_camera: /usr/lib/aarch64-linux-gnu/libopencv_videoio.so.4.1.1
simple_camera: /usr/lib/aarch64-linux-gnu/libopencv_imgcodecs.so.4.1.1
simple_camera: /usr/lib/aarch64-linux-gnu/libopencv_calib3d.so.4.1.1
simple_camera: /usr/lib/aarch64-linux-gnu/libopencv_features2d.so.4.1.1
simple_camera: /usr/lib/aarch64-linux-gnu/libopencv_flann.so.4.1.1
simple_camera: /usr/lib/aarch64-linux-gnu/libopencv_imgproc.so.4.1.1
simple_camera: /usr/lib/aarch64-linux-gnu/libopencv_core.so.4.1.1
simple_camera: CMakeFiles/simple_camera.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/cds-nano-3/edge-ml/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable simple_camera"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/simple_camera.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/simple_camera.dir/build: simple_camera

.PHONY : CMakeFiles/simple_camera.dir/build

CMakeFiles/simple_camera.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/simple_camera.dir/cmake_clean.cmake
.PHONY : CMakeFiles/simple_camera.dir/clean

CMakeFiles/simple_camera.dir/depend:
	cd /home/cds-nano-3/edge-ml/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/cds-nano-3/edge-ml/src /home/cds-nano-3/edge-ml/src /home/cds-nano-3/edge-ml/build /home/cds-nano-3/edge-ml/build /home/cds-nano-3/edge-ml/build/CMakeFiles/simple_camera.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/simple_camera.dir/depend

