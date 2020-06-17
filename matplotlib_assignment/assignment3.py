from matplotlib import pyplot as plt
import numpy as np

students=['Advait','Ridhiman','Rishabh','Sarthak','Shiv']
marks=[[5,4,4,5,5],[10,9.5,10,10,10],[10,8,10,10,10],[10,10,10,10,10]]
subjects=['Quiz','Diary+Observation','Seminar','Report']
clrs=['g','r','b','k','m']

def display(i):
    individual_marks=[marks[0][i]]
    for j in range(1,4,1):
        individual_marks.insert(j,marks[j][i]+individual_marks[j-1])
    plt.plot(subjects,individual_marks,marker='o',color=clrs[i],label=students[i])

for i in range(0,5,1):
    display(i)

plt.ylabel("Marks")
plt.xlabel("Assignments")
plt.legend(loc="upper left")
plt.title("PS I Marks")

plt.show()