import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use("ggplot")
plt.rc("font", family = "Malgun Gothic")

train = pd.read_csv("train.csv", parse_dates = ["datetime"])
train["year"] = train["datetime"].dt.year
train["month"] = train["datetime"].dt.month
train["day"] = train["datetime"].dt.day
train["hour"] = train["datetime"].dt.hour
train["minute"] = train["datetime"].dt.minute
train["second"] = train["datetime"].dt.second
train["dayofweek"] = train["datetime"].dt.dayofweek
sns.pointplot(x = "hour", y = "count", data = train, hue = "workingday")
plt.show()
print(train)


