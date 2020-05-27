from matplotlib import pyplot as plt

plt.style.use("seaborn-colorblind")

slices = [31.17, 17.75, 7.79, 7.05, 6.09, 5.67]
labels = ['Python', 'Java', 'Javascript', 'C#', 'PHP', 'C/C++']
explode = [0.15, 0.05, 0.05, 0.05, 0.05, 0.05]
colors = ['#13b6ec', '#40c33c','#bc43a7', '#19e6b8','#ad5352', '#c2cb34']

plt.pie(slices, labels = labels, explode = explode, colors = colors, shadow = True, startangle = 60, autopct = '%1.1f%%', wedgeprops = {'edgecolor': 'black'})

plt.title("Popularity of Programming Languages in 2020 Worldwide")
plt.tight_layout()
plt.show()

