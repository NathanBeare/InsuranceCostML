from DataCleaning import inputData
import matplotlib.pyplot as plt
import numpy as np


class Calculator(object):
    def __init__(self, data):
        self.diagnosisCategories = ['Pulmonary Treatments', 'Cardiovascular Treatments', 'Neurological Treatments',
                               'GI Treatments',
                               'Renal Treatments', 'Trauma Treatments', 'Orthopedic Treatment', 'Other']

        self.stateDict = {'AL': 0, 'AK': 1, 'AZ': 2, 'AR': 3, 'CA': 4, 'CO': 5, 'CT': 6, 'DE': 7,
                          'FL': 8, 'GA': 9, 'HI': 10, 'ID': 11, 'IL': 12, 'IN': 13, 'IA': 14,
                          'KS': 15, 'KY': 16, 'LA': 17, 'ME': 18, 'MD': 19, 'MA': 20, 'MI': 21,
                          'MN': 22, 'MS': 23, 'MO': 24, 'MT': 25, 'NE': 26, 'NV': 27, 'NH': 28,
                          'NJ': 29, 'NM': 30, 'NY': 31, 'NC': 32, 'ND': 33, 'OH': 34, 'OK': 35,
                          'OR': 36, 'PA': 37, 'RI': 38, 'SC': 39, 'SD': 40, 'TN': 41, 'TX': 42,
                          'UT': 43, 'VT': 44, 'VA': 45, 'WA': 46, 'WV': 47, 'WI': 48, 'WY': 49,
                          'DC': 50}
        self.diagnosis = raw_input("Pick a type of treatment:")
        self.total_data = data
        # print self.total_data

    def plot_averages(self):


        conditions = [] #a list of the 50 US states plus DC
        for key in (self.stateDict.keys()):
            conditions.append(key)

        # print len(conditions)
        plt.figure(1,figsize=(20,20))

        plt.title("Cost of "+ str(self.diagnosisCategories[int(self.diagnosis)]+ " in the US."))
        # print len(state)
        plt.bar(conditions, (self.statesCost), width=.4)
        plt.show()

        # print count
    def model (self):
        self.statesCost=[]
        nationalData = []
        self.total_data = np.array((self.total_data))
        for y in range(len(self.total_data)):
            diag = int(self.total_data[y][0])
            if diag == int(self.diagnosis):
               nationalData.append((self.total_data[y][4]).round(3))

        self.meanNationalData = np.mean(nationalData)
        # print("NATIONAL AVG COST: " +str(meanNationalData))

        for x in range (51):
            stateData = []
            for y in range(len(self.total_data)):
                diag= int(self.total_data[y][0])
                state = int(self.total_data[y][1])

                if diag == int(self.diagnosis) and state==int(x):

                    stateData.append(self.total_data[y][4])
            stateData = (np.array(stateData))
            self.statesCost.append(np.mean((stateData).round(3)))
            self.minStateCost = min(self.statesCost)
            self.maxStateCost = max(self.statesCost)
        # print ((statesCost))

        self.cheapestState = ''
        for x in range(len(self.statesCost)):
            if self.statesCost[x] == min(self.statesCost):
                for key in self.stateDict.keys():
                    if self.stateDict[key] == x:
                        self.cheapestState = key


        # print ("CHEAPEST STATE TO GET A ___ TREATMENT = " + (smallestState))
        # print (minCost)
        # print (len(statesCost))
        # plot_averages(diagnosis)
        return [self.meanNationalData, self.minStateCost, self.maxStateCost, self.cheapestState]


def main():
    data = inputData("inpatientCharges.csv")
    data.readFile()
    categoryDict = data.biggerCategories()
    df = data.outFinalDataFrame()
    df.to_csv("FinalDataSet.csv")
    calc = Calculator(df)
    results = calc.model()
    for a in range(3):
        results[a] = float(results[a])
        results[a] = np.round(results[a], decimals=2)
    print "National cost for getting " + str(calc.diagnosisCategories[int(calc.diagnosis)]) + "in the US: " + str(results[0])
    print "Cheapest cost for getting " + str(calc.diagnosisCategories[int(calc.diagnosis)]) + "in the US: " + str(results[1])
    print "This is in " + str(results[3])
    print "Total Disparity for this treatment: " + str(results[1]) + "-" + str(results[2])
    print "now plotting total average for that treatment in all 50 states"
    calc.plot_averages()

    # print data.model(7)


if __name__ == main():
    main()
