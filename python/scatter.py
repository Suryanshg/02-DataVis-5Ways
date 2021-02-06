import pandas as pd
import matplotlib.pyplot as plt

colors = {'bmw':'orange', 'ford':'green', 'honda':'lightblue', 'mercedes':'darkblue', 'toyota':'purple'}


df = pd.read_csv("../cars-sample.csv")
plt.scatter( x=df['Weight'], y=df['MPG'],alpha=0.5, c=df['Manufacturer'].map(colors), s = (df['Weight']//1000)*15 )
plt.xlabel("Weight")
plt.ylabel("MPG")
plt.show()
