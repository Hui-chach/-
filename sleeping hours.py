##import pandas as pd
##df = pd.read_csv("sleeping_hours.csv", encoding = "euc-kr", header = [0,1], index_col = [0,1])
##df = df.T
##df4 = df.rename_axis(index=["연도", "수면시간"])
##print(df4["학업성적"].loc["2018","상"])
##
##

##import pandas as pd
##df = pd.read_csv("sleeping_hours.csv", encoding = "euc-kr", header = [0,1], index_col = [0,1])
##df = df.T
##df4 = df.rename_axis(index=["연도", "수면시간"])
##print(df4["학업성적"].iloc[0:6,0])
##
##
##import pandas as pd
##import matplotlib.pyplot as plt
##
##df = pd.read_csv("sleeping_hours.csv", encoding = "euc-kr", header = [0,1], index_col = [0,1])
##df = df.T
##df = df.rename_axis(index = ["연도", "수면시간"])
##
##times = ["5시간 미만", "5~6시간", "6~7시간", "7~8시간", "8~9시간", "9시간 이상"]
##
##high_2018 = df["학업성적"].iloc[0:6,0]
##middle_2018 = df["학업성적"].iloc[0:6,1]
##low_2018 = df["학업성적"].loc["2018", "하"]
##plt.rc("font", family = "Malgun Gothic")
##plt.title("2018년 학업 성적별 수면 시간")
##plt.plot(times, high_2018, label = "상")
##plt.plot(times, middle_2018, label = "중")
##plt.plot(times, low_2018, label = "하")
##plt.legend()
##
##plt.show()
##plt.plot()
##
##
##import pandas as pd
##import matplotlib.pyplot as plt
##
##df = pd.read_csv("sleeping_hours.csv", encoding = "euc-kr", header =[0,1], index_col = [0,1])
##df = df.T
##df = df.rename_axis(index = ["연도", "수면시간"])
##times = ["5시간 미만", "5~6시간", "6~7시간", "7~8시간", "8~9시간", "9시간 이상"]
##high_2019 = df["학업성적"].loc["2019", "상"]
##middle_2019 = df["학업성적"].loc["2019", "중"]
##low_2019 = df["학업성적"].loc["2019", "하"]
##plt.rc("font", family = "Malgun Gothic")
##plt.plot(times, high_2019, label = "상")
##plt.plot(times, middle_2019, label = "중")
##plt.plot(times, low_2019, label = "하")
##plt.legend()
##
##plt.show()
##plt.plot()

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sleeping_hours.csv", encoding = "euc-kr", header = [0,1], index_col = [0,1])
df = df.T
df = df.rename_axis(index = ["연도", "수면시간"])

times = ["5시간 미만", "5~6시간", "6~7시간", "7~8시간", "8~9시간", "9시간 이상"]

element_2019 = df["학교급"].loc["2019", "초등학교"]
middle_2019 = df["학교급"].loc["2019", "중학교"]
high_2019 = df["학교급"].loc["2019", "고등학교"]

plt.rc("font", family = "Malgun Gothic")
plt.plot(times, element_2019, label = "초등학교")
plt.plot(times, middle_2019, label = "중학교")
plt.plot(times, high_2019, label = "고등학교")
plt.legend()
plt.show()






