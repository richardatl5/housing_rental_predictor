import streamlit as st
import pandas as pd

def app():

    data = pd.read_csv('././ListVsRentBedsTotal.csv')

    st.write("""
    # Rental Price Data
    """)
    st.write("""When assessing the Zillow data from Quandl, we wanted to see if anything had a significant impact on rent prices. We looked at these three things:
    * The number of days a property is on Zillow and the effect that has on the rent price
    * Square footage of a property and the effect that has on rent price
    * Number of bedrooms a property has and the effect that has on rent price""")

    st.write('---')

    st.write('**Days on Zillow**')
    st.write('When looking at the number of days on Zillow and rent prices, the plot below shows there is not much of a correlation between the two. The r-squared is: 0.2424063747309388')
    st.image("././R-squared-DaysOnZillow.png")

    st.write("**Square Footage**")
    st.write('When looking at the square footage of a property and rent prices, the plot below shows there is some correlation between the two. The r-squared is: 0.7967550272920328')
    st.image("././R-squared-Sqft.png")

    st.write("**Number of Bedrooms**")
    st.write("""When looking at the number of bedrooms a property has and rent prices, the bottom row of plots in the Pairplot below shows there is definite correlation between the two.""")
    st.image("././PairPlot-#BR.png")

    st.write("""The plot below shows the high r-squared of: 0.9623828220461137 between Rent Prices and Median Rental Price for 3 bedroom rentals.""")
    st.image("././R-squared-#BR.png")

    st.write("**Conclusion**")
    st.write("""we see that the number of bedrooms a rental has plays a large part in rental prices. The square footage has a small impact, and the days the rental is listed on Zillow has a very small impact.""")
    



    


