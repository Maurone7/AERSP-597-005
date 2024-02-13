import numpy as np; import matplotlib.pyplot as plt

func_m = lambda ratio, m: (m/ratio + ratio/m)**2
m  = 0

ranges_list = [np.linspace(0, np.sqrt(2), 100), np.linspace(np.sqrt(2), np.sqrt(6), 100), np.linspace(np.sqrt(6), np.sqrt(12), 100), np.linspace(np.sqrt(12), np.sqrt(20), 100)]
for ranges in ranges_list:
    m += 1
    plt.plot(ranges, func_m(ranges, m), label='m = {}'.format(m))
plt.xlabel(r'$\frac{a}{b}$'), plt.ylabel('k'), plt.legend(), plt.title(r'$k=(\frac{mb}{a}+\frac{a}{mb})^2$'), plt.xlim(0, 5), plt.ylim(2, 9)
plt.savefig('output.png')