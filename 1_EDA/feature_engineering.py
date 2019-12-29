# Derive text related metrics (number of characters, words, lines, unique words) and lexical density for the movie script.

# Add count column of characters, words, lines
df['#characters'] = df.script.str.len()
df['#words'] = df.script.str.split().str.len()
df['#lines'] = df.script.str.split('\n').str.len()

# Add uniq words column
df['#uniq_words'] = df.script.apply(lambda x: len(set(x.split())))
# Divide uniq_words by words to create lexical density column
df['lexical_density'] = df['#uniq_words'] / df['#words']

df.head()

# df_2 = df.groupby(['script']).apply(' '.join).reset_index()

