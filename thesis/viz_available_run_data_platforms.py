# curl -X POST "https://www.ebi.ac.uk/ena/portal/api/search" -H  "accept: */*" -H  "Content-Type: application/x-www-form-urlencoded" -d "dataPortal=ena&download=true&fields=run_accession%2Cfirst_public%2Cinstrument_platform%2Cinstrument_model%2Cread_count%2Cbase_count%2Cfastq_bytes&format=tsv&result=read_run&sortDirection=asc" > available_run_platforms2.tsv

import sys
import subprocess
import pandas as pd
from io import StringIO
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import date
import sys 

# get date
TODAY=date.today()

def retrieve_data():
    cmd="curl -X POST \"https://www.ebi.ac.uk/ena/portal/api/search\" -H  \"accept: */*\" -H  \"Content-Type: application/x-www-form-urlencoded\" -d \"dataPortal=ena&download=true&fields=run_accession%2Cfirst_public%2Cinstrument_platform%2Cinstrument_model%2Cread_count%2Cbase_count%2Cfastq_bytes%2Clibrary_source&format=tsv&result=read_run&sortDirection=asc\""
    p = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if p.returncode == 0:
        df = pd.read_csv(StringIO(p.stdout.decode()), sep='\t')
        return df
    else:
        print("Failed.")
        sys.exit(0)

df = retrieve_data()

df['first_public'] = pd.to_datetime(df['first_public'])
df['year'] = df['first_public'].dt.year

sns.set_context('paper')
sns.set_style('whitegrid')

height = 1.5
aspect = 5

# g = sns.catplot(
#     data=df.groupby(['year', 'instrument_platform']).agg({'run_accession': 'count'}).reset_index(), 
#     x='year', 
#     y='run_accession', 
#     kind='bar', 
#     row='instrument_platform', 
#     sharey=False, 
#     height=height, 
#     aspect=aspect,
#     color='grey'
# )
# g.set_axis_labels(
#     "Year published", "Count of\nsequencing runs")
# g.set_titles("{row_name}")

# g.fig.subplots_adjust(top=0.5)
# g.fig.suptitle(f"Retreived {TODAY}")

# plt.savefig('platform_overview.pdf')
# plt.savefig('platform_overview.png')

# g = sns.catplot(
#     data=df.groupby(['year', 'instrument_platform', 'library_source']).agg({'run_accession': 'count'}).reset_index(), 
#     x='year', 
#     y='run_accession', 
#     kind='bar', 
#     row='instrument_platform', 
#     sharey=False, 
#     height=height, 
#     aspect=aspect,
#     # color='grey'
#     hue = 'library_source'
# )
# g.set_axis_labels(
#     "Year published", "Count of\nsequencing runs")
# g.set_titles("{row_name}")

# g.fig.subplots_adjust(top=0.9)
# g.fig.suptitle(f"Retreived {TODAY}")

# plt.savefig('platform_overview_source.pdf')
# plt.savefig('platform_overview_source.png')

g = sns.catplot(
    data=df.loc[df.library_source.isin(['GENOMIC', 'METAGENOMIC'])].groupby(['year', 'instrument_platform', 'library_source']).agg({'run_accession': 'count'}).reset_index(), 
    x='year', 
    y='run_accession', 
    kind='bar', 
    row='instrument_platform', 
    sharey=False, 
    height=height, 
    aspect=aspect,
    # color='grey'
    hue = 'library_source'
)
g.set_axis_labels(
    "Year published", "Count of\nsequencing runs")
g.set_titles("{row_name}")

g.fig.subplots_adjust(top=0.9)
g.fig.suptitle(f"Retreived {TODAY}")

plt.savefig('platform_overview_source_mg.pdf')
plt.savefig('platform_overview_source_mg.png')
