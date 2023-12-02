import pandas as pd

df = pd.read_csv("atlanta_city_posts_1.csv")
df2 = pd.read_csv("atlanta_city_posts_2.csv")

frames = [df, df2]
result = pd.concat(frames)

print(len(result))

result.to_csv("atlanta_city_posts.csv", index=False)

