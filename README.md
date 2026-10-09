🎬 Netflix Customer Churn — Data Analysis Dashboard

live link : https://netflixcustomerchurndataanalysis.streamlit.app/

An interactive **Exploratory Data Analysis (EDA)** dashboard built with Python to explore Netflix customer behavior and patterns associated with customer churn. The dashboard uses **Streamlit, Pandas, NumPy, Matplotlib, and Seaborn**.

> **Project focus:** Data analysis and visualization. Observed patterns are not proof of causation or guaranteed outcomes.

## 🚀 Live Demo

- **Streamlit Dashboard:** https://netflixcustomerchurndataanalysis.streamlit.app/
- **GitHub Repository:** https://github.com/Rishu6262

## 📌 Project Overview

Customer churn occurs when customers stop using or renewing a service. This project provides an interactive dashboard where users can upload a CSV or Excel dataset and explore customer information through summary metrics, statistical tables, and visualizations.

## 🎯 Objectives

- Understand dataset structure and quality.
- Explore customer and subscription distributions.
- Compare churn patterns across customer segments.
- Examine relationships between engagement metrics and churn.
- Identify potential outliers using the IQR method.
- Present findings in an easy-to-navigate dashboard.

## 🧰 Tech Stack

| Tool / Library | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Interactive dashboard UI |
| Pandas | Data loading, grouping, manipulation, and summaries |
| NumPy | Numerical computing |
| Matplotlib | Plot creation and customization |
| Seaborn | Statistical visualizations |
| OpenPyXL | Reading Excel `.xlsx` files |

## 📊 Dashboard Sections

### 1. Overview
- Total customers, active customers, and churned customers
- Overall churn rate and average watch hours
- Missing-value and duplicate-row checks
- Dataset shape and statistical summary
- Churn distribution charts

### 2. Distributions
- Age distribution with histogram and KDE
- Watch-hours distribution
- Age distribution by gender

### 3. Churn Analysis
- Churn by subscription type
- Churn rate by region
- Churn rate by payment method
- Customer churn by device
- Churn rate by favorite genre

### 4. Customer Behavior
- Watch hours compared with churn status
- Age compared with churn status
- Average daily watch time compared with churn
- Comparisons by subscription, region, payment method, and device

### 5. Relationships
- Age vs. watch hours
- Last login days vs. watch hours
- Last login days vs. average daily watch time
- Correlation heatmap for numerical variables
- Numerical feature comparisons by churn status

### 6. Outlier Analysis
- IQR-based outlier summary
- Quartiles, IQR, lower/upper bounds, and outlier counts
- Boxplots for watch hours and average daily watch time when those columns exist

### 7. Data Explorer
- Dataset preview
- Column data types
- Missing-value and unique-value counts
- Statistical description

## 📁 Expected Dataset Columns

The dashboard requires a target column named `churned`, coded as:
- `0` = Active
- `1` = Churned

For the full set of visualizations, the dataset can include:

```text
customer_id
age
gender
subscription_type
watch_hours
last_login_days
region
device
monthly_fee
payment_method
number_of_profiles
avg_watch_time_per_day
favorite_genre
churned
```

Individual visualizations depend on the presence of their relevant columns. Upload a CSV or Excel file using the sidebar to begin.

## ⚙️ Run Locally

### 1. Clone your repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd YOUR_REPOSITORY_FOLDER
```

Replace the placeholders with your actual repository URL and folder name.

### 2. Create a virtual environment (recommended)

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Create `requirements.txt`

```text
streamlit
pandas
numpy
matplotlib
seaborn
openpyxl
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

### 4. Run the dashboard

If your main file is named `streamlitApp.py`:

```bash
python -m streamlit run streamlitApp.py
```

The terminal will show a local URL, usually `http://localhost:8501`.

## ☁️ Deploy on Streamlit Community Cloud

1. Push `streamlitApp.py` and `requirements.txt` to GitHub.
2. Open [Streamlit Community Cloud](https://streamlit.io/cloud).
3. Create a new app and connect your repository.
4. Select the correct branch.
5. Set **Main file path** to `streamlitApp.py`.
6. Deploy the app.

## 📈 Analytical Methods

- Descriptive statistics
- Missing-value and duplicate checks
- Histograms and KDE plots
- Count plots and bar plots
- Boxplots
- Scatter plots
- Correlation heatmap
- IQR-based outlier detection
- Grouped churn-rate comparisons

### IQR method

```text
IQR = Q3 - Q1
Lower Bound = Q1 - 1.5 × IQR
Upper Bound = Q3 + 1.5 × IQR
```

Values outside these bounds are flagged as potential outliers. An outlier is not automatically an error and should be investigated before removal.

## 💡 How to Use

1. Open the dashboard.
2. Upload a CSV or Excel dataset in the sidebar.
3. Select a section from the sidebar navigation.
4. Review charts, summary metrics, and tables.
5. Use the results to formulate data-supported observations.

## ⚠️ Interpretation Notes

- Churn-rate comparisons show associations in the dataset; they do not prove causation.
- Correlation does not establish cause and effect.
- Outliers should not be removed automatically without understanding the data.
- Results depend on the quality and representativeness of the uploaded dataset.
- The app expects `churned` to use numeric `0` and `1` values for the Active/Churned labels and churn-rate calculations.

## 🔮 Future Improvements

- Add filters for subscription, region, and device.
- Add downloadable filtered data and chart exports.
- Add automated insight summaries.
- Add statistical significance testing for selected comparisons.
- Improve validation for unexpected category labels and missing required columns.

## 👨‍💻 Author

**Rishu Gurjar**  
B.Tech Student | Python | Data Analysis | Machine Learning

- **GitHub:** Add your GitHub profile URL.
- **LinkedIn:** Add your LinkedIn profile URL.

## 📄 License

Choose a license before publishing this repository. For example, add an MIT `LICENSE` file if you want others to reuse the project under the MIT License.
'''
path = Path("/mnt/data/README.md")
path.write_text(readme, encoding="utf-8")
print(f"Created: {path}")
