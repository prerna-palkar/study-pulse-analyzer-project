import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go


# ==============================
# Load Data
# ==============================

df = pd.read_csv("data.csv")

if df.empty:
    print("No study data found.")
    exit()


# ==============================
# Calculate Dashboard Metrics
# ==============================

total_sessions = len(df)
total_hours = df["Duration"].sum() / 60
average_productivity = df["Productivity"].mean()

best_subject_data = (
    df.groupby("Subject")["Productivity"]
    .mean()
    .sort_values(ascending=False)
)

best_subject = best_subject_data.index[0]
best_score = best_subject_data.iloc[0]


# ==============================
# Prepare Chart Data
# ==============================

study_time = (
    df.groupby("Subject")["Duration"]
    .sum()
    .reset_index()
)

productivity = (
    df.groupby("Subject")["Productivity"]
    .mean()
    .reset_index()
)


# ==============================
# Create Dashboard
# ==============================

fig = make_subplots(
    rows=2,
    cols=2,
    specs=[
        [{"type": "indicator"}, {"type": "indicator"}],
        [{"type": "bar"}, {"type": "bar"}]
    ],
    vertical_spacing=0.18,
    horizontal_spacing=0.12,
    subplot_titles=(
        "",
        "",
        "Study Time by Subject",
        "Average Productivity by Subject"
    )
)


# ==============================
# KPI 1 - Study Hours
# ==============================

fig.add_trace(
    go.Indicator(
        mode="number",
        value=total_hours,
        number={
            "suffix": " hrs",
            "font": {"size": 34}
        },
        title={
            "text": "TOTAL STUDY TIME"
        }
    ),
    row=1,
    col=1
)


# ==============================
# KPI 2 - Productivity
# ==============================

fig.add_trace(
    go.Indicator(
        mode="number",
        value=average_productivity,
        number={
            "suffix": "/100",
            "font": {"size": 34}
        },
        title={
            "text": "AVG PRODUCTIVITY"
        }
    ),
    row=1,
    col=2
)


# ==============================
# Chart 1 - Study Time
# ==============================

fig.add_trace(
    go.Bar(
        x=study_time["Subject"],
        y=study_time["Duration"],
        text=study_time["Duration"],
        textposition="outside",
        hovertemplate=(
            "<b>%{x}</b><br>"
            "Study Time: %{y} minutes"
            "<extra></extra>"
        )
    ),
    row=2,
    col=1
)


# ==============================
# Chart 2 - Productivity
# ==============================

fig.add_trace(
    go.Bar(
        x=productivity["Subject"],
        y=productivity["Productivity"],
        text=productivity["Productivity"].round(1),
        textposition="outside",
        hovertemplate=(
            "<b>%{x}</b><br>"
            "Productivity: %{y:.1f}/100"
            "<extra></extra>"
        )
    ),
    row=2,
    col=2
)


# ==============================
# Dashboard Layout
# ==============================

fig.update_layout(
    title={
        "text": (
            "📚 <b>StudyPulse</b>"
            "<br><sup>Smart Study Performance Dashboard</sup>"
        ),
        "x": 0.5,
        "xanchor": "center"
    },

    height=800,

    showlegend=False,

    margin={
        "l": 60,
        "r": 60,
        "t": 120,
        "b": 60
    },

    hovermode="closest",

    template="plotly_white"
)


# ==============================
# Axis Labels
# ==============================

fig.update_xaxes(
    title_text="Subject",
    row=2,
    col=1
)

fig.update_yaxes(
    title_text="Minutes",
    row=2,
    col=1
)

fig.update_xaxes(
    title_text="Subject",
    row=2,
    col=2
)

fig.update_yaxes(
    title_text="Productivity Score",
    range=[0, 100],
    row=2,
    col=2
)


# ==============================
# Show Dashboard
# ==============================

fig.show()


# ==============================
# Print Insight
# ==============================

print("\n" + "=" * 45)
print("             STUDYPULSE INSIGHT")
print("=" * 45)

print(f"Total Sessions      : {total_sessions}")
print(f"Total Study Time    : {total_hours:.2f} hours")
print(f"Average Productivity: {average_productivity:.2f}/100")
print(f"Best Subject        : {best_subject}")
print(f"Best Subject Score  : {best_score:.2f}/100")

print("=" * 45)pyt