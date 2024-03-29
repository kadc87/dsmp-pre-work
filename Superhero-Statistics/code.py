# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path

#Code starts here 
data = pd.read_csv(path)
data['Gender'].replace('-', 'Agender', inplace = True)
gender_count = data['Gender'].value_counts()
plt.bar(gender_count, 0.8) 


# --------------
#Code starts here
alignment = data['Alignment'].value_counts()
print(alignment)
labels = 'good', 'bad', 'neutral'
plt.pie(alignment, labels = labels)
plt.title('Character Alignment', loc = 'center')


# --------------
#Code starts here
sc_df = data[['Strength', 'Combat']].copy()
sc_covariance = sc_df.cov()['Strength']['Combat']
print(sc_covariance)
sc_strength = sc_df['Strength'].std()
sc_combat = sc_df['Combat'].std()
sc_pearson = sc_covariance / (sc_combat * sc_strength)
print(sc_pearson)
ic_df = data[['Intelligence', 'Combat']].copy()
ic_covariance = ic_df.cov()['Intelligence']['Combat']
print(ic_covariance)
ic_intelligence = ic_df['Intelligence'].std()
ic_combat = ic_df['Combat'].std()
ic_pearson = ic_covariance / (ic_combat * ic_intelligence)
print(ic_pearson)


# --------------
#Code starts here
total_high = data['Total'].quantile(0.99)
super_best = data [data['Total'] > total_high]
print(super_best)
super_best_names = super_best['Name'].tolist()
print(super_best_names)


# --------------
#Code starts here
fig, (ax_1, ax_2, ax_3) = plt.subplots(3, 1)
data.boxplot('Intelligence', ax = ax_1)
data.boxplot('Speed', ax = ax_2)
data.boxplot('Power', ax = ax_3)


