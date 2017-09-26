
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
from bokeh.io import output_notebook, show, curdoc
from bokeh.models import ColumnDataSource,HoverTool,ColorBar
from bokeh.plotting import figure, show, output_file
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from bokeh.layouts import layout
from bokeh.layouts import row

output_notebook()

data = pd.read_csv('Wholesale customers data.csv')


# In[2]:

data = data.drop('Channel',axis=1)
data = data.drop('Region',axis=1)
data.head(10)


# In[3]:

kmeans = KMeans(n_clusters=4)
kmeans.fit(data[['Milk','Grocery']])
data['cluster'] = kmeans.labels_

colormap = {0: 'red', 1: 'blue', 2: 'green', 3: 'yellow', 4: 'orange'}
colors = [colormap[x] for x in data['cluster']]

p = figure(title = "Wholesale Customers Data", tools="hover,lasso_select,pan,wheel_zoom,box_zoom,reset,save")
p.xaxis.axis_label = 'Milk'
p.yaxis.axis_label = 'Grocery' 

Milk = data['Milk'].tolist()
Grocery = data['Grocery'].tolist()
Fresh = data['Fresh'].tolist()
Frozen = data['Frozen'].tolist()
Detergents_Paper = data['Detergents_Paper'].tolist()
Delicassen = data['Delicassen'].tolist()

source = ColumnDataSource(data={
    'x' : Milk,
    'y' : Grocery
})

p.asterisk('x', 'y', color=colors, source=source, fill_alpha=0.2, size=12)
show(p)



# In[6]:

from bokeh.io import output_file, show
from bokeh.layouts import widgetbox
from bokeh.models.widgets import CheckboxGroup
from bokeh.layouts import column
from bokeh.io import curdoc
from bokeh.models import CustomJS, ColumnDataSource, Slider
from bokeh.plotting import figure, output_file, show

def update_plot(attr, old, new):
    source.data = {
          'x' : new[0],
            'y' : new[1]
        }
    
callback = CustomJS(args=dict(source=source), code="""
        var data = source.data;
        var f = cb_obj.active
        x = f[0]
        y = f[1]
        source.change.emit();
    """)



checkbox_group = CheckboxGroup(labels=list(data.columns), active=[0, 1])
checkbox_group.on_change('active', update_plot)

layout = row(checkbox_group, p)
curdoc().add_root(layout)

show(layout)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



