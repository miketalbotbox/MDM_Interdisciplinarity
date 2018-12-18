
# coding: utf-8

# # Subject Search Function
# 
# Author(s): Mike Talbot  
# Date Created: 18/12/18  
# Date Lat Modified: 18/12/18  
# 
# 
# 
# Utility:  
# Boiling down the network stuff from Authors_Connectivity_Matrix
# 

# In[2]:


import networkx as nx

def CreateGraph(AuthorIDs, AuthorSubject, Plot_Graph = False):
    
    Total_Subjects = []
    for person in AuthorSubject:
        for subject in person:
            if subject not in Total_Subjects:
                Total_Subjects.append(subject)
    print(Total_Subjects)           
    Max_Authors = len(AuthorIDs)
    Size_Subject = len(Total_Subjects) 
    Colour_Map = []*(Size_Subject + Max_Authors)
    Colour_Map[0:Size_Subject] = ['b']*Size_Subject
    Colour_Map[Size_Subject:] = ['r']*Max_Authors
    Subject_Graph = nx.Graph()
    Subject_Graph.add_nodes_from(Total_Subjects)
    Subject_Graph.add_nodes_from(AuthorIDs[0:Max_Authors].tolist())

    Connection_List = []
    for index in range(Max_Authors):
        person = AuthorIDs[index].tolist()
        #print(Total_Subjects[index])
        subjects = AuthorSubject[index]
        for subject in subjects:
            Connection_List.append((person,subject))

    Subject_Graph.add_edges_from(Connection_List)
    if Plot_Graph == True:
        nx.draw(Subject_Graph, node_color = Colour_Map)
        
    return Subject_Graph
        
def FindPerson(SubjectGraph, Subject_or_Person):
    output = SubjectGraph[Subject_or_Person]
    return output

