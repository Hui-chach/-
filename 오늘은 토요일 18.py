##import pandas as pd
##import seaborn as sns
##
##df = sns.load_dataset("penguins")
##df.columns = ["종", "섬", "부리길이_mm", "부리너비_mm","날개길이_mm", "체중_g", "성별"]
##
##
##print(df.isnull().sum()
##print(df["성별"].value_counts()
##df = df.dropna()
##df = df[["종", "부리길이_mm", "날개길이_mm", "성별"]]
##import matplotlib.pyplot as plt
##plt.rc("font", family = "Malgun Gothic")
##sns.scatterplot(x = "부리길이_mm", y = "날개길이_mm", data = df,hue = "종", style = "성별")
##plt.xlabel("부리길이(mm)", size = 20)
##plt.ylabel("날개길이(mm)", size = 20)
##plt.show()
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("강아지_평균수명.csv", encoding = "utf-8")
df = df.head(7)
plt.rc("font", family = "Malgun Gothic")
sns.barplot(x = "품종", y = "평균수명", data = df)
plt.show()
