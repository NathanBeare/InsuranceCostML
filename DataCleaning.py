import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


'''
input data class has methods to clean irregularly formatted data from starting data set inpatientCharges.csv
'''

class inputData(object):
    def __init__(self, fileName):
        self.fileName = fileName
        self.stateDict = {'AL': 0, 'AK': 1, 'AZ': 2, 'AR': 3, 'CA': 4, 'CO': 5, 'CT': 6, 'DE': 7,
                     'FL': 8, 'GA': 9, 'HI': 10, 'ID': 11, 'IL': 12, 'IN': 13, 'IA': 14,
                     'KS': 15, 'KY': 16, 'LA': 17, 'ME': 18, 'MD': 19, 'MA': 20, 'MI': 21,
                     'MN': 22, 'MS': 23, 'MO': 24, 'MT': 25, 'NE': 26, 'NV': 27, 'NH': 28,
                     'NJ': 29, 'NM': 30, 'NY': 31, 'NC': 32, 'ND': 33, 'OH': 34, 'OK': 35,
                     'OR': 36, 'PA': 37, 'RI': 38, 'SC': 39, 'SD': 40, 'TN': 41, 'TX': 42,
                     'UT': 43, 'VT': 44, 'VA': 45, 'WA': 46, 'WV': 47, 'WI': 48, 'WY': 49,
                     'DC': 50}


    def readFile(self):
        '''
        parses starting data set, generating dataframe and outputing dataset to a csv file of consistent formatting
        '''

        with open(self.fileName, "r") as fh:  # create fileHandle for file of name fileName
            total_data = []
            header = fh.readline()  # the first line of myodata-2.txt file contains only header information. we dont need this.
            for line in fh:
                new_line_info = []
                '''Two different formats in file, from different sources
                '''
                try:
                    line_info = line.replace('\n', '').split('"')  # some gene descritions contain commas within them, so split by " instead
                    discrete_info = line_info[0].split(',')
                    diag = discrete_info[0][6:]
                    state = discrete_info[1]
                    discharges = discrete_info[2]
                    covCharge = line_info[1].replace("$","").replace(",","")
                    totCharge = line_info[3].replace("$","").replace(",","")
                    medCharge = line_info[5].replace("$","").replace(",","")

                except:
                    line_info = line.replace('\n', '').split('"')  # some gene descritions contain commas within them, so split by " instead
                    diag = line_info[1][6:].replace(",",'')
                    state = line_info[2].split(",")[1]
                    discharges = line_info[2].split(",")[2]
                    covCharge = line_info[3].replace("$", "").replace(",", "")
                    totCharge = line_info[5].replace("$", "").replace(",", "")
                    medCharge = line_info[7].replace("$", "").replace(",", "")

                new_line_info.append(diag)
                new_line_info.append(state)
                new_line_info.append(discharges)
                new_line_info.append(covCharge)
                new_line_info.append(totCharge)
                new_line_info.append(medCharge)

                total_data.append(new_line_info)


        total_data=pd.DataFrame(total_data)
        total_data.to_csv('./cleanerData.csv')
        # print "outputed pto cleanerData.csv"


    def biggerCategories(self):
        '''
        Categorize individual medical procedures into broader treatment categories
        returns a dictionary with category index as key, list of procedures under that category as value
        Must be run after readFile

        clean up later
        '''
        categories = ('pulm', 'cards', 'neur', 'gi', 'renal', 'trauma', 'ortho', 'other')
        categoryList = []
        for x in range(len(categories)):
            categoryList.append([])
        pulm = []
        cards = []
        neur = []
        gi = []
        renal = []
        trauma = []
        ortho = []
        other = []
        with open("cleanerData.csv") as fh:
            for line in fh:
                if ("RESPIRA") in line or ("PULMON") in line or  ("BRONCH") in line or ("PNEUMO") in line:
                    pulmdiag = line.split(',')[1]
                    if pulmdiag not in pulm:
                        pulm.append(pulmdiag)

                if ("CARDI") in line or ("ATHERO") in line or ("CHEST PAIN") in line or ("HEART") in line or ("CIRCULA") in line or ("HYPERT") in line or ("VASC") in line or ("ISCHEMI") in line or ("EXTRACRANI") in line:
                    carddiag = line.split(',')[1]
                    if carddiag not in cards:
                        cards.append(carddiag)

                if ("NEUR") in line or ("CRANI") in line or ("PSYCH") in line or ("EQUILIB") in line or ("NERV") in line or ("SEIZURE") in line:
                    neurdiag = line.split(',')[1]
                    if neurdiag not in neur:
                        neur.append(neurdiag)

                if ("RENAL") in line or ("KIDNEY") in line:
                    rendiag = line.split(',')[1]
                    if rendiag not in renal:
                        renal.append(rendiag)
                        # print neurdiag
                if ("DIGEST") in line or ("G.I.") in line or ("GASTRO") in line or ("PANCREA") in line or ("LAPARO") in line or ("BOWEL") in line:
                    gidiag = line.split(',')[1]
                    if gidiag not in gi:
                        gi.append(gidiag)

                if ("FX") in line or ("FRACT") in line or ("DISPLACEM") in line or ("COLLAPS") in line:
                    traumadiag = line.split(',')[1]
                    if traumadiag not in trauma:
                        trauma.append(traumadiag)
                if ("ORTH") in line or ("REPLACEMENT") in line or ("FUSION") in line or ("JOINT") in line or ("BACK PROBLEMS") in line:
                    orthoDiag = line.split(',')[1]
                    if orthoDiag not in ortho:
                        ortho.append(orthoDiag)
                if ("NUTRIT") in line or ("POISON") in line or ("SEPTI") in line or ("SYMPT") in line or ("DIABE") in line or ("BLOOD") in line or ("CELLU") in line or ("PARASITIC") in line or ("ALCOHOL") in line:
                    diag = line.split(',')[1]
                    if diag not in other:
                        other.append(diag)
        # print pulm
        self.categoryDict = { 0:pulm, 1:cards, 2:neur, 3:gi, 4:renal, 5:trauma, 6:ortho, 7:other}


        return self.categoryDict
            # print len(other)
            # for info in other:
            #     print info

    def outFinalDataFrame(self):
        with open("cleanerData.csv") as fr:
            self.total_data = []
            header = fr.readline()
            for line in fr:
                line_info = []
                line = line.split(',')
                diag = line[1]
                for key in self.categoryDict.iterkeys():
                    if diag in self.categoryDict[key]:
                        currentCategory = key


                        line_info.append(int(currentCategory))

                state = self.stateDict[line[2]]

                # state = self.stateDict[line[2]]

                line_info.append(int(state))
                discharges = line[3]
                covCost= line[4]
                totCost=line[5]
                medCost = line[6]
                line_info.append(float(discharges))
                line_info.append(float(covCost))
                line_info.append(float(totCost))
                line_info.append(float(medCost))


                self.total_data.append(line_info)

            self.total_data=pd.DataFrame(self.total_data)
            return self.total_data


def main():
    data = inputData("inpatientCharges.csv")
    data.readFile()
    categoryDict = data.biggerCategories()
    df = data.outFinalDataFrame()
    df.to_csv("FinalDataSet.csv")
    # print data.model(7)


if __name__ == main():
    main()
