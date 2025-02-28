# Lecture 2: Examples of Time Series Data

## Lecture Overview
- **Course**: Time Series Forecasting with Applications in R
- **Lecture**: Second
- **Topics Recap**: 
  - Examples of Time Series from various domains: Finance, Climatology, Ecology, Environmental Sciences, etc.
  - Data types: Cross-sectional, Time Series, Panel data (combination of Cross-sectional and Time Series).

---

## Why Study Time Series?
1. **Understanding Trends and Patterns**:
   - Trends indicate long-term movement (upward/downward).
   - Example: Google stock price showing periods of trends and no trends.

2. **Predicting Future Events**:
   - Forecasting future values such as stock prices for companies like Google and Apple.

3. **Inferencing Probability Models**:
   - Understanding how observations are related and fitting distributions/models to the data.

4. **Confidence Intervals and Hypothesis Testing**:
   - Developing statistical models to analyze parameters of the series.

---

## Time Series Notation
- **Preferred Notation**:
  - $\( X_t, X_{t+H}, X_{t+2H}, X_{t+3H}, \dots \)$
  - $\( H \)$: Time gap between observations.
  - $\( \frac{1}{H} \)$: Sampling frequency.

- **Example**:
  - Observing daily temperature:
    - Observations collected every other day $(\( H=2 \))$.
    - Sampling frequency: $\( \frac{1}{H} = \frac{1}{2} \)$.

---

## Importance of Ordering in Time Series
- Observations must be sequential.
- Dependency on time makes ordering crucial (e.g., temperature data).

---

## Examples of Time Series Applications
1. **CO2 Levels in Atmosphere**:
   - Period: 1960–2020.
   - Observations: Upward trend and seasonality.

2. **Oil Spot Price**:
   - No overall trend or seasonality, but local trends may exist.

3. **SGST Revenues in India**:
   - Period: 2017–2020.
   - Observations: Mild upward trend.

4. **Delhi Air Quality Index**:
   - Seasonal pattern with no overall trend; local trends visible.

5. **Quarterly Sugar Cane Prices in India**:
   - Distinction between **monthly** vs. **quarterly** data collection.

---

## Choosing Time Scales
- **Key Factors**:
  1. Scale of required forecasts (e.g., daily vs. monthly forecasts).
  2. Level of noise in data.

- **Example**:
  - Forecast next-day sales at a grocery store:
    - Use daily aggregates instead of minute-by-minute data (minute data contains excessive noise).

---

## Noise in Time Series
- **Definition**: Random fluctuations without discernible patterns.
- **Example**: Minute-by-minute sales data with rapid fluctuations.

---

## Types of Time Series
1. **Long Time Series**:
   - Contains many observations.
   - Examples: Weekly interest rates (5 years), daily stock prices (5 years).

2. **Short Time Series**:
   - Contains few observations.
   - Examples: Census data (30 observations), yearly student enrollments since 2000.

---

## Practical Examples
1. **Indian Population (1955–2024)**:
   - Data collected every 5 years.
   - Observations:
     - Upward trend.
     - Non-stationary due to the trend.

2. **International Airline Data**:
   - Period: January 1949 – December 1960.
   - Observations:
     - Upward trend, seasonality.
     - Variability increases over time.

---

## Summary
- Time series often exhibit trends, seasonality, and variability.
- Differences between **stationary** and **non-stationary** series will be discussed in future lectures.
- Non-stationary examples include data with trends, seasonality, or changing variability.
