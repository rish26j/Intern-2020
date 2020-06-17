import matplotlib.pyplot as plt

sarthak_marks = [5, 6, 7,10,15,25,35]
advait_marks = [5, 6, 7,10,15,25,35]
shiv_marks = [5, 6, 7,10,15,25,35]
ridhiman_marks = [4, 5, 6,9,13.5,21.5,31.5]
rishabh_marks = [4, 5, 6,9,14,24,34]

marks_range = [5, 6, 7,10,15,25,35]

plt.scatter(marks_range, sarthak_marks, label='Sarthak', color='r')
plt.scatter(marks_range, advait_marks, label='Adwait', color='g')
plt.scatter(marks_range, shiv_marks, label='Shiv Shankar', color='b')
plt.scatter(marks_range, ridhiman_marks, label='Ridhiman', color='m')
plt.scatter(marks_range, rishabh_marks, label='Rishabh', color='k')

plt.title('PS I Marks')
plt.xlabel('Marks Range')
plt.ylabel('Marks Scored')
plt.legend()
plt.show()
