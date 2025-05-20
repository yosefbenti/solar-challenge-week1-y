import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# This must be the very first Streamlit command!
st.set_page_config(page_title="Solar Dashboard", layout="centered")

def load_uploaded_data():
    st.sidebar.header("Upload CSV Files")
    benin_file = st.sidebar.file_uploader("Upload benin_clean.csv", type=["csv"])
    sierra_file = st.sidebar.file_uploader("Upload sierraleone_clean.csv", type=["csv"])
    togo_file = st.sidebar.file_uploader("Upload togo_clean.csv", type=["csv"])

    if benin_file and sierra_file and togo_file:
        df1 = pd.read_csv(benin_file)
        df2 = pd.read_csv(sierra_file)
        df3 = pd.read_csv(togo_file)
        df1['Country'] = 'Benin'
        df2['Country'] = 'Sierra_Leone'
        df3['Country'] = 'Togo'
        return pd.concat([df1, df2, df3], ignore_index=True)
    else:
        st.warning("Please upload all three CSV files from the sidebar to proceed.")
        return None

# Comment out or remove the old load_data() usage
# df = load_data()

df = load_uploaded_data()

if df is not None:
    st.title("Cross-Country Solar Energy Dashboard")

    countries = st.multiselect("Select Countries", df['Country'].unique(), default=list(df['Country'].unique()))
    metric = st.selectbox("Select Metric", ['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'RH', 'WS', 'WSgust',
                'WSstdev','WD','WDstdev','BP','Cleaning','Precipitation',
                'TModA','TModB'])

    filtered_df = df[df['Country'].isin(countries)]

    st.subheader(f"{metric} Distribution by Country")
    fig, ax = plt.subplots()
    sns.boxplot(x='Country', y=metric, data=filtered_df, ax=ax, palette='Set3')
    st.pyplot(fig)

    st.subheader("Top Regions by Average GHI")
    top = df.groupby('Country')['GHI'].mean().sort_values(ascending=False).reset_index()
    st.dataframe(top)
