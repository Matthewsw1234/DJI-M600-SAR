# DJI-M600-SAR
M600 Drone Custom Thermal Detection Payload With Gimbal

This Project is currently not in its full state. It currently is a proof of concept that I wish to take further with updates over time.

# How to set up on Raspberry Pi for object detection (Note: Only tested on Pi 5 with Bookworm OS as of 4/2/2024)
Installation on a Fresh Install of Bookworm, please set up an internet connection beforehand
Type these commands into Command Terminal
Set up a VM if you want, I did not as this is the only purpose this Pi will be used for currently

sudo rm /usr/lib/python3.11/EXTERNALLY-MANAGED (stops externally managed error)
sudo pip3 install opencv-python
sudo pip3 install mediapipe

That is it for setup.
