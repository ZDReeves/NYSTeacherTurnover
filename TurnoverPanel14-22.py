# -*- coding: utf-8 -*-
"""
Created on Fri May  3 10:39:17 2024

@author: zacha
"""

#\\This script is extremely long (I apologize). Here, I clean staff data from 2014-2022 in order to isolate the turnover data.
# It's important to note that NYSED separated their teacher experience data from their turnover data
# in 2018. Thus, there is an additional merge for 2018-2022 in order to find the turnover rates for the different experience
# levels.
import pandas as pd


#\\Cleaning 2014
file_path = './Inputs/2014Staff.xlsx'
staff14 = pd.read_excel(file_path)
staff14["ENTITY_CD"] = staff14["ENTITY_CD"].astype(str)
staff14["YEAR"] = staff14["YEAR"].astype(str)
staff14["ENTITY_CD"] = staff14["ENTITY_CD"].str[-4:]
staff14 = staff14[~staff14['SCHOOL_NAME'].str.contains('County')]
staff14= staff14.query("ENTITY_CD=='0000'")
staff14 = staff14.query("YEAR=='2014'")

#//Calculate the turnover rate for experienced teachers
staff14['PER_TURN_ALL'] = staff14['PER_TURN_ALL']/100
staff14['PER_TURN_FIVE_YRS'] = staff14['PER_TURN_FIVE_YRS']/100
staff14["NUM_TOT_TURN"] = staff14["PER_TURN_ALL"]*staff14["NUM_TEACH"]
staff14["NUM_INEXP_TURN"] = staff14["PER_TURN_FIVE_YRS"]*staff14["NUM_FEWER_3YRS_EXP"]
staff14["NUM_EXP_TURN"] = staff14["NUM_TOT_TURN"] - staff14["NUM_INEXP_TURN"]
staff14["NUM_TEACH_EXP"] = staff14["NUM_TEACH"]-staff14["NUM_FEWER_3YRS_EXP"]
staff14["PER_TURN_EXP"] = staff14["NUM_EXP_TURN"]/staff14["NUM_TEACH_EXP"]
staff14 = staff14[['SCHOOL_NAME','YEAR','PER_TURN_ALL','PER_TURN_FIVE_YRS', 'PER_TURN_EXP']]
staff14 = staff14.rename(columns={'PER_TURN_FIVE_YRS': 'PER_TURN_INEXP'})
staff14 = staff14.rename(columns={'SCHOOL_NAME': 'DISTRICT'})
staff14 = staff14.set_index('YEAR', drop=True)

#\\Cleaning 2015
file_path = './Inputs/Staff2015.xlsx'
staff15 = pd.read_excel(file_path)
staff15["ENTITY_CD"] = staff15["ENTITY_CD"].astype(str)
staff15["YEAR"] = staff15["YEAR"].astype(str)
staff15["ENTITY_CD"] = staff15["ENTITY_CD"].str[-4:]
staff15 = staff15[~staff15['SCHOOL_NAME'].str.contains('County')]
staff15= staff15.query("ENTITY_CD=='0000'")
staff15 = staff15.query("YEAR=='2015'")

#//Calculate the turnover rate for experienced teachers
staff15['PER_TURN_ALL'] = staff15['PER_TURN_ALL']/100
staff15['PER_TURN_FIVE_YRS'] = staff15['PER_TURN_FIVE_YRS']/100
staff15["NUM_TOT_TURN"] = staff15["PER_TURN_ALL"]*staff15["NUM_TEACH"]
staff15["NUM_INEXP_TURN"] = staff15["PER_TURN_FIVE_YRS"]*staff15["NUM_FEWER_3YRS_EXP"]
staff15["NUM_EXP_TURN"] = staff15["NUM_TOT_TURN"] - staff15["NUM_INEXP_TURN"]
staff15["NUM_TEACH_EXP"] = staff15["NUM_TEACH"]-staff15["NUM_FEWER_3YRS_EXP"]
staff15["PER_TURN_EXP"] = staff15["NUM_EXP_TURN"]/staff15["NUM_TEACH_EXP"]
staff15 = staff15[['SCHOOL_NAME','YEAR','PER_TURN_ALL','PER_TURN_FIVE_YRS', 'PER_TURN_EXP']]
staff15 = staff15.rename(columns={'PER_TURN_FIVE_YRS': 'PER_TURN_INEXP'})
staff15 = staff15.rename(columns={'SCHOOL_NAME': 'DISTRICT'})
staff15 = staff15.set_index('YEAR', drop=True)

#Cleaning 2016
file_path = './Inputs/Staff2016.xlsx'
staff16 = pd.read_excel(file_path)
staff16["ENTITY_CD"] = staff16["ENTITY_CD"].astype(str)
staff16["YEAR"] = staff16["YEAR"].astype(str)
staff16["ENTITY_CD"] = staff16["ENTITY_CD"].str[-4:]
staff16 = staff16[~staff16['SCHOOL_NAME'].str.contains('County')]
staff16= staff16.query("ENTITY_CD=='0000'")
staff16 = staff16.query("YEAR=='2016'")

#//Calculate the turnover rate for experienced teachers
staff16['PER_TURN_ALL'] = staff16['PER_TURN_ALL']/100
staff16['PER_TURN_FIVE_YRS'] = staff16['PER_TURN_FIVE_YRS']/100
staff16["NUM_TOT_TURN"] = staff16["PER_TURN_ALL"]*staff16["NUM_TEACH"]
staff16["NUM_INEXP_TURN"] = staff16["PER_TURN_FIVE_YRS"]*staff16["NUM_FEWER_3YRS_EXP"]
staff16["NUM_EXP_TURN"] = staff16["NUM_TOT_TURN"] - staff16["NUM_INEXP_TURN"]
staff16["NUM_TEACH_EXP"] = staff16["NUM_TEACH"]-staff16["NUM_FEWER_3YRS_EXP"]
staff16["PER_TURN_EXP"] = staff16["NUM_EXP_TURN"]/staff16["NUM_TEACH_EXP"]
staff16 = staff16[['SCHOOL_NAME','YEAR','PER_TURN_ALL','PER_TURN_FIVE_YRS', 'PER_TURN_EXP']]
staff16 = staff16.rename(columns={'PER_TURN_FIVE_YRS': 'PER_TURN_INEXP'})
staff16 = staff16.rename(columns={'SCHOOL_NAME': 'DISTRICT'})
staff16 = staff16.set_index('YEAR', drop=True)

#\\Cleaning 2017
file_path = './Inputs/Staff2017.xlsx'
staff17 = pd.read_excel(file_path)
staff17["ENTITY_CD"] = staff17["ENTITY_CD"].astype(str)
staff17["YEAR"] = staff17["YEAR"].astype(str)
staff17["ENTITY_CD"] = staff17["ENTITY_CD"].str[-4:]
staff17 = staff17[~staff17['SCHOOL_NAME'].str.contains('County')]
staff17= staff17.query("ENTITY_CD=='0000'")
staff17 = staff17.query("YEAR=='2017'")

#//Calculate the turnover rate for experienced teachers
staff17['PER_TURN_ALL'] = staff17['PER_TURN_ALL']/100
staff17['PER_TURN_FIVE_YRS'] = staff17['PER_TURN_FIVE_YRS']/100
staff17["NUM_TOT_TURN"] = staff17["PER_TURN_ALL"]*staff17["NUM_TEACH"]
staff17["NUM_INEXP_TURN"] = staff17["PER_TURN_FIVE_YRS"]*staff17["NUM_FEWER_3YRS_EXP"]
staff17["NUM_EXP_TURN"] = staff17["NUM_TOT_TURN"] - staff17["NUM_INEXP_TURN"]
staff17["NUM_TEACH_EXP"] = staff17["NUM_TEACH"]-staff17["NUM_FEWER_3YRS_EXP"]
staff17["PER_TURN_EXP"] = staff17["NUM_EXP_TURN"]/staff17["NUM_TEACH_EXP"]
staff17 = staff17[['SCHOOL_NAME','YEAR','PER_TURN_ALL','PER_TURN_FIVE_YRS', 'PER_TURN_EXP']]
staff17 = staff17.rename(columns={'PER_TURN_FIVE_YRS': 'PER_TURN_INEXP'})
staff17 = staff17.rename(columns={'SCHOOL_NAME': 'DISTRICT'})
staff17 = staff17.set_index('YEAR', drop=True)


#\\Cleaning 2018 -> This year the necessary data was split into two separate databases
file_path = './Inputs/Staff2018.xlsx'
staff18 = pd.read_excel(file_path)
staff18["ENTITY_CD"] = staff18["ENTITY_CD"].astype(str)
staff18["YEAR"] = staff18["YEAR"].astype(str)
staff18["ENTITY_CD"] = staff18["ENTITY_CD"].str[-4:]
staff18 = staff18[~staff18['SCHOOL_NAME'].str.contains('County')]
staff18= staff18.query("ENTITY_CD=='0000'")
staff18 = staff18.query("YEAR=='2018'")
staff18['PER_TURN_ALL'] = staff18['PER_TURN_ALL']/100
staff18['PER_TURN_FIVE_YRS'] = staff18['PER_TURN_FIVE_YRS']/100
staff18["NUM_TOT_TURN"] = staff18["PER_TURN_ALL"]*staff18["NUM_TEACH"]
staff18 = staff18.rename(columns={'SCHOOL_NAME': 'DISTRICT'})

#Clean experience dataset
file_path = './Inputs/2018experience.xlsx'
exp2018 = pd.read_excel(file_path)
exp2018["ENTITY_CD"] = exp2018["ENTITY_CD"].astype(str)
exp2018["YEAR"] = exp2018["YEAR"].astype(str)
exp2018["ENTITY_CD"] = exp2018["ENTITY_CD"].str[-4:]
exp2018 = exp2018[~exp2018['ENTITY_NAME'].str.contains('County')]
exp2018= exp2018.query("ENTITY_CD=='0000'")
exp2018 = exp2018.query("YEAR=='2018'")
exp2018 = exp2018.rename(columns={'ENTITY_NAME': 'DISTRICT'})
exp2018 = exp2018[['YEAR', 'DISTRICT', 'NUM_TEACH_INEXP', 'PER_TEACH_INEXP']]

#Merge with staff data
staff18 = staff18.merge(exp2018, how='outer', on=['YEAR','DISTRICT'])

#//Calculate the turnover rate for experienced teachers
staff18["NUM_INEXP_TURN"] = staff18["PER_TURN_FIVE_YRS"]*staff18["NUM_TEACH_INEXP"]
staff18["NUM_EXP_TURN"] = staff18["NUM_TOT_TURN"] - staff18["NUM_INEXP_TURN"]
staff18["NUM_TEACH_EXP"] = staff18["NUM_TEACH"]-staff18["NUM_TEACH_INEXP"]
staff18["PER_TURN_EXP"] = staff18["NUM_EXP_TURN"]/staff18["NUM_TEACH_EXP"]
staff18 = staff18.rename(columns={'PER_TURN_FIVE_YRS': 'PER_TURN_INEXP'})
staff18 = staff18[['DISTRICT','YEAR','PER_TURN_ALL','PER_TURN_INEXP', 'PER_TURN_EXP']]
staff18 = staff18.set_index('YEAR', drop=True)

#2019
file_path = './Inputs/Staff2019.xlsx'
staff19 = pd.read_excel(file_path)
staff19["ENTITY_CD"] = staff19["ENTITY_CD"].astype(str)
staff19["YEAR"] = staff19["YEAR"].astype(str)
staff19["ENTITY_CD"] = staff19["ENTITY_CD"].str[-4:]
staff19 = staff19[~staff19['SCHOOL_NAME'].str.contains('County')]
staff19= staff19.query("ENTITY_CD=='0000'")
staff19 = staff19.query("YEAR=='2019'")
staff19['PER_TURN_ALL'] = staff19['PER_TURN_ALL']/100
staff19['PER_TURN_FIVE_YRS'] = staff19['PER_TURN_FIVE_YRS']/100
staff19["NUM_TOT_TURN"] = staff19["PER_TURN_ALL"]*staff19["NUM_TEACH"]
staff19 = staff19.rename(columns={'SCHOOL_NAME': 'DISTRICT'})

#Clean 2019 experience dataset
file_path = './Inputs/2019experience.xlsx'
exp2019 = pd.read_excel(file_path)
exp2019["ENTITY_CD"] = exp2019["ENTITY_CD"].astype(str)
exp2019["YEAR"] = exp2019["YEAR"].astype(str)
exp2019["ENTITY_CD"] = exp2019["ENTITY_CD"].str[-4:]
exp2019 = exp2019[~exp2019['ENTITY_NAME'].str.contains('County')]
exp2019= exp2019.query("ENTITY_CD=='0000'")
exp2019 = exp2019.query("YEAR=='2019'")
exp2019 = exp2019.rename(columns={'ENTITY_NAME': 'DISTRICT'})
exp2019 = exp2019[['YEAR', 'DISTRICT', 'NUM_TEACH_INEXP', 'PER_TEACH_INEXP']]

#\\Merge with 2019 staff
staff19 = staff19.merge(exp2019, how='outer', on=['YEAR','DISTRICT'])

#//Calculate the turnover rate for experienced teachers
staff19["NUM_INEXP_TURN"] = staff19["PER_TURN_FIVE_YRS"]*staff19["NUM_TEACH_INEXP"]
staff19["NUM_EXP_TURN"] = staff19["NUM_TOT_TURN"] - staff19["NUM_INEXP_TURN"]
staff19["NUM_TEACH_EXP"] = staff19["NUM_TEACH"]-staff19["NUM_TEACH_INEXP"]
staff19["PER_TURN_EXP"] = staff19["NUM_EXP_TURN"]/staff19["NUM_TEACH_EXP"]
staff19 = staff19.rename(columns={'PER_TURN_FIVE_YRS': 'PER_TURN_INEXP'})
staff19 = staff19[['DISTRICT','YEAR','PER_TURN_ALL','PER_TURN_INEXP', 'PER_TURN_EXP']]
staff19 = staff19.set_index('YEAR', drop=True)


#\\2020
file_path = './Inputs/Staff2020.xlsx'
staff20 = pd.read_excel(file_path)
staff20["ENTITY_CD"] = staff20["ENTITY_CD"].astype(str)
staff20["YEAR"] = staff20["YEAR"].astype(str)
staff20["ENTITY_CD"] = staff20["ENTITY_CD"].str[-4:]
staff20 = staff20[~staff20['SCHOOL_NAME'].str.contains('County')]
staff20 = staff20.query("ENTITY_CD=='0000'")
staff20 = staff20.query("YEAR=='2020'")
staff20['PER_TURN_ALL'] = staff20['PER_TURN_ALL']/100
staff20['PER_TURN_FIVE_YRS'] = staff20['PER_TURN_FIVE_YRS']/100
staff20["NUM_TOT_TURN"] = staff20["PER_TURN_ALL"]*staff20["NUM_TEACH"]
staff20 = staff20.rename(columns={'SCHOOL_NAME': 'DISTRICT'})

#Clean 2020 experience dataset
file_path = './Inputs/2020experience.xlsx'
exp2020 = pd.read_excel(file_path)
exp2020["ENTITY_CD"] = exp2020["ENTITY_CD"].astype(str)
exp2020["YEAR"] = exp2020["YEAR"].astype(str)
exp2020["ENTITY_CD"] = exp2020["ENTITY_CD"].str[-4:]
exp2020 = exp2020[~exp2020['ENTITY_NAME'].str.contains('County')]
exp2020= exp2020.query("ENTITY_CD=='0000'")
exp2020 = exp2020.query("YEAR=='2020'")
exp2020 = exp2020.rename(columns={'ENTITY_NAME': 'DISTRICT'})
exp2020 = exp2020[['YEAR', 'DISTRICT', 'NUM_TEACH_INEXP', 'PER_TEACH_INEXP']]

#Merge with 2020 staff
staff20 = staff20.merge(exp2020, how='outer', on=['YEAR','DISTRICT'])

#//Calculate the turnover rate for experienced teachers
staff20["NUM_INEXP_TURN"] = staff20["PER_TURN_FIVE_YRS"]*staff20["NUM_TEACH_INEXP"]
staff20["NUM_EXP_TURN"] = staff20["NUM_TOT_TURN"] - staff20["NUM_INEXP_TURN"]
staff20["NUM_TEACH_EXP"] = staff20["NUM_TEACH"]-staff20["NUM_TEACH_INEXP"]
staff20["PER_TURN_EXP"] = staff20["NUM_EXP_TURN"]/staff20["NUM_TEACH_EXP"]
staff20 = staff20.rename(columns={'PER_TURN_FIVE_YRS': 'PER_TURN_INEXP'})
staff20 = staff20[['DISTRICT','YEAR','PER_TURN_ALL','PER_TURN_INEXP', 'PER_TURN_EXP']]
staff20 = staff20.set_index('YEAR', drop=True)


#\\2021
file_path = './Inputs/Staff2021.xlsx'
staff21 = pd.read_excel(file_path)
staff21["ENTITY_CD"] = staff21["ENTITY_CD"].astype(str)
staff21["YEAR"] = staff21["YEAR"].astype(str)
staff21["ENTITY_CD"] = staff21["ENTITY_CD"].str[-4:]
staff21 = staff21[~staff21['SCHOOL_NAME'].str.contains('County')]
staff21= staff21.query("ENTITY_CD=='0000'")
staff21 = staff21.query("YEAR=='2021'")
staff21['PER_TURN_ALL'] = staff21['PER_TURN_ALL']/100
staff21['PER_TURN_FIVE_YRS'] = staff21['PER_TURN_FIVE_YRS']/100
staff21["NUM_TOT_TURN"] = staff21["PER_TURN_ALL"]*staff21["NUM_TEACH"]
staff21 = staff21.rename(columns={'SCHOOL_NAME': 'DISTRICT'})

#Clean 2021 experience dataset
file_path = './Inputs/2021experience.xlsx'
exp2021 = pd.read_excel(file_path)
exp2021["ENTITY_CD"] = exp2021["ENTITY_CD"].astype(str)
exp2021["YEAR"] = exp2021["YEAR"].astype(str)
exp2021["ENTITY_CD"] = exp2021["ENTITY_CD"].str[-4:]
exp2021 = exp2021[~exp2021['ENTITY_NAME'].str.contains('County')]
exp2021 = exp2021.query("ENTITY_CD=='0000'")
exp2021 = exp2021.query("YEAR=='2021'")
exp2021 = exp2021.rename(columns={'ENTITY_NAME': 'DISTRICT'})
exp2021 = exp2021[['YEAR', 'DISTRICT', 'NUM_TEACH_INEXP', 'PER_TEACH_INEXP']]

#Merge with 2021 staff
staff21 = staff21.merge(exp2021, how='outer', on=['YEAR','DISTRICT'])

#//Calculate the turnover rate for experienced teachers
staff21["NUM_INEXP_TURN"] = staff21["PER_TURN_FIVE_YRS"]*staff21["NUM_TEACH_INEXP"]
staff21["NUM_EXP_TURN"] = staff21["NUM_TOT_TURN"] - staff21["NUM_INEXP_TURN"]
staff21["NUM_TEACH_EXP"] = staff21["NUM_TEACH"]-staff21["NUM_TEACH_INEXP"]
staff21["PER_TURN_EXP"] = staff21["NUM_EXP_TURN"]/staff21["NUM_TEACH_EXP"]
staff21 = staff21.rename(columns={'PER_TURN_FIVE_YRS': 'PER_TURN_INEXP'})
staff21 = staff21[['DISTRICT','YEAR','PER_TURN_ALL','PER_TURN_INEXP', 'PER_TURN_EXP']]
staff21 = staff21.set_index('YEAR', drop=True)


#\\2022
file_path = './Inputs/Staff2022.xlsx'
staff22 = pd.read_excel(file_path)
staff22["ENTITY_CD"] = staff22["ENTITY_CD"].astype(str)
staff22["YEAR"] = staff22["YEAR"].astype(str)
staff22["ENTITY_CD"] = staff22["ENTITY_CD"].str[-4:]
staff22 = staff22[~staff22['SCHOOL_NAME'].str.contains('County')]
staff22= staff22.query("ENTITY_CD=='0000'")
staff22 = staff22.query("YEAR=='2022'")
staff22['PER_TURN_ALL'] = staff22['PER_TURN_ALL']/100
staff22['PER_TURN_FIVE_YRS'] = staff22['PER_TURN_FIVE_YRS']/100
staff22["NUM_TOT_TURN"] = staff22["PER_TURN_ALL"]*staff22["NUM_TEACH"]
staff22 = staff22.rename(columns={'SCHOOL_NAME': 'DISTRICT'})

#Clean 2022 experience dataset
file_path = './Inputs/2022experience.xlsx'
exp2022 = pd.read_excel(file_path)
exp2022["ENTITY_CD"] = exp2022["ENTITY_CD"].astype(str)
exp2022["YEAR"] = exp2022["YEAR"].astype(str)
exp2022["ENTITY_CD"] = exp2022["ENTITY_CD"].str[-4:]
exp2022 = exp2022[~exp2022['ENTITY_NAME'].str.contains('County')]
exp2022 = exp2022.query("ENTITY_CD=='0000'")
exp2022 = exp2022.query("YEAR=='2022'")
exp2022 = exp2022.rename(columns={'ENTITY_NAME': 'DISTRICT'})
exp2022 = exp2022[['YEAR', 'DISTRICT', 'NUM_TEACH_INEXP', 'PER_TEACH_INEXP']]

#Merge with 2022 staff
staff22 = staff22.merge(exp2022, how='outer', on=['YEAR','DISTRICT'])

#//Calculate the turnover rate for experienced teachers
staff22["NUM_INEXP_TURN"] = staff22["PER_TURN_FIVE_YRS"]*staff22["NUM_TEACH_INEXP"]
staff22["NUM_EXP_TURN"] = staff22["NUM_TOT_TURN"] - staff22["NUM_INEXP_TURN"]
staff22["NUM_TEACH_EXP"] = staff22["NUM_TEACH"]-staff22["NUM_TEACH_INEXP"]
staff22["PER_TURN_EXP"] = staff22["NUM_EXP_TURN"]/staff22["NUM_TEACH_EXP"]
staff22 = staff22.rename(columns={'PER_TURN_FIVE_YRS': 'PER_TURN_INEXP'})
staff22 = staff22[['DISTRICT','YEAR','PER_TURN_ALL','PER_TURN_INEXP', 'PER_TURN_EXP']]
staff22 = staff22.set_index('YEAR', drop=True)

#\\Merging Turnover Data into a panel dataframe
panel = staff14.merge(staff15, how='outer', on=['YEAR', 'DISTRICT', 'PER_TURN_ALL', 'PER_TURN_INEXP', 'PER_TURN_EXP'])
panel = panel.merge(staff16, how='outer', on=['YEAR', 'DISTRICT', 'PER_TURN_ALL', 'PER_TURN_INEXP', 'PER_TURN_EXP'])
panel = panel.merge(staff17, how='outer', on=['YEAR', 'DISTRICT', 'PER_TURN_ALL', 'PER_TURN_INEXP', 'PER_TURN_EXP'])
panel = panel.merge(staff18, how='outer', on=['YEAR', 'DISTRICT', 'PER_TURN_ALL', 'PER_TURN_INEXP', 'PER_TURN_EXP'])
panel = panel.merge(staff19, how='outer', on=['YEAR', 'DISTRICT', 'PER_TURN_ALL', 'PER_TURN_INEXP', 'PER_TURN_EXP'])
panel = panel.merge(staff20, how='outer', on=['YEAR', 'DISTRICT', 'PER_TURN_ALL', 'PER_TURN_INEXP', 'PER_TURN_EXP'])
panel = panel.merge(staff21, how='outer', on=['YEAR', 'DISTRICT', 'PER_TURN_ALL', 'PER_TURN_INEXP', 'PER_TURN_EXP'])
panel = panel.merge(staff22, how='outer', on=['YEAR', 'DISTRICT', 'PER_TURN_ALL', 'PER_TURN_INEXP', 'PER_TURN_EXP'])

#Exports the panel to a CSV
Outputs = './Outputs/'
panel.to_csv(Outputs + 'TurnoverPanel.csv', index=True)


#\\Making a Descriptive Bar Chart for average turnover rate for each experience level for 2014-2022
import matplotlib.pyplot as plt
import seaborn as sns
fig4, ax4=plt.subplots()
panel_avg = panel[['PER_TURN_ALL', 'PER_TURN_INEXP', 'PER_TURN_EXP']].mean()
panel_avg.plot.barh(title="Avg. Turnover from 2014-2022", color=['navy', 'lightseagreen', 'royalblue'], ax=ax4)
plt.show()
plt.savefig(Outputs + "AvgTurn14.22.png")

#\\Creates a line chart showing the development over time
fig3, ax3=plt.subplots()
plt.rcParams['figure.dpi'] = 300
ax3.set_ylim(0.0, 0.3)
lineplt = panel.groupby('YEAR')[['PER_TURN_ALL', 'PER_TURN_EXP', 'PER_TURN_INEXP']].mean()
sns.lineplot(data=panel[['PER_TURN_ALL', 'PER_TURN_EXP', 'PER_TURN_INEXP']], palette="mako", ax=ax3)
plt.savefig(Outputs + "TurnoverOverYears.png")