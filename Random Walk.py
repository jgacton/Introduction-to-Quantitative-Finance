import random
import matplotlib.pyplot as plt


def geometric_random_walk(length, bias):
    value = 100
    values = [value]

    for i in range(1, length):
        a = random.randint(1, 100)
        if a <= (bias * 100):
            value = value * 0.99
        else:
            value = value * 1.01
        values.append(value)

    plt.plot(values)
    plt.ylabel("Simulated Values")
    plt.show()


def arithmetic_random_walk():
    value = 100
    values = [value]

    for i in range(1, 1000):
        a = random.randint(1, 100)
        if a <= 50:
            value += 1
        else:
            value -= 1
        values.append(value)

    plt.plot(values)
    plt.ylabel("Simulated Values")
    plt.show()


geometric_random_walk(10000, 0.5)
