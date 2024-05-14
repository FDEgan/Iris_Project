# Palmer Penguin Dataset Analysis

## Table of Contents
- [Palmer Penguin Dataset Analysis](#palmer-penguin-dataset-analysis)
  - [Table of Contents](#table-of-contents)
  - [Overview ](#overview-)
  - [Repository Structure ](#repository-structure-)
  - [Aims of the Project: ](#aims-of-the-project-)
  - [Dataset Description ](#dataset-description-)
  - [Tools Used ](#tools-used-)
  - [Code Example ](#code-example-)
    - [Histogram](#histogram)
    - [Bar Chart](#bar-chart)
    - [LM Plot](#lm-plot)
  - [Summary of Analysis ](#summary-of-analysis-)
  - [Future Research ](#future-research-)
  - [Contributors ](#contributors-)
  - [License ](#license-)

## Overview <a name=overview>
This project focuses on analyzing the Palmer Penguin dataset, the dataset is a well-known dataset collated by Dr. Kristen Gorman and the Palmer Station, Antarctica LTER. It is widely used in the data analytics and science communities, for research and studies and is seen as being a natural successor to the Iris dataset by many people. The dataset contains information collected across three islands on three penguin species, namely Adélie, Chinstrap, and Gentoo. The project is broken into three overlapping sections: tasks, project, and a conclusion. 

## Repository Structure <a name=structure>
- `penguins.ipynb`: Jupyter notebook containing all the analysis on the Palmer Penguin dataset.
- `README.md`: Overview of the project and repository.
- `.gitignore`: File to specify untracked files to ignore in the repository.

## Aims of the Project: <a name=aims>
1. **Create Repository**: 
   - Created a GitHub repository with a README.md and a .gitignore.
2. **Data Overview**: 
   - Loaded the Palmer Penguin dataset into the Jupyter notebook.
   - Provided an overview of the dataset and the variables it contains.
3. **Variable Types**:
   - Suggested the types of variables that should be used to model the variables in the data set in Python, explaining the rationale.
4. **Data Visualization**:
   - Created a bar chart of an appropriate variable in the data set.
      - Created a Bar Chart of `bill_length_mm` broken down by `species`.
   - Created a histogram of an appropriate variable in the data set.
      - Created a Histogram of `body_mass_g`.
5. **Correlation Analysis**:
   - Selected two variables from the data set and provided an analysis of how correlated they are.
     - The project focused on the `flipper_length_mm` and `body_mass_g` variables to conduct the correlation analysis.

## Dataset Description <a name=dataset>
- **Dataset Name:** Palmer Penguin Dataset
- **Source:** [Palmer Penguins](https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv)
- **Number of Instances:** 344
- **Number of Attributes:** 7

| Column Name       | Description                                   |
|-------------------|-----------------------------------------------|
| `species`           | The species of penguin                              |
| `island`            | The island where the penguin was found              |
| `bill_length_mm`    | The length of the penguin's bill in millimeters     |
| `bill_depth_mm`     | The depth of the penguin's bill in millimeters      |
| `flipper_length_mm` | The length of the penguin's flipper in millimeters  |
| `body_mass_g`       | The body mass of the penguin in grams               |
| `sex`               | The gender of the penguin                           |

## Tools Used <a name=tools>
- Python
  - Pandas
  - NumPy
  - Matplotlib
  - Seaborn
  - Scipy
  - tabulate
  - warnings

## Code Example <a name=code>
### Histogram<a name=hist>
```
plt.figure(figsize=(8, 8)) # Setting the Figure size
# Creating the Histplot using the data frame originally created
hist = sns.histplot(df, x="body_mass_g", bins=num_bins) # Using Body mass for the basis of the Histogram. Using a bin size determined previously.
plt.yticks([]) # Setting the tick marks to be blank by assigning an empty list.
plt.xlabel('') # Setting the x-axis label to be blank
plt.ylabel('') # Setting the y-axis label to be blank
plt.title('Histogram of Body Mass ', size=18, color='#4f4e4e') # Setting the title of the plot, assigning it a font size of 18 and using a hex color to designate font color.
for i in hist.patches: # Looping through each bar in the histplot.
    # Using the .annotate element to add text to the graph. 
    hist.annotate(format(i.get_height(), '.2f'), # Getting Height of each graph to 2 decimal places
                  # First getting the x-cord of the left hand side and adding the width. Then dividing by 2 to centre where the text should be.
                   (i.get_x() + i.get_width() / 2., i.get_height()), # get_height is used to denote where on the Y axis the text should be
                   ha = 'center', va = 'center', # Aligning the text to be horizontally and vertically centred.
                   size=10, # Setting font size to 10
                   xytext = (0, -14), # Setting coordinates for the text on the x & y axis
                   textcoords = 'offset points') # Offsetting the text in points
sns.despine(left=True) # Using the despine function to remove the axis lines on the left hand side.
plt.grid(False) # Setting the grid to be false to remove the grid lines
plt.show() # Showing the plot`
```
### Bar Chart<a name=bar>

```
plt.figure(figsize=(8, 10)) # Setting Figure size to be 8 by 10 
ax = sns.barplot(x="species", y="bill_length_mm", # Creating a Bar Plot with species on the X axis and bill length on the y axis.
                  errorbar=None,data=df) # Using the data frame I earlier created. Setting Error Bar to None to remove black line at the top of the bar chart.
plt.yticks([]) # Setting the tick marks to be blank by assigning an empty list.
plt.xlabel('') # Setting the x-axis label to be blank
plt.ylabel('') # Setting the y-axis label to be blank
plt.title('Average Bill Length (mm) Per Penguin Species', size=18, color='#4f4e4e') # Setting the title of the plot, assigning it a font size of 18 and using a hex color to designate font color.
# .patches is a common element used with graphical objects in Python.
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
sns.despine(left=True) # Using the despine function to remove the axis lines on the left hand side.
plt.show() # Showing the plot
```

### LM Plot<a name=lm>

```
sns.set_style("white") # Creating a white background and removing grid lines.
lm = sns.lmplot( # Creating the LM Plot.
    # Using the original dat frame I created.
    data=df, x="flipper_length_mm", y="body_mass_g", # Having the Flipper Length on the X-axis & Body Mass on the Y-axis.
    hue="species", # Setting Species to be the colour.
    col="island", # Using the col parameter to create a seperate chart for each Island.
    height=8, # Setting Height to 8.
    aspect=.8, # Setting width to be .8.
    markers= ["x","o","*"] # Adding in different symbols per species.
)
plt.show() # Showing the plot.
```
## Summary of Analysis <a name=summary>

## Future Research <a name=future>



## Contributors <a name=contributors>
- [Barry Egan]([GitHub URL](https://github.com/FDEgan))

## License <a name=license>

Distributed under the MIT License. Please click on below for more information on usage.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
