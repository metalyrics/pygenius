import pandas as pd

def process_lyrics(string_lyrics):
    return [verse.strip() for verse in string_lyrics.splitlines() if verse.strip() != '']

def generate_lyrics_dataframe(string_lyrics):
    lyrics = process_lyrics(string_lyrics)
    current_tag = None
    tags = []
    verses = []
    for line in lyrics:
        if line[0] == '[':
            current_tag = line
        else:
            verses.append(line)
            tags.append(current_tag)
    df = pd.DataFrame({ 'verses': verses, 'tags': tags })
    return df