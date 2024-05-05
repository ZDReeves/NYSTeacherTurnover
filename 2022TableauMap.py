# -*- coding: utf-8 -*-
"""
Created on Fri May  3 11:52:30 2024

@author: zacha
"""

#\\This script merges the 2022 district level dataset created in 2022_Clean_and_merge.py with spatial data in order to create an interactive
# map showing district level characteristics. The beginning of this script creates district-level data for all of New York City.
# The NYSED website publishes data for each individual geographic district in NYC (there are 31), whereas the census only has geometry for the
# entire NYC school district. Therefore, the beginning of this script pulls out data for NYC specifically and 
# calculates the turnover rate for each experience level for the city as a whole.
import pandas as pd
file_path = './Outputs/dist_characteristics.csv'
districts = pd.read_csv(file_path)
districts["YEAR"] = districts["YEAR"].astype(str)
districts['PER_TURN_ALL'] = districts['PER_TURN_ALL']*100
districts['PER_TURN_EXP'] = districts['PER_TURN_EXP']*100
districts['PER_TURN_INEXP'] = districts['PER_TURN_INEXP']*100

#\\NYC Demographics
file_path = './Inputs/Demographics.xlsx'
NYCdemo = pd.read_excel(file_path)
NYCdemo["YEAR"] = NYCdemo["YEAR"].astype(str)
NYCdemo["ENTITY_CD"] = NYCdemo["ENTITY_CD"].astype(str)
NYCdemo = NYCdemo[NYCdemo["ENTITY_NAME"].str.startswith('NYC Public Schools')]
NYCdemo = NYCdemo.query("YEAR=='2022'")
NYCdemo = NYCdemo.query("ENTITY_CD=='1'")
NYCdemo = NYCdemo[['ENTITY_NAME','YEAR','PER_ELL', 'PER_BLACK', 'PER_HISP', 'PER_ASIAN', 'PER_WHITE', 'PER_SWD']]
NYCdemo = NYCdemo.rename(columns={'ENTITY_NAME': 'DISTRICT'})

#NYC FRPL
file_path = './Inputs/FreeReducedPriceLunch.xlsx'
NYCfrpl = pd.read_excel(file_path)
NYCfrpl["YEAR"] = NYCfrpl["YEAR"].astype(str)
NYCfrpl["ENTITY_CD"] = NYCfrpl["ENTITY_CD"].astype(str)
NYCfrpl = NYCfrpl[NYCfrpl["ENTITY_NAME"].str.startswith('NYC Public Schools')]
NYCfrpl = NYCfrpl.query("YEAR=='2022'")
NYCfrpl = NYCfrpl.query("ENTITY_CD=='1'")
NYCfrpl['PER_FRPL'] = NYCfrpl['PER_FREE_LUNCH'] + NYCfrpl['PER_REDUCED_LUNCH']
NYCfrpl = NYCfrpl[['ENTITY_NAME','YEAR','PER_FRPL', 'PER_FREE_LUNCH', 'PER_REDUCED_LUNCH']]
NYCfrpl = NYCfrpl.rename(columns={'ENTITY_NAME': 'DISTRICT'})

#NYC Enrollment
file_path = './Inputs/Enrollment.xlsx'
NYCenroll = pd.read_excel(file_path)
NYCenroll["YEAR"] = NYCenroll["YEAR"].astype(str)
NYCenroll["ENTITY_CD"] = NYCenroll["ENTITY_CD"].astype(str)
NYCenroll = NYCenroll[NYCenroll["ENTITY_NAME"].str.startswith('NYC Public Schools')]
NYCenroll = NYCenroll.query("YEAR=='2022'")
NYCenroll = NYCenroll.query("ENTITY_CD=='1'")
NYCenroll = NYCenroll[['ENTITY_NAME','YEAR','K12']]
NYCenroll = NYCenroll.rename(columns={'ENTITY_NAME': 'DISTRICT'})

#NYC Funding
file_path = './Inputs/ExpPerPupil.xlsx'
NYCexpend = pd.read_excel(file_path)
NYCexpend["ENTITY_CD"] = NYCexpend["ENTITY_CD"].astype(str)
NYCexpend["YEAR"] = NYCexpend["YEAR"].astype(str)
NYCexpend["ENTITY_CD"] = NYCexpend["ENTITY_CD"].str[-4:]
NYCexpend = NYCexpend[~NYCexpend['ENTITY_NAME'].str.contains('County')]
NYCexpend = NYCexpend.query("ENTITY_CD=='0000'")
NYCexpend = NYCexpend.query("YEAR=='2022'")
NYCexpend = NYCexpend[NYCexpend['ENTITY_NAME'].str.startswith('NYC')]
NYCexpend = NYCexpend[['ENTITY_NAME','YEAR','PER_STATE_LOCAL_EXP','PER_FED_STATE_LOCAL_EXP']]
NYCexpend = NYCexpend.rename(columns={'ENTITY_NAME': 'DISTRICT'})
NYCexpend['DISTRICT'] = "NYC Public Schools"


#NYC Staff Calculations: I needed to add up staff counts for each geograhic districts before finding the turnover rates. This is because each geographic
# district has vastly different amounts of teachers, so taking an average of turnover rates for the 31 geographic districts would
# distort the counts for the city as a whole.
file_path = './Outputs/dist_characteristics.csv'
NYCstaff = pd.read_csv(file_path)
NYCstaff = NYCstaff[NYCstaff["DISTRICT"].str.startswith('NYC GEOG')]
NYCstaff = NYCstaff[['DISTRICT','YEAR','NUM_TEACH', 'NUM_TEACH_INEXP', 'NUM_TEACH_EXP', 'NUM_TOT_TURN',
                     'NUM_INEXP_TURN', 'NUM_EXP_TURN']]
NYCstaff = NYCstaff[['NUM_TEACH', 'NUM_TEACH_INEXP', 'NUM_TEACH_EXP','NUM_TOT_TURN', 'NUM_INEXP_TURN', 'NUM_EXP_TURN']].sum()
NYCstaff['PER_TURN_ALL'] = NYCstaff['NUM_TOT_TURN']/NYCstaff['NUM_TEACH']*100
NYCstaff['PER_TURN_EXP'] = NYCstaff['NUM_EXP_TURN']/NYCstaff['NUM_TEACH_EXP']*100
NYCstaff['PER_TURN_INEXP'] = NYCstaff['NUM_INEXP_TURN']/NYCstaff['NUM_TEACH_INEXP']*100
NYCstaff['PER_TEACH_EXP'] = NYCstaff['NUM_TEACH_EXP']/NYCstaff['NUM_TEACH']*100
NYCstaff['PER_TEACH_INEXP'] = NYCstaff['NUM_TEACH_INEXP']/NYCstaff['NUM_TEACH']*100
NYCstaff = NYCstaff.to_frame().T
NYCstaff['DISTRICT'] = "NYC Public Schools"
NYCstaff['YEAR'] = '2022'


#Merge for total NYC data
NYCmerged = NYCstaff.merge(NYCdemo, how='outer', on=['DISTRICT', 'YEAR'])
NYCmerged = NYCmerged.merge(NYCfrpl, how='outer', on=['DISTRICT', 'YEAR'])
NYCmerged = NYCmerged.merge(NYCenroll, how='outer', on=['DISTRICT', 'YEAR'])
NYCmerged = NYCmerged.merge(NYCexpend, how='outer', on=['DISTRICT', 'YEAR'])
NYCmerged['DISTRICT'] = "NEW YORK CITY DEPARTMENT OF EDUCATION"
NYCmerged = NYCmerged[['DISTRICT', 'YEAR', 'PER_TEACH_EXP', 'PER_TEACH_INEXP','PER_TURN_ALL',
                                                  'PER_TURN_INEXP', 'PER_TURN_EXP', 'PER_ELL', 'PER_FRPL',
                                                  'PER_BLACK', 'PER_HISP', 'PER_ASIAN', 'PER_WHITE', 'PER_SWD',
                                                  'K12', 'PER_FED_STATE_LOCAL_EXP']]

#Merge NYC Data with the rest of the State Data
NYS = NYCmerged.merge(districts, how='outer', on=['DISTRICT', 'YEAR', 'PER_TEACH_EXP', 'PER_TEACH_INEXP','PER_TURN_ALL',
                                                  'PER_TURN_INEXP', 'PER_TURN_EXP', 'PER_ELL', 'PER_FRPL',
                                                  'PER_BLACK', 'PER_HISP', 'PER_ASIAN', 'PER_WHITE', 'PER_SWD',
                                                   'K12', 'PER_FED_STATE_LOCAL_EXP'])

#\\ The NYSED data uses abbreviations such as UF, CSD, and SD whereas the census shapefile does not. So, I converted the names into
# terms that match across both datasets.
NYS['DISTRICT_SPLIT'] = NYS['DISTRICT'].str.split()
NYS['DISTRICT'] = NYS['DISTRICT'].str.replace('UF', 'UNION FREE ')
NYS['DISTRICT'] = NYS['DISTRICT'].str.replace('CSD', 'CENTRAL SCHOOL DISTRICT')
NYS['DISTRICT'] = NYS['DISTRICT'].str.replace('SD', 'SCHOOL DISTRICT')
NYS = NYS.drop(columns='DISTRICT_SPLIT')

#Merging with GEO DATA
import geopandas as gpd
file_path = './Inputs/tl_2020_36_unsd.zip'
geodata = gpd.read_file(file_path)
discolumn = geodata['NAME']
discolumn = discolumn.str.upper()
geodata['NAME']=discolumn
geodata = geodata.rename(columns={'NAME':'DISTRICT'})
geodata = geodata.merge(NYS,on='DISTRICT',how='outer',indicator=False)


#Creating GEOJSON File to be uploaded to Tableau
Outputs = './Outputs/'
tableaufile = geodata.to_file(Outputs + 'NYSdisrictinfo.geojson', driver='GeoJSON')
