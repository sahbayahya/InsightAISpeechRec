import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile


def audio_plotter(filename):

    # Read the audio file
    sampling_freq, signal = wavfile.read(filename)
    # Display the params
    print('\nSignal shape:', signal.shape)
    print('Datatype:', signal.dtype)
    print('Signal duration:', round(signal.shape[0] / float(sampling_freq), 2), 'seconds')
    # Normalize the signal
    signal = signal / np.power(2, 15)

    # Extract the first 50 values
    signal = signal[:50]

    # Construct the time axis in milliseconds
    time_axis = 1000 * np.arange(0, len(signal), 1) / float(sampling_freq)

    # Plot the audio signal
    plt.plot(time_axis, signal, color='black')
    plt.xlabel('Time (milliseconds)')
    plt.ylabel('Amplitude')
    plt.title('Input audio signal')
    plt.show()
    return

if __name__=="__main__":

    audio_plotter(filename='random_sound.wav')
