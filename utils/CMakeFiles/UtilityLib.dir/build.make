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
CMAKE_SOURCE_DIR = /home/cds-nano-3/edge-ml

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/cds-nano-3/edge-ml

# Include any dependencies generated for this target.
include utils/CMakeFiles/UtilityLib.dir/depend.make

# Include the progress variables for this target.
include utils/CMakeFiles/UtilityLib.dir/progress.make

# Include the compile flags for this target's objects.
include utils/CMakeFiles/UtilityLib.dir/flags.make

utils/CMakeFiles/UtilityLib.dir/motion_detection.cpp.o: utils/CMakeFiles/UtilityLib.dir/flags.make
utils/CMakeFiles/UtilityLib.dir/motion_detection.cpp.o: utils/motion_detection.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/cds-nano-3/edge-ml/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object utils/CMakeFiles/UtilityLib.dir/motion_detection.cpp.o"
	cd /home/cds-nano-3/edge-ml/utils && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/UtilityLib.dir/motion_detection.cpp.o -c /home/cds-nano-3/edge-ml/utils/motion_detection.cpp

utils/CMakeFiles/UtilityLib.dir/motion_detection.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/UtilityLib.dir/motion_detection.cpp.i"
	cd /home/cds-nano-3/edge-ml/utils && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/cds-nano-3/edge-ml/utils/motion_detection.cpp > CMakeFiles/UtilityLib.dir/motion_detection.cpp.i

utils/CMakeFiles/UtilityLib.dir/motion_detection.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/UtilityLib.dir/motion_detection.cpp.s"
	cd /home/cds-nano-3/edge-ml/utils && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/cds-nano-3/edge-ml/utils/motion_detection.cpp -o CMakeFiles/UtilityLib.dir/motion_detection.cpp.s

# Object files for target UtilityLib
UtilityLib_OBJECTS = \
"CMakeFiles/UtilityLib.dir/motion_detection.cpp.o"

# External object files for target UtilityLib
UtilityLib_EXTERNAL_OBJECTS =

utils/libUtilityLib.a: utils/CMakeFiles/UtilityLib.dir/motion_detection.cpp.o
utils/libUtilityLib.a: utils/CMakeFiles/UtilityLib.dir/build.make
utils/libUtilityLib.a: utils/CMakeFiles/UtilityLib.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/cds-nano-3/edge-ml/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX static library libUtilityLib.a"
	cd /home/cds-nano-3/edge-ml/utils && $(CMAKE_COMMAND) -P CMakeFiles/UtilityLib.dir/cmake_clean_target.cmake
	cd /home/cds-nano-3/edge-ml/utils && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/UtilityLib.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
utils/CMakeFiles/UtilityLib.dir/build: utils/libUtilityLib.a

.PHONY : utils/CMakeFiles/UtilityLib.dir/build

utils/CMakeFiles/UtilityLib.dir/clean:
	cd /home/cds-nano-3/edge-ml/utils && $(CMAKE_COMMAND) -P CMakeFiles/UtilityLib.dir/cmake_clean.cmake
.PHONY : utils/CMakeFiles/UtilityLib.dir/clean

utils/CMakeFiles/UtilityLib.dir/depend:
	cd /home/cds-nano-3/edge-ml && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/cds-nano-3/edge-ml /home/cds-nano-3/edge-ml/utils /home/cds-nano-3/edge-ml /home/cds-nano-3/edge-ml/utils /home/cds-nano-3/edge-ml/utils/CMakeFiles/UtilityLib.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : utils/CMakeFiles/UtilityLib.dir/depend
