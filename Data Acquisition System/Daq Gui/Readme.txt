*The folder has the code for the graphical user interface designed for the system

*The GUI has been developed using Python-Kivy framework.

*When the vehicle comes into motion the CVT rotates and sensors attached to the cvt notess the rpm of the cvt
 and passes the data to the arduino.

*The following software present in this folder reads the data from the arduino and stores in the excel-sheet
 and further the data is provided for analysis.


*Requirements
->Python 2.7.9
->python -m pip install --upgrade pip wheel setuptools
->python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
->python -m pip install kivy.deps.gstreamer
->python -m pip install kivy
 
*To start the the software the script launch.py has to be run.  