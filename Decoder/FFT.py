import scipy 
import numpy as np
from scipy.io import wavfile
import matplotlib
import matplotlib.pyplot as plot


#int Fs, array sized x*2 init_Data read from wav
Fs, init_Data = wavfile.read('lovecures.wav')

#time should be a array
Time=np.arange(0, len(init_Data)/Fs, 1/Fs)

# Plot the signal read from wav file
plot.subplot(211)
plot.title('Time domain signals')
plot.plot(Time,init_Data)
plot.xlabel('Time')
plot.ylabel('Amplitude')

# in frequency domain Signals
L_init_Data = init_Data[:,0]
fft_freq = np.fft.fft(L_init_Data)
L_fft_freq = abs(fft_freq)
dB_L_fft_freq = 10*np.log(L_fft_freq )

freq_space = np.arange(0, Fs,Fs/(len(L_init_Data)))

#dB_freq_space = 10*np.log(freq_space)
plot.subplot(212)
plot.plot(freq_space,dB_L_fft_freq,'blue')
plot.title('Frequency domain signals')
plot.xlabel('Frequency/Hz')
plot.ylabel('Amplitude/dB')


#normalise
#L_fft_freq = L_fft_freq[range(int(len(L_fft_freq)/2))]
#freq_space = freq_space[range(int(len(freq_space)/2))]
#plot.subplot(313)
#plot.plot(freq_space,L_fft_freq,'blue')
#plot.show()
#33391236