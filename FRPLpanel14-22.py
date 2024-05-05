# -*- coding: utf-8 -*-
"""
Created on Fri May  3 11:17:15 2024

@author: zacha
"""
#\\Importing the NYS datasets on Free or Reduced Price Lunch 
import pandas as pd

#\\As was the case for the Turnover datasets, I extracted the district level data by using a query to identify
# the ENTITY_CDs. A key component of this script is that the NYS Department of Ed. separated FRPL data 
# from other demographic data for the 2017/18 school year. Thus, years 2018-2022 require a seprate merge to 
# create a dataset like those from 2014-2017. 

file_path = './Inputs/FRPL2014.xlsx'
FRPL14 = pd.read_excel(file_path)
FRPL14["ENTITY_CD"] = FRPL14["ENTITY_CD"].astype(str)
FRPL14["YEAR"] = FRPL14["YEAR"].astype(str)
FRPL14["ENTITY_CD"] = FRPL14["ENTITY_CD"].str[-4:]
FRPL14= FRPL14[~FRPL14['ENTITY_NAME'].str.contains('County')]
FRPL14= FRPL14.query("ENTITY_CD=='0000'")
FRPL14= FRPL14.query("YEAR=='2014'")
FRPL14 = FRPL14[['ENTITY_NAME','YEAR','PER_FREE_LUNCH', 'PER_REDUCED_LUNCH','PER_BLACK', 'PER_HISP', 'PER_ASIAN']]
FRPL14 = FRPL14.rename(columns={'ENTITY_NAME': 'DISTRICT'})
FRPL14['PER_FRPL'] = FRPL14['PER_FREE_LUNCH'] + FRPL14['PER_REDUCED_LUNCH']
FRPL14['PER_MINORITY'] = FRPL14['PER_BLACK'] + FRPL14['PER_HISP'] + FRPL14['PER_ASIAN']
FRPL14 = FRPL14.set_index('YEAR', drop=True)

#\\Cleaning the 2015 Data to prepare for merging into a panel
file_path = './Inputs/FRPL2015.xlsx'
FRPL15 = pd.read_excel(file_path)
FRPL15["ENTITY_CD"] = FRPL15["ENTITY_CD"].astype(str)
FRPL15["YEAR"] = FRPL15["YEAR"].astype(str)
FRPL15["ENTITY_CD"] = FRPL15["ENTITY_CD"].str[-4:]
FRPL15= FRPL15[~FRPL15['ENTITY_NAME'].str.contains('County')]
FRPL15= FRPL15.query("ENTITY_CD=='0000'")
FRPL15= FRPL15.query("YEAR=='2015'")
FRPL15 = FRPL15[['ENTITY_NAME','YEAR','PER_FREE_LUNCH', 'PER_REDUCED_LUNCH','PER_BLACK', 'PER_HISP', 'PER_ASIAN']]
FRPL15 = FRPL15.rename(columns={'ENTITY_NAME': 'DISTRICT'})
FRPL15['PER_FRPL'] = FRPL15['PER_FREE_LUNCH'] + FRPL15['PER_REDUCED_LUNCH']
FRPL15['PER_MINORITY'] = FRPL15['PER_BLACK'] + FRPL15['PER_HISP'] + FRPL15['PER_ASIAN']
FRPL15 = FRPL15.set_index('YEAR', drop=True)

#\\Cleaning the 2016 Data to prepare for merging into a panel
file_path = './Inputs/FRPL2016.xlsx'
FRPL16 = pd.read_excel(file_path)
FRPL16["ENTITY_CD"] = FRPL16["ENTITY_CD"].astype(str)
FRPL16["YEAR"] = FRPL16["YEAR"].astype(str)
FRPL16["ENTITY_CD"] = FRPL16["ENTITY_CD"].str[-4:]
FRPL16= FRPL16[~FRPL16['ENTITY_NAME'].str.contains('County')]
FRPL16= FRPL16.query("ENTITY_CD=='0000'")
FRPL16= FRPL16.query("YEAR=='2016'")
FRPL16 = FRPL16[['ENTITY_NAME','YEAR','PER_FREE_LUNCH', 'PER_REDUCED_LUNCH','PER_BLACK', 'PER_HISP', 'PER_ASIAN']]
FRPL16 = FRPL16.rename(columns={'ENTITY_NAME': 'DISTRICT'})
FRPL16['PER_FRPL'] = FRPL16['PER_FREE_LUNCH'] + FRPL16['PER_REDUCED_LUNCH']
FRPL16['PER_MINORITY'] = FRPL16['PER_BLACK'] + FRPL16['PER_HISP'] + FRPL16['PER_ASIAN']
FRPL16 = FRPL16.set_index('YEAR', drop=True)

#\\Cleaning the 2017 Data to prepare for merging into a panel
file_path = './Inputs/FRPL2017.xlsx'
FRPL17 = pd.read_excel(file_path)
FRPL17["ENTITY_CD"] = FRPL17["ENTITY_CD"].astype(str)
FRPL17["YEAR"] = FRPL17["YEAR"].astype(str)
FRPL17["ENTITY_CD"] = FRPL17["ENTITY_CD"].str[-4:]
FRPL17= FRPL17[~FRPL17['ENTITY_NAME'].str.contains('County')]
FRPL17= FRPL17.query("ENTITY_CD=='0000'")
FRPL17= FRPL17.query("YEAR=='2017'")
FRPL17 = FRPL17[['ENTITY_NAME','YEAR','PER_FREE_LUNCH', 'PER_REDUCED_LUNCH','PER_BLACK', 'PER_HISP', 'PER_ASIAN']]
FRPL17 = FRPL17.rename(columns={'ENTITY_NAME': 'DISTRICT'})
FRPL17['PER_FRPL'] = FRPL17['PER_FREE_LUNCH'] + FRPL17['PER_REDUCED_LUNCH']
FRPL17['PER_MINORITY'] = FRPL17['PER_BLACK'] + FRPL17['PER_HISP'] + FRPL17['PER_ASIAN']
FRPL17 = FRPL17.set_index('YEAR', drop=True)

#\\Cleaning the 2018 Data to prepare for merging into a panel. For the 2017/18 school year,
# the NYS Department of Ed. separated FRPL data from other demographic data into two separate datasets. So,
# for 2018-2022, I merged the demographics dataset with the FRPL dataset to produce the same
# set of information as was contained in the single dataset for 2014-2017.
file_path = './Inputs/FRPL2018.xlsx'
FRPL18 = pd.read_excel(file_path)
FRPL18["ENTITY_CD"] = FRPL18["ENTITY_CD"].astype(str)
FRPL18["YEAR"] = FRPL18["YEAR"].astype(str)
FRPL18["ENTITY_CD"] = FRPL18["ENTITY_CD"].str[-4:]
FRPL18= FRPL18[~FRPL18['ENTITY_NAME'].str.contains('County')]
FRPL18= FRPL18.query("ENTITY_CD=='0000'")
FRPL18= FRPL18.query("YEAR=='2018'")
FRPL18 = FRPL18[['ENTITY_NAME','YEAR','PER_FREE_LUNCH', 'PER_REDUCED_LUNCH']]
FRPL18 = FRPL18.rename(columns={'ENTITY_NAME': 'DISTRICT'})
FRPL18['PER_FRPL'] = FRPL18['PER_FREE_LUNCH'] + FRPL18['PER_REDUCED_LUNCH']
FRPL18 = FRPL18.set_index('YEAR', drop=True)

file_path = './Inputs/2018demo.xlsx'
demo18 = pd.read_excel(file_path)
demo18["ENTITY_CD"] = demo18["ENTITY_CD"].astype(str)
demo18["YEAR"] = demo18["YEAR"].astype(str)
demo18["ENTITY_CD"] = demo18["ENTITY_CD"].str[-4:]
demo18= demo18[~demo18['ENTITY_NAME'].str.contains('County')]
demo18= demo18.query("ENTITY_CD=='0000'")
demo18= demo18.query("YEAR=='2018'")
demo18 = demo18[['ENTITY_NAME','YEAR','PER_BLACK', 'PER_HISP', 'PER_ASIAN']]
demo18 = demo18.rename(columns={'ENTITY_NAME': 'DISTRICT'})
demo18['PER_MINORITY'] = demo18['PER_BLACK'] + demo18['PER_HISP'] + demo18['PER_ASIAN']
demo18 = demo18.set_index('YEAR', drop=True)
demo18 = demo18.merge(FRPL18, how='outer', on=['YEAR', 'DISTRICT'])

#\\Cleaning the 2019 Data to prepare for merging into a panel
file_path = './Inputs/FRPL2019.xlsx'
FRPL19 = pd.read_excel(file_path)
FRPL19["ENTITY_CD"] = FRPL19["ENTITY_CD"].astype(str)
FRPL19["YEAR"] = FRPL19["YEAR"].astype(str)
FRPL19["ENTITY_CD"] = FRPL19["ENTITY_CD"].str[-4:]
FRPL19= FRPL19[~FRPL19['ENTITY_NAME'].str.contains('County')]
FRPL19= FRPL19.query("ENTITY_CD=='0000'")
FRPL19= FRPL19.query("YEAR=='2019'")
FRPL19 = FRPL19[['ENTITY_NAME','YEAR','PER_FREE_LUNCH', 'PER_REDUCED_LUNCH']]
FRPL19 = FRPL19.rename(columns={'ENTITY_NAME': 'DISTRICT'})
FRPL19['PER_FRPL'] = FRPL19['PER_FREE_LUNCH'] + FRPL19['PER_REDUCED_LUNCH']
FRPL19 = FRPL19.set_index('YEAR', drop=True)

file_path = './Inputs/2019demo.xlsx'
demo19 = pd.read_excel(file_path)
demo19["ENTITY_CD"] = demo19["ENTITY_CD"].astype(str)
demo19["YEAR"] = demo19["YEAR"].astype(str)
demo19["ENTITY_CD"] = demo19["ENTITY_CD"].str[-4:]
demo19 = demo19[~demo19['ENTITY_NAME'].str.contains('County')]
demo19 = demo19.query("ENTITY_CD=='0000'")
demo19 = demo19.query("YEAR=='2019'")
demo19 = demo19[['ENTITY_NAME','YEAR','PER_BLACK', 'PER_HISP', 'PER_ASIAN']]
demo19 = demo19.rename(columns={'ENTITY_NAME': 'DISTRICT'})
demo19['PER_MINORITY'] = demo19['PER_BLACK'] + demo19['PER_HISP'] + demo19['PER_ASIAN']
demo19 = demo19.set_index('YEAR', drop=True)
demo19 = demo19.merge(FRPL19, how='outer', on=['YEAR', 'DISTRICT'])

#\\Cleaning the 2020 Data to prepare for merging into a panel
file_path = './Inputs/FRPL2020.xlsx'
FRPL20 = pd.read_excel(file_path)
FRPL20["ENTITY_CD"] = FRPL20["ENTITY_CD"].astype(str)
FRPL20["YEAR"] = FRPL20["YEAR"].astype(str)
FRPL20["ENTITY_CD"] = FRPL20["ENTITY_CD"].str[-4:]
FRPL20= FRPL20[~FRPL20['ENTITY_NAME'].str.contains('County')]
FRPL20= FRPL20.query("ENTITY_CD=='0000'")
FRPL20= FRPL20.query("YEAR=='2020'")
FRPL20 = FRPL20[['ENTITY_NAME','YEAR','PER_FREE_LUNCH', 'PER_REDUCED_LUNCH']]
FRPL20 = FRPL20.rename(columns={'ENTITY_NAME': 'DISTRICT'})
FRPL20['PER_FRPL'] = FRPL20['PER_FREE_LUNCH'] + FRPL20['PER_REDUCED_LUNCH']
FRPL20 = FRPL20.set_index('YEAR', drop=True)

file_path = './Inputs/2020demo.xlsx'
demo20 = pd.read_excel(file_path)
demo20["ENTITY_CD"] = demo20["ENTITY_CD"].astype(str)
demo20["YEAR"] = demo20["YEAR"].astype(str)
demo20["ENTITY_CD"] = demo20["ENTITY_CD"].str[-4:]
demo20 = demo20[~demo20['ENTITY_NAME'].str.contains('County')]
demo20 = demo20.query("ENTITY_CD=='0000'")
demo20 = demo20.query("YEAR=='2020'")
demo20 = demo20[['ENTITY_NAME','YEAR','PER_BLACK', 'PER_HISP', 'PER_ASIAN']]
demo20 = demo20.rename(columns={'ENTITY_NAME': 'DISTRICT'})
demo20['PER_MINORITY'] = demo20['PER_BLACK'] + demo20['PER_HISP'] + demo20['PER_ASIAN']
demo20 = demo20.set_index('YEAR', drop=True)
demo20 = demo20.merge(FRPL20, how='outer', on=['YEAR', 'DISTRICT'])

#\\Cleaning the 2021 Data to prepare for merging into a panel
file_path = './Inputs/FRPL2021.xlsx'
FRPL21 = pd.read_excel(file_path)
FRPL21["ENTITY_CD"] = FRPL21["ENTITY_CD"].astype(str)
FRPL21["YEAR"] = FRPL21["YEAR"].astype(str)
FRPL21["ENTITY_CD"] = FRPL21["ENTITY_CD"].str[-4:]
FRPL21= FRPL21[~FRPL21['ENTITY_NAME'].str.contains('County')]
FRPL21= FRPL21.query("ENTITY_CD=='0000'")
FRPL21= FRPL21.query("YEAR=='2021'")
FRPL21 = FRPL21[['ENTITY_NAME','YEAR','PER_FREE_LUNCH', 'PER_REDUCED_LUNCH']]
FRPL21 = FRPL21.rename(columns={'ENTITY_NAME': 'DISTRICT'})
FRPL21['PER_FRPL'] = FRPL21['PER_FREE_LUNCH'] + FRPL21['PER_REDUCED_LUNCH']
FRPL21 = FRPL21.set_index('YEAR', drop=True)

file_path = './Inputs/2021demo.xlsx'
demo21 = pd.read_excel(file_path)
demo21["ENTITY_CD"] = demo21["ENTITY_CD"].astype(str)
demo21["YEAR"] = demo21["YEAR"].astype(str)
demo21["ENTITY_CD"] = demo21["ENTITY_CD"].str[-4:]
demo21 = demo21[~demo21['ENTITY_NAME'].str.contains('County')]
demo21 = demo21.query("ENTITY_CD=='0000'")
demo21 = demo21.query("YEAR=='2021'")
demo21 = demo21[['ENTITY_NAME','YEAR','PER_BLACK', 'PER_HISP', 'PER_ASIAN']]
demo21 = demo21.rename(columns={'ENTITY_NAME': 'DISTRICT'})
demo21['PER_MINORITY'] = demo21['PER_BLACK'] + demo21['PER_HISP'] + demo21['PER_ASIAN']
demo21 = demo21.set_index('YEAR', drop=True)
demo21 = demo21.merge(FRPL21, how='outer', on=['YEAR', 'DISTRICT'])

#\\Cleaning the 2022 Data to prepare for merging into a panel
file_path = './Inputs/FRPL2022.xlsx'
FRPL22 = pd.read_excel(file_path)
FRPL22["ENTITY_CD"] = FRPL22["ENTITY_CD"].astype(str)
FRPL22["YEAR"] = FRPL22["YEAR"].astype(str)
FRPL22["ENTITY_CD"] = FRPL22["ENTITY_CD"].str[-4:]
FRPL22= FRPL22[~FRPL22['ENTITY_NAME'].str.contains('County')]
FRPL22= FRPL22.query("ENTITY_CD=='0000'")
FRPL22= FRPL22.query("YEAR=='2022'")
FRPL22 = FRPL22[['ENTITY_NAME','YEAR','PER_FREE_LUNCH', 'PER_REDUCED_LUNCH']]
FRPL22 = FRPL22.rename(columns={'ENTITY_NAME': 'DISTRICT'})
FRPL22['PER_FRPL'] = FRPL22['PER_FREE_LUNCH'] + FRPL22['PER_REDUCED_LUNCH']
FRPL22 = FRPL22.set_index('YEAR', drop=True)

file_path = './Inputs/Demographics.xlsx'
demo22 = pd.read_excel(file_path)
demo22["ENTITY_CD"] = demo22["ENTITY_CD"].astype(str)
demo22["YEAR"] = demo22["YEAR"].astype(str)
demo22["ENTITY_CD"] = demo22["ENTITY_CD"].str[-4:]
demo22 = demo22[~demo22['ENTITY_NAME'].str.contains('County')]
demo22 = demo22.query("ENTITY_CD=='0000'")
demo22 = demo22.query("YEAR=='2022'")
demo22 = demo22[['ENTITY_NAME','YEAR','PER_BLACK', 'PER_HISP', 'PER_ASIAN']]
demo22 = demo22.rename(columns={'ENTITY_NAME': 'DISTRICT'})
demo22['PER_MINORITY'] = demo22['PER_BLACK'] + demo22['PER_HISP'] + demo22['PER_ASIAN']
demo22 = demo22.set_index('YEAR', drop=True)
demo22 = demo22.merge(FRPL22, how='outer', on=['YEAR', 'DISTRICT'])

#\\Mergins all of the demographic data into one panel
DEMOpanel = FRPL14.merge(FRPL15, how='outer', on=['YEAR', 'DISTRICT', 'PER_FREE_LUNCH', 'PER_REDUCED_LUNCH', 'PER_FRPL',
                                                  'PER_BLACK', 'PER_HISP', 'PER_ASIAN', 'PER_MINORITY'])
DEMOpanel = DEMOpanel.merge(FRPL16, how='outer', on=['YEAR', 'DISTRICT', 'PER_FREE_LUNCH', 'PER_REDUCED_LUNCH', 'PER_FRPL',
                                                     'PER_BLACK', 'PER_HISP', 'PER_ASIAN', 'PER_MINORITY'])
DEMOpanel = DEMOpanel.merge(FRPL17, how='outer', on=['YEAR', 'DISTRICT', 'PER_FREE_LUNCH', 'PER_REDUCED_LUNCH', 'PER_FRPL',
                                                     'PER_BLACK', 'PER_HISP', 'PER_ASIAN', 'PER_MINORITY'])
DEMOpanel = DEMOpanel.merge(demo18, how='outer', on=['YEAR', 'DISTRICT', 'PER_FREE_LUNCH', 'PER_REDUCED_LUNCH', 'PER_FRPL',
                                                     'PER_BLACK', 'PER_HISP', 'PER_ASIAN', 'PER_MINORITY'])
DEMOpanel = DEMOpanel.merge(demo19, how='outer', on=['YEAR', 'DISTRICT', 'PER_FREE_LUNCH', 'PER_REDUCED_LUNCH', 'PER_FRPL',
                                                     'PER_BLACK', 'PER_HISP', 'PER_ASIAN', 'PER_MINORITY'])
DEMOpanel = DEMOpanel.merge(demo20, how='outer', on=['YEAR', 'DISTRICT', 'PER_FREE_LUNCH', 'PER_REDUCED_LUNCH', 'PER_FRPL',
                                                     'PER_BLACK', 'PER_HISP', 'PER_ASIAN', 'PER_MINORITY'])
DEMOpanel = DEMOpanel.merge(demo21, how='outer', on=['YEAR', 'DISTRICT', 'PER_FREE_LUNCH', 'PER_REDUCED_LUNCH', 'PER_FRPL',
                                                     'PER_BLACK', 'PER_HISP', 'PER_ASIAN', 'PER_MINORITY'])
DEMOpanel = DEMOpanel.merge(demo22, how='outer', on=['YEAR', 'DISTRICT', 'PER_FREE_LUNCH', 'PER_REDUCED_LUNCH', 'PER_FRPL',
                                                     'PER_BLACK', 'PER_HISP', 'PER_ASIAN', 'PER_MINORITY'])

#\\Exporting to a CSV to merge with the Turnover Panel from the previous script.
Outputs = './Outputs/'
DEMOpanel.to_csv(Outputs + 'DEMOpanel.csv', index=True)
