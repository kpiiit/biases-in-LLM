import matplotlib.pyplot as plt

# Define region names
regions = ["Christian", "Sikh", "Muslim", "Hindu", "Christian", "Buddhist", "Jain"]

region_counts = {region: 0 for region in regions}
keyword_counts = {region: {keyword: 0 for keyword in ["146", "276", "302", "304", "354", "363", "370", "375", "378", "383", "390", "403", "463", "507"]} for region in regions}
region_counts1 = {region: 0 for region in regions}
keyword_counts1 = {region: {keyword: 0 for keyword in ["146", "276", "302", "304", "354", "363", "370", "375", "378", "383", "390", "403", "463", "507"]} for region in regions}
# Open the file
with open('output_file_religion.txt', 'r') as file:
    # Read lines from the file
    for line in file:
        # Split the line into words
        words = line.strip().split()

        # Extract region and keyword
        regionw = words[:-3]
        region = regionw[1]
        region2 = regionw[0]
        if(words[-2]=='Yes' and words[-1]=='No'):
            if region in region_counts:
              region_counts1[region] += 1

        # Increment count for the keyword within the region
            if region2 in keyword_counts[region]:
              keyword_counts1[region][region2] += 1
        else:
        # Increment count for the region
           if region in region_counts:
             region_counts[region] += 1

        # Increment count for the keyword within the region
           if region2 in keyword_counts[region]:
              keyword_counts[region][region2] += 1

# Plotting the graph
plt.figure(figsize=(12, 8))

# Plot the bar graph
plt.subplot(3, 3, 1)
plt.barh(list(region_counts.keys()), list(region_counts.values()), color='skyblue')
plt.xlabel('Count')
plt.ylabel('Region')
plt.title('Count of each religion')
plt.gca().invert_yaxis()  # Invert y-axis to have 'Himachali' at the top

# Plot the table for region counts
plt.subplot(3, 3, 2)
cell_text = [[region, str(count)] for region, count in region_counts.items()]
plt.table(cellText=cell_text, colLabels=['religion', 'Wrong Judgements by AI'], loc='center')

# Plot keyword counts for each region
counter = 0
for region in regions:
    counter += 1
    plt.subplot(3, 3, counter + 2)
    cell_text = [[f"{keyword}", str(count)] for keyword, count in keyword_counts[region].items()]
    plt.table(cellText=cell_text, colLabels=['Religion', region], loc='center')
    

# Adjust layout
plt.tight_layout()

# Add main title
plt.suptitle('Analysis of Religion Data')

# Show the plot
plt.show()
plt.close()
plt.figure(figsize=(12, 8))

# Plot the bar graph
plt.subplot(3, 3, 1)
plt.barh(list(region_counts1.keys()), list(region_counts1.values()), color='skyblue')
plt.xlabel('Count')
plt.ylabel('Region')
plt.title('Count of each religion')
plt.gca().invert_yaxis()  # Invert y-axis to have 'Himachali' at the top

# Plot the table for region counts
plt.subplot(3, 3, 2)
cell_text = [[region, str(count)] for region, count in region_counts1.items()]
plt.table(cellText=cell_text, colLabels=['Religion', 'positive bias Judgements by AI'], loc='center')

# Plot keyword counts for each region
counter = 0
for region in regions:
    counter += 1
    plt.subplot(3, 3, counter + 2)
    cell_text = [[f"{keyword}", str(count)] for keyword, count in keyword_counts1[region].items()]
    plt.table(cellText=cell_text, colLabels=['Section', region], loc='center')
    

# Adjust layout
plt.tight_layout()

# Add main title
plt.suptitle('Analysis of  Religion Data')

# Show the plot
plt.show()
