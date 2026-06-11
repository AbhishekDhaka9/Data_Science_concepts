import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

tips = sns.load_dataset("tips")
sns.scatterplot(x="total_bill", y="tip", data=tips)
plt.show()


sns.barplot(x="total_bill",y="tip")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.show()

sns.histplot(tips["total_bill"], stat="density", kde=True)
plt.xlabel("Total Bill")
plt.ylabel("Density")
plt.title("Distribution of Total Bill")
plt.show()

sns.boxplot(x="day", y="total_bill", data=tips)
plt.xlabel("Day of the Week")
plt.ylabel("Total Bill")
plt.title("Boxplot of Total Bill by Day")
plt.show()

sns.violinplot(x="day", y="total_bill", data=tips)
plt.xlabel("Day of the Week")
plt.ylabel("Total Bill")
plt.title("Violin Plot of Total Bill by Day")
plt.show()

sns.heatmap(tips.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

sns.pairplot(tips)
plt.show()

sns.lmplot(x="total_bill", y="tip", data=tips)
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.title("Linear Regression of Tip vs Total Bill")
plt.show()

sns.countplot(x="day", data=tips)
plt.xlabel("Day of the Week")
plt.ylabel("Count")
plt.title("Count of Tips by Day")
plt.show()

sns.catplot(x="day", y="total_bill", data=tips, kind="box")
plt.xlabel("Day of the Week")
plt.ylabel("Total Bill")
plt.title("Boxplot of Total Bill by Day")
plt.show()

sns.catplot(x="day", y="total_bill", data=tips, kind="violin")
plt.xlabel("Day of the Week")
plt.ylabel("Total Bill")
plt.title("Violin Plot of Total Bill by Day")
plt.show()

sns.blend_palette(["#FF5733", "#33FF57", "#3357FF"], n_colors=10)
sns.set_style("whitegrid")  
sns.set_context("talk")
sns.set_palette("Set2")
