import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution

class Binomial(Distribution):
    """ Binomial distribution class for calculating and 
        visualizing a Binomial distribution.
        
        Attributes:
            mean (float) representing the mean value of the distribution
            stdev (float) representing the standard deviation of the distribution
            data_list (list of floats) a list of floats to be extracted from the data file
            p (float) representing the probability of an event occurring
                    
        """
    def __init__(self, p = 0.5, n = 20 ): 
    
        self.p = p 
        self.n = n 

        Distribution.__init__(self, self.calculate_mean(), self.calculate_stdev())  

    def calculate_mean(self): 
        """Function to calculate the mean from p and n
        
        Args: 
            None
        
        Returns: 
            float: mean of the data set
    
        """
        self.mean = self.p * self.n
        return self.mean
         
    def calculate_stdev(self):
        """Function to calculate the standard deviation from p and n.
        
        Args: 
            None
        
        Returns: 
            float: standard deviation of the data set
    
        """
        self.stdev = math.sqrt(self.n * self.p * (1 - self.p))
        return self.stdev

    def replace_stats_with_data(self):
        """Function to calculate p and n from the data set. The function updates the p and n variables of the object.
        
        Args: 
            None
        
        Returns: 
            float: the p value
            float: the n value
    
        """
        self.n = len(self.data)
        self.p= sum(self.data) / len(self.data)
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()

        return self.p, self.n 

    def plot_bar(self):
        """Function to output a bar chart of the data set."""
        counts = [self.n - sum(self.data), sum(self.data)]
        plt.figure(figsize=(10, 6))
        bars = plt.bar(['0', '1'], counts, color=['lightblue', 'lightgreen'])
        plt.title('Bar Chart of Data', fontsize=16)
        plt.xlabel('Outcome', fontsize=12)
        plt.ylabel('Count', fontsize=12)
        plt.xticks(fontsize=10)
        plt.yticks(fontsize=10)
        
        # Add value labels on top of each bar
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height,
                     f'{height}',
                     ha='center', va='bottom')
        
        plt.tight_layout()
        plt.show()

    def pdf(self, k):
        """Probability density function calculator for the binomial distribution."""
        a = math.factorial(self.n) / (math.factorial(k) * math.factorial(self.n - k))
        b = (self.p ** k) * ((1 - self.p) ** (self.n - k))
        return a * b

    def plot_pdf(self):
        """Function to plot the pdf of the binomial distribution."""
        x = list(range(self.n + 1))
        y = [self.pdf(k) for k in x]
        
        plt.figure(figsize=(12, 6))
        bars = plt.bar(x, y, color='skyblue', alpha=0.7)
        plt.title('Probability Density Function of Binomial Distribution', fontsize=16)
        plt.xlabel('Number of Successes', fontsize=12)
        plt.ylabel('Probability', fontsize=12)
        plt.xticks(fontsize=10)
        plt.yticks(fontsize=10)
        
        # Add value labels on top of each bar
        for bar in bars:
            height = bar.get_height()
            if height > 0.01:  # Only label bars with significant probability
                plt.text(bar.get_x() + bar.get_width()/2., height,
                         f'{height:.3f}',
                         ha='center', va='bottom', fontsize=8)
        
        plt.tight_layout()
        plt.show()
        
        return x, y
    
    def __add__(self, other):
   
        
        """Function to add together two Binomial distributions with equal p
        
        Args:
            other (Binomial): Binomial instance
            
        Returns:
            Binomial: Binomial distribution
            
        """
        
        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise
        
        result = Binomial()
        result.n = self.n + other.n
        result.p = self.p
        result.calculate_mean()
        result.calculate_stdev()
        
        return result
    
    def __repr__(self):
        """Function to output the characteristics of the Binomial instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the Binomial object
        
        """
        return f"mean {self.mean}, standard deviation {self.stdev}, p {self.p}, n {self.n}"