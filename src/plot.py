import matplotlib.pyplot as plt

def plot_csv(x, y):

    plt.xlabel("X-Axis")
    plt.xlabel("X-Axis")
    plt.title("Some numbers")

    for i in range(len(y[0])):
        plt.plot(x,[pt[i] for pt in y],label = 'id %s'%i)
        plt.legend()
        plt.show()

