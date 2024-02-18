# Open the file
with open('extracted_data.txt', 'r') as file:
    # Read lines from the file up to line 2880
   lines = list(file)
with open('output_file.txt', 'a') as output_file:
    # Process each chunk of 32 lines
    for i in range(0, len(lines), 32):
        chunk = lines[i:i+32]
        count=0
        count1=0
        count3=0
        # Process each line in the chunk
        for line in chunk:
            # Split the line into words
            words = line.strip().split()

            # Take the last two words and create a tuple
            if(words[-2]=='No' and words[-1]=='Yes'):
                count = count+1
            elif(words[-2]=='Yes' and words[-1]=='Yes'):
                count1 = count1 +1
            elif(words[-2]=='Yes' and words[-1]=='No'):
                count3+=1
        # Check if the second-to-last word in the last line of the chunk is 'No' or 'Yes'
        if(count != 32 and count >0):
            for kp in chunk:
            # Split the line into words
              words = kp.strip().split()

            # Take the last two words and create a tuple
              if(words[-2]=='No' and words[-1]=='Yes'):
                output_file.write(kp)
             
        elif(count1 != 32 and count1 >0):
            for kp in chunk:
            # Split the line into words
              words = kp.strip().split()

            # Take the last two words and create a tuple
             
              if(words[-2]=='Yes' and words[-1]=='Yes'):
                output_file.write(kp)
              
        if(count3 != 32 and count3 >0):
            for kp in chunk:
            # Split the line into words
              words = kp.strip().split()

            # Take the last two words and create a tuple
             
              
              if(words[-2]=='Yes' and words[-1]=='No'):
                output_file.write(kp)
