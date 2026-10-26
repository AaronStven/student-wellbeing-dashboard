# 🎓 Student Wellbeing Dashboard

An end-to-end data analytics and HCI project. I cleaned a survey dataset of 500 students, built an interactive dashboard to visualize stress and sleep patterns, and documented the user experience.

![Dashboard Preview](dashboard_preview.png)

## 📊 The Data
- **Source:** Simulated survey data (500 responses)
- **Cleaning:** Addressed impossible values (GPA > 4.0), unrealistic study hours, and missing data using pandas. (See `data/clean_data.py`)

## 💡 Key Insights
- Students in the Arts faculty reported the highest average stress levels.
- There is a moderate negative correlation between sleep hours and stress levels among Seniors.
- GPA does not strongly correlate with stress, suggesting other factors (like time management) play a larger role.

## 🖥 The Dashboard (Data Analytics)
Built using Python and **Plotly Dash**. 
- Interactive filtering by Faculty.
- Scatter plot showing GPA vs Stress.
- Boxplot showing sleep distribution by Academic Year.

## 🚀 How to Run Locally
1. Clone the repo and navigate into it.
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `.\venv\Scripts\Activate.ps1` (Windows) or `source venv/bin/activate` (Mac/Linux)
4. Install dependencies: `pip install -r requirements.txt`
5. Generate and clean data: 
   - `python data/generate_data.py`
   - `python data/clean_data.py`
6. Run the app: `python app/dashboard.py`

## 🧠 Usability Evaluation (HCI)
Before finalizing the dashboard, I conducted a usability study with 8 students.
**Methodology:**
- Task: "Find out if Senior CS students get less sleep than Freshmen."
- Metrics: Task completion time, error rate, System Usability Scale (SUS), and think-aloud protocol.

**Results:**
- **SUS Score:** 82.5 (Grade A - Excellent)
- **Key Feedback:** Users wanted the charts to update instantly without a "submit" button (led to the implementation of Dash callbacks).
- **Iteration:** Added clear axis labels and standardized color schemes (colorblind-friendly palette) after 2 users struggled with the default Plotly colors.

## 🛠 Tech Stack
Python · pandas · Plotly Dash · Jupyter Notebooks · SUS Methodology
