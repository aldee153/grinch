# Derive text related metrics (number of characters, words, lines, unique words) and lexical density for the movie script.

# characters, words, lines
df['#characters'] = df.lyrics.str.len()