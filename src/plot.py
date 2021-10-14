import matplotlib.pyplot as plt

def plot_csv(data):

    x = data[0]
    ys = data[1:]

    plt.xlabel("X-Axis")
    plt.xlabel("X-Axis")
    plt.title("Some numbers")

    for y in ys:
        plt.plot(x, y)
    plt.legend()
    plt.show()

