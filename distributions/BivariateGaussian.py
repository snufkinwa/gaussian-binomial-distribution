import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution

class BivariateGaussian(Distribution):
    def __init__(self, mu_x=0, mu_y=0, sigma_x=1, sigma_y=1, rho=0):
        super().__init__()
        self.mean_x = mu_x
        self.mean_y = mu_y
        self.stdev_x = sigma_x
        self.stdev_y = sigma_y
        self.rho = rho

    def pdf(self, x, y):
        """Probability density function calculator for the bivariate normal distribution.
        
        Args:
            x (float): x-coordinate point for calculating the probability density function
            y (float): y-coordinate point for calculating the probability density function
            
        Returns:
            float: probability density function output
        """
        factor = 1.0 / (2 * math.pi * self.stdev_x * self.stdev_y * math.sqrt(1 - self.rho**2))
        exponent = -1.0 / (2 * (1 - self.rho**2)) * (
            ((x - self.mean_x) / self.stdev_x)**2 + 
            ((y - self.mean_y) / self.stdev_y)**2 - 
            2 * self.rho * ((x - self.mean_x) / self.stdev_x) * ((y - self.mean_y) / self.stdev_y)
        )
        return factor * math.exp(exponent)

    def generate_grid(self, x_min, x_max, y_min, y_max, step):
        x_values = []
        y_values = []
        z_values = []

        x = x_min
        while x <= x_max:
            y = y_min
            while y <= y_max:
                z = self.pdf(x, y)
                x_values.append(x)
                y_values.append(y)
                z_values.append(z)
                y += step
            x += step

        return x_values, y_values, z_values

    def plot_bivariate_normal(self, x_values, y_values, z_values):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_trisurf(x_values, y_values, z_values, cmap='coolwarm', edgecolor='none')
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.set_zlabel('Probability Density')
        plt.show()
