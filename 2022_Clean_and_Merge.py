# -*- coding: utf-8 -*-
"""
Created on Fri May  3 11:05:09 2024

@author: zacha
"""

#\\The first section of this script reads the excel files for relevant 2022 data.
import pandas as pd
import os

attendance = pd.read_excel("Attendance.xlsx")
demo = pd.read_excel("Demographics.xlsx")
expend = pd.read_excel("ExpPerPupil.xlsx")
staff = pd.read_excel("StaffData.xlsx")
experience = pd.read_excel("TPExperience.xlsx")
frpl = pd.read_excel("FreeReducedPriceLunch.xlsx")
enrollment = pd.read_excel("Enrollment.xlsx")

#\\This section repeats similar steps for cleaning each of the excel files.
# In particular, it trims the files down to only include school district level data (entity_cd==0000)
# for the specific variables we care about.
script_dir = os.path.dirname(os.path.abspath())
enrollment["ENTITY_CD"] = enrollment["ENTITY_CD"].astype(str)
enrollment["YEAR"] = enrollment["YEAR"].astype(str)
enrollment["ENTITY_CD"] = enrollment["ENTITY_CD"].str[-4:]
enrollment = enrollment[~enrollment['ENTITY_NAME'].str.contains('County')]
enrollment = enrollment.query("ENTITY_CD=='0000'")
enrollment = enrollment.query("YEAR=='2022'")
enrollment = enrollment[['ENTITY_NAME','YEAR','K12']]
enrollment = enrollment.rename(columns={'ENTITY_NAME': 'DISTRICT'})


frpl["ENTITY_CD"] = frpl["ENTITY_CD"].astype(str)
frpl["YEAR"] = frpl["YEAR"].astype(str)
frpl["ENTITY_CD"] = frpl["ENTITY_CD"].str[-4:]
frpl = frpl[~frpl['ENTITY_NAME'].str.contains('County')]
frpl= frpl.query("ENTITY_CD=='0000'")
frpl= frpl.query("YEAR=='2022'")
frpl = frpl[['ENTITY_NAME','YEAR','PER_FREE_LUNCH', 'PER_REDUCED_LUNCH']]
frpl = frpl.rename(columns={'ENTITY_NAME': 'DISTRICT'})
frpl['PER_FRPL'] = frpl['PER_FREE_LUNCH'] + frpl['PER_REDUCED_LUNCH']


attendance["ENTITY_CD"] = attendance["ENTITY_CD"].astype(str)
attendance["YEAR"] = attendance["YEAR"].astype(str)
attendance["ENTITY_CD"] = attendance["ENTITY_CD"].str[-4:]
attendance = attendance[~attendance['ENTITY_NAME'].str.contains('County')]
attendance = attendance.query("ENTITY_CD=='0000'")
attendance = attendance.query("YEAR=='2022'")
attendance = attendance[['ENTITY_NAME','YEAR','ATTENDANCE_RATE']]
attendance = attendance.rename(columns={'ENTITY_NAME': 'DISTRICT'})


demo["ENTITY_CD"] = demo["ENTITY_CD"].astype(str)
demo["YEAR"] = demo["YEAR"].astype(str)
demo["ENTITY_CD"] = demo["ENTITY_CD"].str[-4:]
demo = demo[~demo['ENTITY_NAME'].str.contains('County')]
demo = demo.query("ENTITY_CD=='0000'")
demo = demo.query("YEAR=='2022'")
demo = demo[['ENTITY_NAME','YEAR','PER_ELL', 'PER_BLACK', 'PER_HISP', 'PER_ASIAN', 'PER_WHITE', 'PER_SWD']]
demo = demo.rename(columns={'ENTITY_NAME': 'DISTRICT'})

expend["ENTITY_CD"] = expend["ENTITY_CD"].astype(str)
expend["YEAR"] = expend["YEAR"].astype(str)
expend["ENTITY_CD"] = expend["ENTITY_CD"].str[-4:]
expend = expend[~expend['ENTITY_NAME'].str.contains('County')]
expend = expend.query("ENTITY_CD=='0000'")
expend = expend.query("YEAR=='2022'")
expend = expend[['ENTITY_NAME','YEAR','PER_STATE_LOCAL_EXP','PER_FED_STATE_LOCAL_EXP']]
expend = expend.rename(columns={'ENTITY_NAME': 'DISTRICT'})


staff["ENTITY_CD"] = staff["ENTITY_CD"].astype(str)
staff["YEAR"] = staff["YEAR"].astype(str)
staff["ENTITY_CD"] = staff["ENTITY_CD"].str[-4:]
staff = staff[~staff['SCHOOL_NAME'].str.contains('County')]
staff = staff.query("ENTITY_CD=='0000'")
staff = staff.query("YEAR=='2022'")
staff = staff[['SCHOOL_NAME','YEAR','PER_TURN_ALL','PER_TURN_FIVE_YRS']]
staff = staff.rename(columns={'SCHOOL_NAME': 'DISTRICT'})

#//This section cleans the teacher experience data in a similar way to the other excel files.
# But there is one key difference: I calculate Number of experienced teachers and the percentage of
# teachers who are considered "experienced". This is then used to calculate the turnover rate among 
# experienced teachers after mergins all of the files together.
experience["ENTITY_CD"] = experience["ENTITY_CD"].astype(str)
experience["YEAR"] = experience["YEAR"].astype(str)
experience["ENTITY_CD"] = experience["ENTITY_CD"].str[-4:]
experience = experience[~experience['ENTITY_NAME'].str.contains('County')]
experience = experience.query("ENTITY_CD=='0000'")
experience = experience.query("YEAR=='2022'")
experience = experience[['ENTITY_NAME','YEAR','NUM_TEACH', 'NUM_TEACH_INEXP','PER_TEACH_INEXP']]
experience = experience.rename(columns={'ENTITY_NAME': 'DISTRICT'})
experience['NUM_TEACH_EXP'] = experience["NUM_TEACH"] - experience['NUM_TEACH_INEXP']
experience['PER_TEACH_EXP'] = experience["NUM_TEACH_EXP"]/experience['NUM_TEACH']*100

#// This section just merges everything together.
dist_characteristics = staff.merge(experience, how='left', on=['DISTRICT', 'YEAR'])
dist_characteristics = dist_characteristics.merge(frpl, how='left', on=['DISTRICT', 'YEAR'])
dist_characteristics = dist_characteristics.merge(enrollment, how='left', on=['DISTRICT', 'YEAR'])
dist_characteristics = dist_characteristics.merge(attendance, how='left', on=['DISTRICT','YEAR'])
dist_characteristics = dist_characteristics.merge(demo, how='left', on=['DISTRICT','YEAR'])
dist_characteristics = dist_characteristics.merge(expend, how='left', on=['DISTRICT', 'YEAR'])

#//This section calculates the turnover rate for experienced teachers using the total number of teachers, the number of inexperienced teachers,
# the total turnover percentage, and the turnover rate among inexperienced teachers. 
dist_characteristics['PER_TURN_ALL'] = dist_characteristics['PER_TURN_ALL']/100
dist_characteristics['PER_TURN_FIVE_YRS'] = dist_characteristics['PER_TURN_FIVE_YRS']/100
dist_characteristics["NUM_TOT_TURN"] = dist_characteristics["PER_TURN_ALL"]*dist_characteristics["NUM_TEACH"]
dist_characteristics["NUM_INEXP_TURN"] = dist_characteristics["PER_TURN_FIVE_YRS"]*dist_characteristics["NUM_TEACH_INEXP"]
dist_characteristics["NUM_EXP_TURN"] = dist_characteristics["NUM_TOT_TURN"] - dist_characteristics["NUM_INEXP_TURN"]
dist_characteristics["NUM_TEACH_EXP"] = dist_characteristics["NUM_TEACH"]-dist_characteristics["NUM_TEACH_INEXP"]
dist_characteristics["PER_TURN_EXP"] = dist_characteristics["NUM_EXP_TURN"]/dist_characteristics["NUM_TEACH_EXP"]
dist_characteristics = dist_characteristics.rename(columns={'PER_TURN_FIVE_YRS': 'PER_TURN_INEXP'})
dist_turnover = dist_characteristics[['DISTRICT','YEAR','PER_TURN_ALL','PER_TURN_INEXP', 'PER_TURN_EXP']]
dist_turnover = dist_turnover.set_index('YEAR', drop=True)

#//This exports the information to csv files that will be used in later scripts
dist_turnover.to_csv('dist_turnover.csv', index=False)
dist_characteristics.to_csv('dist_characteristics.csv', index=False)
