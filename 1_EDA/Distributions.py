# Now that we have text metrics, a quick histogram spread on all metrics.

# Most script lines are under X characters, X lines, X words.
# Most script lines use around X unique words
# Lexical density is spread across, mostly curved up between X and X.

# Lexical density is pretty high considering how other singer's lyrics usually are.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df.hist(sharey=True, layout=(2, 3), figsize=(15, 8));

# Plot violin plots for distributions
cols_metrics = df.select_dtypes(include=[np.number]).columns
fig, axs = plt.subplots(ncols=len(cols_metrics), figsize=(16, 5))
# Word Length Distribution
pd.Series(len(x) for x in ' '.join(df.script).split()).value_counts().sort_index().plot(kind='bar', figsize=(12, 3))
# Looking at the word lengths, median length is 4 letters. But there exists decent long tail of longer length words.


