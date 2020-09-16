# Script for testing/debugging the Python-only, i.e -- not hardware interfacing --
# components of the kidPy module.

import kidPy
import numpy as np
import matplotlib.pyplot as plt

path= './example_vna_sweep/'
print('gc: ' + '\n' + str(kidPy.gc) + '\n\n')
print('regs: ' + '\n' + str(kidPy.regs) + '\n\n')
print('kidPy.captions: ' + '\n' + str(kidPy.captions) + '\n\n')
print('main_opts: ' + '\n' + str(kidPy.main_opts) + '\n\n')
print('plot_caption:' + '\n' + str(kidPy.plot_caption) + '\033[0m\n\n')
print('plot_opts' + '\n' + str(kidPy.plot_opts) + '\n\n')

print('Testing openStoredSweep()\n\n')
Is, Qs= kidPy.openStoredSweep('./example_vna_sweep/')
print('Is shape: ' + str(Is.shape)+'  ,  Qs shape: ' + str(Qs.shape))

print('Testing plotVNASweep()\n\n')
kidPy.plotVNASweep(path)

print('Testing filter_trace()\n\n')
bb_freqs = np.load(path + 'bb_freqs.npy')
sweep_freqs = np.load(path + 'sweep_freqs.npy')
chan_freqs, mags= kidPy.filter_trace(path, bb_freqs, sweep_freqs)
plt.plot(chan_freqs, mags)
plt.title('Mags')
plt.xlabel('chan_freqs')
plt.ylabel('mags')
plt.savefig(path + 'Mags.png')
plt.close()

print('Testing lowpass_cosine()\n\n')
f_3db= (1.0 / kidPy.smoothing_scale)
filtered= kidPy.lowpass_cosine(mags, kidPy.lo_step, f_3db, 0.1*f_3db, padd_data=True)
plt.plot(chan_freqs, filtered)
plt.title('lowpass_cosine Filtered Mags')
plt.xlabel('chan_freqs')
plt.ylabel('filtered')
plt.savefig(path + 'lowpass_cosinePlot.png')
plt.close()

# Other Plots
plt.plot(chan_freqs, mags-filtered)
plt.title('Mags Minus Filtered Mags')
plt.xlabel('chan_freqs')
plt.ylabel('mags-filtered')
plt.savefig(path + 'MagsMinusFiltermags.png')
plt.close()

plt.plot(chan_freqs)
plt.title('Chan Freqs')
plt.ylabel('chan_freqs')
plt.savefig(path + 'ChanFreqs.png')
plt.close()


print('Testing findFreqs()\n\n')
kidPy.findFreqs(path, plot=True)

