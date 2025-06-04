# 🦠 COVID-19 Hospital Utilization & Mortality Trends

## 🧾 Abstract
This project analyzes hospital utilization and mortality trends during the COVID-19 pandemic using publicly available data from the U.S. Department of Health and Human Services. By leveraging Power BI, the project visualizes key metrics such as hospital visit volumes, mortality rates by condition, and facility-level patient loads from 2018 to 2021. These interactive dashboards help reveal patterns in healthcare demand, highlight conditions with higher in-hospital death rates, and track the impact of COVID-19 on hospital systems. The analysis provides insights useful for healthcare planning and emergency preparedness.

---

## 🚀 Key Features

- 📁 **Dataset**: Hospital utilization and mortality data covering visits, deaths, and diagnosis categories (2018–2021)
- 📊 **Analysis Tools**: Power BI for interactive dashboard creation
- 🎯 **Techniques Used**:
  - Time-series trend analysis
  - Condition-specific mortality and visit volume tracking
  - Facility-level patient load comparisons
- 🧠 **Insights**:
  - COVID-19 dominated hospital visits and mortality in 2021.
  - Emergency departments and inpatient discharges showed higher death rates (~3%).
  - Substance use disorders and stroke were leading non-COVID causes of mortality.
  - Some hospitals consistently had high patient volumes across the study period.

---

## 🛠️ Methodology

### 1. Data Preprocessing
- Cleaned raw CSV data using Python to remove invalid entries and standardize date formats.
- Extracted year, month, and quarter from date fields for time-based analysis.
- Standardized column names and removed corrupted data entries.

### 2. Data Modeling
- Designed a star schema in Power BI with fact tables for utilization and mortality counts.
- Created dimension tables for dates, health conditions, and facilities.
- Maintained many-to-one relationships to optimize dashboard performance.

### 3. Visualization
- Developed three dashboards focusing on:
  - Overall hospital usage and mortality overview
  - COVID-19 specific condition trends
  - Facility-level patient volume analysis
- Used KPIs, stacked bar charts, line graphs, and drillable visuals for insights.
- Applied consistent color schemes and user-friendly layouts.

### 4. Calculated Measures
- Mortality Rate (%)
- Total Visits
- Year-over-Year Encounter Growth (%)
- Max Visits by Hospital
- Facility Load Indicators (planned)

---

## 📈 Results

| Factor                       | Observation                                          |
|------------------------------|----------------------------------------------------|
| COVID-19 Impact              | Sharp increase in visits and mortality in 2021     |
| Mortality Rate               | ~3% in emergency departments and inpatient discharges |
| High-Risk Conditions         | Stroke and substance use disorders prominent in deaths |
| Facility Utilization         | Kaiser Fontana had highest patient volumes (~201K)  |
| Visit Trends                | Significant drop in 2020 visits with rebound in 2021 |

---

## 💻 Deployment

- Power BI Desktop used to build dashboards with imported cleaned CSV data.
- Reports include slicers for year, condition category, care setting, and hospital.
- Dashboard files (`.pbix`) provide interactive exploration of trends.
- Suitable for healthcare analysts and hospital administrators.

---

## 👨‍💻 Authors

- **PADMAVATHI VYSHNAVI MADARAMPALLI** – Data cleaning, modeling, visualization, Data acquisition, DAX calculations, dashboard design  
Master’s in Information Technology and Management – ILLINOIS INSTITUTE OF TECHNOLOGY

---

## 📚 References

1. U.S. Department of Health and Human Services – COVID-19 Hospital Utilization Dataset  
2. Power BI Documentation – [https://docs.microsoft.com/power-bi/](https://docs.microsoft.com/power-bi/)  
3. CDC COVID-19 Data Tracker – [https://covid.cdc.gov/covid-data-tracker/](https://covid.cdc.gov/covid-data-tracker/)  
4. WHO – COVID-19 Situation Reports and Hospital Resource Guidelines  

---

## 🔮 Future Work

- Add geographic visualizations with state and regional breakdowns.  
- Incorporate patient demographics like age, gender, and insurance status.  
- Implement forecasting models to predict hospital capacity needs.  
- Enable live data refresh using Power BI Service integration.  
- Enhance dashboards with tooltips explaining key metrics and formulas.  

---

## 📄 License

This project is licensed under the MIT License – see the `LICENSE` file for details.
