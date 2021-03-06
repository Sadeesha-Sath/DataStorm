# -*- coding: utf-8 -*-
"""Copy of Day3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1F-TbIXr615jlSSxH6JPwoa9mjEOTN10y
"""

!git clone https://github.com/Sadeesha-Sath/DataStorm.git

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [15, 5]

train_data = pd.read_csv('./DataStorm/train_data.csv', parse_dates = ['DateID'], infer_datetime_format = True)

train_data

train_data['DateID']

grouped_data = train_data.groupby(['ItemCode'])

grouped_data.indices

sorted_data = {
    'category_1': {},
    'category_2': {},
    'category_3': {},
    'category_4': {}
}
sorted_data2 = {
    'category_1': {},
    'category_2': {},
    'category_3': {},
    'category_4': {}
}


for itemID, grp in grouped_data:    
    sorted_data[grp['CategoryCode'].iloc[0]][itemID] = grp.set_index('DateID').sort_values('DateID')['DailySales']
    
for key, val in sorted_data.items():
    sorted_data2[key] = pd.Series(val)
    
sorted_data3 = pd.Series(sorted_data2)

"""sorted_data - Group karapu tka sort kala date eka anuwa
sorted_data2 - sorted_data3 eka hadanna temp var ekak wage
srted_data_3 - sorted datama tama python dictionary wenuwata pandas series walin (mata hithuna pythin dict ekak widiyata thiyanawata wada pandas series ekak widiyata thiyana eka wada lesi wei kiyala. eth aththatama wadak nathi una anthimata)
"""

sorted_data

sorted_data2

sorted_data3

sorted_data3['category_1']

:
for i in sorted_data3['category_1']:
    plt.plot(i)

for i in sorted_data3['category_2']:
    plt.plot(i)

for i in sorted_data3['category_3']:
    plt.plot(i)

for i in sorted_data3['category_4']:
    plt.plot(i)

for cat in sorted_data3:
    for item in cat:
        print(item)

dates = pd.date_range('2021-10-01', '2022-02-13', freq='D')
dates

sorted_data3['category_1'][3418]

template = pd.Series([0 for _ in range(len(dates))], index=dates)

template

fff = template.add(sorted_data3['category_1'][3418], fill_value=0)

plt.plot(fff)
plt.plot(sorted_data3['category_1'][3418])

template

sorted_data4 = sorted_data3.copy()

for cat in sorted_data3.keys():
    print(cat)
    for item in sorted_data3[cat].keys():
        sorted_data4[cat][item] = template.add(sorted_data3[cat][item], fill_value=0).copy()

for i in sorted_data4['category_1']:
    plt.plot(i)

for i in sorted_data4['category_2']:
    plt.plot(i)

for i in sorted_data4['category_3']:
    plt.plot(i)

for i in sorted_data4['category_4']:
    plt.plot(i)

plt.plot(sorted_data4['category_1'][3418].rolling(7).sum())
plt.plot(sorted_data4['category_1'][3418])

from sklearn.linear_model import LinearRegression

x = np.array(range(130)).reshape(-1, 1)
y = np.array(sorted_data4['category_1'][3418].rolling(7).sum().values.copy()[6:]).reshape(-1, 1)

y

linear_regressor = LinearRegression()
linear_regressor.fit(x, y)

linear_regressor.predict(x)

plt.plot(x, y)
plt.plot(np.array(range(158)).reshape(-1, 1), linear_regressor.predict(np.array(range(158)).reshape(-1, 1)))

plt.plot(x, y)
plt.plot(np.array(range(130, 130 + 28)).reshape(-1, 1), linear_regressor.predict(np.array(range(130, 130 + 28)).reshape(-1, 1)))

linear_regressor.predict(np.array(range(130, 130 + 28)).reshape(-1, 1))

plt.plot(x, y)
plt.plot(np.array(range(136, 136 + 28, 7)).reshape(-1, 1), linear_regressor.predict(np.array(range(136, 136 + 28, 7)).reshape(-1, 1)))

linear_regressor.predict(np.array(range(136, 136 + 28, 7)).reshape(-1, 1))

x = np.array(range(130)).reshape(-1, 1)
predictions = {}

for cat_id in sorted_data4.keys():
    for item_code in sorted_data4[cat_id].keys():
        item = sorted_data4[cat_id][item_code]
        y = np.array(item.rolling(7).sum().values.copy()[6:]).reshape(-1, 1)
        linear_regressor = LinearRegression()
        linear_regressor.fit(x, y)
        for w, s in enumerate(linear_regressor.predict(np.array(range(136, 136 + 28, 7)).reshape(-1, 1))):
            predictions[f"{cat_id}_{item_code}_w{w+1}"] = max(round(float(s)), 0)
predictions

out_df = pd.DataFrame(pd.Series(predictions), columns=["WeeklySales"])
out_df.index.name = "ID"
out_df

out_df.to_csv('out', index=True)

len(sorted_data4['category_1']) + len(sorted_data4['category_2']) + len(sorted_data4['category_3']) + len(sorted_data4['category_4'])

