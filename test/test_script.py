import pytest
from distributions import Gaussian, Binomial, BivariateGaussian

def test_gaussian():
    gaussian = Gaussian(mu=5, sigma=2)
    gaussian.read_data_file('./data/gaussian_data.txt')

    mean = gaussian.calculate_mean()
    assert mean == pytest.approx(78.09, rel=1e-2), f"Expected mean: 78.09, got: {mean}"

    stdev = gaussian.calculate_stdev()
    assert stdev == pytest.approx(92.87, rel=1e-2), f"Expected stdev: 92.87, got: {stdev}"

    pdf_value = gaussian.pdf(76)
    assert pdf_value == pytest.approx(0.00429, rel=1e-2), f"Expected PDF value: ~0.0042, got: {pdf_value}"

    gaussian2 = Gaussian(mu=10, sigma=3)
    gaussian_sum = gaussian + gaussian2
    assert gaussian_sum.mean == pytest.approx(88.0, rel=1e-2), f"Expected sum mean: 88.0, got: {gaussian_sum.mean}"
    assert gaussian_sum.stdev == pytest.approx(92.923, rel=1e-2), f"Expected sum stdev: 92.92, got: {gaussian_sum.stdev}"

def test_binomial():
    binomial = Binomial(p=0.4, n=20)
    binomial.read_data_file('./data/binomial_data.txt')

    mean = binomial.calculate_mean()
    assert mean == pytest.approx(8.0, rel=1e-2), f"Expected mean: 8.0, got: {mean}"

    stdev = binomial.calculate_stdev()
    assert stdev == pytest.approx(2.190, rel=1e-2), f"Expected stdev: 2.190, got: {stdev}"

    p, n = binomial.replace_stats_with_data()
    assert p == pytest.approx(0.615, rel=1e-2), f"Expected p: 0.615, got: {p}"
    assert n == 13, f"Expected n: 13, got: {n}"

    pdf_value = binomial.pdf(5)
    assert pdf_value == pytest.approx(0.05439, rel=1e-2), f"Expected PDF value: ~0.0543, got: {pdf_value}"

    binomial1 = Binomial(p=0.4, n=25)
    binomial2 = Binomial(p=0.4, n=30)
    binomial_sum = binomial1 + binomial2
    assert binomial_sum.mean == pytest.approx(22.0, rel=1e-2), f"Expected sum mean: 22.0, got: {binomial_sum.mean}"
    assert binomial_sum.stdev == pytest.approx(3.633, rel=1e-2), f"Expected sum stdev: 3.633, got: {binomial_sum.stdev}"

def test_bivariate_gaussian():
    bivariate = BivariateGaussian(mu_x=5, mu_y=5, sigma_x=1.5, sigma_y=1.5, rho=0)

    pdf_value = bivariate.pdf(1, 2)
    expected_pdf_value = 0.0002734579110202697
    assert pdf_value == pytest.approx(expected_pdf_value, rel=1e-2), f"Expected PDF value: ~{expected_pdf_value}, got: {pdf_value}"

if __name__ == "__main__":
    pytest.main()
