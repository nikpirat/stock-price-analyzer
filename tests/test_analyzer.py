import unittest
import pandas as pd
from src.analyzer import moving_average, summary_stats, calculate_daily_return


class TestAnalyzer(unittest.TestCase):

    def setUp(self):
        """Setup sample data for testing"""
        self.df = pd.DataFrame({
            'Date': ['2025-01-01', '2025-01-02', '2025-01-03', '2025-01-04', '2025-01-05'],
            'Open': [150.12, 151.20, 152.50, 153.30, 154.00],
            'High': [152.50, 153.00, 154.00, 155.20, 156.00],
            'Low': [149.80, 150.10, 151.00, 152.00, 153.20],
            'Close': [151.10, 152.40, 153.20, 154.10, 155.50],
            'Volume': [1200000, 1150000, 1250000, 1100000, 1300000]
        })
        self.df['Date'] = pd.to_datetime(self.df['Date'])

    def test_calculate_returns(self):
        """Test that daily returns are calculated correctly"""
        df_with_returns = calculate_daily_return(self.df)
        self.assertTrue('Daily Return' in df_with_returns.columns)  # Ensure 'Daily Return' column exists
        self.assertAlmostEqual(df_with_returns['Daily Return'][1], (152.40 - 151.10) / 151.10, places=5)

    def test_moving_average(self):
        """Test moving average calculation"""
        df_ma = moving_average(self.df, window=3)
        self.assertEqual(len(df_ma), len(self.df))  # Same length as input
        self.assertTrue(df_ma.isna().sum() < 3)  # Ensure that the first few are NaN due to the window size

    def test_summary_stats(self):
        # Ensure 'Daily Return' is calculated
        self.df = calculate_daily_return(self.df)

        # Call summary_stats with the updated DataFrame
        stats = summary_stats(self.df)

        # Perform your assertions on the stats
        self.assertIn('mean', stats)
        self.assertIn('volatility', stats)
        self.assertIn('max', stats)
        self.assertIn('min', stats)


if __name__ == '__main__':
    unittest.main()
