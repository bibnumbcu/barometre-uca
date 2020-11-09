%matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_complete = pd.read_csv("Data/outputs/publis_lorraine_completes")
df_complete_20162019 = df_complete.loc[(df_complete['published_year'] == 2016.0) | (df_complete['published_year'] == 2017.0) 
                                       | (df_complete['published_year'] == 2018.0) | (df_complete['published_year'] == 2019.0),:]

df_complete_20162019.is_oa = df_complete_20162019.is_oa.astype(bool)

df_complete_20162019['oa_publisher_repository'] = df_complete_20162019.oa_type=='publisher;repository'
df_complete_20162019['oa_repository'] = df_complete_20162019.oa_type=='repository'
df_complete_20162019['oa_publisher'] = df_complete_20162019.oa_type=='publisher'
df_complete_20162019['oa_unk'] = df_complete_20162019.oa_type=='unknown'


df_oa_global_year = pd.DataFrame(df_complete_20162019.groupby(['published_year'])[['is_oa', 'oa_repository', 'oa_publisher', 'oa_unk', 'oa_publisher_repository']].agg(['count', np.mean])).reset_index()
df_oa_global_year.columns = ['published_year', 'nb_doi', 'oa_mean', 'nbdoi1', 'oa_repository_mean', 'nb_doi2', 'oa_publisher_mean', 'nb_doi3', 'oa_unk_mean', 'nb_doi4', 'oa_publisher_repository_mean']
df_oa_global_year['year_label'] = df_oa_global_year.apply(lambda x:"{}\nn={}|".format(int(x.published_year), int(x.nb_doi)), axis=1)
df_oa_global_year = df_oa_global_year.sort_values(by='published_year', ascending=True)

graph_type = 'poster'

if graph_type == 'poster':
    fig, (ax) = plt.subplots(figsize=(15, 10), dpi=100, facecolor='w', edgecolor='k')
else:
    fig, (ax) = plt.subplots(figsize=(10, 12), dpi=100, facecolor='w', edgecolor='k')


#ax.grid(color='grey', linestyle='--', linewidth=0.4)

# Example data
years = df_oa_global_year.year_label.tolist()
y_pos = np.arange(len(years))

oa_publisher_repository_mean = df_oa_global_year.oa_publisher_repository_mean.tolist() 
oa_repository_mean = df_oa_global_year.oa_repository_mean.tolist() 
oa_publisher_mean = df_oa_global_year.oa_publisher_mean.tolist() 
oa_unk_mean = df_oa_global_year.oa_unk_mean.tolist()

from operator import add
oa_total_mean = list( map(add, oa_publisher_repository_mean, oa_repository_mean))
oa_total_mean = list( map(add, oa_total_mean, oa_publisher_mean)  )
oa_total_mean = list( map(add, oa_total_mean, oa_unk_mean)  )     


rect1 = ax.bar(y_pos, oa_publisher_mean, align='center', alpha = 1.0, color='#f1e15b',
        hatch='/',
       # bottom = oa_publisher_mean,
        ecolor='black', label="Publisher hosted")

ax.bar(y_pos, oa_publisher_repository_mean, align='center', alpha = 1.0, color='#B3E62C',
        hatch='o/',
        bottom = oa_publisher_mean,
        ecolor='black', label="Publiser & Repository hosted")

ax.bar(y_pos, oa_repository_mean, align='center',alpha = 1.0, color='#61cdbb', hatch='o',
       bottom = [oa_publisher_mean[i] + oa_publisher_repository_mean[i] for i in range(0, len(oa_publisher_mean))], 
         ecolor='black', label="Repository hosted")


ax.bar(y_pos, oa_unk_mean, align='center', 
        bottom = [oa_repository_mean[i] + oa_publisher_mean[i] + oa_publisher_repository_mean[i] for i in range(0, len(oa_publisher_mean))], 
        ecolor='black', alpha = 1.0, color='#205A7D', label="Unknown host type")

w = rect1[0].get_width()
for year_ix in range(0, 4):
    ax.annotate("{:,.0%}".format(oa_total_mean[year_ix]),
                        xy=(year_ix , oa_total_mean[year_ix]),
                        xytext=(0, 20),  # 3 points vertical offset
                        size=25,
                        textcoords="offset points",
                        ha='center', va='bottom')

ax.set_xticks(y_pos)
ax.set_xticklabels(years, fontsize = 25)
#ax.invert_xaxis()  # labels read top-to-bottom
ax.set_ylim([0,0.8])
ax.set_yticklabels(['{:,.0%}'.format(x) for x in ax.get_yticks()], fontsize = 25)
ax.legend(fontsize=20)
ax.yaxis.grid(ls='--', alpha=0.4)

plt.tight_layout()
plt.savefig('oa_host_type_evolution.png', dpi=100)
