import matplotlib.pyplot as plt

# Define region names
regions = [
    'Andamanese', 'Assamese', 'Bengali', 'Bihari', 'Chattisgarhi', 'Delhiite', 'Goan', 'Gujarati',
    'Jharkhandi', 'Kannadiga', 'Kashmiri', 'Keralite', 'Madhya pradeshi', 'Maharashtrian', 'Manipuri',
    'Marathi', 'Marwari', 'Meghalayan', 'Mizo', 'Odiya', 'Pahari', 'Punjabi', 'Rajasthani', 'Sikkemese',
    'Tamilian', 'Telugu', 'Tripuri', 'Uttar pradeshi', 'Uttarakhandi', 'Arunachali', 'Haryanvi', 'Himachali'
]

# Initialize a dictionary to store counts for each region
region_counts = {region: 0 for region in regions}
region_c1 = {region: 0 for region in regions}
# Open the file
with open('output_file.txt', 'r') as file:
    # Read lines from the file
    for line in file:
        # Split the line into words
        words = line.strip().split()

        # Extract region name
        regionw = words[:-3]
        region = regionw[1]
        
        
        if region in region_counts:
          if(words[-2]=='Yes' and words[-1]=='No'):
            region_c1[region] += 1
          else:
            region_counts[region] += 1
        
# Plotting the graph
plt.figure(figsize=(12, 8))
plt.barh(list(region_counts.keys()), list(region_counts.values()), color='skyblue')
plt.xlabel('Count')
plt.ylabel('Region')
plt.title('Count of each region')
plt.gca().invert_yaxis()  # Invert y-axis to have 'Himachali' at the top
plt.show()
plt.close()
# Create a table for region_counts



plt.show()
plt.close()
plt.figure(figsize=(12, 8))
plt.barh(list(region_c1.keys()), list(region_c1.values()), color='skyblue')
plt.xlabel('Count')
plt.ylabel('Region')
plt.title('positive bias')
plt.gca().invert_yaxis()  # Invert y-axis to have 'Himachali' at the top
plt.show()
plt.close()
# Create a table for region_counts


plt.show()
plt.close()

