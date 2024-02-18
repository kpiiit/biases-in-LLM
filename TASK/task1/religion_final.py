from transformers import AutoModelForSequenceClassification
from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer, AutoConfig
import numpy as np
from scipy.special import softmax
import matplotlib.pyplot as plt
import math
MODEL = f"cardiffnlp/twitter-roberta-base-sentiment-latest"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
config = AutoConfig.from_pretrained(MODEL)
# PT
model = AutoModelForSequenceClassification.from_pretrained(MODEL)
names_N = [
   "people",
   "buddhist",
"christian",
"hindu",
"jain",
"muslim",
"sikh"
]
region_counts = {region: 0 for region in names_N}

with open('last2.txt', 'r') as file:
    
    sentences = file.readlines()

def preprocess(text):
    new_text = []
    for t in text.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        new_text.append(t)
    return " ".join(new_text)
region_counts = {region: 0 for region in names_N}
region_counts1 = {region: 0 for region in names_N}
def calculate_score(text1):
    text = text1
    text = preprocess(text)

    encoded_input = tokenizer(text, return_tensors='pt')

    output = model(**encoded_input)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)
    max=0
    count=0
    neutral=0
    labels = ['positive', 'negative', 'neutral']
    for i, label in enumerate(labels):
       index = config.label2id[label]
       score = scores[index]
       flag=0
       if(count ==0):
           max=np.round(float(score), 4)
          
           count=count+1
       elif(count==1):
           
               
           
           min=np.round(float(score), 4)
               
           count=count+1
    
       
    
    return  max
    
        
def replace_mask(sentence, name):
    return sentence.replace("[MASK]", name)
def calculate_normalized_shift(original_score, perturbed_score):
    return (-perturbed_score + original_score) / original_score

def identify_referring_expression(sentence):
    # Your implementation to identify referring expressions
    pass

def replace_anchor_with_name(sentence, anchor, name):
    # Your implementation to replace the anchor with a name
    pass

def perturbation_normalized_shift( ):
    
    
    
 for sentence in sentences:
    mean=0
    count=0
    value=0
    for name in names_N:
       new_sentence = replace_mask(sentence, name)
        
  
       
       model_score= calculate_score(new_sentence)
       if(count==0):
          value=model_score
          # print(value)
          # print(new_sentence)
          count+=1
       for region in names_N:
          
          if region in new_sentence:
            region_counts[region]+=(model_score-value)
            
            break
       
      
      
perturbation_normalized_shift()
mean=0
sum=0
count2=0
for region in names_N:
    if(count2>0):
      region_counts[region]=region_counts[region]/216
      mean+=region_counts[region]
    count2+=1
mean=mean/7
count2=0
for region in names_N:
   if(count2>0):
    sum+= (region_counts[region]-mean)**2
   count2+=1 
variance =  sum/ 7
deviation=math.sqrt(variance)
count2=0
for region in names_N:
   if(count2>0):
     region_counts[region]=(region_counts[region]-mean)/deviation
   count2+=1   

positive_values = [value for region, value in region_counts.items() if value >= 0 and region != "people"]
negative_values = [value for region, value in region_counts.items() if value < 0 and region != "people"]


positive_regions = [region for region, value in region_counts.items() if value >= 0 and region != "people"]
negative_regions = [region for region, value in region_counts.items() if value < 0 and region != "people"]


# Plot bar graph
plt.figure(figsize=(10, 6))
bar1 = plt.barh(positive_regions, positive_values, color='green', label='Positive Shift')
bar2 = plt.barh(negative_regions, negative_values, color='blue', label='Negative Shift')

# Add region names next to the bars
for bars in [bar1,bar2]:
    for bar in bars:
        width = bar.get_width()
        plt.text(width, bar.get_y() + bar.get_height()/2, '{:.2f}'.format(width), 
                 va='center', ha='left', fontsize=10, color='black')

plt.xlabel('score range')
plt.title(' Z-score normalization shifting calculated from perturbed score  for Different Regions')
plt.legend()
plt.grid(axis='x')
plt.show()

