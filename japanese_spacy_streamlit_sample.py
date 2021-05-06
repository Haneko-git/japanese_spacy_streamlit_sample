"""
-reference
spacy_streamlit link:https://github.com/explosion/spacy-streamlit
spacy model download link:https://spacy.io/models/ja

-install
>pip install spacy-streamlit --pre

-model download
>python -m spacy download ja_core_news_sm
>python -m spacy download ja_core_news_md
>python -m spacy download ja_core_news_lg

-usage
>streamlit run japanese_spacy_streamlit_sample.py
"""
import spacy_streamlit

models = ["ja_core_news_md", "ja_core_news_sm"]
default_text = "もうすぐ梅雨。日本のオリンピックはどうなる？"
spacy_streamlit.visualize(models, default_text)
