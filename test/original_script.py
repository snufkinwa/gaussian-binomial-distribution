from distributions import Gaussian, Binomial, BivariateGaussian

def test_gaussian():
    print("\nTesting Gaussian Class\n" + "-"*50)
    # Create a Gaussian distribution instance
    gaussian = Gaussian(mu=5, sigma=2)
    
     # Read data from the file
    gaussian.read_data_file('gaussian_data.txt')

    # Test calculate_mean method
    mean = gaussian.calculate_mean()
    print(f"Calculated mean: {mean}")

    # Test calculate_stdev method
    stdev = gaussian.calculate_stdev()
    print(f"Calculated standard deviation: {stdev}")

    # Test plot_histogram method
    print("Plotting histogram...")
    gaussian.plot_histogram()

    # Test pdf method
    x = 5
    pdf_value = gaussian.pdf(x)
    print(f"PDF value at {x}: {pdf_value}")

    # Test plot_histogram_pdf method
    print("Plotting histogram with PDF...")
    gaussian.plot_histogram_pdf()

    # Test the __add__ method
    gaussian2 = Gaussian(mu=10, sigma=3)
    gaussian_sum = gaussian + gaussian2
    print(f"Sum of Gaussians: mean {gaussian_sum.mean}, standard deviation {gaussian_sum.stdev}")

    # Test the __repr__ method
    print(gaussian)

def test_binomial():
    print("\nTesting Binomial Class\n" + "-"*50)
    # Create a Binomial distribution instance
    binomial = Binomial(p=0.4, n=20)
    
    # Add some data
    binomial.read_data_file('binomial_data.txt')

    # Test calculate_mean method
    mean = binomial.calculate_mean()
    print(f"Calculated mean: {mean}")

    # Test calculate_stdev method
    stdev = binomial.calculate_stdev()
    print(f"Calculated standard deviation: {stdev}")

    # Test replace_stats_with_data method
    p, n = binomial.replace_stats_with_data()
    print(f"Calculated p: {p}, Calculated n: {n}")

    # Test plot_bar method
    print("Plotting bar chart of expected counts...")
    binomial.plot_bar()

    # Test pdf method
    k = 5
    pdf_value = binomial.pdf(k)
    print(f"PDF value at {k}: {pdf_value}")

    # Test plot_pdf method
    print("Plotting PDF...")
    binomial.plot_pdf()

    # Test the __add__ method
    binomial1 = Binomial(p=0.4, n =25)
    binomial2 = Binomial(p=0.4, n=30)

    binomial_sum = binomial1 + binomial2
    print(f"Sum of Binomials: mean {binomial_sum.mean}, standard deviation {binomial_sum.stdev}, p {binomial_sum.p}, n {binomial_sum.n}")

    # Test the __repr__ method
    print(binomial)

def test_bivariate_gaussian():
    print("\nTesting Bivariate Gaussian Class\n" + "-"*50)
    # Create a Bivariate Gaussian distribution instance
    bivariate = BivariateGaussian(mu_x=5, mu_y=5, sigma_x=1.5, sigma_y=1.5, rho=0)

    # Test pdf method
    x, y = 1, 2
    pdf_value = bivariate.pdf(x, y)
    print(f"PDF value at ({x}, {y}): {pdf_value}")

    # Test generate_grid and plot_bivariate_normal methods
    print("Generating grid and plotting bivariate normal distribution...")
    x_values, y_values, z_values = bivariate.generate_grid(0, 10, 0, 10, 0.1)
    bivariate.plot_bivariate_normal(x_values, y_values, z_values)

if __name__ == "__main__":
    test_gaussian()
    test_binomial()
    test_bivariate_gaussian()
