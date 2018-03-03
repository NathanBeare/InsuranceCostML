import pandas as pd


train = pd.read_csv("inpatientCharges.csv")

#print(train.describe())

categorical_variables = train.dtypes.loc[train.dtypes == 'object'].index
#print(categorical_variables)
# print(train[categorical_variables].apply(lambda x: len(x.unique())))

print(train['DRG Definition'].value_counts().to_frame().to_csv('./output.csv'))

# with open("forRyan.txt",'w') as fw:
#     fw.write(str((train['DRG Definition'].value_counts())))