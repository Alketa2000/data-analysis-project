
import pandas as pd
import matplotlib.pyplot as plt
print("FILE I RI PO EKZEKUTOHET")
df = pd.read_csv("data.csv")

print("DATASET:")
print(df)

# TOTAL & MESATARE
total = df["amount"].sum()
avg = df["amount"].mean()

print("\nTOTAL:", total)
print("MESATARE:", avg)

# SIPAS KATEGORIVE (i renditur)
category_sum = df.groupby("category")["amount"].sum().sort_values(ascending=False)

print("\nSIPAS KATEGORIVE:")
print(category_sum.to_string())

# GRAFIK
category_sum.plot(kind="bar", title="Shpenzime sipas kategorive")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.tight_layout()
plt.show()
