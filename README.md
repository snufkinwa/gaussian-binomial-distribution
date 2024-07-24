<p align="center">
<img src="https://i.imgur.com/t4n96Yg.png" width="500px">
</p>

# Gaussian and Binomial Distributions Package

This Python package provides tools for calculating and visualizing Gaussian and Binomial distributions. It is a part of the AWS AI/ML Scholarship program and is particularly useful in educational and practical applications within the fields of Machine Learning and Artificial Intelligence.

## Key Applications in Machine Learning and AI

- **Data Modeling**: Both Gaussian and Binomial distributions are crucial in the statistical modeling of data, which is a fundamental aspect of training and evaluating AI models.
- **Feature Engineering**: Understanding the distribution of various features can help in creating better features that improve machine learning models.
- **Algorithm Assumptions**: Many machine learning algorithms assume data to be normally distributed. This package can help in verifying these assumptions.
- **Performance Metrics**: Binomial distribution is particularly useful in classification tasks where the outcome is binary, such as computing the probability of success or failure.

## Installation

Clone this repository to your local machine:

```bash
git clone git@github.com:snufkinwa/gaussian-binomial-distribution.git
```

Navigate into the package directory:

```bash
cd gaussian-binomial-distribution
```

Install the package:

```bash
pip install .
```

## Usage

### Gaussian Distribution

To use the Gaussian distribution module:

```python
from distributions import Gaussian

# Create a Gaussian distribution instance
gaussian = Gaussian(mu=5, sigma=2)

# Read data from a file
gaussian.read_data_file('gaussian_data.txt')

# Calculate mean and standard deviation
mean = gaussian.calculate_mean()
stdev = gaussian.calculate_stdev()

# Plot histogram and PDF
gaussian.plot_histogram_pdf()

# Plot 3D histogram and PDF
gaussian.plot_3d_histogram_pdf()

```

#### Histogram of Data and Probability Density Function

<p align="center">
<img src="https://i.imgur.com/0zpMODP.png" width="400px">
</p>
<p align="center">
<img src="https://i.imgur.com/7XXuLlQ.png" width="400px">
</p>

### Binomial Distribution

To use the Binomial distribution module:

```python
from distributions import Binomial

# Create a Binomial distribution instance
binomial = Binomial(p=0.4, n=20)

# Read data from a file
binomial.read_data_file('binomial_data.txt')

# Calculate mean and standard deviation
mean = binomial.calculate_mean()
stdev = binomial.calculate_stdev()

# Plot histogram and PDF
binomial.plot_bar()
binomial.plot_pdf()
```

#### Bar Chart

<p align="center">
<img src="https://i.imgur.com/ZAnpLOX.png" width="400px">
</p>

#### Probability Density Function

<p align="center">
<img src="https://i.imgur.com/K8r6QGU.png" width="400px">
</p>

### Bivariate Gaussian

To use the Bivariate Gaussian distribution module:

```python
from distributions import BivariateGaussian

# Create a Bivariate Gaussian distribution instance
bivariate = BivariateGaussian(mu_x=5, mu_y=5, sigma_x=1, sigma_y=1, rho=0)

# Generate a grid of points
x_values, y_values, z_values = bivariate.generate_grid(0, 10, 0, 10, 0.1)

# Plot the Bivariate Gaussian distribution
bivariate.plot_bivariate_normal(x_values, y_values, z_values)

```

#### 3D Visualization

**Note:** This class is still being improved upon

<p align="center">
<img src="https://i.imgur.com/835Wl1D.png" width="400px">
</p>

## Acknowledgments

This project was developed with the help of hints and foundational code provided by [Udacity](https://github.com/udacity) as part of the AI Programming with Python.
