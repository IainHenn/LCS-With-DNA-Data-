import random 
import pandas as pd 
import seaborn as sns


def generateDNA():
    DNA = []
    for i in range(100):
        num = random.randint(1,4)
        match num:
            case 1:
                DNA.append("A")
            case 2:
                DNA.append("C")
            case 3:
                DNA.append("T")
            case 4:
                DNA.append("G")
    return DNA


def EditDistance(w1, w2):
    l1 = len(w1)
    l2 = len(w2)
    matrix = [[0] * (l1+1) for i in range(l2+1)]
    
    '''
    w1 is associated with the j index (inner)
    w2 is associated with the i index (outer)
    '''

    for i in range(l2+1):
        for j in range(l1+1):

            #base case
            if(i == 0):
                matrix[i][j] = j
            elif(j == 0):
                matrix[i][j] = i
            
            #if the last letter in both words is the same
            elif(w1[j-1] == w2[i-1]):
                matrix[i][j] = matrix[i-1][j-1]
            
            #if the word needs to be replaced, inserted, or removed 
            else:
                replace = matrix[i-1][j-1]
                insert = matrix[i][j-1]
                remove = matrix[i-1][j]
                matrix[i][j] = 1 + min(remove,insert,replace)

    return matrix[l2][l1]

DNA1_set = []
DNA2_set = []
Edit_Distance_btw_sets = []

for i in range(20):
    temp1 = generateDNA()
    temp2 = generateDNA()
    DNA1_set.append(temp1)
    DNA2_set.append(temp2)
    Edit_Distance_btw_sets.append(EditDistance(temp1,temp2))



ED_df = pd.DataFrame({'Edit_Distance' : Edit_Distance_btw_sets})

sns.histplot(data = ED_df, x = "Edit_Distance")