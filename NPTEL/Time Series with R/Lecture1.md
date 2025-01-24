
## Lecture 1: Introduction to Time Series

---

### What is a Time Series?
- **Definition**: Time series is data observed over time where observations depend on time order.
- **Difference from other data**:
  - Unlike data from classical inference (e.g., regression, hypothesis testing), time series is **not independent**.
  - In classical datasets, observations are i.i.d (Independent and Identically Distributed).
  - In time series:
    - Observations are chronological.
    - Dependencies exist between data points due to time factors.

---

### Example: Difference Between Random Variables and Time Series Data
1. **Random Variables**:
   - Example: Outcomes of rolling a die (X₁, X₂, ..., X₁₀₀).
   - Observations are independent; no pattern exists between outcomes.

2. **Time Series**:
   - Example: Closing prices of a stock (X₁, X₂, ..., X₁₀₀).
   - Observations are dependent:
     - Stock prices follow patterns over time.
     - X₃ depends on X₂, and so on.

---

### Key Characteristics of Time Series Data
1. **Ordered Observations**:
   - E.g., Xₜ, Xₜ₊₁, ..., Xₜ₊₁₀ follow a sequence in time.
   - Observations depend on time (`t`).

2. **Timeframe Notation**:
   - Can vary:
     - Daily
     - Weekly
     - Monthly
     - Annually

3. **Comparison with Classical Data**:
   - Classical Data:
     - Independent observations from a distribution (e.g., Normal, Binomial).
   - Time Series Data:
     - Observations are dependent on time.

---

### Types of Data

#### 1. **Cross-Sectional Data**:
   - Observations collected from different entities at a **single point in time**.
   - Examples:
     - Maximum humidity levels at 20 locations on a particular day.
     - Closing stock prices of 20 stocks on a particular day.
     - Heights of students measured on a particular day.

#### 2. **Time Series Data**:
   - Observations collected for a **single entity over a period of time**.
   - Examples:
     - Daily maximum humidity levels for a month.
     - Closing stock price of a company over 6 months.
     - Quarterly student enrollment in a college over 5 years.

#### 3. **Panel Data (Longitudinal Data)**:
   - Combination of cross-sectional and time series data.
   - Observations are collected for **different entities over time**.
   - Examples:
     - Annual cancer mortality rates of Indian states (2015–2023).
     - Yearly sales of 10 companies over 10 years.
     - Daily maximum temperatures of 5 cities in India over a year.

---

### Steps in Analyzing Time Series Data

1. **Plot the Data**:
   - Visualize data to identify patterns and trends.
   - Example: Google stock prices over time.
   - Insights:
     - Trends: Upward/downward movement.
     - Stagnation or repetition patterns.

2. **Study Past Behavior**:
   - Analyze historical data to understand trends and behaviors.

3. **Identify Patterns and Trends**:
   - Look for:
     - Upward/downward trends.
     - Seasonal or cyclical patterns.
     - Repetitions.

4. **Use Past Data for Forecasting**:
   - Forecast future values based on historical data.
   - Example: Predict Google stock prices for the next 10 days.

---

### Applications of Time Series Analysis

1. **Retail Stores**:
   - Forecast daily, monthly, or annual sales.

2. **Energy Companies**:
   - Predict reserves, production, demand, supply, and prices.

3. **Educational Institutions**:
   - Forecast student enrollment for upcoming semesters or years.

4. **International Financial Organizations**:
   - Forecast inflation or other economic activities.

5. **Transportation Companies**:
   - Predict travel demand for specific seasons or periods.

6. **Banks and Lending Institutions**:
   - Forecast new home purchases.

7. **Venture Capital Firms**:
   - Evaluate market potential and business plans.

8. **Weather Forecasting**:
   - Predict precipitation, temperature, humidity, etc.

---

### Overview of the Course

#### Weeks 1–2:
   - Introduction to Time Series.
   - Concepts of stationarity and non-stationarity.
   - Basic models:
     - Moving Average (MA).
     - Autoregressive (AR).

#### Weeks 3–4:
   - Stationarity tests.
   - Advanced models:
     - ARIMA, SARIMA.
   - Model identification.

#### Weeks 5–6:
   - Forecasting methods.
   - Comparing forecasts.
   - Fractionally Integrated Processes.

#### Weeks 7–8:
   - Multivariate Time Series.
   - Co-integration and causality analysis.

#### Weeks 9–10:
   - Fourier Transformations.
   - Spectral density analysis.
   - Volatility modeling (ARCH, GARCH).

#### Weeks 11–12:
   - Non-linear models.
   - Markov switching models.
   - Machine Learning applications:
     - Neural Networks.
     - Decision Trees.
     - Reinforcement Learning.

---

### Practical Component
- Use **R software** for hands-on implementation.
- Focus on applying theoretical concepts to real-world datasets.

---
