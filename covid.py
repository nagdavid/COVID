import pandas as pd 
df = pd.read_csv("COVID.csv")

#Q. 1) Show the number of Confirmed, Deaths and Recovered cases in each Region.
import pandas as pd

df= pd.DataFrame({
    'Region': ['Region1', 'Region2', 'Region1', 'Region3', 'Region2'],
    'Confirmed': [100, 200, 150, 300, 250],
    'Deaths': [10, 20, 15, 30, 25],
    'Recovered': [90, 180, 135, 270, 225]
})
result = df.groupby('Region').sum()
# print(result)

#Q. 2) Remove all the records where the Confirmed Cases is Less Than 10
import pandas as pd

df = pd.DataFrame({
    'Region': ['Region1', 'Region2', 'Region3', 'Region4'],
    'Confirmed': [5, 15, 8, 20],
    'Deaths': [1, 2, 1, 3],
    'Recovered': [4, 10, 5, 15]
})

filtered_data = df[df['Confirmed'] >= 10]
# print(filtered_data)

#Q. 3) In which Region, maximum number of Confirmed cases were recorded ?
import pandas as pd
df = pd.DataFrame({
    'Region': ['Region1', 'Region2', 'Region3'],
    'Confirmed': [100, 200, 150]
})
max_confirmed_region = df.loc[df['Confirmed'].idxmax(), 'Region']
# print("Region with maximum confirmed cases:", max_confirmed_region)

#Q. 4) In which Region, minimum number of Deaths cases were recorded ?
import pandas as pd
df = pd.DataFrame({
    'Region': ['Region1', 'Region2', 'Region3'],
    'Deaths': [10, 5, 8]
})
min_deaths_region = df.loc[df['Deaths'].idxmin(), 'Region']
# print("Region with minimum deaths cases:", min_deaths_region)


#Q. 5) How many Confirmed, Deaths & Recovered cases were reported from India till 29 April 2020 ?
import pandas as pd
df = pd.read_csv('COVID.csv')

india_data = df[(df['Region'] == 'India') & (df['Date'] <= '2020-04-29')]

confirmed_cases = india_data['Confirmed'].sum()
deaths_cases = india_data['Deaths'].sum()
recovered_cases = india_data['Recovered'].sum()
# print("Confirmed cases reported from India till April 29, 2020:", confirmed_cases)
# print("Deaths reported from India till April 29, 2020:", deaths_cases)
# print("Recovered cases reported from India till April 29, 2020:", recovered_cases)


#Q. 6-A ) Sort the entire data wrt No. of Confirmed cases in ascending order.
import pandas as pd
df = pd.DataFrame({
    'Region': ['Region1', 'Region2', 'Region3'],
    'Confirmed': [100, 50, 150],
    'Deaths': [10, 5, 15],
    'Recovered': [90, 45, 135]
})
sorted_data = df.sort_values(by='Confirmed')
# print(sorted_data)


#Q. 6-B ) Sort the entire data wrt No. of Recovered cases in descending order.
import pandas as pd
df = pd.DataFrame({
    'Region': ['Region1', 'Region2', 'Region3'],
    'Confirmed': [100, 50, 150],
    'Deaths': [10, 5, 15],
    'Recovered': [90, 45, 135]
})
sorted_data = df.sort_values(by='Recovered', ascending=False)
# print(sorted_data)




