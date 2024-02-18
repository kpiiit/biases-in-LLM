# Open the file
with open('religion_data.txt', 'r') as file:
    
   lines = lines = list(file)
with open('output_file_religion.txt', 'a') as output_file:
    
    for i in range(0, len(lines), 7):
        chunk = lines[i:i+7]
        count=0
        count1=0
        # Process each line in the chunk
        for line in chunk:
            # Split the line into words
            words = line.strip().split()

            # Take the last two words and create a tuple
            if(words[-2]=='No' and words[-1]=='Yes'):
                output_file.write(line)
             
            elif(words[-2]=='Yes' and words[-1]=='Yes'):
                output_file.write(line)
            elif(words[-2]=='Yes' and words[-1]=='No'):
                output_file.write(line)
             

        
