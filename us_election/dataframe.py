import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"us_election\US-2016-primary.csv", sep = ";")

candidate_name = "John Kasich"
candidate_df = df[df["candidate"] == candidate_name]
print(df.head())

plt.hist(candidate_df['fraction_votes'], bins=10, color='skyblue', edgecolor='black', density=True)
plt.title(f"Fraction of Votes for {candidate_name} by County (Normalized)")
plt.xlabel("Fraction of Votes")
plt.ylabel("Fraction of Counties")
plt.show()
