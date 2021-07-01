def weight_gain_when_healthy(chickweight_df):
    return(
        chickweight_df
        .assign(weight_diff=lambda x: x['weight'].diff())
        .assign(sick=chickweight_df.sick.fillna(0))
        .loc[lambda x: x['sick'] == 0, 'weight_diff']
        .mean()
    )

class TestWeightGainWhenHealthy(unittest.TestCase):
    def test_weight_gain_when_healthy_default(self):
        test_df = pd.DataFrame({
            'weight': [100, 105, 120, 120, 120],
            'sick': [0, 0, 0, 1, 1],
            'time': [0, 1, 2, 3, 4]
        })
        result = weight_gain_when_healthy(test_df)
        self.assertEqual(10, result)
    
    def test_weight_gain_when_healthy_dirty_data(self):
        test_df = pd.DataFrame({
            'weight': [100, 105, 120, 120, 120],
            'sick': [0, 0, 0, 'bar', 42],
            'time': [0, 1, 2, 3, 4]
        })
        result = weight_gain_when_healthy(test_df)
        self.assertEqual(10, result)
    
    def test_weight_gain_when_healthy_missing_data(self):
        test_df = pd.DataFrame({
            'weight': [100, 105, 120, 120, 120],
            'sick': [0, np.nan, None, 1, 1],
            'time': [0, 1, 2, 3, 4]
        })
        result = weight_gain_when_healthy(test_df)
        self.assertEqual(10, result)

unittest.main(argv=['ignored', '-v', 'TestWeightGainWhenHealthy'], exit=False)
