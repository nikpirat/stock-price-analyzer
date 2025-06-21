import unittest
import pandas as pd
from src.visualizer import plot_price, plot_moving_averages, plot_daily_returns_histogram

class TestVisualizer(unittest.TestCase):

    def setUp(self):
        """Setup sample data for testing"""
        self.df = pd.DataFrame({
            'Date': ['2025-01-01', '2025-01-02', '2025-01-03', '2025-01-04', '2025-01-05'],
            'Close': [151.10, 152.40, 153.20, 154.10, 155.50]
        })
        self.df['Date'] = pd.to_datetime(self.df['Date'])

    def test_plot_price(self):
        """Test that plot_price runs without error"""
        try:
            plot_price(self.df)
        except Exception as e:
            self.fail(f"plot_price raised {e} unexpectedly!")

    def test_plot_moving_averages(self):
        """Test that plot_moving_averages runs without error"""
        try:
            plot_moving_averages(self.df)
        except Exception as e:
            self.fail(f"plot_moving_averages raised {e} unexpectedly!")

    def test_plot_daily_returns_histogram(self):
        # Calculate the daily return before plotting
        self.df['Daily Return'] = self.df['Close'].pct_change()

        # Now call the plotting function
        try:
            plot_daily_returns_histogram(self.df)
        except Exception as e:
            self.fail(f"plot_daily_returns_histogram raised {e} unexpectedly!")

if __name__ == '__main__':
    unittest.main()