#!/usr/bin/env python
# coding: utf-8

# In[34]:


# Libraries Imported.
import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats
import warnings
from itertools import combinations
import os


# In[35]:


#Turning off user warnings in the notebook.
warnings.filterwarnings('ignore' ) 


# In[36]:


current_directory = os.getcwd() # Get the current working directorY. This will allow for the graphs, text and other outputs to be neatly stored on the end users current directory when the file is ran.


# In[37]:


folder_name = 'Text Files' # Setting what I want to call the folder
folder_path = os.path.join(current_directory, folder_name) # Creating the folder name at the current directory
if not os.path.exists(folder_path): # Logic to see if the folder already exists
    os.makedirs(folder_path) # If it doesn't exist create the new folder.


# In[38]:


sum_folder = 'Summary' # Setting what I want to call the folder
sum_path = os.path.join(current_directory, sum_folder) # Creating the folder name at the current directory
if not os.path.exists(sum_path): # Logic to see if the folder already exists
    os.makedirs(sum_path)


# In[39]:


exp_folder = 'Exploratory' # Setting what I want to call the folder
exp_path = os.path.join(current_directory, exp_folder) # Creating the folder name at the current directory
if not os.path.exists(exp_path): # Logic to see if the folder already exists
    os.makedirs(exp_path) # If it doesn't exist create the new folder.


# In[40]:


dist_folder = 'Distribution' # Setting what I want to call the folder
dist_path = os.path.join(current_directory, dist_folder) # Creating the folder name at the current directory
if not os.path.exists(dist_path): # Logic to see if the folder already exists
    os.makedirs(dist_path) # If it doesn't exist create the new folder.


# In[41]:


corr_folder = 'Correlation' # Setting what I want to call the folder
corr_path = os.path.join(current_directory, corr_folder) # Creating the folder name at the current directory
if not os.path.exists(corr_path): # Logic to see if the folder already exists
    os.makedirs(corr_path) # If it doesn't exist create the new folder.


# In[42]:


df = sns.load_dataset('iris') # Loading in Dataset


# In[43]:


trans_df_stats = df.describe().T # Creating a new data frame where the descriibe function output is transposed


# In[44]:


summary_txt = trans_df_stats.to_string(float_format='%.2f') # Creating a new data frame where the transposed data frame is formatted to 2 decimal places
file_path = os.path.join(folder_path, 'summary_statistics.txt') # Creating the text file at the designated folder name
with open(file_path, 'w') as file: # Accessing the file path in write mode and if the files exists overwriting it and otherwise creating it
    file.write(summary_txt) # Writing the summary text to a file


# In[45]:


spec_df_stats = df.groupby('species').describe() # Creating a new data frame where the numeric variables are grouped by the species and then describe method run on them to create summary statistics
pd.set_option('display.max_columns', None) # Setting max number of cloumns to display to be none, so all show
pd.set_option('display.expand_frame_repr', False) # Setting it so that the output displays the text on a single line.


# In[46]:


trans_spec_df_stats = spec_df_stats.T # Creating a new data frame from the previous data frame where the descriibe function output is transposed.
summary_txt = trans_spec_df_stats.to_string(float_format='%.2f') # Creating a new data frame where the transposed data frame is formatted to 2 decimal places
file_path = os.path.join(folder_path, 'species_summary_statistics.txt') # Creating the text file at the designated folder name
with open(file_path, 'w') as file: # Accessing the file path in write mode and if the files exists overwriting it and otherwise creating it
    file.write(summary_txt) # Writing the summary text to a file


# In[47]:


background_text = """ 
Background of the Dataset

The Iris dataset is a popular dataset, that has been widely used in the  pattern recognition and machine learning domains. The dataset was introduced by the British statistician and biologist Ronald Fisher in 1936, in a paper titled "The use of multiple measurements in taxonomic problems". The dataset contains the sepal length, sepal width, petal length, and petal width of a smaple of 150 samples of Iris flowers. The Iris flowers fall into one of three categories: setosa, versicolor, or virginica.

Overview of Variables

Categorical:

    species: This variable indicates the species of Iris. It has three categories: setosa, versicolor, and virginica.

Numerical:

    sepal_length_cm: Length of the sepal in centimeters.
    sepal_width_cm: Width of the sepal in centimeters.
    petal_length_cm: Length of the petal in centimeters.
    petal_width_cm: Width of the petal in centimeters.
""" # Creating the Markdown text that will be outputted as a png file to a folder.

plt.figure(figsize=(8, 6)) # Setting the size of the plot/ output.
# Adding text to the plot 
plt.text(0.5, 0.5, # Designating the co-ordinates of the text
        background_text, # Using the text created previously
        va='center', # Centring the text vertically
        ha='center', # Centring the text horizontally
        wrap=True) # Setting the text to wrap in case it doesn't fit on the plot
plt.axis('off') # Turing off the axis lines
plt.savefig(os.path.join(sum_path, 'background.png',), # Saving the figure to the folder designated previously
             dpi=300, # Setting the resolution of the image
             bbox_inches='tight', # Setting the bounding box to fit the plot area
             pad_inches=0.1) # Setting the padding around the plot 


# In[48]:


# Creating a table to display Variable Name/ Brief Description/ Variable Type/ Data Type & Sample Data.
data = [
    ["sepal_length", "Length of sepal in cm", "Numerical", "Float", "5.1, 4.9, 4.7, 4.6, 5.0"],
    ["sepal_width", "Width of sepal in cm", "Numerical", "Float", "3.5, 3.0, 3.2, 3.1, 3.6"],
    ["petal_length", "Length of petal in cm", "Numerical", "Float", "1.4, 1.4, 1.3, 1.5, 1.4"],
    ["petal_width", "Width of petal in cm", "Numerical", "Float", "0.2, 0.3, 0.2, 0.4, 0.1"],
    ["species", "Species of Iris", "Categorical", "String", "setosa, virginica, versicolor"]
] # Creating a list of lists, whereby each list represents a row in the table and then each list contains a value for Variable Name/ Brief Description/ Variable Type/ Data Type & Sample Data..

df_desc = pd.DataFrame(data, columns=["Variable", "Description", "Variable Type", "Data Type", "Sample Data"]) # Creating a data frame from the data created in the previous step and passing on the headers for the columns
# Creating a formatted table using the tabulate library
tabular_data = tabulate(df_desc, # Setting the data I want to use
                        tablefmt='pipe') # Using the pipe format for styling the table i.e colons to indicate alignment of the columns

fig, ax = plt.subplots(figsize=(20, 10)) # Creating a sub plot.
ax.axis('tight') # Setting the axis to be just about big enough to show all data.
ax.axis('off') # Turning the axis formatting off
table = ax.table(cellText=df_desc.values, # Creating the table and specifying the data to be used
        colLabels=df_desc.columns, # Specifies the column labels
        bbox=[0,0,1,1], # Setting it so the table expands the full figure
        colLoc='center', # Centering the columns
        cellLoc='center') # Centering the cell values

table.auto_set_font_size(False) # Disabling the adjustment of the font size
table.set_fontsize(14) # Setting font size as 14

plt.savefig(os.path.join(sum_path, 'description.png',), # Saving the figure to the folder designated previously
                        dpi=300, # Setting the resolution of the image 
                        bbox_inches='tight', # Setting the bounding box to fit the plot area
                        pad_inches=0.05) # Setting the padding


# In[49]:


# Markdown content
var_desc_text = """
Categorical Variables

The species variable is a categorical variable. The reasoning for this is:

1. The values are qualitative, in that they are not measured in a value that can be measured.
2. There is no means to perform numerical calculations on them.
3. The values cannot be ordered or ranked in any way other than alphabetically.
4. There are only a distinct number of values in the variable.

Additionally, it is a  string as they it is represented by alphabetical characters, is used to categorise and has no non-numeric values.


Numerical Variables

The sepal_length, sepal_width, petal_length, and petal_width variables are all numerical. The reasoning for this is:

1. The values for these variables are quantitative, in that they are measured with a value that can be measured and the value is a number.
2. Numerical operations can be performed on them.
3. They can be ordered or ranked based on value.

The sepal_length, sepal_width, petal_length, and petal_width have a float data type as they can be represented to a number of decimal places and are so in the data collected.
""" # Creating the Markdown text that will be outputted as a png file to a folder.


plt.figure(figsize=(8, 6))# Setting the size of the plot/ output.
# Setting the size of the plot/ output.
plt.text(0.5, 0.5, # Designating the co-ordinates of the text
        var_desc_text, # Using the text created previously
        va='center', # Centring the text verrtically
        ha='center', # Centring the text horizontally
        wrap=True) # Setting the text to wrap in case it doesn't fit on the plot
plt.axis('off') # Turning the axis off
plt.savefig(os.path.join(sum_path,'variables.png',), # Saving the figure to the folder designated previously
        dpi=300, # Setting the resolution of the image 
        bbox_inches='tight', # Setting the bounding box to fit the plot area
        pad_inches=0.05) # Setting the padding


# In[50]:


df_eda = df.copy(deep=True) # Creating a copy of the data source for doing some exploration


# In[51]:


df_eda['petal_area'] = df_eda['petal_length'] * df_eda['petal_width'] # Creating a petal area variable
df_eda['sepal_area'] = df_eda['sepal_length'] * df_eda['sepal_width'] # Creating a sepal area variable


# In[52]:


vols = [] # Creating an empty list to store the volumes

# Calculate frustum volume for each row using a for loop
for index, row in df_eda.iterrows():
    h = row['sepal_length'] # Getting the height
    r1 = row['petal_width'] / 2 # Getting the radius of the petal
    r2 = row['sepal_width'] / 2 # Getting the radius of the sepal
    vol = (1/3) * np.pi * h * (r1**2 + r1*r2 + r2**2) # Applying the variables to the formula 
    vols.append(vol) # Appending each colume to the volumes list

df_eda['flower_volume'] = vols # Adding the volumes to the dataframe


# In[53]:


#Creating a function for assigning the label to the bar chart
def bar_label(ax): # Defining the function and its input
    for i in ax.patches: # Looping through each bar in the barplot.
        # Using the .annotate element to add text to the graph. 
        ax.annotate(format(i.get_height(), '.2f'), # Getting the height to 2 decimal places. .get_height will return the height of the bar. This is done for all bars in the graph as its a for loop.
                    # .get_x will return the x-coordinate of the left hand side of each bar/ .get_width returns the width of the bar.
                    # First getting the x-cord of the left hand side and adding the width. Then dividing by 2 to centre where the text should be.
                       (i.get_x() + i.get_width() / 2., i.get_height()), # get_height is used to denote where on the Y axis the text should be
                       ha = 'center', va = 'center', # Aligning the text to be horizontally and vertically centred.
                       size=18, # Denoting the font size of the text to be 18.
                       # Setting the coordinates of the text on the x axis to be 0, as I am happy with the text being centred.
                       xytext = (0, -14),  # Setting the coordinates of text on the y axis to be -14, as I would like the text to be just below the top of the bar.
                       color='white',
                       textcoords = 'offset points') # Offsetting the text from reference points.


# In[67]:


plt.figure(figsize=(25, 15)) # Setting the size of the figure

# Plot for sepal width
plt.subplot(2, 2, 1) # Setting on what sub plot the graph should be positioned
ax_1 = sns.barplot(data=df, # Using the data from the dataframe created
                  x="species", # Setting species to be on the x-axis
                  y="sepal_width",  # Setting sepal width to be on the y-axis
                  hue="species", # Setting species to be the colour of the bars
                  color='skyblue', # Setting the color to be Sky Blue
                  edgecolor='black', # Adding a feint black line around the bars for display purposes
                  errorbar=None, # Removing the error bar from the graph
                  dodge=False, # Turning off dodge on the plot so the display looks neater
                  legend= False, # Turning off the legend
                  linewidth=1.5) # Setting the line width of the black line around the bars.
plt.yticks([]) # Setting the tick marks to be blank by assigning an empty list.
plt.xticks([]) # Setting the tick marks to be blank by assigning an empty list.
plt.xlabel('') # Setting the x-axis label to be blank
plt.ylabel('') # Setting the y-axis label to be blank
plt.title('Mean Sepal Width Per Species', # Setting the name of the plot
           size=18, # Setting the font size of the plot
           color='#4f4e4e') # Setting the color of the title


# Plot for sepal length
plt.subplot(2, 2, 2) # Setting on what sub plot the graph should be positioned
ax_2 = sns.barplot(data=df, # Using the data from the dataframe created
                  x="species", # Setting species to be on the x-axis
                  y="sepal_length",  # Setting sepal length to be on the y-axis
                  hue="species", # Setting species to be the colour of the bars
                  color='skyblue', # Setting the color to be Sky Blue
                  edgecolor='black', # Adding a feint black line around the bars for display purposes
                  errorbar=None, # Removing the error bar from the graph
                  dodge=False, # Turning off dodge on the plot so the display looks neater
                  legend= False, # Turning off the legend
                  linewidth=1.5) # Setting the line width of the black line around the bars.
plt.yticks([]) # Setting the tick marks to be blank by assigning an empty list.
plt.xticks([]) # Setting the tick marks to be blank by assigning an empty list.
plt.xlabel('') # Setting the x-axis label to be blank
plt.ylabel('') # Setting the y-axis label to be blank
plt.title('Mean Sepal Length Per Species', # Setting the name of the plot
           size=18, # Setting the font size of the plot
           color='#4f4e4e') # Setting the color of the title

# Plot for petal length
plt.subplot(2, 2, 3) # Setting on what sub plot the graph should be positioned
ax_3 = sns.barplot(data=df, # Using the data from the dataframe created
                  x="species", # Setting species to be on the x-axis
                  y="petal_length",  # Setting petal length to be on the y-axis
                  hue="species", # Setting species to be the colour of the bars
                  color='skyblue', # Setting the color to be Sky Blue
                  edgecolor='black', # Adding a feint black line around the bars for display purposes
                  errorbar=None, # Removing the error bar from the graph
                  dodge=False, # Turning off dodge on the plot so the display looks neater
                  legend= False, # Turning off the legend
                  linewidth=1.5) # Setting the line width of the black line around the bars.
plt.yticks([]) # Setting the tick marks to be blank by assigning an empty list.
plt.xticks([]) # Setting the tick marks to be blank by assigning an empty list.
plt.xlabel('') # Setting the x-axis label to be blank
plt.ylabel('') # Setting the y-axis label to be blank
plt.title('Mean Petal Length Per Species', # Setting the name of the plot
           size=18, # Setting the font size of the plot
           color='#4f4e4e') # Setting the color of the title


# Plot for petal width
plt.subplot(2, 2, 4) # Setting on what sub plot the graph should be positioned
ax_4 = sns.barplot(data=df, # Using the data from the dataframe created
                  x="species", # Setting species to be on the x-axis
                  y="petal_width",  # Setting petal width to be on the y-axis
                  hue="species", # Setting species to be the colour of the bars
                  color='skyblue', # Setting the color to be Sky Blue
                  edgecolor='black', # Adding a feint black line around the bars for display purposes
                  errorbar=None, # Removing the error bar from the graph
                  dodge=False, # Turning off dodge on the plot so the display looks neater
                  legend=True,
                  linewidth=1.5) # Setting the line width of the black line around the bars.
plt.yticks([]) # Setting the tick marks to be blank by assigning an empty list.
plt.xticks([]) # Setting the tick marks to be blank by assigning an empty list.
plt.xlabel('') # Setting the x-axis label to be blank
plt.ylabel('') # Setting the y-axis label to be blank
plt.legend(bbox_to_anchor=(1, 1), loc='upper left') # Moving legend to the top right.
plt.title('Mean Petal Length Per Species', # Setting the name of the plot
           size=18, # Setting the font size of the plot
           color='#4f4e4e') # Setting the color of the title
sns.despine(left=True) # Using the despine function to remove the axis lines on the left hand side

# Add a title to the figure
plt.suptitle('Mean Measurement Per Species', size=24, color='#4f4e4e') # Setting the overall title of the graph

bar_label(ax_1) # Applying the function to the plot
bar_label(ax_2) # Applying the function to the plot
bar_label(ax_3) # Applying the function to the plot
bar_label(ax_4) # Applying the function to the plot

# Show plot
plt.savefig(os.path.join(exp_path, 'Bar Chart.png')) # Saving the plot to the desired folder


# ### Distribution Analysis

# In[55]:


plt.rcParams.update({'font.size': 14}) # Set font sizes
plt.figure(figsize=(25, 15))  # Setting the size of the plot
ax = sns.countplot(data=df, # Creating a Countplot using the data from the data frame created
                   y="species", # Coloring based on the species
                   edgecolor='black',# Creating a black line around the chart
                   palette='Set3', # Setting the color pallette for the chart
                   linewidth=2) # Setting the width of the black line around the charts
plt.title('Distribution of Species', # Setting the plot title
           size=20) # Setting the size of the font
plt.xlabel('Frequency', # Setting the X-axis label
            size=20) # Setting the size of the font
plt.ylabel('Species', # Setting the Y-axis label
            size=20) # Setting the size of the font

total = len(df['species']) # Calculating the number of data points/ values in the data source.
for p in ax.patches: # Using a for loop to get and apply a label to each bar in the plot
    percent = '{:.2f}%'.format(100 * p.get_width()/total) # Getting the percentage value each bar makes up by getting the width of it as a proportion of the total variable. Formatting to 2 decimal places
    x_ax = p.get_width() # Getting the co-ordinates of the x-axis for applying the label
    y_ax = p.get_y() + p.get_height()/2 # Getting the centre point of the bars for applying the label
    ax.annotate(percent, (x_ax, y_ax), # Adding the text to the label/ percent being the text to apply/ x_ax & y_ax beign the coordinates
                ha='left', # Aligning the labels to horizontally left aligned
                va='center', # Aligning the labels to veritcally centrally aligned
                fontsize=14) # Setting the font size

plt.savefig(os.path.join(exp_path, 'CountPlot.png')) # Saving the plot to the desired folder


# In[56]:


a, ax = plt.subplots(2, 2, # Creating a sub plot and 
                    figsize=(25, 25)) # Creating the size of the sub plot
sns.boxplot(x="species", # Creating a box plot where species is on the x-axis
            y="sepal_length", # Setting the sepal length to be on the y-axis
            data=df, # Using data from the data frame
            ax=ax[0, 0], # Setting the axis this plot is to be on
            palette='Set3') # Setting the color pallette to use
ax[0, 0].set_title('Sepal Length', size=16) # Setting the title of the plot and the size
ax[0, 0].set_xlabel('Flower Species', size=14) # Setting the title of the x-axis and the size
ax[0, 0].set_ylabel('Sepal Length', size=14) # Setting the title of the y-axis and the size

sns.boxplot(x="species", # Creating a box plot where species is on the x-axis
            y="sepal_width", # Setting the sepal width to be on the y-axis
            data=df, # Using data from the data frame
            ax=ax[0, 1], # Setting the axis this plot is to be on
            palette='Set3') # Setting the color pallette to use
ax[0, 1].set_title('Sepal Width', size=16) # Setting the title of the plot and the size
ax[0, 1].set_xlabel('Flower Species', size=14) # Setting the title of the x-axis and the size
ax[0, 1].set_ylabel('Sepal Width', size=14) # Setting the title of the y-axis and the size

sns.boxplot(x="species", # Creating a box plot where species is on the x-axis
            y="petal_length", # Setting the petal length to be on the y-axis
            data=df, # Using data from the data frame
            ax=ax[1, 0], # Setting the axis this plot is to be on
            palette='Set3') # Setting the color pallette to use
ax[1, 0].set_title('Petal Length', size=16) # Setting the title of the plot and the size
ax[1, 0].set_xlabel('Flower Species', size=14) # Setting the title of the x-axis and the size
ax[1, 0].set_ylabel('Petal Length', size=14) # Setting the title of the y-axis and the size

sns.boxplot(x="species", # Creating a box plot where species is on the x-axis
            y="petal_width", # Setting the petal width to be on the y-axis
            data=df, # Using data from the data frame
            ax=ax[1, 1], # Setting the axis this plot is to be on
            palette='Set3') # Setting the color pallette to use
ax[1, 1].set_title('Petal Width', size=16) # Setting the title of the plot and the size
ax[1, 1].set_xlabel('Flower Species', size=14) # Setting the title of the x-axis and the size
ax[1, 1].set_ylabel('Petal Width', size=14) # Setting the title of the y-axis and the size

plt.tight_layout() # Setting a tight layout so the subplot adjusts as required
plt.savefig(os.path.join(dist_path, 'BoxPlot.png')) # Saving the plot to the desired folder


# In[57]:


numeric_df = df.select_dtypes(include=[np.number]) # Creating a new data frame that takes in only numeric data types
column_combinations = list(combinations(numeric_df.columns, 2)) # Creating all possible dual variable combinations

fig, axes = plt.subplots(3, 2, figsize=(25, 25)) # Create a 3 by 2 subplot and denoting the size of the plot
# Using a for loop to generate a regression plot for each variable combination and add the correlation information
# Using axes.flatten to return a single flat array to allow the plotting of the data.
for i, ax in enumerate(axes.flatten()): # Returning the index and value of each grid in a one dimensional array
    if i < len(column_combinations): # Checking if the index is within the specified number of combinations, to avoid a continious loop. Acts as an exit clause
        x_column, y_column = column_combinations[i] # Assigning values
        
        sns.regplot(data=numeric_df, # Creating a regression plot using the data frame
                    x=x_column, # Assigning the x-column value to be on the x-axis
                    y=y_column, # Assigning the x-column value to be on the x-axis
                    ax=ax) #  Setting where the sub plot should be for each plot
        
        r_value, p_value = stats.pearsonr(numeric_df[x_column], numeric_df[y_column]) # Calculating the Pearson Correlation and P value for the combinations
        r_squared = r_value**2 # Calculating the R_Squared value
        
        ax.text(0.02, 0.98, #Adding text to the plots in the top left corner
                f"Pearson Correlation = {r_value:.2f}\nR-squared = {r_squared:.2f}\nP-value = {p_value:.2f}", # Formatting the Pearson Correlation/ P_Value and R_Squared values to 2 decimal places
                transform=ax.transAxes, # Getting the current axis instance interpreting the coordinates relative to the axes of the plot
                fontsize=12, # Setting the font size
                va='top') # Setting the text to be aligned to the top
        
        ax.grid(False) # Turning off the grid lines on the plots
        ax.set_xlabel(x_column) # Assigning the X-axis label to be the x_column value
        ax.set_ylabel(y_column)  # Assigning the Y-axis label to be the y_column value
        ax.set_title(f'Regression plot: {x_column} vs {y_column}') # Setting the plot title


plt.tight_layout() # Setting a tight layout so the subplot adjusts as required
plt.savefig(os.path.join(corr_path, 'Scatter.png')) # Saving the figure to the desired folder


# In[58]:


numeric_df = df.select_dtypes(include=[np.number]) # Creating a new data frame that takes in only numeric data types
def create_table_dist(): # Creating a function to calculate the Skewness/ Kurtosis/ Mean and Median of values
    skewness = numeric_df.skew() # Calculating the Skewness
    kurtosis = numeric_df.kurt() # Calculating the Kurtosis
    mean_val = numeric_df.mean() # Calculating the Mean
    median_val = numeric_df.median() # Calculating the Median
    
    table = pd.DataFrame({
        'Skewness': skewness,
        'Kurtosis': kurtosis,
        'Mean': mean_val,
        'Median': median_val
    }) #Creating a data frame to store the values
    
    return table # Returning the table of the results


# In[59]:


table = create_table_dist() # Creating a data frame by calling the function
    


# In[60]:


# Convert DataFrame to a formatted string
dist_summary_txt = table.to_string(float_format='%.2f') # Creating a new data frame of the distirbution data where the data frame is formatted to 2 decimal places

file_path = os.path.join(folder_path, 'distribution_summary_statistics.txt') # Creating the text file at the designated folder name
with open(file_path, 'w') as file: # Accessing the file path in write mode and if the files exists overwriting it and otherwise creating it
    file.write(dist_summary_txt) # Writing the summary text to a file


# In[61]:


def plot_distribution(data, title, bin_size): #Creating a function that takes in the data to be used/ Title of the graph/ Bin Size
    # Creating a Histogram
    sns.histplot(data, # Passing in the data that was specified in the function parameter
                kde=True, # Setting the kernel density estimate to be true to visualise the distribution
                bins=bin_size, # Passing in the bin size speciefied in the function parameter
                color='skyblue', # Setting the color of the bars
                edgecolor='black', # Setting the line around the perimeter of the bars to be black
                linewidth=2) # Setting the width of the bar to be 2
    
    # Adding mean and median lines
    mean_val = data.mean() # Creating a variable that calculates the mean of the data specified in the function parameter
    median_val = data.median() # Creating a variable that calculates the mean of the data specified in the function parameter
    plt.axvline(x=mean_val, # Adding a vertical line to the x-axis of the mean calculated in the previous step
                label='Mean Value', # Setting the title of the label
                color='red', # Setting color of the line
                linewidth=3, # Setting the width of the line
                linestyle='-') # Setting the style of the line
    plt.axvline(x=median_val, # Adding a vertical line to the x-axis of the median calculated in the previous step
                label='Median Value', # Setting the title of the label
                color='green', # Setting color of the line
                linewidth=3, # Setting the width of the line
                linestyle='-') # Setting the style of the line

    # Adding skewness, kurtosis, mean, and median to the plot
    skewness = data.skew() # Creating a variable that calculates the skewness of the data specified in the function parameter
    kurtosis = data.kurt() # Creating a variable that calculates the kurtosis of the data specified in the function parameter
    plt.text(0.98, 0.88, # Setting the X & Y co-ordinates of the text to be added to the plot. Positioned in the top right corner
            f'Skewness: {skewness:.2f}\nKurtosis: {kurtosis:.2f}\nMean: {mean_val:.2f}\nMedian: {median_val:.2f}', # Formatting the values on the chart to be 2 decimal places
             transform=plt.gca().transAxes, # Getting the current axis instance interpreting the coordinates relative to the axes of the plot
             fontsize=14, # Setting font size
             bbox=dict(facecolor='yellow', # Setting the background color of the box
                       alpha=0.8), # Setting the transparency of the text box
                       verticalalignment='top', # Setting the text to be vertically aligned to the top
                       horizontalalignment='right') # Setting the horizontal alignment to be to the right

    # Plot formatting
    plt.title(title, size=20) # Setting the title of the plot to take in the value inputted in the function parameter
    plt.xlabel('Value', size=14) # Setting the text and size of the text on the X-Axis
    plt.ylabel('Frequency', size=14) # Setting the text and size of the text on the X-Axis
    plt.xticks(size=14) # Setting the size of the tick marks on the x axis
    plt.yticks(size=14) # Setting the size of the tick marks on the x axis
    plt.grid(axis='y', # Adding grid lines to the y-axis
             linestyle='-', # Setting the style of the line
             alpha=0.6) # Setting the transparency of the grid lines
    plt.legend(fontsize=14) # Setting the size of the legend

# Create subplots
plt.figure(figsize=(25, 25))  # Setting the size of the plot

plt.subplot(2, 2, 1) # Setting on what sub plot the graph should be positioned
plot_distribution(df['sepal_length'], 'Distribution of Sepal Length', bin_size=7) # Inputting function parameters to create plot

plt.subplot(2, 2, 2) # Setting on what sub plot the graph should be positioned
plot_distribution(df['sepal_width'], 'Distribution of Sepal Width', bin_size=8) # Inputting function parameters to create plot

plt.subplot(2, 2, 3) # Setting on what sub plot the graph should be positioned
plot_distribution(df['petal_length'], 'Distribution of Petal Length', bin_size=5) # Inputting function parameters to create plot

plt.subplot(2, 2, 4) # Setting on what sub plot the graph should be positioned
plot_distribution(df['petal_width'], 'Distribution of Petal Width', bin_size=5) # Inputting function parameters to create plot

# Show plot
plt.tight_layout() # Setting a tight layout so the subplot adjusts as required
plt.savefig(os.path.join(dist_path, 'Histogram.png')) # Saving the figure to the desired folder


# In[62]:


results = [] # Creating an empty list to store results from the for loop
for col1, col2 in column_combinations: # Creating a for loop to iterate over all combinations of the numeric columns
    r_value, p_value = stats.pearsonr(numeric_df[col1], numeric_df[col2]) # Calculating the correlation & p value for all combinations
    r_squared = r_value**2 # Calculating the r-squared value
    
    results.append({
        'Variable 1': col1,
        'Variable 2': col2,
        'Pearson r-value': r_value,
        'P-value': p_value,
        'R-squared': r_squared
    }) # Appending the results to the empty list previously created as a dictionary.


# In[63]:


result_df = pd.DataFrame(results) # Creating the dataframe of the results for the correlation of each variable.


# In[64]:


corr_summary_txt = result_df.to_string(float_format='%.2f') # Creating a new data frame of the correlation data where the data frame is formatted to 2 decimal places

file_path = os.path.join(folder_path, 'correlation_summary_statistics.txt') # Creating the text file at the designated folder name
with open(file_path, 'w') as file: # Accessing the file path in write mode and if the files exists overwriting it and otherwise creating it
    file.write(corr_summary_txt) # Writing the summary text to a file

plt.rcParams.update({'font.size': 14}) # Set font sizes

# Violin plot for each variable
plt.figure(figsize=(25, 15))  # Setting the size of the plot

# Violin plot for sepal length
plt.subplot(2, 2, 1)
sns.violinplot(data=df, x="species", y="sepal_length", palette="Set1", inner="quartile")
plt.title('Violin Plot of Sepal Length by Species', fontsize=20)
plt.xlabel('Species', fontsize=18)
plt.ylabel('Sepal Length (cm)', fontsize=18)

# Violin plot for sepal width
plt.subplot(2, 2, 2)
sns.violinplot(data=df, x="species", y="sepal_width", palette="Set2", inner="quartile")
plt.title('Violin Plot of Sepal Width by Species', fontsize=20)
plt.xlabel('Species', fontsize=18)
plt.ylabel('Sepal Width (cm)', fontsize=18)

# Violin plot for petal length
plt.subplot(2, 2, 3)
sns.violinplot(data=df, x="species", y="petal_length", palette="Set3", inner="quartile")
plt.title('Violin Plot of Petal Length by Species', fontsize=20)
plt.xlabel('Species', fontsize=18)
plt.ylabel('Petal Length (cm)', fontsize=18)

# Violin plot for petal width
plt.subplot(2, 2, 4)
sns.violinplot(data=df, x="species", y="petal_width", palette="Set1", inner="quartile")
plt.title('Violin Plot of Petal Width by Species', fontsize=20)
plt.xlabel('Species', fontsize=18)
plt.ylabel('Petal Width (cm)', fontsize=18)

plt.tight_layout()
plt.savefig(os.path.join(exp_path, 'Violin Plot.png')) # Saving the plot to the desired folder


plt.figure(figsize=(30, 15)) # Setting the size of the figure

# Plot for sepal width
plt.subplot(1, 3, 1) # Setting on what sub plot the graph should be positioned
axe_1 = sns.barplot(data=df_eda, # Using the data from the dataframe created
                  x="species", # Setting species to be on the x-axis
                  y="sepal_area",  # Setting sepal width to be on the y-axis
                  hue="species", # Setting species to be the colour of the bars
                  color='skyblue', # Setting the color to be Sky Blue
                  edgecolor='black', # Adding a feint black line around the bars for display purposes
                  errorbar=None, # Removing the error bar from the graph
                  legend=False,
                  dodge=False, # Turning off dodge on the plot so the display looks neater
                  linewidth=1.5) # Setting the line width of the black line around the bars.
plt.yticks([]) # Setting the tick marks to be blank by assigning an empty list.
plt.xticks([]) # Setting the tick marks to be blank by assigning an empty list.
plt.xlabel('') # Setting the x-axis label to be blank
plt.ylabel('') # Setting the y-axis label to be blank
plt.title('Mean Sepal Area Per Species', # Setting the name of the plot
           size=18, # Setting the font size of the plot
           color='#4f4e4e') # Setting the color of the title

# Plot for sepal width
plt.subplot(1, 3, 2) # Setting on what sub plot the graph should be positioned
axe_2 = sns.barplot(data=df_eda, # Using the data from the dataframe created
                  x="species", # Setting species to be on the x-axis
                  y="petal_area",  # Setting sepal width to be on the y-axis
                  hue="species", # Setting species to be the colour of the bars
                  color='skyblue', # Setting the color to be Sky Blue
                  edgecolor='black', # Adding a feint black line around the bars for display purposes
                  legend=False,
                  errorbar=None, # Removing the error bar from the graph
                  dodge=False, # Turning off dodge on the plot so the display looks neater
                  linewidth=1.5) # Setting the line width of the black line around the bars.
plt.yticks([]) # Setting the tick marks to be blank by assigning an empty list.
plt.xticks([]) # Setting the tick marks to be blank by assigning an empty list.
plt.xlabel('') # Setting the x-axis label to be blank
plt.ylabel('') # Setting the y-axis label to be blank
plt.title('Mean Petal Area Per Species', # Setting the name of the plot
           size=18, # Setting the font size of the plot
           color='#4f4e4e') # Setting the color of the title

# Plot for sepal width
plt.subplot(1, 3, 3) # Setting on what sub plot the graph should be positioned
axe_3 = sns.barplot(data=df_eda, # Using the data from the dataframe created
                  x="species", # Setting species to be on the x-axis
                  y="flower_volume",  # Setting sepal width to be on the y-axis
                  hue="species", # Setting species to be the colour of the bars
                  color='skyblue', # Setting the color to be Sky Blue
                  edgecolor='black', # Adding a feint black line around the bars for display purposes
                  errorbar=None, # Removing the error bar from the graph
                  legend=True,
                  dodge=False, # Turning off dodge on the plot so the display looks neater
                  linewidth=1.5) # Setting the line width of the black line around the bars.
plt.yticks([]) # Setting the tick marks to be blank by assigning an empty list.
plt.xticks([]) # Setting the tick marks to be blank by assigning an empty list.
plt.xlabel('') # Setting the x-axis label to be blank
plt.ylabel('') # Setting the y-axis label to be blank
plt.legend(bbox_to_anchor=(1, 1), loc='upper left') # Moving legend to the top right.
plt.title('Mean Flower Volume Per Species', # Setting the name of the plot
           size=18, # Setting the font size of the plot
           color='#4f4e4e') # Setting the color of the title
sns.despine(left=True) # Using the despine function to remove the axis lines on the left hand side


# Add a title to the figure
plt.suptitle('Mean Measurement Per Species', size=24, color='#4f4e4e') # Setting the overall title of the graph

bar_label(axe_1) # Applying the function to the plot
bar_label(axe_2) # Applying the function to the plot
bar_label(axe_3) # Applying the function to the plot


# Show plot
plt.savefig(os.path.join(exp_path, 'Bar Chart Calculated Variables.png')) # Saving the plot to the desired folder