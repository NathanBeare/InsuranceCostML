import pandas as pd
import numpy as np



def readFile(fileName):

    with open(fileName, "r") as fh:  # create fileHandle for file of name fileName
        total_data = []
        rowCount = 0
        header = fh.readline()  # the first line of myodata-2.txt file contains only header information. we dont need this.

        for line in fh:
            new_line_info = []

            try:

                line_info = line.replace('\n', '').split('"')  # some gene descritions contain commas within them, so split by " instead
                discrete_info = line_info[0].split(',')
                diag = discrete_info[0][6:]
                state = discrete_info[1]
                discharges = discrete_info[2]
                covCharge = line_info[1].replace("$","").replace(",","")
                totCharge = line_info[3].replace("$","").replace(",","")
                medCharge = line_info[5].replace("$","").replace(",","")
                rowCount += 1

                # print rowCount
                # print state
            except:
                # print line
                line_info = line.replace('\n', '').split('"')  # some gene descritions contain commas within them, so split by " instead
                diag = line_info[1][6:].replace(",",'')
                state = line_info[2].split(",")[1]
                discharges = line_info[2].split(",")[2]
                covCharge = line_info[3].replace("$", "").replace(",", "")
                totCharge = line_info[5].replace("$", "").replace(",", "")
                medCharge = line_info[7].replace("$", "").replace(",", "")
                rowCount += 1

            new_line_info.append(diag)
            new_line_info.append(state)
            new_line_info.append(discharges)
            new_line_info.append(covCharge)
            new_line_info.append(totCharge)
            new_line_info.append(medCharge)
            total_data.append(new_line_info)

    #
    total_data=pd.DataFrame(total_data)
    total_data.to_csv('./CLEANDATA.csv')


def biggerCategories(fileName):
    pulm = []
    cards = []
    neur = []
    gi = []
    renal = []
    trauma = []
    ortho = []
    other = []
    with open(fileName) as fh:
        for line in fh:

            if ("RESPIRA") in line or ("PULMON") in line or  ("BRONCH") in line or ("PNEUMO") in line:
                pulmdiag = line.split(',')[1]
                if pulmdiag not in pulm:
                    pulm.append(pulmdiag)

            if ("CARDI") in line or ("ATHERO") in line or ("CHEST PAIN") in line or ("HEART") in line or ("CIRCULA") in line or ("HYPERT") in line or ("VASC") in line or ("ISCHEMI") in line or ("EXTRACRANI"):
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

            if ("FX") in line or ("FRACT") in line or ("DISPLACEM") in line:
                traumadiag = line.split(',')[1]
                if traumadiag not in trauma:
                    trauma.append(traumadiag)
            if ("ORTH") in line or ("REPLACEMENT") in line or ("FUSION") in line or ("JOINT") in line or ("BACK PROBLEMS") in line:
                orthoDiag = line.split(',')[1]
                if orthoDiag not in ortho:
                    ortho.append(orthoDiag)
            if ("NUTRIT") in line or ("POISON") in line or ("SEPTI") in line or ("SYMPT") in line or ("SYNCO") in line or ("DIABE") in line or ("BLOOD") in line or ("CELLU") in line or ("PARASITIC") in line or ("ALCOHOL" in line):
                diag = line.split(',')[1]
                if diag not in other:
                    other.append(diag)
    return [pulm, cards, neur, gi, renal, trauma, ortho, other]
        # print len(other)
        # for info in other:
        #     print info

def outFinalDataFrame(bigCategories, cleanData):
    stateDict = {'AL': 0, 'AK': 1, 'AZ': 2, 'AR': 3, 'CA': 4, 'CO': 5, 'CT': 6, 'DE': 7,
     'FL': 8, 'GA': 9, 'HI': 10, 'ID': 11, 'IL': 12, 'IN': 13, 'IA': 14,
     'KS': 15, 'KY': 16, 'LA': 17, 'ME': 18, 'MD': 19, 'MA': 20, 'MI': 21,
     'MN': 22, 'MS': 23, 'MO': 24, 'MT': 25, 'NE': 26, 'NV': 27, 'NH': 28,
     'NJ': 29, 'NM': 30, 'NY': 31, 'NC': 32, 'ND': 33, 'OH': 34, 'OK': 35,
     'OR': 36, 'PA': 37, 'RI': 38, 'SC': 39, 'SD': 40, 'TN': 41, 'TX': 42,
     'UT': 43, 'VT': 44, 'VA': 45, 'WA': 46, 'WV': 47, 'WI': 48, 'WY': 49,
     'DC': 50}

    with open("CLEANDATA.csv") as fr:
        total_data = []

        header = fr.readline()
        for line in fr:
            line_info = []
            line = line.split(',')
            diag = line[1]
            currentCategory = ''
            for x in range(len(bigCategories)):
                if diag in bigCategories[x]:
                    currentCategory = str(x)
                    # print currentCategory
            line_info.append(int(currentCategory))
                        # count +=1
            state = stateDict[line[2]]
            line_info.append(int(state))
            discharges = line[3]
            covCost= line[4]
            totCost=line[5]
            medCost = line[6]
            line_info.append(float(discharges))
            line_info.append(float(covCost))
            line_info.append(float(totCost))
            line_info.append(float(medCost))
            total_data.append(line_info)

        total_data=pd.DataFrame(total_data)
        return total_data


    # print count


# readFile("inpatientCharges.csv")
bigCategories = biggerCategories("CLEANDATA.csv")
df = outFinalDataFrame(bigCategories, "CLEANDATA.csv")
df.to_csv("FinalDataSet.csv")