
# coding: utf-8

# # Subject Weightings 
# A comparison of similarities between subjects

# In[ ]:


import numpy as np

def CreateWeights(Authors_Subjects_List, Total_Subjects):    
    Subject_Weights = []
    for subject in Total_Subjects:
        weight = np.sqrt(sum(x.count(subject) for x in Authors_Subjects_List))
        Subject_Weights.append(weight)
    Subject_Weights_Array = np.array(Subject_Weights)
    #print(Subject_Weights_Array)
    #print(len(Subject_Weights_Array))
    Total_Subjects.remove('nan')
    Total_Subjects_Array = np.array(Total_Subjects)
    Weighting = np.zeros((len(Total_Subjects),len(Total_Subjects))) #An NxN Matrix
    for author in Authors_Subjects_List:
        for Original_Subject in Total_Subjects:
            for Compared_Subject in Total_Subjects:
                #if Compared_Subject != Original_Subject:
                if (Compared_Subject in author                 and Original_Subject in author):
                    O = np.where(Total_Subjects_Array == Original_Subject)
                    C = np.where(Total_Subjects_Array == Compared_Subject)
                    #print(Subject_Weights_Array[O])
                    Weighting[O,C] += 1/ (Subject_Weights_Array[O]*Subject_Weights_Array[C])
    return Weighting

