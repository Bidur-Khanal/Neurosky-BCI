from numpy import *
from scipy.signal import *
import matplotlib.pyplot as plt
from numpy.fft import *
from matplotlib import *
from scipy import *
from pylab import *
import pandas as pd
from matplotlib import style
import matplotlib.animation as animation
from scipy.fftpack import fft, ifft
import csv
import numpy as np
import seaborn as sns
import pandas as pd
import math
style.use('classic')
import pywt


df2 = pd.read_csv("attention0.csv")

eeg = df2['raw_data']

y= array(eeg)

L = len(y)  # signal length
fs = 500.0  # sampling rate
T = 1 / fs  # sample time
t = linspace(1, L, L) * T  # time vector


f = fs * linspace(0, L / 10, L / 10) / L  # single side frequency vector, real frequency up to fs/2
Y = fft(y)


figure()
filtered = []
b = []  # store filter coefficient
cutoff = [0.5, 4.0, 7.0, 12.0, 30.0]

for band in range(0, len(cutoff) - 1):
    wl = 2 * cutoff[band] / fs * pi
    wh = 2 * cutoff[band + 1] / fs * pi
    M = 512  # Set number of weights as 128
    bn = zeros(M)



    for i in range(0, M):  # Generate bandpass weighting function
        n = i - M / 2  # Make symmetrical
        if n == 0:
            bn[i] = wh / pi - wl / pi;
        else:
            bn[i] = (sin(wh * n)) / (pi * n) - (sin(wl * n)) / (pi * n)  # Filter impulse response

    bn = bn * kaiser(M, 5)  # apply Kaiser window, window shape= 5
    b.append(bn)

    [w, h] = freqz(bn, 1)
    filtered.append(convolve(bn, y))  # filter the signal by convolving the signal with filter coefficients

figure(figsize=[16, 10])
subplot(2, 1, 1)
plot(y)
for i in range(0, len(filtered)):
    y_p = filtered[i]
    print(y_p[int(M / 2):int(L + M / 2)])
    plot(y_p[int(M / 2):int(L + M / 2)])
axis('tight')
title('Time domain')
xlabel('Time (seconds)')

subplot(2, 1, 2)
plot(f, 2 * abs(Y[int(0):int(L / 10)]))
for i in range(0, len(filtered)):
    Y = filtered[i]
    Y = fft(Y[int(M / 2):int(L + M / 2)])
    plot(f, abs(Y[int(0):int(L / 10)]))
axis('tight')
legend(['original', 'delta band, 0-4 Hz', 'theta band, 4-7 Hz', 'alpha band, 7-12 Hz', 'beta band, 12-30 Hz'])

for i in range(0, len(filtered)):  # plot filter's frequency response
    H = abs(fft(b[i], L))
    H = H * 1.2 * (max(Y) / max(H))
    plot(f, 3 * H[int(0):int(L / 10)], 'k')
axis('tight')
title('Frequency domain')
xlabel('Frequency (Hz)')
subplots_adjust(left=0.04, bottom=0.04, right=0.99, top=0.97)
show()