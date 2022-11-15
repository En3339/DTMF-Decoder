# DTMF the python code runs in a python environment, such as 'python 3.7'.
# Author : En Lu & Zhengyang Li.
# All rights reserved.
This is a Group project including decoding a DTMF signal into a sequence of digits.
The decoder aims to decode the DTMF key press signal. When a key is pressed, it generates a signal inccludes a high freq. and low freq.. By FFT, the frequencies can be detected and by that, it decodes the signal and transform into a digit. By cutting signal pieces, the it can continiously decode a signal into a sequence of digits.

The "fft.py" aims to plot a signal in both time domain and freq. domain.

The "touchtonedecoder.py" reads a touchtone signal from "touchtones.dat". It detects each possiable pressed keys in the signal. However, the sensitivity of detecting 2 same digits remains to explore for against touch by mistake. The example of one digits detect is shown in the fig below. If the one signal cut have 2 frequency of 230 and 336Hz. According to the reference table, it should be "5"



![image](https://user-images.githubusercontent.com/56938146/155968261-4ce82711-67b1-4b96-8c58-a74e12de3b30.png)



The DTMF reference table is shown here:



![image](https://user-images.githubusercontent.com/56938146/155968640-5c9ec760-696b-4bc9-a8e6-f375bf12c56b.png)



Since our signal is 500 Hz, the table can be transformed by Nyquist theriom.


![image](https://user-images.githubusercontent.com/56938146/155968770-176d3c6e-dc8c-4597-9cb1-7af8dad4c01d.png)




