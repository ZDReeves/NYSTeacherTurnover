# -*- coding: utf-8 -*-
"""
Created on Fri May  3 11:19:11 2024

@author: zacha
"""

#\\This section imports the two panel datasets created in previous scripts. Then, it takes the turnover rates and
# multiples them by 100 to make them more user friendly. 
import pandas as pd
file_path = './Outputs/TurnoverPanel.csv'
TurnoverPanel = pd.read_csv(file_path)
file_path = './Outputs/DEMOpanel.csv'
DemoPanel = pd.read_csv(file_path)
TurnoverPanel["YEAR"] = TurnoverPanel["YEAR"].astype(str)
DemoPanel["YEAR"] = DemoPanel["YEAR"].astype(str)
merged = TurnoverPanel.merge(DemoPanel, how='outer', on=['YEAR','DISTRICT'])
merged['PER_TURN_ALL'] = merged['PER_TURN_ALL']*100
merged['PER_TURN_EXP'] = merged['PER_TURN_EXP']*100
merged['PER_TURN_INEXP'] = merged['PER_TURN_INEXP']*100
Outputs = './Outputs/'
merged.to_csv(Outputs + 'merged.csv', index=False)

#\\Setting up the entity and year fixed effects for each of the models in this script
import statsmodels.api as sm
fixed_effects_entity = pd.get_dummies(merged['DISTRICT'])
fixed_effects_time = pd.get_dummies(merged['YEAR'])
data_with_FE = pd.concat([merged, fixed_effects_entity, fixed_effects_time], axis=1)
data_with_FE['PER_TURN_ALL']=data_with_FE['PER_TURN_ALL'].astype(float)
data_with_FE['PER_TURN_EXP']=data_with_FE['PER_TURN_EXP'].astype(float)
data_with_FE['PER_TURN_INEXP']=data_with_FE['PER_TURN_INEXP'].astype(float)
data_with_FE['PER_FRPL']=data_with_FE['PER_FRPL'].astype(float)
data_with_FE['PER_MINORITY']=data_with_FE['PER_MINORITY'].astype(float)
data_with_FE = data_with_FE.dropna(subset="PER_TURN_ALL")
data_with_FE = data_with_FE.dropna(subset="PER_TURN_EXP")
data_with_FE = data_with_FE.dropna(subset="PER_TURN_INEXP")
data_with_FE = data_with_FE.dropna(subset="PER_FRPL")
data_with_FE = data_with_FE.dropna(subset="PER_MINORITY")

#\\Model #1: Y=Total turnover, X= %FRPL
print('Model #1')
dep_var1  = data_with_FE[['PER_TURN_ALL']]
ind_vars1 = data_with_FE[['PER_FRPL']]
ind_vars1 = sm.add_constant(ind_vars1)
model1 = sm.OLS(dep_var1, ind_vars1)
results1 = model1.fit()
print( results1.summary() )


#\\Model #2: Y=Total turnover, X= %FRPL, %Minority
print('Model #2')
dep_var2  = data_with_FE[['PER_TURN_ALL']]
ind_vars2 = data_with_FE[['PER_FRPL', 'PER_MINORITY']]
ind_vars2 = sm.add_constant(ind_vars2)
model2 = sm.OLS(dep_var2, ind_vars2)
results2 = model2.fit()
print( results2.summary() )

#\\Model #3: Y=Experienced turnover, X= %FRPL
print('Model #3')
dep_var3  = data_with_FE[['PER_TURN_EXP']]
ind_vars3 = data_with_FE[['PER_FRPL']]
ind_vars3 = sm.add_constant(ind_vars3)
model3 = sm.OLS(dep_var3, ind_vars3)
results3 = model3.fit()
print( results3.summary() )


#\\Model #4: Y=Experienced turnover, X= %FRPL, %Minority
print('Model #4')
dep_var4  = data_with_FE[['PER_TURN_EXP']]
ind_vars4 = data_with_FE[['PER_FRPL', 'PER_MINORITY']]
ind_vars4 = sm.add_constant(ind_vars4)
model4 = sm.OLS(dep_var4, ind_vars4)
results4 = model4.fit()
print( results4.summary() )

#\\Model #5: Y=Inexperienced turnover, X= %FRPL
print('Model #5')
dep_var5  = data_with_FE[['PER_TURN_INEXP']]
ind_vars5 = data_with_FE[['PER_FRPL']]
ind_vars5 = sm.add_constant(ind_vars5)
model5 = sm.OLS(dep_var5, ind_vars5)
results5 = model5.fit()
print( results5.summary() )


#\\Model #6: Y=Inexperienced turnover, X= %FRPL, %Minority
print('Model #6')
dep_var5  = data_with_FE[['PER_TURN_INEXP']]
ind_vars5 = data_with_FE[['PER_FRPL', 'PER_MINORITY']]
ind_vars5 = sm.add_constant(ind_vars5)
model5 = sm.OLS(dep_var5, ind_vars2)
results5 = model5.fit()
print( results5.summary() )