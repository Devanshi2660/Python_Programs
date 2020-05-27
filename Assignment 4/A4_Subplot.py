import matplotlib.pyplot as plt
plt.style.use('seaborn')

fig1, (ax1,ax2) = plt.subplots(nrows = 2, ncols = 1)

year_x = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]

py_y = [6.5, 7.2, 8.4, 9.8, 10.5, 12, 14.6, 19.7, 25.2, 28.9, 30.8]
ax2.plot(year_x, py_y, color = '#936c8a', label = 'PYTHON')



python_y = [2.8, 3.1, 4.1, 5.1, 6.9, 9.1, 11.6, 18.1, 24.2, 29.9, 31.8]
ax1.plot(year_x, python_y, color = '#8716e9',label = 'Python')


java_y = [34.7, 34.1, 34.6, 32.9, 33.4, 33.1, 30.3, 28.3, 25.8, 23.3, 21.6]
ax1.plot(year_x, java_y,color = '#2c9bd3', label = 'Java')

javascript_y = [8.5, 8.2, 8, 9.1, 8.3, 7.9, 8.8, 9, 9.2, 8.8, 9]
ax1.plot(year_x, javascript_y,  color = '#15ea60', label = 'Javascript')

c_y = [14.9, 17.5, 11.7, 10.7, 10.7, 10.3, 10.1, 8.8, 8, 7.2, 6.2]
ax1.plot(year_x, c_y, color = '#bfaf40', label = 'C/C++')

csharp_y = [5.8, 4.8, 8.9, 9.4, 8.6, 8.2, 7.6, 6.7, 6.3, 6.6, 6.2]
ax1.plot(year_x, csharp_y, color = '#b9467e',label = 'C#')

php_y = [17.8, 16, 15.7, 14.8, 13.6, 12.4, 11.3, 9.7, 7.5 , 6.4, 6.2]
ax1.plot(year_x, php_y, color = 'black', label = 'PHP')

ax2.set_xlabel('Year')
ax2.set_ylabel('Contribution(%)')
ax2.set_title('Popularity of Python Programming Language over past 10 years Worldwide')

ax2.legend()


ax1.set_xlabel('Year')
ax1.set_ylabel('Contribution(%)')
ax1.set_title('Popularity of Programming Languages over past 10 years in India')

ax1.legend()

plt.tight_layout()
plt.show()
