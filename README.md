# Exploring the CORD-19 Metadata

This notebook explores a subset of the **CORD-19 dataset**.  
We will perform data cleaning, preparation, analysis, and visualization to understand trends in COVID-19 research.

**Goals:**
- Inspect dataset structure and missing values  
- Clean and prepare data for analysis  
- Explore publication trends over time  
- Identify top journals and sources  
- Analyze frequent words in paper titles (table, bar chart, word cloud)


Tools used

Python 3.7+

pandas

matplotlib

seaborn

streamlit

wordcloud

jupyter

Usage
1. Run Jupyter Notebook

For data cleaning, EDA, and visualizations:

jupyter notebook notebook.ipynb

2. Run Streamlit App

For interactive exploration:

streamlit run app.py


🗂 Dataset

Source: Kaggle - CORD-19 Research Challenge Metadata

Sample used: 4000 rows for faster exploration

📊 Visualizations

Publications per year

Top journals and sources

Frequent title words (table & word cloud)

Interactive filters for deeper exploration

Conclusion

This project helps to:

Understand publication trends in COVID-19 research

Identify top journals and sources

Explore frequent themes in research titles

Both static (Notebook) and interactive (Streamlit) approaches are demonstrated.


## 📝 Findings

- The number of publications increased sharply in 2018, reflecting the global research response to COVID-19.  
- A few journals and sources contributed the majority of publications.  
- Frequent title words include **virus**, **influenza**, **infection**, **respiratory**, and **human**, showing common research themes.  
- The dataset contains many missing values in abstracts and sources, requiring cleaning before analysis.  

---

## ⚠️ Challenges

- Some columns had a high percentage of missing values (especially abstracts and source/journal).  
- The dataset was large, so I worked with a **sample of 4000 rows** for easier processing.  
- Handling different date formats and converting them into a usable **year column** required extra care.  
- Installing and running Streamlit for the first time took some setup effort.  

---

## 💡 Reflection

- This project improved my understanding of the **data science workflow**: cleaning, analyzing, visualizing, and deploying with Streamlit.  
- I learned how to build **interactive dashboards** and combine them with data exploration in Jupyter Notebook.  
- Working with real-world messy data taught me how important **data cleaning** is before analysis.  
- I also saw the value of **documentation** and **sharing code on GitHub** for reproducibility.  

