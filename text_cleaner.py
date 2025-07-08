import pandas as pd
import re


def clean_text(text):
    if pd.isnull(text):
        return ""
    text = text.lower().replace('\n', ' ')
    text = text.replace('’', "'").replace(
        '“', '"').replace('”', '"').replace('—', '-')
    text = re.sub(r"[^a-z0-9\s\.\?!]", "", text)  # keep . ? !
    text = re.sub(r"\s+", " ", text).strip()
    return text
