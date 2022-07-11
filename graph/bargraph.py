from turtle import color
import matplotlib.pyplot as bar

year = [2001, 2002, 2003, 2004, 2005]
income = [1000, 800, 700, 900, 1500]

bar.bar(year,
        income,
        width=0.5,
        color=['red', 'orange', 'yellow', 'blue', 'green'])
bar.xlabel('year')
bar.ylabel('income')
bar.title('My Progress')
bar.show()