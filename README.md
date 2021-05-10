# Image Crossfading
A simple python program that does a cross-fade effect between 2 images, generating an arbitrary number of intermediate images

## Usage
After choosing 2 images of compatible extentions (jpg, jpeg, etc... **PNG not supported yet**), you can mannualy provide the path (explained in options below) or simply **paste both images on the *INPUT*  ditectory**. Than, run:

`./bin/make.sh` 

to install dependences, then

`python3 fade.py`

to run the actual program (optionally specifying your preferences explained below)

## Options
#### -i or --image
Use this to specify how many intermediate images you want to generate for the crossfading effect, 2 of them being each original image. 
If not given, it will be set to 10 by dafault

###### Ex:. 
`python3 fade.py -i 20`

This will generate 20 new images, 2 of them being the original files and 18 transition images

#### -p or --path
Use this to manually specift the full path to both your image files.

###### Ex:. 
`python3 -p /home/user/dowloads/img1.jpg /home/user/dowloads/img2.jpg`

This will generate the crossfading effect between images img1.jpg and img2.jpg, even if you have images on the **INPUT** directory



