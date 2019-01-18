from scipy import stats

#comments are for the weak
#real coders go no comments
#wait these are comments
#guess im not a real coder

dHFusionNoCal = (6.15, 4.2, 3.33, 4.22, 4.27)
dHFusionYesCal = (7.44, 4.5, 5, 4.45, 5.34)

NaOHinH2ONoCal = (-43.03, -36, -20.66, -21, -25.72)
NaOHinH2OYesCal = (-51.42, -38, -20.84, -22.2, -32.15)

print("delta H fusion - ignore vs include heat capacity of calorimeter")
print(stats.ttest_rel(dHFusionNoCal,dHFusionYesCal))

print("dissolve NaOH in H2O - ignore vs include heat capacity of calorimeter")
print(stats.ttest_rel(NaOHinH2ONoCal,NaOHinH2OYesCal))

# with p value and stats 
# to use, uncomment this 

# dHFusionNoCal = (6.15, 4.2, 3.33, 4.22, 4.27)
# dHFusionYesCal = (7.44, 4.5, 5, 4.45, 5.34)

# NaOHinH2ONoCal = (-43.03, -36, -20.66, -21, -25.72)
# NaOHinH2OYesCal = (-51.42, -38, -20.84, -22.2, -32.15)

# print("delta H fusion - ignore vs include heat capacity of calorimeter")
# print(stats.ttest_rel(dHFusionNoCal,dHFusionYesCal))
# statistic, pvalue=stats.ttest_rel(dHFusionNoCal,dHFusionYesCal)
# print("value of t-statistic = ", statistic,4)
# print("pvalue = ", pvalue,4)

# print("dissolve NaOH in H2O - ignore vs include heat capacity of calorimeter")
# print(stats.ttest_rel(NaOHinH2ONoCal,NaOHinH2OYesCal))
# statistic, pvalue=stats.ttest_rel(NaOHinH2ONoCal,NaOHinH2OYesCal)
# print("value of t-statistic = ", statistic,4)
# print("pvalue = ", pvalue,4)
