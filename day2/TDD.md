# GitHub Copilot for Python Development Exercise

## Data Analysis Tool with Pandas and Visualization

### Objective

Create a Python data analysis tool that processes CSV datasets, performs statistical analysis, and generates visualizations using Pandas, Matplotlib, and Seaborn with GitHub Copilot assisting your development process.

### Setup

1. Create a new directory: `data-analyzer`
2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install required packages:
   ```bash
   pip install pandas matplotlib seaborn pytest jupyter
   ```
4. Create the project structure:

   ```
   data-analyzer/
   ├── data/
   │   └── sample_data.csv
   ├── src/
   │   ├── __init__.py
   │   ├── data_loader.py
   │   ├── analyzer.py
   │   └── visualizer.py
   ├── tests/
   │   ├── __init__.py
   │   ├── test_data_loader.py
   │   ├── test_analyzer.py
   │   └── test_visualizer.py
   └── main.py
   ```

5. Create a sample CSV file in the data directory with the following content:

```csv
date,category,amount,customer_id
2023-01-05,groceries,124.56,C001
2023-01-08,electronics,899.99,C002
2023-01-10,groceries,75.25,C003
2023-01-15,clothing,149.99,C001
2023-01-20,electronics,450.00,C004
2023-01-22,groceries,65.75,C002
2023-01-25,clothing,89.99,C003
2023-01-28,groceries,112.34,C001
2023-02-01,electronics,1299.99,C004
2023-02-05,groceries,94.55,C002
2023-02-10,clothing,199.99,C001
2023-02-15,groceries,87.25,C003
2023-02-20,electronics,349.99,C002
2023-02-25,groceries,132.45,C004
2023-03-01,clothing,79.99,C003
```

### Exercise Steps

#### 1. Implement Data Loader

Open `data_loader.py` and add:

```python
# Create a DataLoader class that:
# - Loads CSV files into pandas DataFrames
# - Validates the data (checks for required columns, handles missing values)
# - Performs basic data cleaning (date parsing, type conversion)
# - Has methods for filtering data by date range and categories
```

Let Copilot help you implement the class, then review and adjust as needed.

#### 2. Implement Data Analysis

Open `analyzer.py` and add:

```python
# Create a DataAnalyzer class that takes a DataFrame and provides:
# - Summary statistics (mean, median, std dev by category)
# - Time series analysis (spending trends over time)
# - Spending distribution analysis
# - Top spending categories
# - Customer segmentation by spending patterns
```

Use Copilot to help implement these methods. Pay attention to how Copilot suggests handling the various analytical tasks.

#### 3. Implement Visualization

Open `visualizer.py` and add:

```python
# Create a DataVisualizer class that takes analysis results and generates:
# - Bar charts for spending by category
# - Line charts for spending over time
# - Pie charts for spending distribution
# - Heatmaps for correlation between variables
# - Each method should support customization options (colors, titles, etc.)
# - Methods should return the figure and also have an option to save to file
```

Let Copilot help implement the visualization functions. Add comments to guide it toward creating clean, properly labeled visualizations.

#### 4. Create Tests

Open the test files and add:

```python
# Write tests for the DataLoader class:
# - Test that data is loaded correctly
# - Test validation of required columns
# - Test date filtering functionality
# - Test category filtering functionality
```

Repeat with similar comments for the other test files. Use Copilot to help generate appropriate test cases.

#### 5. Implement Main Application

Open `main.py` and add:

```python
# Create a command-line interface that:
# - Takes a CSV file path as input
# - Allows selecting analysis type (summary, time-series, category, etc.)
# - Allows selecting visualization type
# - Supports saving results to files
# - Has a help menu explaining functionality
```

Let Copilot help implement the command-line interface. Check that it integrates all the components properly.

#### 6. Test and Improve

Run your application:

```bash
python main.py data/sample_data.csv --analysis summary --plot bar --output results
```

Use Copilot to help fix any issues that arise, by adding comments describing the problems.

### Bonus Challenges (Optional)

If you finish early, try implementing one of these features with Copilot's help:

1. Add export functionality to different formats (Excel, JSON, etc.)
2. Implement predictive analysis for future spending trends
3. Add interactive visualizations using Plotly
4. Implement a simple web interface using Flask or Streamlit
