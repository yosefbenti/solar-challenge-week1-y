import os
import streamlit as st
from utils import data_processing, stats  # Assuming these exist and are correct
import pandas as pd

def load_all_data():
    files = {
        'Benin': 'data/benin_clean.csv',
        'Sierra Leone': 'data/sierraleone_clean.csv',
        'Togo': 'data/togo_clean.csv'
    }
    dfs = []
    countries = []
    for country, filepath in files.items():
        if os.path.exists(filepath):
            df = data_processing.load_data(filepath)
            dfs.append(df)
            countries.append(country)
        else:
            st.warning(f"File not found: {filepath}")
    return dfs, countries

def show_summary_table(dfs, countries):
    # Build a summary DataFrame with mean, median, std for GHI, DNI, DHI per country
    summary_rows = []
    for df, country in zip(dfs, countries):
        summary_rows.append({
            'Country': country,
            'GHI Mean': df['GHI'].mean(),
            'GHI Median': df['GHI'].median(),
            'GHI Std': df['GHI'].std(),
            'DNI Mean': df['DNI'].mean(),
            'DNI Median': df['DNI'].median(),
            'DNI Std': df['DNI'].std(),
            'DHI Mean': df['DHI'].mean(),
            'DHI Median': df['DHI'].median(),
            'DHI Std': df['DHI'].std()
        })
    summary_df = pd.DataFrame(summary_rows)
    st.subheader("Summary Statistics by Country")
    st.dataframe(summary_df)

def plot_boxplots(dfs, countries):
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    # Combine data adding 'Country' column for plotting
    combined = pd.DataFrame()
    for df, country in zip(dfs, countries):
        tmp = df.copy()
        tmp['Country'] = country
        combined = pd.concat([combined, tmp])
    
    metrics = ['GHI', 'DNI', 'DHI']
    for metric in metrics:
        plt.figure(figsize=(8, 5))
        sns.boxplot(x='Country', y=metric, data=combined)
        plt.title(f'Boxplot of {metric} by Country')
        st.pyplot(plt)
        plt.clf()

def run_ghi_anova(dfs):
    from scipy.stats import f_oneway, kruskal
    # Collect GHI values for each country
    ghi_values = [df['GHI'].dropna() for df in dfs]
    
    # Run ANOVA
    f_stat, p_val = f_oneway(*ghi_values)
    
    st.subheader("ANOVA test for GHI differences across countries")
    st.write(f"F-statistic: {f_stat:.4f}")
    st.write(f"P-value: {p_val:.4e}")
    
    if p_val < 0.05:
        st.write("There is a statistically significant difference in GHI between countries.")
    else:
        st.write("No statistically significant difference detected in GHI between countries.")

def main():
    st.title("Solar Challenge: Cross-Country Comparison")

    dfs, countries = load_all_data()

    if not dfs:
        st.error("No data files found. Please add cleaned CSV files to the 'data' folder.")
        return

    show_summary_table(dfs, countries)
    plot_boxplots(dfs, countries)
    run_ghi_anova(dfs)

    st.markdown("""
    ### Key Observations:
    - Summarize your observations here.
    - Example: Country X shows highest median GHI but also greatest variability.
    - Example: Statistical testing indicates significant differences between countries.
    """)

if __name__ == "__main__":
    main()
