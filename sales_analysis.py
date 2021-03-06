import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

data = pd.read_csv('superstore_sales.csv')

print(data.head(4))
print(data.dtypes)
print(data.isna().sum())
print(data.describe())
print(data.shape)
print(data.columns)
print(data.info())
print(data['order_date'].min())
print(data['order_date'])

# Sales trend
data['sales'] = pd.to_numeric(data['sales'])
data['order_date'] = pd.to_datetime(data['order_date'], format = '%m/%d/%Y')
data['month_year'] = data['order_date'].apply(lambda x: x.strftime('%Y-%m'))
group_sales = data.groupby('month_year').sum()['sales'].reset_index()
plt.figure(figsize = (16,6))
plt.plot(group_sales['month_year'], group_sales['sales'])
plt.xticks(rotation = 'vertical', size=8)
plt.show()

# Top 10 products by sales

group_sales_by_name = data.groupby('product_name').sum()['sales'].reset_index()
ordered_top_sales = group_sales_by_name.sort_values(('sales'), ascending = False)
print(ordered_top_sales.head(10))

# Most selling products

most_selling_product = pd.DataFrame(data.groupby('product_name').sum()['quantity'])
most_selling_product_ordered = most_selling_product.sort_values(('quantity'), ascending = False)
print(most_selling_product_ordered.head(10))

# Most preferred shipping mode

some = sns.countplot(x="ship_mode", data=data)
plt.figure(figsize = (10,7))
plt.show()

# Which are the most profitable category and subcategory

most_profitable_cat_subcat = pd.DataFrame(data.groupby(['category', 'sub_category']).sum()['profit'])
most_profitable_cat_subcat = most_profitable_cat_subcat.sort_values((['category','profit']), ascending = False)[:1]
print(most_profitable_cat_subcat)

# Print all data types and their unique values

for column in data.columns:
    if data[column].dtype == object:
        print(str(data[column]) + ':' + str(data[column].unique()))
        print(data[column].value_counts())
        print('------------------------------------------------------')
        print()