import unittest
import pandas as pd
from src.data_cleaner import clean_data

class TestDataCleaner(unittest.TestCase):

    def setUp(self):
        """Setup sample data for testing"""
        self.df = pd.DataFrame({
            'Date': ['2025-01-01', '2025-01-02', '2025-01-03', '2025-01-04', '2025-01-05'],
            'Open': [150.12, 151.20, 152.50, 153.30, 154.00],
            'High': [152.50, 153.00, 154.00, 155.20, 156.00],
            'Low': [149.80, 150.10, 151.00, 152.00, 153.20],
            'Close': [151.10, 152.40, 153.20, 154.10, None],  # Last value is None
            'Volume': [1200000, 1150000, 1250000, 1100000, 1300000]
        })

    def test_clean_data_remove_duplicates(self):
        """Test that exact duplicate rows are removed and NaN rows are dropped"""
        # Create an exact duplicate of the first row, ensuring all values and types match
        duplicate_row = pd.DataFrame([{
            'Date': pd.to_datetime('2025-01-01'),
            'Open': 150.12,
            'High': 152.50,
            'Low': 149.80,
            'Close': 151.10,
            'Volume': 1200000
        }])

        # Concatenate the duplicate row to the original DataFrame
        self.df = pd.concat([self.df, duplicate_row], ignore_index=True)

        # Clean data
        self.df_cleaned = clean_data(self.df)

        # Print the length before and after
        print(f"Before: {len(self.df)}, After: {len(self.df_cleaned)}")

        # The expected length should be 4, because 1 duplicate and 1 NaN row are removed
        self.assertEqual(len(self.df_cleaned), 4)

    def test_clean_data_remove_na(self):
        """Test that rows with NaN 'Close' values are removed"""
        self.df_cleaned = clean_data(self.df)
        self.assertTrue(self.df_cleaned['Close'].notna().all())  # No NaN values in 'Close'

    def test_clean_data_negative_prices(self):
        """Test that rows with negative prices are removed"""
        self.df.loc[2, 'Close'] = -1  # Set a negative value for 'Close'
        self.df_cleaned = clean_data(self.df)
        self.assertNotIn(-1, self.df_cleaned['Close'].values)  # Ensure negative prices are removed


if __name__ == '__main__':
    unittest.main()