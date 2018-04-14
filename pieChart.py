from matplotlib import pyplot as plt
methods = ["Credit Card","Debit Card","Apple Pay","Cash","Other"]
percent = [250,170,50,90,20]
plt.pie(percent, autopct="%0.2f%%",labels=methods)
plt.axis("Equal")
plt.savefig("pieChart.png")
plt.show()