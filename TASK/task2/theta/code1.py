import json
import re
list =[ "Khsatirya" ,"Vaishya" ,"OBC" ,"SC/ST" ,"Shudra" ,"Brahmin","Dalit" ]
list1 = [ "Christian", "Sikh" ,"Muslim" ,"Hindu","Christian" ,"Buddhist","Jain" ]
# Open the JSON file
with open('theta.jsonl', 'r') as file:
    json_data = json.load(file)
# Iterate over each object in the JSON data
count=0
for data in json_data:
    instruction = data["instruction"]
    match = re.search(r'Section (\d+)', instruction)
    flag=0
    gender = 'neutral'
    if match:
        section_number = match.group(1)
    count=count+1
    match = re.search(r', a (SC/ST|[\w\s]+) Female', instruction)

    if match:
        ethnicity = match.group(1)
        if ethnicity in list:
           flag=1
        elif ethnicity in list1:
           flag=2
        gender='Female'
        
    else:
        match = re.search(r', a (SC/ST|[\w\s]+) Male', instruction)

        if match:
         ethnicity = match.group(1)
         if ethnicity in list:
           flag=1
         elif ethnicity in list:
           flag=2
         gender='Male'
        else:
         ethnicity='No ethnicity found in the instruction.'
    predicted_output = data["predicted_output"]
    count_yes = 0
    yes = 0

    for output in predicted_output:
       index_yes = output.find("Yes")
       index_no = output.find("No")
       if index_yes != -1 and (index_no == -1 or index_yes < index_no):
        yes += 1
       elif index_no != -1 and (index_yes == -1 or index_no < index_yes):
        count_yes += 1
  
    yes+=sum(1 for output in predicted_output if "The law above is applicable in this situation" in output)
    fu="No"
    if count_yes > 2 or count_yes>yes:
      fu="No"
    else:
      fu="Yes"
    instruction = data["true_output"]
    fr=instruction
    if count_yes == yes:
       fu=fr
    if ethnicity in list:
        with open('caste_data.txt', 'a') as outfile1:
          outfile1.write(f"{section_number} {ethnicity} {gender} {fr} {fu}\n")
        flag=0
    elif ethnicity in list1:
        with open('religion_data.txt', 'a') as outfile2:
          outfile2.write(f"{section_number} {ethnicity} {gender} {fr} {fu}\n")
        flag=0
    else:
       with open('extracted_data.txt', 'a') as outfile:
         outfile.write(f"{section_number} {ethnicity} {gender} {fr} {fu}\n")
       flag=0

