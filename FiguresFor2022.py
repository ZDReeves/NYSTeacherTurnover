# -*- coding: utf-8 -*-
"""
Created on Fri May  3 11:23:14 2024

@author: zacha
"""

#\\Making a Descriptive Bar Chart
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = './Outputs/dist_turnover.csv'
TurnoverRates2022 = pd.read_csv(file_path)
file_path = './Outputs/dist_characteristics.csv'
Districts = pd.read_csv(file_path)

#\\This section creates a bar chart showing the turnover rates for all teachers, experienced teachers, and inexperienced teachers.
fig1, ax1=plt.subplots()
TurnoverRates2022 = TurnoverRates2022[['PER_TURN_ALL', 'PER_TURN_INEXP', 'PER_TURN_EXP']].mean()
TurnoverRates2022.plot.barh(title="Turnover by Experience in 2022", color=['navy', 'lightseagreen', 'royalblue'], ax=ax1)
plt.tight_layout()
Outputs = './Outputs/'
plt.savefig(Outputs + "2022TurnoverByExp.png")
plt.show()


#\\This makes a hexplot showing the connection between total turnover and the % of students with a FRPl plan
hexplot = sns.jointplot(data=Districts, x=Districts['PER_FRPL'], y=Districts['PER_TURN_ALL'], kind='hex')
regline = sns.regplot(x=Districts['PER_FRPL'], y=Districts['PER_TURN_ALL'],data=Districts, scatter=False, ax=plt.gca())
plt.savefig(Outputs + "TotTurn_FRPL.png")
plt.show()


#\\This makes a hexplot showing the connection between inexperienced teacher turnover and the % of students with a FRPl plan
hexplot = sns.jointplot(data=Districts, x=Districts['PER_FRPL'], y=Districts['PER_TURN_INEXP'], kind='hex')
regline = sns.regplot(x=Districts['PER_FRPL'], y=Districts['PER_TURN_INEXP'],data=Districts, scatter=False, ax=plt.gca())
plt.savefig(Outputs + "InexpTurn_FRPL.png")
plt.show()

#\\This makes a hexplot showing the connection between experienced teachers turnover and the % of students with a FRPl plan
hexplot = sns.jointplot(data=Districts, x=Districts['PER_FRPL'], y=Districts['PER_TURN_EXP'], kind='hex')
regline = sns.regplot(x=Districts['PER_FRPL'], y=Districts['PER_TURN_EXP'],data=Districts, scatter=False, ax=plt.gca())
plt.savefig(Outputs + "ExpTurn_FRPL.png")
plt.show()


#\\This section does the same analyses as above but focuses on large districts (top 25% = 180 districts)
top_25per = Districts.loc[Districts['K12'].nlargest(180).index]
hexplot = sns.jointplot(data=top_25per, x=top_25per['PER_FRPL'], y=top_25per['PER_TURN_INEXP'], kind='hex')
regline = sns.regplot(x=top_25per['PER_FRPL'], y=top_25per['PER_TURN_INEXP'],data=top_25per, scatter=False, ax=plt.gca())
plt.savefig(Outputs + "Big_Inexp_FRPL.png")
plt.show()

hexplot = sns.jointplot(data=top_25per, x=top_25per['PER_FRPL'], y=top_25per['PER_TURN_EXP'], kind='hex')
regline = sns.regplot(x=top_25per['PER_FRPL'], y=top_25per['PER_TURN_EXP'],data=top_25per, scatter=False, ax=plt.gca())
plt.savefig(Outputs + "Big_Exp_FRPL.png")
plt.show()

hexplot = sns.jointplot(data=top_25per, x=top_25per['PER_FRPL'], y=top_25per['PER_TURN_ALL'], kind='hex')
regline = sns.regplot(x=top_25per['PER_FRPL'], y=top_25per['PER_TURN_ALL'],data=top_25per, scatter=False, ax=plt.gca())
plt.savefig(Outputs + "Big_All_FRPL.png")
plt.show()




