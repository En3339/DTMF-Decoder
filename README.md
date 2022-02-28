# DTMF the python code can run in a python environment, such as 'python 3.7'.
# Author : En Lu & Zhengyang Li.
# For any useage.
This is a Group project including decoding a DTMF signal into a sequence of digits.
The decoder aims to decode the DTMF key press signal. When a key is pressed, it generates a signal inccludes a high freq. and low freq.. By FFT, the frequencies can be detected and by that, it decodes the signal and transform into a digit. By cutting signal pieces, the it can continiously decode a signal into a sequence of digits.

The "fft.py" aims to plot a signal in both time domain and freq. domain

The "touchtonedecoder.py" reads a touchtone signal from "touchtones.dat". It detects each possiable pressed keys in the signal. However, the sensitivity of detecting 2 same digits remains to explore for against touch by mistake.
![pic1](https://user-images.githubusercontent.com/56938146/155967938-35af3c91-533f-4662-a5db-77bc22b19b37.svg)
![pic2](https://user-images.githubusercontent.com/56938146/155967979-e3a3dbc4-1242-4781-bbb5-5ee1a450c057.svg)
