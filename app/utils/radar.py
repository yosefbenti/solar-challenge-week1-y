import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def show_radar_chart(df):
    # Define categories for the radar chart
    categories = ['GHI', 'DNI', 'DHI', 'ModA', 'ModB']
    
    # Make sure all categories exist in the dataframe
    categories = [cat for cat in categories if cat in df.columns]
    
    if not categories:
        st.warning("No valid columns found for radar chart.")
        return
    
    # Get average values for these categories
    values = df[categories].mean().values.flatten().tolist()
    values += values[:1]  # Repeat the first value to close the loop
    
    # Calculate angles for each axis in the plot
    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
    angles += angles[:1]  # Complete the loop
    
    # Create polar subplot
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    
    # Draw the outline of the radar chart
    ax.fill(angles, values, color='red', alpha=0.25)
    ax.plot(angles, values, color='red', linewidth=2)
    
    # Set category labels
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    
    # Optional: set range of radial axis (you can customize)
    ax.set_ylim(0, max(values)*1.1)
    
    # Display the plot with Streamlit
    st.pyplot(fig)
