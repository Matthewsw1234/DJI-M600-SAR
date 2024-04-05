# Hello! SO YOU, YES YOU!

## You want to train your own model to use on your Raspberry Pi(5)? Just follow thes instructions and be on your way!

This is done fully on the Raspberry Pi as your main Dektop using labelImg. You are free to do this on your own machine but I will not supply the setup process.

First, make an `images` folder within the repository and place all of the images you would wish to train in it. The images are best for training if you have many angles of the object and different backrounds. Make sure they are in JPEG format. You will start seeing errors the more you go if they are not JPEG so save yourself the pain later and convert them online. I reccomend Cloudconvert.

Open Command Terminal

``` shell
sudo agpt-get install pyqt5-dev-tools

sudo pip3 install labelimg
```

``` shell
labelimg
```

Now you will be within the Labeling Software.

If you go to click PascalVOC, you will notice that it will crash immeditaly. That is because it is not designed to run on the Pi.

To fix it, follow these steps

## Set up labelImg to work on Raspberry Pi

First, navigate to /usr/local/lib/python3.11/dist-packages/libs in the file manager and locate canvas.py and replace with canvas.py from my repository:

``` shell
sudo rm -rf /usr/local/lib/python3.11/dist-packages/libs/canvas.py

cd DJI-M600-SAR

sudo mv canvas.py /usr/local/lib/python3.11/dist-packages/libs

cd ..
```

Next, navigate to /usr/local/lib/python3.11/dist-packages/labelImg in the file manager and locate labelImg.py and replace with labelImg.py from my repository:

``` shell
sudo rm -rf /usr/local/lib/python3.11/dist-packages/labelImg/labelImg.py

cd DJI-M600_SAR

sudo mv labelImg.py /usr/local/lib/python3.11/dist-packages/labelImg

cd ..
```

Next, reopen labelImg with: labelImg in a command window

``` shell
labelImg
```

## Using labelImg

Click `Open Dir` to open the directory to your images folder. Please find and select that folder.

Click `Change Save Dir` and select the images folder once again to save the .xml files to it

Once you see your images, click either `Create RectBox` or `W` on your keyboard and you should see two axis show up. This is the corner of your rectangle to determine your detection model.

Click and Drag the rectangle around your object or thing you want to train the model on. Try to make this as close to the model as possible for the best reliability.

A box will pop up with a text section. Please place what you would like the object to be called. Remember this name exactly as it will be important later.

Click `Ok`, `Save`, and `Next Image` to move on. Do this for every Image.

## Training

Please make a new folder within the repository named: `Training`.

Within it, please make two folders named: `train` and `validate`.

Copy all of the images and .xml files from `images` and place them into `train` and `validate`.

Go to a Command Terminal and type:

``` shell
cd DJI-M600-SAR

sudo zip -r Training.zip Training/*
```

Please upload this zip file to your `Google Drive`.

Open the Web and go to `Google Colab`.

Open the file `tflite_custom_model.ipynb` as a notebook.

Navigate to `Change Runtime Type` and select `Python 3` and the `T4 GPU`.

Note:  This will run fine without a GPU. It will just take a little longer.

Just Run Thorugh every PlayButton and follow when it asks for you to confirm certain commands.

When You get to `from google.colab import drive` just sign into your `Google Drive` and carry on. This is where it grabs that earlier `Training` file that was zipped.

After you unzip `Training` in the next command. Please upload `train.py` from the repository to colab.

Open `train.py` and under `train_data` and `val_data`, find `noun`. Replace these with the name of the object you wanted to detect. If you have only one, please delete the other. If you have more than two, please add more spaces.

Note: This is the exact name of the object I said to remember earlier. This has to be exactly the same name.

Save the file with Ctrl S and run the final block.

Once it ends, you will see the output file: `Your-Model.tflite`. Download it to your Pi and move it to the repository.

Open `detect.py` and scroll to def main() and look for `Your-Model.tflite`. Add a comment before my file with a # and uncomment `Your-Model.tflite`. 

## That's It. YOU DID IT!

Enjoy running your own custom model. I highly recommend that you test your model and make changes as needed. But that's it!