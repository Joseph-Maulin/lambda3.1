
import pandas as pd
from my_lambdata.my_mod import enlarge

print("HELLO")

df = pd.DataFrame({"a":[1,2,3], "b":[4,5,6]})

print(df.head())

print(enlarge(df["a"].sum()))
