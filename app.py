import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Set the title and icon of the app
st.set_page_config(
    page_title="E-commerce Data Analysis",
    page_icon="✊",
    layout="wide"
)

# Display headers and subheaders in your app
st.header('E-commerce Data Analysis')
st.subheader('🛒 | Explore Customer Shopping Habits, Churn, and Purchase Patterns')



# Load data_1
df = pd.read_csv("customer_data_1.csv")
df = df.drop(columns=df.columns[0])

# Loda data_2
RFM = pd.read_csv("RFM.csv")

cust_seg_count = RFM['Segment'].value_counts()
cust_seg_percent = cust_seg_count / cust_seg_count.sum() * 100
custom_order = ['High Value', 'Key Development', 'Normal Value', 'Churned High Value', 'Hibernated Normal Value']
cust_seg_ordered = cust_seg_count.reindex(custom_order, fill_value=0)



# Display text in your app
# Set the Subpages
tab1, tab2, tab3, tab4 = st.tabs(["Data", "Consumer Buying Trend Insights", "Demographic Analysis", "Customer Lifetime Value"])


# Frist page of 'Data Info Page'
with tab1:
   
    st.subheader("Description")
    st.markdown(''':bulb:
                The **E-commerce Customer Behavior and Purchase Dataset** is a synthetic dataset generated using the Faker Python library. 
                It is not real e-commerce data, so the analysis results do not have real-world significance.''')
    st.markdown(''':small_red_triangle:
                The purpose of using this virtual dataset is to provide a reference for e-commerce data analysis through some related analysis.''')
    with st.expander("Data Preview"):
        st.write(df)
        
    st.subheader("Column Information")
    with st.container(border=True):
        st.write('- Customer_ID: A unique identifier for each customer.')
        st.write('- Customer_Age: The age of the customer (generated by Faker).')
        st.write('- Gender: The gender of the customer (generated by Faker).')
        st.write('- Purchase_Date: The date of each purchase made by the customer.')
        st.write('- Product_Category: The category or type of the purchased product.')
        st.write('- Product_Price: The price of the purchased product.')
        st.write('- Quantity: The quantity of the product purchased.')
        st.write('- Per_Purchase_Amount: The product amount spent by the customer in each transaction.')
        st.write('- Payment_Method: The method of payment used by the customer (e.g., credit card, PayPal).')
        st.write('- Churn: A binary column indicating whether the customer has churned (0 for retained, 1 for churned).')
        st.write('- R: (Recency) The number of days between the consumer’s last consumption and the analysis date.')
        st.write('- F: (Frequency) The total number of purchases made by each customer.')
        st.write('- M: (Monetary) The total spending per customer.')
        st.write('- Age_Group: Age groups based on Age column.')

 
# The 2nd Page of 'Consumer Buying Trend Insights' page
with tab2:
    def Total_Sales_Distribution_by_Years():
        
        st.markdown(''':bulb:
                    :grey[Understanding sales distribution across different categories and years is crucial for businesses to make informed decisions and devise effective strategies.By exploring the trends and patterns in sales, businesses can gain valuable insights into consumer preferences, market trends, and potential areas for growth or improvement.]''')
        sale_by_year = df.groupby('Year')['Per_Purchase_Amount'].sum().reset_index(name='Amount')
        fig = px.bar(sale_by_year, x='Year', y='Amount',title ="Total Sales Distribution by Years")
        fig.update_layout(xaxis_type='category')
        st.plotly_chart(fig,use_container_width=True )
     

    def sales_amount_comparison_by_years():
        st.markdown(''':bulb:
                    :grey[In this analysis, we delve into the dynamics of sales distribution across various product categories such as home goods, electronics, books, and clothing over different years. By exploring the trends and patterns in sales, businesses can gain valuable insights into consumer preferences, market trends, and potential areas for growth or improvement.]''')
        selected_year = st.slider("Select Year", min_value=df['Year'].min(), max_value=df['Year'].max())
        filtered_df = df[df['Year'] == selected_year]
        fig = px.bar(filtered_df, x='Product_Category', y='Per_Purchase_Amount', title='Sales Comparison of Product Categories by Years',
                     labels={'Per_Purchase_Amount': 'Sales Amount', 'Product_Category': 'Category'})
        st.plotly_chart(fig)

    def sales_trend_by_months():
        st.markdown(''':bulb:
                    :grey[The categories we focus on - home goods, electronics, books, and clothing - represent diverse segments of consumer goods, each with its unique characteristics and market dynamics. By dissecting sales data within these categories, we aim to uncover actionable insights that can drive strategic decision-making and optimize resource allocation.]''')
        year_selected = st.slider("Year Select", min_value=df['Year'].min(), max_value=df['Year'].max())
        filtered_df = df[df['Year'] == year_selected]
        filtered_df_agg = df.groupby(["Month","Product_Category"])
        filtered_df_agg_sum = filtered_df_agg["Per_Purchase_Amount"].sum().reset_index(name = "Amount")
        fig = px.line(filtered_df_agg_sum, x='Month', y='Amount',color = "Product_Category",title='Sales Trends of Product Category over 12-months (2021-2024)',
              labels={'Amount': 'Sales Amount', 'Month': 'Month'})
        fig.update_xaxes(tickvals=list(range(1, 13)), ticktext=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
        st.plotly_chart(fig)

    def total_sales_trend():
        st.markdown(''':bulb:
                    :grey[Tracking the change in sales amounts over months provides businesses with critical insights into revenue patterns and consumer behavior throughout the year.Understanding how sales amounts vary from month to month enables businesses to anticipate demand, allocate resources efficiently, and tailor marketing strategies accordingly.]''')
        year_selected = st.slider("Year Selected", min_value=df['Year'].min(), max_value=df['Year'].max())
        filtered_df = df[df['Year'] == year_selected]
        filtered_df_agg = filtered_df.groupby(["Month"])["Per_Purchase_Amount"].sum().reset_index(name = "Amount")
        fig = px.line(filtered_df_agg, x='Month', y='Amount',title='Total Sales Trend over 12-months',
              labels={'Amount': 'Sales Amount', 'Month': 'Month'})
        fig.update_xaxes(tickvals=list(range(1, 13)), ticktext=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
        st.plotly_chart(fig)
    
    def main():
        st.subheader("Sales Analysis Dashboard")
        st.markdown('**Basic Info**')
        with st.expander("About Consumer Buying Trend Insights"):
            st.write("Total sales amount trend by years")
            st.write("Total sales amount comparison in four categories in different years")
            st.write("Sales Trend of Product Ctegories over 12 months")
            st.write("Total sales trend compariosn over 4 years")
        
        Total_Sales_Distribution_by_Years()

        sales_amount_comparison_by_years()

        sales_trend_by_months()

        total_sales_trend()

    if __name__ == "__main__":
        main()

    


# The 3rd Page of 'Demographic Analysis' page
with tab3:
    st.subheader("Demographic Analysis")
    st.markdown(''':bulb:
                :grey[Demographic Analysis analyzes customers' average purchase amount, favorite categories, and time buying habits by age group and gender.]''')
    st.markdown('**Basic Info**')
    with st.expander("About Demographic Analysis"):
        st.write("Average purchase amount by age group")
        st.write("Most popular product categories by different age groups")
        st.write("Most popular product categories by genders")
        st.write("Frequency distribution of purchase dates to identify peak shopping times (e.g., weekends, holidays, end of month)")
 
    age_groups = [20, 30, 40, 50, 60, 70, 80]

    def categorize_age(age):
        for i, group in enumerate(age_groups):
           if age <= group:
              if group == 20:
                  return f"{group}-{group + 9}"
              else:
                  return f"{group - 10}-{group - 1}"
        return f"{age_groups[-1]}+"   
    
    df['Age Group'] = df['Age'].apply(categorize_age)

    def generate_plots(year):
        
        st.markdown("**Average Purchase Amount by Age Group**",unsafe_allow_html=True)
        st.markdown(''':bulb: **Any help with data-driven decision-making?**''')
        st.write("Pricing strategy optimization: Adjust product prices to target age groups with higher purchasing power to increase revenue.")
        st.write("Targeted marketing campaigns: Develop targeted marketing strategies based on the purchasing habits of different age groups to increase sales conversion rates.")
        st.write("Product and Service Optimization: Understanding the preferences of high-purchasing-value age groups, improving product features and enhancing service quality to increase customer satisfaction.")

        average_purchase_by_age = df[df['Year'] == year].groupby(['Age Group'])['Per_Purchase_Amount'].mean().reset_index()
        fig = px.bar(average_purchase_by_age, x='Age Group', y='Per_Purchase_Amount', labels={'Per_Purchase_Amount': 'Average Purchase Amount'})
        st.plotly_chart(fig)
    
        st.markdown("**Most Popular Product Categories by Age Group**",unsafe_allow_html=True)
        st.markdown(''':bulb: **Any help with data-driven decision-making?**''')
        st.write("Product Development and Positioning: Adjust the product development direction and positioning strategy according to the product preferences of customers of different age groups.")
        st.write("Promotional activities and advertising: Develop targeted promotional activities and advertising strategies for different age groups.")
        st.write("Channel optimization: Adjust sales channels and distribution strategies according to the shopping preferences of customers of different age groups.")
        st.write("Market Segmentation and Customized Marketing: Target and customize marketing campaigns and personalized services to improve market coverage and sales efficiency.")

        popular_products_age = df[df['Year'] == year].groupby(['Age Group', 'Product_Category']).size().unstack().reset_index()
        fig = px.bar(popular_products_age, x='Age Group')
        st.plotly_chart(fig)
        
        st.markdown("**Most Popular Product Categories by Gender**",unsafe_allow_html=True)
        st.markdown(''':bulb: **Any help with data-driven decision-making?**''')
        st.write("Targeted marketing and advertising: marketing strategies and advertising content can be adjusted to better attract consumers of the target gender")
        st.write("Customer service and experience: customer service and shopping experience can be personalized.")
        st.write("Market Segmentation: Segmenting the market further to more accurately target and meet the needs of gender-specific consumers.")
        
        popular_products_gender = df[df['Year'] == year].groupby(['Gender', 'Product_Category']).size().unstack().reset_index()
        fig = px.bar(popular_products_gender, x='Gender')
        st.plotly_chart(fig)
    
   
    def main():
      
        st.markdown("**Purchase Analysis Dashboard**",unsafe_allow_html=True)
        year = st.selectbox("Select Year", [''] + list(df['Year'].unique()))
        
        if year:
           generate_plots(year)
    if __name__ == "__main__":
        main()



# The 4th Page of 'Customer Lifetime Value' page
with tab4:
    st.subheader("RFM Analysis for Customer Segmentation")
    st.markdown(''':bulb:
                :grey[RFM Analysis is a technique used for customer segmentation. It allows grouping customers based on their purchase behavior, enabling the development of strategies for each group.]''')
    st.markdown(''':pushpin:
                **Knowing about customer segments and their percentages can offer significant benefits to both marketing and product strategies.**''')
    st.markdown('**Targeted Campaign**: Tailor marketing campaigns to resonate more effectively with each group.')
    st.markdown('**Personalized Marketing**:  Leveraging customer segment information allows you to personalize your marketing efforts.')
    st.markdown('**Campaign Measurement and Optimization**: By tracking the performance of campaigns across different segments, allows you to optimize future campaigns and continuously improve their effectiveness:')


    st.write("  ")
    st.write("  ")

    st.markdown('**Basic Info**')
    with st.expander("About RFM"):
        st.write('Recency (How recently a customer has made a purchase)')
        st.write('Frequency (How often a customer makes purchases)')
        st.write('Monetary (How much money a customer spends)')
        st.write("  ")
        st.markdown('Based on RFM Score, customer are divided into 5 groups:')
        st.write("- High Value:  Who are loyal and contribute significantly to revenue. They deserve the most attention and personalized offers to retain them.")
        st.write("- Key Development:  Who require focused efforts to increase their purchase frequency or spending amount. Offer promotions, loyalty programs, or personalized recommendations to cultivate them to become high-value customers.")
        st.write("- Normal Value:  Who are valuable and should be nurtured to prevent them from churning. Regular communication, relevant offers, and a good customer experience can help maintain their loyalty.")
        st.write("- Churned High Value:  Who are worth attempting to win back. Analyze the reason for their churn and offer them targeted incentives or reactivation campaigns.")
        st.write("- Hibernated Normal Value:  They have low value but still have the potential to become active customers again. Consider targeted campaigns to re-engage them and remind them of the value you offer.")            

    with st.expander("Data Preview"):
        st.write(RFM)
    st.write('  ')
    
    st.markdown('**Visualizaiton**')
    col1, col2 = st.columns((2))
    with col1:
        st.markdown("**Customer Segments**", unsafe_allow_html=True)
        char_data = pd.DataFrame({'Segment': cust_seg_ordered.index, 'Count': cust_seg_ordered.values})
        fig = px.bar(char_data, x = 'Segment', y = 'Count')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("**Segments Percentage**", unsafe_allow_html=True)
        category_orders = {
        "High Value": 1,
        "Key Development": 2,
        "Normal Value": 3,
        "Churned High Value": 4,
        "Hibernated Normal Value": 5,
        }
        fig = px.pie(char_data, values="Count", names="Segment", hole=0.5,
             category_orders=category_orders)
        st.plotly_chart(fig, theme="streamlit")
    st.write('---')
    
    
    
    st.subheader("Churn Analysis")
    st.markdown(''':pushpin:
                **Churn analysis provides valuable insights into customer behavior, allowing businesses to:**''')
    st.write('- Predict and prevent churn more effectively.')
    st.write('- Improve customer retention strategies.')
    st.write('- Optimize marketing and product development efforts.')
    st.write('- Enhance overall customer satisfaction and loyalty.')
           
    st.write("  ")
    st.write("  ")
    st.write("  ")
    churn_rate = (df['Churn'].sum() / len(df['Churn'])) * 100
    churned_customer = df[df['Churn']==1]
    churned_customer_df = churned_customer[
        ['Customer_ID', 'Product_Category', 'Age Group', 'Gender']]
    
    col1,col2,col3 = st.columns((3))
    with col1:
        st.markdown("**Customer Age Distribution of Churned Customers**", unsafe_allow_html=True)
        
        age_group_cnt = churned_customer_df.groupby('Age Group')['Age Group'].count().reset_index(name='Count')
        fig = px.bar(age_group_cnt, x = 'Age Group', y = 'Count')
        st.plotly_chart(fig, use_container_width=True)
            
    with col2:
        st.markdown("**Gender Distribution of Churned Customers**", unsafe_allow_html=True)
        
        gender_cnt = churned_customer_df.groupby('Gender')['Gender'].count().reset_index(name='Count')
        fig = px.bar(gender_cnt, x = 'Gender', y = 'Count')
        st.plotly_chart(fig, use_container_width=True) 
        
    with col3:
        st.markdown("**Product Category of Churned Customers**", unsafe_allow_html=True)
        
        prod_cate_cnt = churned_customer_df.groupby('Product_Category')['Product_Category'].count().reset_index(name='Count')
        fig = px.bar(prod_cate_cnt, x = 'Product_Category', y = 'Count')
        st.plotly_chart(fig, use_container_width=True)
    
    
    
    col1, col2 = st.columns((2,1))
    
    def time_to_churn_plot(df):
        df['Purchase_Date'] = pd.to_datetime(df['Purchase_Date'])
        
        time_to_churn = df[df['Churn'] == 1].groupby('Customer_ID')['Purchase_Date'].max() - df.groupby('Customer_ID')['Purchase_Date'].min()
        
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.histplot(time_to_churn.dt.days, bins=30, kde=True, ax=ax)
        
        ax.set_title('Time (in days) Between First Purchase and Churn')
        ax.set_xlabel('Days')
        
        return fig
        
    with col1:
        fig = time_to_churn_plot(df)
        st.pyplot(fig)
        
    with col2:
        st.markdown("**Explanation of the plot:**")
        st.write("This plot shows the distribution of time between the first purchase and churn for churned customers.")

    
        
    
    
    
    
        
   
    
    

    
    
   
