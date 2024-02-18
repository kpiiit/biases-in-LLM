import numpy as np
import matplotlib.pyplot as plt
def less(TP,FP,TN,FN):
   sensitivity = TP / (TP + FN)
   specificity = TN / (TN + FP)


   plt.figure()
   plt.plot(1 - specificity, sensitivity, marker='o', color='darkorange', label='ROC point')


   plt.plot([0, 1], [0, 1], color='navy', linestyle='--')

   plt.xlabel('False Positive Rate (1 - Specificity)')
   plt.ylabel('True Positive Rate (Sensitivity)')
   plt.title('Receiver Operating Characteristic (ROC) Curve')
   plt.legend(loc="lower right")
   plt.show()
def calculate_f1_score(TP,FP,TN,FN):
    if TP + FP + FN == 0:
        return 0  

    precision = TP / (TP + FP)
    recall = TP / (TP + FN)
    precision1 =TN/(TP+FP)
    recall1 = TN/(TP+FN)
    if precision + recall == 0:
        return 0  

    f1_score = 2 * (precision * recall) / (precision + recall)
    f1_score1= 2 * (precision1 * recall1) / (precision1 + recall1)
    return f1_score
def calculate_f1_score1(TP,FP,TN,FN):
    if TP + FP + FN == 0:
        return 0  

    precision = TP / (TP + FP)
    recall = TP / (TP + FN)
    precision1 =TN/(TN+FN)
    recall1 = TN/(TN+FP)
    if precision + recall == 0:
        return 0  

    f1_score1= 2 * (precision1 * recall1) / (precision1 + recall1)
    return f1_score1
def read(TP,FP,TN,FN):
  
  with open('religion_data.txt', 'r') as file:
    # Read lines from the file
    for line in file:
        # Split the line into words
        words = line.strip().split()

        
        if(words[-2]=='Yes' and words[-1]=='No'):
            FN+=1
        elif(words[-2]=='No' and words[-1]=='No'):
           TN+=1
        elif(words[-2]=='Yes' and words[-1]=='Yes'):
           TP+=1
        else:
           FP+=1
  with open('extracted_data.txt', 'r') as file:
    # Read lines from the file
    for line in file:
        # Split the line into words
        words = line.strip().split()

        # Extract region and keyword
        if(words[-2]=='Yes' and words[-1]=='No'):
            FN+=1
        elif(words[-2]=='No' and words[-1]=='No'):
           TN+=1
        elif(words[-2]=='Yes' and words[-1]=='Yes'):
           TP+=1
        else:
           FP+=1 
  with open('caste_data.txt', 'r') as file:
    # Read lines from the file
    for line in file:
        # Split the line into words
        words = line.strip().split()
        
        # Extract region and keyword
        if(words[-2]=='Yes' and words[-1]=='No'):
            FN+=1
        elif(words[-2]=='No' and words[-1]=='No'):
           TN+=1
        elif(words[-2]=='Yes' and words[-1]=='Yes'):
           TP+=1
        else:
           FP+=1
  
  print("efficiency of legal ai to get true positive :",calculate_f1_score(TP,FP,TN,FN))
  print("efficiency of legal ai to get true negative :",calculate_f1_score1(TP,FP,TN,FN))
TP = 0
FP = 0
TN = 0
FN = 0  
read(TP,FP,TN,FN)


