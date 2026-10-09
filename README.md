🎬 Netflix Customer Churn — Data Analysis Dashboard

An interactive **Exploratory Data Analysis (EDA)** dashboard built with Python to explore customer engagement, subscription patterns, and churn in a Netflix-style customer dataset. Users can upload a CSV or Excel file and explore the data through interactive sections, summary metrics, statistical tables, and visualizations.

**Core technologies:** Python · Streamlit · Pandas · NumPy · Matplotlib · Seaborn

> **Scope:** This repository's dashboard focuses on data analysis and visualization. It helps explore patterns and associations in the dataset; it does not, by itself, prove why customers churn or predict future churn.

---

## 📌 Table of Contents

- [Project Overview](#-project-overview)
- [Problem Statement](#-problem-statement)
- [Project Objectives](#-project-objectives)
- [Key Features](#-key-features)
- [Dashboard Deep Dive](#-dashboard-deep-dive)
- [Technology Stack](#-technology-stack)
- [Dataset Guide](#-dataset-guide)
- [Data Processing Workflow](#-data-processing-workflow)
- [Analysis Methods](#-analysis-methods)
- [Project Structure](#-project-structure)
- [Run the Project Locally](#️-run-the-project-locally)
- [Deploy with Streamlit Community Cloud](#️-deploy-with-streamlit-community-cloud)
- [How to Use the Dashboard](#-how-to-use-the-dashboard)
- [Interpreting Results Responsibly](#️-interpreting-results-responsibly)
- [Troubleshooting](#-troubleshooting)
- [Future Enhancements](#-future-enhancements)
- [Author](#-author)
- [License](#-license)

---

## 📌 Project Overview

Customer churn refers to customers who stop using or renewing a service. For a subscription-based streaming platform, customer engagement, subscription type, payment method, device preference, and viewing habits can all be useful dimensions to investigate.

This project turns a customer dataset into a multi-section analytics dashboard. Instead of manually inspecting rows in a spreadsheet, users can navigate between charts, customer metrics, data-quality checks, and detailed tables.

### 🌐 Project Links

- **Live Dashboard:**  https://netflixcustomerchurndataanalysis.streamlit.app/
- **GitHub Repository:** https://github.com/Rishu6262

## 🎯 Problem Statement

Customer datasets can contain many columns and thousands of records, making it difficult to quickly understand customer behavior and identify segments with different churn rates. A clear, interactive dashboard makes it easier to explore the data, compare groups, and communicate findings.

**This project addresses the analysis problem by providing:**
- A quick overview of the dataset and churn distribution.
- Segment-level comparisons across available customer attributes.
- Visual exploration of engagement behavior and numerical relationships.
- Data-quality checks and potential outlier detection.
- A simple interface that accepts CSV and Excel files.

## 🎯 Project Objectives

1. Inspect dataset structure, data types, missing values, and duplicate rows.
2. Summarize active and churned customers.
3. Explore distributions of customer and engagement variables.
4. Compare churn rates across subscription, region, payment, device, and genre categories when those fields are available.
5. Investigate relationships between engagement variables and churn status.
6. Flag potential numerical outliers using the Interquartile Range (IQR) method.
7. Present the analysis through a clean, navigable Streamlit interface.

## ✨ Key Features

- **Upload your own data:** supports CSV and Excel files.
- **Interactive navigation:** switch between dashboard sections from the sidebar.
- **KPI overview:** customer counts, churn rate, and average watch hours.
- **Customer segmentation:** compare churn across relevant categories.
- **Engagement analysis:** explore watch hours, last login, age, and daily watch time.
- **Correlation analysis:** view relationships between numerical columns.
- **Outlier exploration:** inspect IQR-based outlier counts and boxplots.
- **Data explorer:** inspect records, column types, and statistical summaries.
- **Netflix-inspired styling:** custom CSS creates a dark, streaming-dashboard visual theme.

---

## 📊 Dashboard Deep Dive

### 1. 🏠 Overview

The Overview section provides a high-level snapshot of the uploaded dataset.

**What it displays**
- Total number of customer records.
- Number of churned customers.
- Number of active customers.
- Overall churn rate.
- Average watch hours, when the relevant column exists.
- Dataset dimensions, missing-value checks, and duplicate-row checks.
- Churn distribution charts.
- A statistical summary of available columns.

**Questions this section helps explore**
- How many customer records are in the dataset?
- What proportion of customers are marked as churned?
- Are there missing values or duplicate records to investigate?
- How are active and churned records distributed?

### 2. 📈 Distributions

This section explores the distribution of numerical and demographic fields.

**Visualizations may include**
- Age histogram with a Kernel Density Estimate (KDE).
- Watch-hours histogram with KDE.
- Age distribution by gender using a boxplot.

**Why it matters:** distribution plots help reveal concentration, spread, skewness, and unusual values before deeper comparisons are made.

### 3. 🎯 Churn Analysis

This section compares churn patterns across available customer categories.

**Possible comparisons**
- Subscription type vs. churn.
- Churn rate by region.
- Churn rate by payment method.
- Device type vs. churn.
- Favorite genre vs. churn rate.

**Questions to investigate**
- Do churn rates differ between subscription groups?
- Are some regions associated with higher churn in this dataset?
- Does churn vary across payment methods or device types?
- Are there differences across favorite-genre groups?

These comparisons show associations in the uploaded data. They do not establish the reason for a customer's decision to leave.

### 4. 👥 Customer Behavior

This section compares customer characteristics and engagement metrics against churn status.

**Analyses may include**
- Watch hours by churn status.
- Age by churn status.
- Average daily watch time by churn status.
- Additional boxplots across available customer segments.

**Why it matters:** side-by-side comparisons can help identify differences in distributions, medians, spread, and potential outliers between active and churned groups.

### 5. 🔗 Relationships

This section explores how numerical variables move in relation to one another.

**Visualizations may include**
- Age vs. watch hours.
- Last login days vs. watch hours.
- Last login days vs. average daily watch time.
- Correlation heatmap for numerical columns.
- Numerical feature comparisons by churn status.

**How to read it**
- A scatter plot can reveal trends, clusters, and unusual observations.
- A correlation heatmap summarizes pairwise linear relationships.
- Correlation does not imply causation, and a weak linear correlation does not rule out every possible relationship.

### 6. 🚨 Outlier Analysis

The dashboard uses the Interquartile Range (IQR) rule to flag potential outliers in selected numerical columns.

For a numerical feature:

```text
IQR = Q3 - Q1
Lower Bound = Q1 - 1.5 × IQR
Upper Bound = Q3 + 1.5 × IQR
```

Values below the lower bound or above the upper bound are flagged as potential outliers.

**What this section helps inspect**
- Number of potential outliers in selected columns.
- Quartiles and IQR-based thresholds.
- Boxplots for watch hours and average daily watch time when those columns are available.

**Important:** an outlier is not automatically incorrect. It may represent a valid customer behavior, a data-entry issue, or a special case. Investigate it before deciding whether to keep, transform, or remove it.

### 7. 📋 Data Explorer

The Data Explorer gives users a closer look at the uploaded dataset.

**It can include**
- A preview of the raw records.
- Column names and data types.
- Missing-value and unique-value counts.
- Descriptive statistics.

This section is useful for checking data quality and understanding what each column contains before interpreting charts.

---

## 🧰 Technology Stack

| Technology | Role in the Project |
|---|---|
| **Python** | Main programming language |
| **Streamlit** | Dashboard layout, navigation, upload controls, metrics, and tables |
| **Pandas** | Loading files, cleaning columns, transforming data, grouping, and summaries |
| **NumPy** | Numerical computing support |
| **Matplotlib** | Figure creation and chart display |
| **Seaborn** | Statistical plots such as histograms, boxplots, count plots, and heatmaps |
| **OpenPyXL** | Excel `.xlsx` file support |

### Why Streamlit?

Streamlit allows the dashboard interface and data-analysis workflow to be built primarily in Python. This makes it convenient to connect data loading, transformations, charts, and interactive controls without creating a separate frontend application for this EDA dashboard.

---

## 📁 Dataset Guide

### Required target column

The dashboard requires a column named `churned`:

| Value | Meaning |
|---:|---|
| `0` | Active |
| `1` | Churned |

The churn-rate calculation assumes the target is represented numerically using `0` and `1`.

### Expected columns

For the broadest set of dashboard views, the dataset may contain these columns:

| Column | Description |
|---|---|
| `customer_id` | Customer identifier |
| `age` | Customer age |
| `gender` | Gender category |
| `subscription_type` | Subscription plan or category |
| `watch_hours` | Total or recorded watch hours, according to the dataset definition |
| `last_login_days` | Days since the customer's last login |
| `region` | Customer region |
| `device` | Device category |
| `monthly_fee` | Monthly subscription fee |
| `payment_method` | Payment method category |
| `number_of_profiles` | Number of profiles associated with the account |
| `avg_watch_time_per_day` | Average daily watch time |
| `favorite_genre` | Favorite content genre |
| `churned` | Binary churn label (`0` = Active, `1` = Churned) |

Column definitions should be confirmed against the actual dataset documentation. In particular, the meaning and units of viewing-time fields depend on the dataset source.

### Supported file formats

- `.csv`
- `.xlsx`
- `.xls`

Individual charts may require specific columns. A chart may not be available if its input columns are missing.

---

## 🔄 Data Processing Workflow

The dashboard follows this general flow:

```text
User opens the Streamlit app
            ↓
Uploads CSV or Excel file
            ↓
Pandas reads the file into a DataFrame
            ↓
Column cleanup and basic validation
            ↓
Prepare churn labels (0 = Active, 1 = Churned)
            ↓
User selects a dashboard section
            ↓
Pandas summaries + Matplotlib/Seaborn visualizations
            ↓
Charts, metrics, and tables appear in the dashboard
```

### Main processing concepts

- **File loading:** CSV files are read with `pandas.read_csv`; Excel files are read with `pandas.read_excel`.
- **Basic cleanup:** accidental unnamed columns may be removed.
- **Target validation:** the dashboard checks for the required `churned` column.
- **Label preparation:** numeric churn values are mapped to readable labels for charts.
- **Summary calculations:** grouped counts, rates, and descriptive statistics support the dashboard.
- **Visualization:** Matplotlib and Seaborn are used to create figures displayed in Streamlit.
- **Caching:** `st.cache_data` is used for the data-loading function to reduce repeated loading work for the same cached input.

This is an EDA workflow, not a machine-learning training pipeline.

---

## 📐 Analysis Methods

| Method | Purpose |
|---|---|
| Descriptive statistics | Summarize numerical and categorical columns |
| Missing-value checks | Identify fields with incomplete records |
| Duplicate-row checks | Flag repeated records for investigation |
| Histograms and KDE | Understand numerical distributions |
| Count plots and bar charts | Compare category counts and group-level rates |
| Boxplots | Compare medians, spread, and potential outliers |
| Scatter plots | Explore relationships between numerical features |
| Correlation heatmap | Summarize pairwise numerical correlations |
| IQR rule | Flag potential numerical outliers |
| Grouped churn-rate analysis | Compare the proportion marked as churned across groups |

### Churn rate

When `churned` is a numeric binary column coded as `0` and `1`, the overall churn rate can be calculated as:

```text
Churn Rate (%) = Mean(churned) × 100
```

For a group of customers, the same calculation can be applied to that group's `churned` values.

---

## 🗂️ Suggested Project Structure

A simple repository structure for the dashboard is:

```text
netflix-customer-churn-analysis/
├── streamlitApp.py
├── requirements.txt
├── README.md
├── Netflix_Customer_Churn.ipynb
└── data/
    └── README.md
```

Your actual repository may contain additional files. If the dataset is uploaded through the dashboard, you do not need to commit it to GitHub unless you have permission to share it and it is appropriate to publish.

### Example `requirements.txt`

```text
streamlit
pandas
numpy
matplotlib
seaborn
openpyxl
```

---

## ⚙️ Run the Project Locally

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd YOUR_REPOSITORY_FOLDER
```

Replace the placeholders with your real repository URL and folder name.

### 2. Create a virtual environment

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks environment activation, you can still run Python and pip through the environment's executable path, or use a terminal where activation is permitted.

### 3. Install dependencies

Create a `requirements.txt` file with the packages shown above, then run:

```bash
python -m pip install -r requirements.txt
```

### 4. Start Streamlit

If the dashboard file is named `streamlitApp.py`, run:

```bash
python -m streamlit run streamlitApp.py
```

Open the local URL printed in the terminal. Streamlit commonly uses:

```text
http://localhost:8501
```

---

## ☁️ Deploy with Streamlit Community Cloud

1. Ensure `streamlitApp.py` and `requirements.txt` are committed to GitHub.
2. Visit [Streamlit Community Cloud](https://streamlit.io/cloud).
3. Create a new app and connect the GitHub repository.
4. Select the correct repository branch.
5. Set the main file path to `streamlitApp.py`.
6. Deploy and test the public app URL.

**Deployment checklist**
- Check that package names in `requirements.txt` match the imports.
- Confirm the main file path and capitalization.
- Test the dashboard with a valid CSV or Excel file.
- Do not commit secrets or private customer data.
- Add the final deployment URL to the Live Dashboard section above.

---

## 💡 How to Use the Dashboard

1. Open the deployed dashboard or run it locally.
2. Upload a CSV or Excel dataset from the sidebar.
3. Choose a section from the **Go to** navigation menu.
4. Review the metrics, charts, and tables.
5. Compare churn rates across groups, where relevant columns are available.
6. Use the Data Explorer and quality checks to validate the dataset before drawing conclusions.
7. Record important observations with the population, metric, and segment clearly identified.

---

## ⚠️ Interpreting Results Responsibly

- **Association is not causation:** a higher churn rate in one segment does not explain why customers left.
- **Data quality matters:** missing values, duplicate rows, incorrect types, and inconsistent labels can affect analysis.
- **Check group sizes:** a rate based on a small group can be unstable.
- **Understand units:** confirm whether viewing fields represent hours, minutes, totals, or daily averages.
- **Outliers need context:** do not remove them automatically.
- **Correlation has limits:** the heatmap mainly describes linear association between numerical variables.
- **Dataset scope matters:** results reflect the uploaded data and may not represent all Netflix customers or actual Netflix operations.
- **No predictive claims:** this EDA dashboard does not forecast future churn unless a separate validated predictive model is explicitly added.

---

## 🧯 Troubleshooting

### `streamlit` is not recognized

Try running Streamlit as a Python module:

```bash
python -m streamlit run streamlitApp.py
```

### `ModuleNotFoundError`

Install dependencies in the same Python environment used to run the dashboard:

```bash
python -m pip install -r requirements.txt
```

### The dashboard asks for a dataset

Upload a supported CSV or Excel file through the sidebar.

### Required column error

Confirm that the uploaded dataset contains a column named exactly `churned` and that its values use numeric `0` and `1` encoding.

### Some charts are missing or fail

Some visualizations require particular columns. Check the dataset column names and data types, and ensure that the relevant columns contain usable values.

### Excel file cannot be read

Install Excel support:

```bash
python -m pip install openpyxl
```

---

## 🔮 Future Enhancements

- Add interactive filters for subscription type, region, device, and other categories.
- Add export options for filtered data and selected charts.
- Add automated summaries of notable EDA findings.
- Add statistical tests for selected group comparisons.
- Improve validation for unexpected target labels, invalid numeric values, and missing required columns.
- Add dashboard screenshots and a sample dataset with permission to share.
- Improve accessibility and responsive layout for smaller screens.

---

## 👨‍💻 Author

**Rishu Gurjar**  
B.Tech Student | Python | Data Analysis | Machine Learning




