#library: have at least 1 func that generates fourier transform

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft,ifft


def generateFFT(signal):
    return fft(signal)
def plotFFT(fourierTranform):
    magnitude = np.abs(fourierTranform)
    frequency_axis = np.fft.fftfreq(len(t), d=t[1] - t[0])
    plt.figure(figsize=(10, 6))
    plt.plot(frequency_axis, magnitude)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.title('Fourier Transform of the Signal')
    plt.grid(True)
    plt.show()
def plotiFFT(fourierTransform,signal):
    sum = ifft(fourierTransform)
    # Plot the original signal
    plt.figure(figsize=(12, 6))

    # Subplot 1: Original Signal
    plt.subplot(2, 1, 1)
    plt.plot(t, values, label='Original Signal', color='blue')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Original Signal')
    plt.grid(True)
    plt.legend()

    # Subplot 2: Reconstructed Signal (Sum of Sinusoids)
    plt.subplot(2, 1, 2)
    plt.plot(t, np.real(sum), label='Sum of Sinusoids (Reconstructed)', color='red')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Sum of Sinusoids (Reconstructed from FFT)')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    startTime = 0.0
    endTime = 10.0
    sampleRate = 1000
    #signal = lambda t: np.tan(np.sin(50*t)*np.pi*np.exp(-t))
    signal = lambda t : np.sin(np.sin(t*3))
    t = np.linspace(startTime, endTime, int((endTime - startTime) * sampleRate), endpoint=False)
    values = signal(t)
    fft = generateFFT(values)
    plotFFT(fft)
    plotiFFT(fft,values)
