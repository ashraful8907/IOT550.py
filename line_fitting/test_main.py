import unittest
import os
import pandas as pd
import numpy as np

class TestSyntheticData(unittest.TestCase):

    def setUp(self):
        """Load the data before running tests."""
        self.csv_path = 'synthetic_data.csv'
        self.plot_path = 'fit_plot.png'
        self.m_true = 2.0
        self.b_true = 5.0
        self.tolerance = 0.5

        # Load data if it exists
        if os.path.exists(self.csv_path):
            self.data = pd.read_csv(self.csv_path)
        else:
            self.data = None

    def test_csv_exists(self):
        """Check that the CSV file was created."""
        self.assertTrue(os.path.exists(self.csv_path), "CSV file not found!")

    def test_plot_exists(self):
        """Check that the plot file was saved."""
        self.assertTrue(os.path.exists(self.plot_path), "Plot file not found!")

    def test_data_is_numeric(self):
        """Ensure that all loaded data are numeric."""
        self.assertIsNotNone(self.data, "Data not loaded!")
        self.assertTrue(np.issubdtype(self.data['X'].dtype, np.number))
        self.assertTrue(np.issubdtype(self.data['Y'].dtype, np.number))

    def test_fit_line(self):
        """Check fitted slope/intercept are close to the true values."""
        X = self.data['X']
        Y = self.data['Y']
        m_fit, b_fit = np.polyfit(X, Y, 1)
        self.assertAlmostEqual(m_fit, self.m_true, delta=self.tolerance)
        self.assertAlmostEqual(b_fit, self.b_true, delta=self.tolerance)

if __name__ == '__main__':
    unittest.main()
