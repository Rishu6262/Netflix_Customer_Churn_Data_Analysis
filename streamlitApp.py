import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="Netflix Customer Churn Analytics",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# GLOBAL STYLE
# ============================================================
sns.set_theme(style="whitegrid")

st.markdown("""
<style>
    /* Main background */
    .stApp {
        background: #08090c;
    }

    /* Main content width */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1500px;
    }

    /* Headings */
    h1, h2, h3 {
        color: #ffffff !important;
    }

    /* Normal text */
    p, label, .stMarkdown, .stCaption {
        color: #d5d5d5;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: #0d0f14;
        border-right: 1px solid #252936;
    }

    /* Metric cards */
    div[data-testid="stMetric"] {
        background: linear-gradient(145deg, #12151c, #0c0e13);
        border: 1px solid #292d38;
        border-radius: 16px;
        padding: 18px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.25);
    }

    div[data-testid="stMetric"] label {
        color: #9da3b0 !important;
    }

    div[data-testid="stMetricValue"] {
        color: #ffffff !important;
    }

    /* Streamlit bordered containers */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        border: 1px solid #2a2e39 !important;
        border-radius: 18px !important;
        background: linear-gradient(145deg, #101319, #0b0d12);
        box-shadow: 0 10px 35px rgba(0,0,0,0.22);
    }

    /* Tabs */
    button[data-baseweb="tab"] {
        color: #aeb4c0 !important;
    }

    button[data-baseweb="tab"][aria-selected="true"] {
        color: #ffffff !important;
    }

    /* Buttons */
    .stButton > button {
        border-radius: 10px;
        border: 1px solid #3a3f4c;
    }

    /* Info boxes */
    .insight-box {
        padding: 16px 18px;
        border-left: 4px solid #e50914;
        background: #12151b;
        border-radius: 0 12px 12px 0;
        margin-top: 8px;
        margin-bottom: 12px;
    }

    .section-title {
        padding: 12px 16px;
        border: 1px solid #292d38;
        border-radius: 14px;
        background: #0f1218;
        margin: 10px 0 18px 0;
    }

    .small-note {
        color: #8f96a3;
        font-size: 0.85rem;
    }
</style>
""", unsafe_allow_html=True)


# ============================================================
# HELPERS
# ============================================================
@st.cache_data
def load_data(uploaded_file):
    """Load CSV/XLSX data."""
    if uploaded_file is None:
        return None

    name = uploaded_file.name.lower()

    if name.endswith(".csv"):
        data = pd.read_csv(uploaded_file)
    elif name.endswith(".xlsx") or name.endswith(".xls"):
        data = pd.read_excel(uploaded_file)
    else:
        raise ValueError("Please upload a CSV or Excel file.")

    # Remove accidental Excel index columns
    unwanted = [c for c in data.columns if str(c).lower().startswith("unnamed")]
    if unwanted:
        data = data.drop(columns=unwanted)

    return data


def prepare_data(data):
    """Small, safe preparation without changing the original analysis."""
    data = data.copy()

    if "churned" not in data.columns:
        raise ValueError(
            "The dataset must contain a 'churned' column."
        )

    data["churned"] = pd.to_numeric(data["churned"], errors="coerce")

    if "customer_id" in data.columns:
        # Keep it in the raw dataframe, but it is not used for analysis.
        pass

    data["churn_label"] = data["churned"].map({
        0: "Active",
        1: "Churned"
    })

    return data


def show_fig(fig):
    """Render matplotlib figure and close it."""
    st.pyplot(fig, use_container_width=True)
    plt.close(fig)


def finish_fig(fig):
    """Common finishing touches."""
    fig.tight_layout()
    show_fig(fig)


def safe_rate(series):
    return (series.mean() * 100)


def numeric_columns(data):
    cols = [
        "age",
        "watch_hours",
        "last_login_days",
        "monthly_fee",
        "number_of_profiles",
        "avg_watch_time_per_day"
    ]
    return [c for c in cols if c in data.columns]


# ============================================================
# SIDEBAR
# ============================================================
st.sidebar.markdown("# 🎬 Netflix Analytics")
st.sidebar.markdown(
    "<div class='small-note'>Customer Churn • Exploratory Data Analysis</div>",
    unsafe_allow_html=True
)

uploaded_file = st.sidebar.file_uploader(
    "Upload dataset",
    type=["csv", "xlsx", "xls"],
    help="Upload your Netflix customer churn dataset."
)

st.sidebar.markdown("---")
st.sidebar.markdown("### Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "🏠 Overview",
        "📊 Distributions",
        "🎯 Churn Analysis",
        "👥 Customer Behavior",
        "🔗 Relationships",
        "🚨 Outlier Analysis",
        "📋 Data Explorer"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown(
    """
    **Libraries**

    🐼 Pandas  
    🔢 NumPy  
    📈 Matplotlib  
    🎨 Seaborn
    """
)


# ============================================================
# LOAD DATA
# ============================================================
if uploaded_file is None:
    st.warning(
        "Upload `netflix_customer_churn.csv` from the sidebar to start the dashboard."
    )
    st.stop()

try:
    df = prepare_data(load_data(uploaded_file))
except Exception as e:
    st.error(f"Could not load the dataset: {e}")
    st.stop()


# ============================================================
# HEADER
# ============================================================
st.markdown(
    """
    <div style="
        padding: 25px 28px;
        border: 1px solid #2a2e39;
        border-radius: 22px;
        background: linear-gradient(135deg, #11141b, #090a0e);
        margin-bottom: 22px;
    ">
        <div style="font-size: 0.78rem; letter-spacing: 3px; color: #e50914;">
            NETFLIX CUSTOMER INTELLIGENCE
        </div>
        <h1 style="margin: 8px 0 4px 0;">
            Customer Churn Analytics
        </h1>
        <div style="color:#9da3b0;">
            Interactive EDA dashboard built with Pandas, NumPy, Matplotlib and Seaborn.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# OVERVIEW
# ============================================================
if page == "🏠 Overview":

    st.markdown(
        "<div class='section-title'><h2>📌 Dataset Snapshot</h2></div>",
        unsafe_allow_html=True
    )

    total_customers = len(df)
    churned_customers = int((df["churned"] == 1).sum())
    active_customers = int((df["churned"] == 0).sum())
    churn_rate = safe_rate(df["churned"])

    c1, c2, c3, c4, c5 = st.columns(5)

    c1.metric("👥 Customers", f"{total_customers:,}")
    c2.metric("🔴 Churned", f"{churned_customers:,}")
    c3.metric("🟢 Active", f"{active_customers:,}")
    c4.metric("📉 Churn Rate", f"{churn_rate:.2f}%")

    if "watch_hours" in df:
        c5.metric("🎬 Avg Watch Hours", f"{df['watch_hours'].mean():.2f}")

    st.markdown("<br>", unsafe_allow_html=True)

    # Data quality
    q1, q2, q3 = st.columns(3)

    with q1:
        with st.container(border=True):
            st.subheader("🧹 Missing Values")
            missing = int(df.isna().sum().sum())
            st.metric("Total missing cells", f"{missing:,}")

    with q2:
        with st.container(border=True):
            st.subheader("♻️ Duplicate Rows")
            duplicates = int(df.duplicated().sum())
            st.metric("Duplicate rows", f"{duplicates:,}")

    with q3:
        with st.container(border=True):
            st.subheader("🧱 Dataset Shape")
            st.metric("Rows", f"{df.shape[0]:,}")
            st.metric("Columns", f"{df.shape[1]:,}")

    st.markdown("<br>", unsafe_allow_html=True)

    # Churn distribution
    with st.container(border=True):
        st.subheader("🎯 Customer Churn Distribution")

        col1, col2 = st.columns(2)

        with col1:
            fig, ax = plt.subplots(figsize=(7, 5))
            sns.countplot(
                data=df,
                x="churn_label",
                ax=ax
            )
            ax.set_title("Active vs Churned Customers", fontsize=14, fontweight="bold")
            ax.set_xlabel("Customer Status")
            ax.set_ylabel("Number of Customers")
            ax.grid(axis="y", alpha=0.2)
            finish_fig(fig)

        with col2:
            counts = df["churned"].value_counts().sort_index()
            labels = ["Active", "Churned"]

            fig, ax = plt.subplots(figsize=(7, 5))
            ax.pie(
                counts.values,
                labels=labels,
                autopct="%1.2f%%",
                startangle=90,
                wedgeprops={"edgecolor": "white", "linewidth": 1.2}
            )
            ax.set_title("Customer Churn Composition", fontsize=14, fontweight="bold")
            finish_fig(fig)

    st.markdown("<br>", unsafe_allow_html=True)

    with st.container(border=True):
        st.subheader("📋 Quick Statistical Summary")
        st.dataframe(
            df.describe(include="all").T,
            use_container_width=True
        )


# ============================================================
# DISTRIBUTIONS
# ============================================================
elif page == "📊 Distributions":

    st.markdown(
        "<div class='section-title'><h2>📊 Distribution Analysis</h2></div>",
        unsafe_allow_html=True
    )

    # Age
    with st.container(border=True):
        st.subheader("👤 Age Distribution")

        fig, ax = plt.subplots(figsize=(11, 5))
        sns.histplot(
            data=df,
            x="age",
            bins=20,
            kde=True,
            ax=ax
        )
        ax.set_title("Age Distribution with KDE", fontsize=15, fontweight="bold")
        ax.set_xlabel("Age")
        ax.set_ylabel("Customers")
        finish_fig(fig)

    # Watch hours
    with st.container(border=True):
        st.subheader("🎬 Watch Hours Distribution")

        fig, ax = plt.subplots(figsize=(11, 5))
        sns.histplot(
            data=df,
            x="watch_hours",
            bins=30,
            kde=True,
            ax=ax
        )
        ax.set_title("Watch Hours Distribution with KDE", fontsize=15, fontweight="bold")
        ax.set_xlabel("Watch Hours")
        ax.set_ylabel("Customers")
        finish_fig(fig)

    # Age by gender
    with st.container(border=True):
        st.subheader("⚥ Age Distribution by Gender")

        fig, ax = plt.subplots(figsize=(11, 5))
        sns.boxplot(
            data=df,
            x="gender",
            y="age",
            ax=ax
        )
        ax.set_title("Age vs Gender", fontsize=15, fontweight="bold")
        ax.set_xlabel("Gender")
        ax.set_ylabel("Age")
        finish_fig(fig)


# ============================================================
# CHURN ANALYSIS
# ============================================================
elif page == "🎯 Churn Analysis":

    st.markdown(
        "<div class='section-title'><h2>🎯 Churn Analysis</h2></div>",
        unsafe_allow_html=True
    )

    # Subscription
    if "subscription_type" in df.columns:
        with st.container(border=True):
            st.subheader("💳 Customer Churn by Subscription Type")

            fig, ax = plt.subplots(figsize=(11, 5))
            sns.countplot(
                data=df,
                x="subscription_type",
                hue="churn_label",
                ax=ax
            )
            ax.set_title(
                "Customer Churn by Subscription Type",
                fontsize=15,
                fontweight="bold"
            )
            ax.set_xlabel("Subscription Type")
            ax.set_ylabel("Customers")
            finish_fig(fig)

            subscription_rate = (
                df.groupby("subscription_type")["churned"]
                .mean()
                .sort_values(ascending=False)
                .mul(100)
            )

            st.markdown("**Churn rate by subscription:**")
            st.dataframe(
                subscription_rate.rename("Churn Rate (%)").round(2),
                use_container_width=True
            )

    # Region
    if "region" in df.columns:
        with st.container(border=True):
            st.subheader("🌍 Churn Rate by Region")

            region_rate = (
                df.groupby("region")["churned"]
                .mean()
                .sort_values(ascending=False)
                .mul(100)
            )

            fig, ax = plt.subplots(figsize=(11, 5))
            sns.barplot(
                x=region_rate.values,
                y=region_rate.index,
                ax=ax
            )
            ax.set_title(
                "Churn Rate by Region",
                fontsize=15,
                fontweight="bold"
            )
            ax.set_xlabel("Churn Rate (%)")
            ax.set_ylabel("Region")
            finish_fig(fig)

    # Payment
    if "payment_method" in df.columns:
        with st.container(border=True):
            st.subheader("💰 Churn Rate by Payment Method")

            payment_rate = (
                df.groupby("payment_method")["churned"]
                .mean()
                .sort_values(ascending=False)
                .mul(100)
            )

            fig, ax = plt.subplots(figsize=(11, 5))
            sns.barplot(
                x=payment_rate.values,
                y=payment_rate.index,
                ax=ax
            )
            ax.set_title(
                "Churn Rate by Payment Method",
                fontsize=15,
                fontweight="bold"
            )
            ax.set_xlabel("Churn Rate (%)")
            ax.set_ylabel("Payment Method")
            finish_fig(fig)

    # Device
    if "device" in df.columns:
        with st.container(border=True):
            st.subheader("📱 Customer Churn by Device")

            fig, ax = plt.subplots(figsize=(11, 5))
            sns.countplot(
                data=df,
                x="device",
                hue="churn_label",
                ax=ax
            )
            ax.set_title(
                "Customer Churn by Device",
                fontsize=15,
                fontweight="bold"
            )
            ax.set_xlabel("Device")
            ax.set_ylabel("Customers")
            finish_fig(fig)

    # Genre
    if "favorite_genre" in df.columns:
        with st.container(border=True):
            st.subheader("🎭 Churn by Favorite Genre")

            genre_rate = (
                df.groupby("favorite_genre")["churned"]
                .mean()
                .sort_values(ascending=False)
                .mul(100)
            )

            fig, ax = plt.subplots(figsize=(11, 5))
            sns.barplot(
                x=genre_rate.values,
                y=genre_rate.index,
                ax=ax
            )
            ax.set_title(
                "Churn Rate by Favorite Genre",
                fontsize=15,
                fontweight="bold"
            )
            ax.set_xlabel("Churn Rate (%)")
            ax.set_ylabel("Favorite Genre")
            finish_fig(fig)


# ============================================================
# CUSTOMER BEHAVIOR
# ============================================================
elif page == "👥 Customer Behavior":

    st.markdown(
        "<div class='section-title'><h2>👥 Customer Behavior Analysis</h2></div>",
        unsafe_allow_html=True
    )

    # Watch hours vs churn
    with st.container(border=True):
        st.subheader("🎬 Watch Hours vs Churn")

        col1, col2 = st.columns(2)

        with col1:
            fig, ax = plt.subplots(figsize=(7, 5))
            sns.boxplot(
                data=df,
                x="churn_label",
                y="watch_hours",
                ax=ax
            )
            ax.set_title("Watch Hours vs Churn", fontweight="bold")
            ax.set_xlabel("Customer Status")
            ax.set_ylabel("Watch Hours")
            finish_fig(fig)

        with col2:
            avg_watch = df.groupby("churn_label")["watch_hours"].mean().sort_values()

            fig, ax = plt.subplots(figsize=(7, 5))
            sns.barplot(
                x=avg_watch.index,
                y=avg_watch.values,
                ax=ax
            )
            ax.set_title("Average Watch Hours by Churn Status", fontweight="bold")
            ax.set_xlabel("Customer Status")
            ax.set_ylabel("Average Watch Hours")
            finish_fig(fig)

    # Age vs churn
    with st.container(border=True):
        st.subheader("👤 Age vs Churn")

        col1, col2 = st.columns(2)

        with col1:
            fig, ax = plt.subplots(figsize=(7, 5))
            sns.boxplot(
                data=df,
                x="churn_label",
                y="age",
                ax=ax
            )
            ax.set_title("Age vs Churn", fontweight="bold")
            ax.set_xlabel("Customer Status")
            ax.set_ylabel("Age")
            finish_fig(fig)

        with col2:
            avg_age = df.groupby("churn_label")["age"].mean().sort_values()

            fig, ax = plt.subplots(figsize=(7, 5))
            sns.barplot(
                x=avg_age.index,
                y=avg_age.values,
                ax=ax
            )
            ax.set_title("Average Age by Churn Status", fontweight="bold")
            ax.set_xlabel("Customer Status")
            ax.set_ylabel("Average Age")
            finish_fig(fig)

    # Average daily watch time
    with st.container(border=True):
        st.subheader("⏱️ Average Watch Time Per Day vs Churn")

        col1, col2 = st.columns(2)

        with col1:
            fig, ax = plt.subplots(figsize=(7, 5))
            sns.boxplot(
                data=df,
                x="churn_label",
                y="avg_watch_time_per_day",
                ax=ax
            )
            ax.set_title(
                "Average Watch Time Per Day vs Churn",
                fontweight="bold"
            )
            ax.set_xlabel("Customer Status")
            ax.set_ylabel("Hours / Day")
            finish_fig(fig)

        with col2:
            avg_daily = (
                df.groupby("churn_label")["avg_watch_time_per_day"]
                .mean()
                .sort_values()
            )

            fig, ax = plt.subplots(figsize=(7, 5))
            sns.barplot(
                x=avg_daily.index,
                y=avg_daily.values,
                ax=ax
            )
            ax.set_title(
                "Average Daily Watch Time by Churn",
                fontweight="bold"
            )
            ax.set_xlabel("Customer Status")
            ax.set_ylabel("Average Hours / Day")
            finish_fig(fig)

    # Four-way categorical behavior
    with st.container(border=True):
        st.subheader("🔍 Multi-Dimensional Customer Behavior")

        fig, axes = plt.subplots(2, 2, figsize=(14, 10))

        sns.boxplot(
            data=df,
            x="subscription_type",
            y="age",
            hue="churn_label",
            ax=axes[0, 0]
        )
        axes[0, 0].set_title("Age by Subscription Type and Churn")

        sns.boxplot(
            data=df,
            x="region",
            y="watch_hours",
            hue="churn_label",
            ax=axes[0, 1]
        )
        axes[0, 1].set_title("Watch Hours by Region and Churn")
        axes[0, 1].tick_params(axis="x", rotation=25)

        sns.boxplot(
            data=df,
            x="payment_method",
            y="last_login_days",
            hue="churn_label",
            ax=axes[1, 0]
        )
        axes[1, 0].set_title("Inactivity by Payment Method and Churn")
        axes[1, 0].tick_params(axis="x", rotation=25)

        sns.boxplot(
            data=df,
            x="device",
            y="avg_watch_time_per_day",
            hue="churn_label",
            ax=axes[1, 1]
        )
        axes[1, 1].set_title("Daily Watch Time by Device and Churn")
        axes[1, 1].tick_params(axis="x", rotation=25)

        finish_fig(fig)


# ============================================================
# RELATIONSHIPS
# ============================================================
elif page == "🔗 Relationships":

    st.markdown(
        "<div class='section-title'><h2>🔗 Relationship & Correlation Analysis</h2></div>",
        unsafe_allow_html=True
    )

    # Scatter plots
    with st.container(border=True):
        st.subheader("📈 Numerical Relationships")

        fig, axes = plt.subplots(1, 3, figsize=(17, 5))

        sns.scatterplot(
            data=df,
            x="age",
            y="watch_hours",
            hue="churn_label",
            alpha=0.65,
            ax=axes[0]
        )
        axes[0].set_title("Age vs Watch Hours")

        sns.scatterplot(
            data=df,
            x="last_login_days",
            y="watch_hours",
            hue="churn_label",
            alpha=0.65,
            ax=axes[1]
        )
        axes[1].set_title("Last Login Days vs Watch Hours")

        sns.scatterplot(
            data=df,
            x="last_login_days",
            y="avg_watch_time_per_day",
            hue="churn_label",
            alpha=0.65,
            ax=axes[2]
        )
        axes[2].set_title("Last Login Days vs Avg Daily Watch Time")

        finish_fig(fig)

    # Correlation heatmap
    with st.container(border=True):
        st.subheader("🔥 Correlation Heatmap")

        cols = [
            "age",
            "watch_hours",
            "last_login_days",
            "avg_watch_time_per_day"
        ]

        cols = [c for c in cols if c in df.columns]

        correlation = df[cols].corr()

        fig, ax = plt.subplots(figsize=(9, 6))
        sns.heatmap(
            correlation,
            annot=True,
            fmt=".2f",
            cmap="Blues",
            linewidths=0.7,
            linecolor="white",
            ax=ax
        )
        ax.set_title(
            "Correlation Heatmap of Continuous Numerical Variables",
            fontsize=15,
            fontweight="bold"
        )
        finish_fig(fig)

    # Churn numerical comparisons
    with st.container(border=True):
        st.subheader("📊 Numerical Features vs Churn")

        fig, axes = plt.subplots(1, 3, figsize=(16, 5))

        sns.barplot(
            data=df,
            x="churn_label",
            y="watch_hours",
            ax=axes[0]
        )
        axes[0].set_title("Watch Hours vs Churned")

        sns.barplot(
            data=df,
            x="churn_label",
            y="age",
            ax=axes[1]
        )
        axes[1].set_title("Age vs Churned")

        sns.barplot(
            data=df,
            x="churn_label",
            y="avg_watch_time_per_day",
            ax=axes[2]
        )
        axes[2].set_title("Avg Watch Time / Day vs Churned")

        finish_fig(fig)


# ============================================================
# OUTLIER ANALYSIS
# ============================================================
elif page == "🚨 Outlier Analysis":

    st.markdown(
        "<div class='section-title'><h2>🚨 IQR Outlier Analysis</h2></div>",
        unsafe_allow_html=True
    )

    st.info(
        "Outliers are detected using the IQR method: "
        "Lower = Q1 - 1.5×IQR and Upper = Q3 + 1.5×IQR."
    )

    num_cols = numeric_columns(df)

    outlier_rows = []

    for col in num_cols:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr

        outliers = df[(df[col] < lower) | (df[col] > upper)]

        outlier_rows.append({
            "Feature": col,
            "Q1": q1,
            "Q3": q3,
            "IQR": iqr,
            "Lower Limit": lower,
            "Upper Limit": upper,
            "Minimum": df[col].min(),
            "Maximum": df[col].max(),
            "Outlier Count": len(outliers)
        })

    outlier_df = pd.DataFrame(outlier_rows)

    with st.container(border=True):
        st.subheader("📋 Outlier Summary")
        st.dataframe(
            outlier_df.style.format({
                "Q1": "{:.2f}",
                "Q3": "{:.2f}",
                "IQR": "{:.2f}",
                "Lower Limit": "{:.2f}",
                "Upper Limit": "{:.2f}",
                "Minimum": "{:.2f}",
                "Maximum": "{:.2f}",
            }),
            use_container_width=True
        )

    # Highlight two features used in notebook's detailed outlier analysis
    detailed_cols = [
        c for c in ["watch_hours", "avg_watch_time_per_day"]
        if c in df.columns
    ]

    if detailed_cols:
        with st.container(border=True):
            st.subheader("📦 Detailed Outlier Boxplots")

            fig, axes = plt.subplots(
                1,
                len(detailed_cols),
                figsize=(12, 5)
            )

            if len(detailed_cols) == 1:
                axes = [axes]

            for ax, col in zip(axes, detailed_cols):
                sns.boxplot(
                    y=df[col],
                    ax=ax
                )
                ax.set_title(
                    col.replace("_", " ").title(),
                    fontweight="bold"
                )

            finish_fig(fig)


# ============================================================
# DATA EXPLORER
# ============================================================
elif page == "📋 Data Explorer":

    st.markdown(
        "<div class='section-title'><h2>📋 Explore Raw Data</h2></div>",
        unsafe_allow_html=True
    )

    with st.container(border=True):
        st.subheader("Dataset Preview")

        rows_to_show = st.slider(
            "Rows to display",
            min_value=5,
            max_value=min(100, len(df)),
            value=10
        )

        st.dataframe(
            df.head(rows_to_show),
            use_container_width=True,
            height=450
        )

    with st.container(border=True):
        st.subheader("🔎 Column Information")

        info_df = pd.DataFrame({
            "Column": df.columns,
            "Data Type": df.dtypes.astype(str).values,
            "Missing Values": df.isna().sum().values,
            "Unique Values": df.nunique().values
        })

        st.dataframe(
            info_df,
            use_container_width=True
        )

    with st.container(border=True):
        st.subheader("📐 Statistical Description")

        st.dataframe(
            df.describe(include="all").T,
            use_container_width=True
        )


# ============================================================
# FOOTER
# ============================================================
st.markdown(
    """
    <div style="
        margin-top: 35px;
        padding: 18px;
        text-align: center;
        border-top: 1px solid #252936;
        color: #777e8b;
    ">
        Netflix Customer Churn Analytics • Built with Python, Pandas,
        NumPy, Matplotlib, Seaborn & Streamlit
    </div>
    """,
    unsafe_allow_html=True)