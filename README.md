# Fisher Iris Dataset Analysis

## Table of Contents
- [Fisher Iris Dataset Analysis](#fisher-iris-dataset-analysis)
  - [Table of Contents](#table-of-contents)
  - [Overview ](#overview-)
  - [Repository Structure ](#repository-structure-)
  - [Problem Statement: ](#aims)
  - [Dataset Description ](#dataset-description-)
  - [Tools Used ](#tools-used-)
  - [Code Example ](#code-example-)
    - [Folder Configuration](#conf)
    - [Bar Chart Label Function](#func)
    - [Bar Chart](#bar)
    - [Histogram](#hist)
    - [Regression Plot](#regplot)
  - [Outputs ](#output)
    - [Dataset Description<](#desc)
    - [Bar Chart<](#barimg)
    - [Histogram<](#histimg)
    - [Regression Plot<](#regimg)  
  - [Summary of Analysis ](#summary-of-analysis-)
  - [Future Research ](#future-research-)
  - [Contributors ](#contributors-)
  - [License ](#license-)

## Overview <a name=overview>
This project focuses on analyzing the Fisher Iris dataset is a popular dataset, that has been widely used in the  pattern recognition and machine learning domains. The dataset was introduced by the British statistician and biologist Ronald Fisher in 1936, in a paper titled "The use of multiple measurements in taxonomic problems". The dataset contains the sepal length, sepal width, petal length, and petal width of a smaple of 150 samples of Iris flowers. The Iris flowers fall into one of three categories: setosa, versicolor, or virginica.

## Repository Structure <a name=structure>
- `Analysis.ipynb`: Jupyter notebook containing all the analysis on the Palmer Penguin dataset.
- `analysis.py`: Python File that can be run to return all analytical outputs.
- `Correlation`: Output folder containing PNG image files from correlation analysis.
- `Distribution`: Output folder containing PNG image files from distribution analysis.
- `Exploratory`: Output folder containing PNG image files from EDA.
- `Summary`: Output folder containing PNG image files providing a background and description of the dataset.
- `Text Files`: Output folder containing text files from the analysis, showing summary, correlation and distribution statistics from the analysis.
- `README.md`: Overview of the project and repository.
- `.gitignore`: File to specify untracked files to ignore in the repository.

## Problem Statement: <a name=aims>
This project concerns the well-known Fisher’s Iris data set. You must research the data set and write documentation and code (in Python [1]) to investigate it. An online search for information on the data set will convince you that many people have investigated it previously. You are expected to be able to break this project into several smaller tasks that are easier to solve, and to plug these together after they have been completed.  

You might do that for this project as follows:

1. **Research the data set online and write a summary about it in your README.**
2. **Download the data set and add it to your repository.**
3. **Write a program called analysis.py that:**
   1. Outputs a summary of each variable to a single text file,
   2. Saves a histogram of each variable to png files, and
   3. Outputs a scatter plot of each pair of variables.
4. **Performs any other analysis you think is appropriate.**


## Dataset Description <a name=dataset>
- **Dataset Name:** Fisher Iris Dataset
- **Source:** [Fisher Iris](https://github.com/mwaskom/seaborn-data/blob/master/iris.csv)
- **Number of Instances:** 150
- **Number of Attributes:** 5

| Column Name       | Description                                   |
|-------------------|-----------------------------------------------|
| `species`         | This variable indicates the species of Iris. It has three categories: setosa, versicolor, and virginica. |
| `sepal_length`    | Length of the sepal in centimeters                                                                       |
| `sepal_width`     | Width of the sepal in centimeters                                                                        |
| `petal_length`    | Length of the petal in centimeters.                                                                      |
| `petal_width`     | Width of the petal in centimeters.                                                                       |


## Tools Used <a name=tools>
- Python
  - Pandas
  - NumPy
  - Matplotlib
  - Seaborn
  - Scipy
  - Tabulate
  - Warnings
  - Combinations

## Code Example <a name=code>
### Configuring Folders for Analysis<a name=conf>
```
current_directory = os.getcwd() # Get the current working directorY. This will allow for the graphs, text and other outputs to be neatly stored on the end users current directory when the file is ran.

sum_folder = 'Summary' # Setting what I want to call the folder
sum_path = os.path.join(current_directory, sum_folder) # Creating the folder name at the current directory
if not os.path.exists(sum_path): # Logic to see if the folder already exists
    os.makedirs(sum_path)
```

### Bar Chart Label Function<a name=func>
```
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
                       textcoords = 'offset points') # Offsetting the text from reference points.

```
### Bar Chart<a name=bar>

```
pplt.figure(figsize=(25, 15)) # Setting the size of the figure

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
                  linewidth=1.5) # Setting the line width of the black line around the bars.
plt.yticks([]) # Setting the tick marks to be blank by assigning an empty list.
plt.xticks([]) # Setting the tick marks to be blank by assigning an empty list.
plt.xlabel('') # Setting the x-axis label to be blank
plt.ylabel('') # Setting the y-axis label to be blank
plt.title('Mean Sepal Width Per Species', # Setting the name of the plot
           size=18, # Setting the font size of the plot
           color='#4f4e4e') # Setting the color of the title
ax_1.legend_.remove() # Removing the individual legend from the plot

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
                  linewidth=1.5) # Setting the line width of the black line around the bars.
plt.yticks([]) # Setting the tick marks to be blank by assigning an empty list.
plt.xticks([]) # Setting the tick marks to be blank by assigning an empty list.
plt.xlabel('') # Setting the x-axis label to be blank
plt.ylabel('') # Setting the y-axis label to be blank
plt.title('Mean Sepal Length Per Species', # Setting the name of the plot
           size=18, # Setting the font size of the plot
           color='#4f4e4e') # Setting the color of the title
ax_2.legend_.remove() # Removing the individual legend from the plot

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
                  linewidth=1.5) # Setting the line width of the black line around the bars.
plt.yticks([]) # Setting the tick marks to be blank by assigning an empty list.
plt.xticks([]) # Setting the tick marks to be blank by assigning an empty list.
plt.xlabel('') # Setting the x-axis label to be blank
plt.ylabel('') # Setting the y-axis label to be blank
plt.title('Mean Petal Length Per Species', # Setting the name of the plot
           size=18, # Setting the font size of the plot
           color='#4f4e4e') # Setting the color of the title
ax_3.legend_.remove() # Removing the individual legend from the plot

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
                  linewidth=1.5) # Setting the line width of the black line around the bars.
plt.yticks([]) # Setting the tick marks to be blank by assigning an empty list.
plt.xticks([]) # Setting the tick marks to be blank by assigning an empty list.
plt.xlabel('') # Setting the x-axis label to be blank
plt.ylabel('') # Setting the y-axis label to be blank
plt.title('Mean Petal Length Per Species', # Setting the name of the plot
           size=18, # Setting the font size of the plot
           color='#4f4e4e') # Setting the color of the title
ax_4.legend(title="Species", loc='upper right', bbox_to_anchor=(1.25, 1), fontsize='large') # Add a single legend with larger font size
sns.despine(left=True) # Using the despine function to remove the axis lines on the left hand side

# Add a title to the figure
plt.suptitle('Mean Measurement Per Species', size=24, color='#4f4e4e') # Setting the overall title of the graph

bar_label(ax_1) # Applying the function to the plot
bar_label(ax_2) # Applying the function to the plot
bar_label(ax_3) # Applying the function to the plot
bar_label(ax_4) # Applying the function to the plot

# Show plot
plt.savefig(os.path.join(exp_path, 'Bar Chart.png')) # Saving the plot to the desired folder
plt.show() # Showing the plot

```

### Histogram - Distribution<a name=hist>

```
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
plt.show() # Showing the plot

```

### Regression Plot<a name=regplot>

```
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
plt.show() # Showing the plot
```
## Output <a name=output>
### Dataset Description<a name=desc>
![description](https://github.com/FDEgan/Iris_Project/assets/157654218/af4a5c9c-7b77-4d37-af8b-4e58799c10b8)

### Bar Chart<a name=barimg>
![Bar Chart](https://github.com/FDEgan/Iris_Project/assets/157654218/feac957c-92ab-4401-96b6-da23e01d53f4)

### Histogram<a name=histimg>
![Histogram](https://github.com/FDEgan/Iris_Project/assets/157654218/37ddfdd2-0bb2-4567-bfdb-d6052b5e2d07)

### Regression Plot<a name=regimg>
![Scatter](https://github.com/FDEgan/Iris_Project/assets/157654218/d0ebb224-cc40-4867-bad0-16a65e230c35)





## Summary of Analysis <a name=summary>

## Future Research <a name=future>



## Contributors <a name=contributors>
- [Barry Egan]([GitHub URL](https://github.com/FDEgan))

## License <a name=license>

Distributed under the MIT License. Please click on below for more information on usage.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
