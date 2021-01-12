""" Helper Classes """

import pandas as pd
import numpy as np


class Helpers(pd.DataFrame):
    def null_count(self):
        count = 0
        for col in self:
            count += self[col].isnull().sum()
        return count

    def randomize(self, seed):
        np.random.seed(seed=seed)
        return self.iloc[np.random.permutation(len(self))]