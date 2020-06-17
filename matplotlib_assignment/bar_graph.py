from matplotlib import pyplot as plt
import numpy as np

students=['Advait','Ridhiman','Rishabh','Sarthak','Shiv']
marks=[[5,4,4,5,5],[10,9.5,10,10,10],[10,8,10,10,10],[10,10,10,10,10]]
total=[]
subjects=['Quiz','Diary + Observation','Seminar','Report','Total']

for i in range(0,5,1):
    s=0
    for j in range(0,4,1):
        s=s+marks[j][i]
    total.insert(i,s)

marks.insert(4,total)
fig,axs = plt.subplots(2,3)

def display(i):
    axs[(i%2),int((i/2))].bar(students,marks[i],color=('g','r','b','k','m'))
    subjects[i]=subjects[i]+" marks"
    axs[(i%2),int((i/2))].set_title(subjects[i])

for i in range(0,5,1):
    display(i)

fig.delaxes(axs[1][2])

plt.show()
