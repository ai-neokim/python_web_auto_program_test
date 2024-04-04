# import matplotlib.pyplot as plt
# import numpy as np

# x = np.arange(3)
# z = np.arange(3)

# years = ['2018','2019','2020']
# values = [100,200,300]


# plt.bar(x,values)
# plt.xticks(x,years)


# plt.bar(z,values)
# plt.xticks(z,years)

# plt.show()

####################################
# from IPython.display import display
# import altair as alt
# import pandas as pd

# df = pd.DataFrame([['Action',5,'F'],
#                    ['Crime',10,'F'],
#                    ['Action',3,'M'],
#                    ['Crime',9,'M']],
#                    columns=['Genre','Rating','Gender'])

# chart = alt.Chart(df).mark_bar().encode(
#     x=alt.X('Genre',axis=alt.Axis(labelAngle=0)),
#     xOffset='Gender',
#     y=alt.Y('Rating',axis=alt.Axis(grid=False)),
#     color='Gender'
# ).configure_view(
#     stroke=None,
# )

# chart.show()
    

#############
# import matplotlib.pyplot as plt
# plt.rc("font", family='NanumGothic')
# plt.title("Web Auto Program")
# #x_data=[1,3,5,7,9]
# #y_data=[5,7,6,1,4]
# x_data=['07-01','07-02','07-03','07-04','07-05']
# y_data=[10,7,6,7,8]

# plt.bar(x_data,y_data) #bar(막대를 표시할 위치, 막대의 높이)
# plt.show()    

###############################################

import pandas as pd
import matplotlib.pyplot as plt

data = [["07-01",10,3],
        ["07-02",15,5],
        ["07-03",25,2],
        ["07-04",20,1],
       ]

df = pd.DataFrame(data, columns=["Date","success","error"])
df.plot(x="Date",y=["success","error"], kind="bar", rot=0, figsize=(8,8)) # figsize:(가로길이, 세로길이) / rot=0 : 카테고리 이름 가로 출력

plt.show()

##################################################