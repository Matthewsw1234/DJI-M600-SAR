Hello! SO YOU, YES YOU! You want to train your own model to use on your Raspberry Pi(5)? Just follow thes instructions and be on your way!

This is done fully on the Raspberry Pi as your main Dektop using LabelImg. You are free to do this on your own machine but I will not supply the setup process.

First, make an images folder and place all of the images you would wish to train in it. Make sure they are in JPEG format. You will start seeing errors the more you go if they are not JPEG so save yourself the pain later and convert them online. I reccomend Cloudconvert.

Open Command Terminal
``` shell
sudo agpt-get install pyqt5-dev-tools

sudo pip3 install labelimg
```
``` shell
labelimg
```
Now you will be within the Labeling Software.