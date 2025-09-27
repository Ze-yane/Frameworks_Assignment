import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from wordcloud import WordCloud
import re

# Set the page title and layout
st.set_page_config(page_title="Exploring the CORD-19 Metadata", layout="wide")

# Function to load the dataset (cached for performance)
@st.cache_data
def load_data():
    return pd.read_csv("metadata.csv")

# Load and preprocess dataset
df = load_data()

# Convert publish_time to datetime and extract year
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year
df['title'] = df['title'].fillna('')

# ---- Sidebar Filters ----
st.sidebar.header("Filters")

# Year range filter
year_min, year_max = int(df['year'].min()), int(df['year'].max())
year_range = st.sidebar.slider(
    "Select Year Range",
    year_min,
    year_max,
    (year_min, year_max)
)

# Number of top journals to show
n_journals = st.sidebar.slider("Number of Top Journals", 5, 50, 20)

# Number of top sources to show
n_sources = st.sidebar.slider("Number of Top Sources", 5, 50, 20)

# Number of rows to preview
n_rows = st.sidebar.slider("Number of Records to Preview", 5, 100, 25)

# Apply year filter
df_filtered = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# ---- Main Content ----

st.title("Exploring the CORD-19 Metadata")

# Publications over time
st.subheader("Publications Over Time")
counts = df_filtered['year'].value_counts().sort_index()
fig, ax = plt.subplots()
sns.barplot(x=counts.index, y=counts.values, ax=ax, color="skyblue")
ax.set_title("Publications per Year")
ax.set_xlabel("Year")
ax.set_ylabel("Number of Papers")
plt.xticks(rotation=45)
st.pyplot(fig)

# Top journals (if available)
if 'journal' in df.columns:
    st.subheader(f"Top {n_journals} Journals")
    top_journals = df_filtered['journal'].value_counts().head(n_journals)
    fig, ax = plt.subplots()
    sns.barplot(y=top_journals.index, x=top_journals.values, ax=ax, palette="viridis")
    ax.set_title("Top Journals by Paper Count")
    ax.set_xlabel("Number of Papers")
    ax.set_ylabel("Journal")
    st.pyplot(fig)

# Frequent words in titles (table + wordcloud)
st.subheader("Frequent Title Words (Top 25)")
stopwords = set(['the','and','of','in','to','for','a','on','with','by','an'])
words = Counter()
for t in df_filtered['title']:
    tokens = re.sub(r'[^a-zA-Z0-9\s]', '', t.lower()).split()
    for w in tokens:
        if w not in stopwords and len(w) > 1:
            words[w] += 1
words_df = pd.DataFrame(words.most_common(25), columns=["Word", "Count"])
st.table(words_df)

# Word Cloud of titles
st.subheader("Word Cloud of Paper Titles")
text = " ".join(df_filtered['title'].dropna().astype(str))
if text.strip():
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)
else:
    st.write("No titles available for word cloud.")

# Distribution of paper count by source
st.subheader(f"Top {n_sources} Sources by Paper Count")
if 'source_x' in df.columns:
    source_col = 'source_x'
elif 'journal' in df.columns:
    source_col = 'journal'
else:
    source_col = None

if source_col:
    top_sources = df_filtered[source_col].value_counts().head(n_sources)
    fig, ax = plt.subplots()
    sns.barplot(y=top_sources.index, x=top_sources.values, ax=ax, palette="magma")
    ax.set_title("Top Sources by Paper Count")
    ax.set_xlabel("Number of Papers")
    ax.set_ylabel("Source")
    st.pyplot(fig)
else:
    st.write("No source or journal column available.")

# Show sample of data
st.subheader(f"Sample of {n_rows} Records")
st.dataframe(df_filtered[['title','year','abstract']].head(n_rows))
