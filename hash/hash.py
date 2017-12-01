import matplotlib.pyplot as plt
import numpy as np


# 11.3.1 The division method
def division_hash():
    n = 2000
    m = 701
    key = np.round(np.random.uniform(1, n, n))
    print key

    code = np.round([k % m for k in key])
    print code

    x = np.arange(n)
    print x

    key_his = np.histogram(key, range(n + 1))
    print key_his[0]
    print key_his[0].shape
    print sum(key_his[0])
    # print key_his[1]

    code_his = np.histogram(code, range(m + 1))
    print code_his[0]
    print code_his[0].shape
    print sum(code_his[0])

    plt.figure(1)

    plt.subplot(211)
    # plt.plot(range(n), key_his[0])
    plt.hist(key)

    # plt.xlabel('Smarts')
    # plt.ylabel('Probability')
    # plt.title('Histogram of IQ')
    # plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
    # plt.axis([-50, 2100, 0, max(key_his[0]) + 2])
    # plt.grid(True)

    # plt.subplot(212)
    # plt.scatter(range(n), code, s=area, c=colors, alpha=0.5)
    # plt.hist(code_his, bins=range(m + 1))
    # plt.plot(range(m), code_his[0])
    # plt.hist(key)

    # plt.xlabel('Smarts')
    # plt.ylabel('Probability')
    # plt.title('Histogram of IQ')
    # plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
    # plt.axis([-50, 800, 0, max(code_his[0]) + 2])
    # plt.grid(True)

    plt.savefig('division_hash.png')
    # plt.show()


if __name__ == '__main__':
    division_hash()
