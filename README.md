# DTMF the python code can run in a python environment, such as 'python 3.7'.
# Author : En Lu & Zhengyang Li.
# For any useage.
This is a Group project including decoding a DTMF signal into a sequence of digits.
The decoder aims to decode the DTMF key press signal. When a key is pressed, it generates a signal inccludes a high freq. and low freq.. By FFT, the frequencies can be detected and by that, it decodes the signal and transform into a digit. By cutting signal pieces, the it can continiously decode a signal into a sequence of digits.
