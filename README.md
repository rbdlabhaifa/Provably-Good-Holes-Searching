# Provably-Good-Holes-Searching

In our application, we are given a set of 2D RGB images that were collected from a remote-controlled drone
above a field or a similar ground. The goal is to have a system that automatically detect “holes” in these
image. More precisely, to return a subset of pixels in the given image, where each pixel is a center of such
a hole. 

![image](pic.png)

# 1. Prerequisites
We have tested the library in **Ubuntu 20.04**, and **Windows** but it should be easy to compile in other platforms.

## Building library and examples for WINDOWS:
## OpenCV
We use [OpenCV](http://opencv.org) to manipulate images and features. Dowload and install instructions can be found at: http://opencv.org.

## Python
Download and install instructions can be found at: https://www.python.org/downloads/windows/

## PILLOW for a larger selection of image file formats: JPEG, BMP, and TIFF image files;
Inter in cmd: ```pip install Pillow```

## Matplotlib
Download and install instructions can be found at: https://matplotlib.org/3.1.1/users/installing.html#building-on-windows

## Building library:
Download project then unzip the files 
OR 
Clone the repository:
```
git clone https://github.com/rbdlabhaifa/Provably-Good-Holes-Searching.git
```

# 2. Examples
run:
```
python3 main.py
```
