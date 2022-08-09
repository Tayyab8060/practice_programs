#import libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

#Define your own data you want to plot
df= pd.DataFrame()
df["Names"]=["Ali", "Hassan", "Junaid", "Husnain"]
df["Number"]=[20,50,90,80]
print(df)

#plot Graph you want
sns.scatterplot(x="Names", y="Number", data=df)
plt.show()



