# Understanding the Revolving Door
## A Quantitative Analysis of Teacher Turnover in New York State
 
### <u> Motivation </u>
High rates of teacher turnover afflict school districts across the country. More than just an inconvenience, research demonstrates that high turnover is associated with decreased academic achievement and instructional quality, and it disproportionately impacts low-income communities and communities of color (Ronfeldt, Loeb & Wyckoff, 2013; Sorenson & Ladd, 2020; Simon & Johnson, 2015). 

As a former teacher, it seems that policy conversations about teacher turnover often ignore the disparate causes of among inexperienced and experienced teachers. Sure, insufficient salaries and difficult working conditions negatively impact everyone, but I believe there are other factors worth interrogating, too. This repository analyzes turnover among experienced teachers and inexperienced teachers across New York State with the hope of motivating further inquiry. 

### <u> Input Data </u>
All of the data used in this analysis can be found in the Inputs file in the repository. I used public data from the New York State Education Department at the district level from 2014-2022. Specifically, I gathered teacher experience and turnover data from the Staff files within their Student and Educator Database and their Report Card Database. Data regarding student demographics comes from the Student and Educator Database as well as the Enrollment Database. A link to the NYSED Data downloads site is located here: https://data.nysed.gov/downloads.php

Additionally, the last script in this repository (2022TableauMap.py) creates a GeoPackage file that can be used to create an interactive map in Tableau. Here, I merge the previously described NYSED data for 2022 with a shapefile for all unified school districts in New York State from the Census: https://www.census.gov/cgi-bin/geo/shapefiles/index.php?year=2022&layergroup=School+Districts.


### <u> Python Scripts </u>
There are six total scripts in this repository, which each producing an an output that is used in a subsequent script. They are labeled below in the order they should be run.

1) [2022_Clean_and_Merge.py] merges individual datasets from the aforementioned databases from the NYSED. It creates two output files: dist_turnover.csv and dist_characteristics.csv; dist_turnover focuses on turnover data for each district whereas dist_characteristics contains district-level demographic information in addition to teacher turnover data. It is also important to acknowledge that NYS only publishes data on tunover for all teachers and for teachers with less than five years of experience (what I call "inexperienced teachers" for simplicity). Accordingly, I needed to calculate the turnover rate among experienced teachers using the data on total turnover and inexperienced turnover.
   
2) [FiguresFor2022.py] creates a bar chart depicting the average turnover rate for all teachers, experienced teachers, and inexperienced teachers at the district level in 2022. It also creates a series of hexplots depicting the correlation between turnover rates and the percentage of students on a Free or Reduced Price Lunch Plan (FRPL) within a district.
   
3) [TurnoverPanel14-22.py] creates a panel dataset for all school districts in NYS from 2014-2022. It does this by merging excel files containing teacher turnover rates and experience at the district level. As a note, from 2014-2017 NYSED had turnover rates experience levels in the same dataset. Starting in 2018, they separated it into two different datasets, which requires additional merges along the way. The script creates the TurnoverPanel.csv file, as well as a bar chart showing average turnover dor each experience level over this time as well as a linechart showing the changes over the course of the panel, too.
   
4) [FRPLpanel4-22] follows suit and creates a panel dataset containing student demographic information, including the percentage of students on a FRPL plan, at the district level. This script creates one output file called DEMOpanel.csv.
   
5) [FixedEffectsRegressions.py] This script does exacly what the name implies: it runs six different fixed effects regressions analyzing the association between the aforementioned turnover rates with the percentage of students on a FRPL and covariates. The results of each regression are contained within the kernel. I include the results from my preferred specifications in the Results section of this README file, too.
   
6) [2022TableauMap.py] This script creates a GeoPackage file that can be used to create an interactive map in Tableau. The map shows numerous district level characteristics, including turnover rates, student demographics, total enrollment, and per-pupil funding. Here, I have an example of the information the map displays for districts across the state.

![TableauMap](https://github.com/ZDReeves/NYSTeacherTurnover/assets/156924085/35ac0870-f15e-473b-8426-1e789b9bdff4)
   
### <u>Results</u>
**Finding #1: The turnover rate among inexperienced teachers is (unsurprisingly) far higher that the rate for experienced teachers.**
![2022TurnoverByExp](https://github.com/ZDReeves/NYSTeacherTurnover/assets/156924085/b192b231-be49-4ed6-80ec-88fcf4465d0c)

**Finding #2: The turnover rate among experienced teachers is positively correlated with FRPL status.**
![Big_Exp_FRPL](https://github.com/ZDReeves/NYSTeacherTurnover/assets/156924085/53d5cbd2-5aae-48a6-bbc8-65a1e9878db6)

**Finding #3: The turnover rate among inexperienced teachers is negatively correlated with FRPL status.**
![Big_Inexp_FRPL](https://github.com/ZDReeves/NYSTeacherTurnover/assets/156924085/f88d1e42-aad3-4f7d-8392-a314d48352cd)

There are a couple important caveats for Finding #2 and Finding #3. The ratio of inexperienced teacher to experienced teachers generally increases as the percentage of students on a FRPL plan increases. Accordingly, these correlations might be driven by the fact that 2/10 inexperienced teachers turning over in a low-income school returns a 20% turnover rate, whereas 2/5 in a high-income school returns a 40% turnover rate. The inverse of this logic applies to experienced teachers too.

**Finding #4: There is a statistically significant positive association between turnover for experienced teachers and FRPL status. There is also a statistically signfiicant negative association between turnover for inexperienced teachers and FRPL status.**

I ran fixed effects regressions to control for time-invariant district-level characteristics. I also included year-effects to control for entity-invariant time effects (such as Covid) that occurred between 2014-2022. Moreover, I ran regressions with and without a district-level measure of racial diversity among students. I included the results of my two preferred specifications below. The others are visible in the kernal after running the regressions.

![InexpFEregression](https://github.com/ZDReeves/NYSTeacherTurnover/assets/156924085/5a3ada6b-d5d6-47cf-b9c9-8d79fa63d807)

![ExpFEregression](https://github.com/ZDReeves/NYSTeacherTurnover/assets/156924085/89e7018d-d3e2-4d95-829b-550cc9b8923a)


### <u>Conclusion</u>
Of course, we cannot make causal conslusion from this analysis; there are numerous other variables that shoule bd included in these models. Nonetheless, my analysis shows that there is a statistically significant negative association between turnover for inexperienced teachers and FRPL percentage, and there is an equally as significant positive relationship between turnover for experienced teachers and FRPL percentage. Further research should investigate whether this is strictly a product of different quantities of experienced and inexperienced teachers.
