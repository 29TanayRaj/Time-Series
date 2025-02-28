# Lecture 6: Time Series Decomposition

1. **Time Series Decomposition**:
   - Breaking a time series into its components.
2. **Introduction to Basic Time Series Models**:
   - Auto-regressive (AR).
   - Moving average (MA).
   - Random walk.
3. **Practical Session in R**.

---

## **Time Series Decomposition**
### **Purpose**
- Break a time series (denoted as $Y_t$) into four main components:
  1. **Trend Component $T_t$**: Represents long-term movement. Also known as secular trend.
  2. **Seasonal Component $S_t$**: Captures periodic variations within a cycle of ≤1 year. Also known as sesonality.
  3. **Cyclical Component $C_t$**: Describes gradual and long-term up-and-down movements with a cycle >1 year.
  4. **Random/Irregular Component $I_t$**: Captures noise or unpredictable fluctuations.

---

## **Systematic vs. Random Components**
### **Systematic Components**
- **Include**: Trend, Seasonality, and Cyclicality.
- **Characteristics**:
  - Arise from permanent causes and are predictable.
- **Examples**:
  - **Trend**: Stock prices showing a long-term upward or downward pattern.
  - **Seasonality**: Repeated patterns in temperature data (e.g., summer months showing high temperatures).
- **Forecasting**:
  - Trend or seasonal patterns can inform future predictions based on observed regularities.

### **Random Component**
- **Include**: Noise or irregular fluctuations.
- **Characteristics**:
  - Caused by entirely random fluctuations (noise).
  - No discernible pattern or repetition.
  - Unpredictable by nature.

---

## **Details of Components**
### 1. **Trend Component (T_t)**
   - Represents long-term movement over time.
   - Observed over an extended period (not short-term).
   - Change in average/mean level.

### 2. **Seasonal Component (S_t)**
   - Regular, periodic variation within a cycle of ≤1 year.
   - **Example**:
     - Monthly temperature data:
       - Peaks (e.g., summers in June/July).
       - Troughs (e.g., winters in December/January).
   - **Key Attribute**:
     - Cycle period ≤1 year.

### 3. **Cyclical Component (C_t)**
   - Gradual and long-term up-and-down movements.
   - **Difference from Seasonality**:
     - Cycle period >1 year (typically ≥2 years).
     - Less regular compared to seasonal patterns.

### 4. **Random/Irregular Component (I_t)**
   - Represents noise or random fluctuations.
   - **Characteristics**:
     - No predictable pattern or structure.

---

## **Understanding Cyclicality**
### **Definition**
- **Cyclicality** refers to long-term fluctuations in a time series with a duration of at least 2 years.
- The cycles are **not at regular intervals**, unlike seasonality.

### **Example**: Business Cycle
- During a boom, the business reaches a **peak**, and during a downturn, it hits a **trough**.
- The **next peak** may not reach the same height as the previous one, and the **next trough** may differ in depth.
- The **irregular intervals** and **dynamic nature** of business performance make cyclicality distinct from seasonality.

### **Key Difference from Seasonality**
- **Seasonality**: Regular, calendar-linked repetitions.
- **Cyclicality**: Irregular repetitions with varying amplitudes and durations.

---

## **Random Variations**
### **Definition**
- Denoted as $I_t$, these are **unpredictable, irregular fluctuations** in the data.
- They result from **entirely random movements** and lack any identifiable pattern, trend, seasonality, or cyclicality.

### **Role in Time Series**
- The **random component** is considered "noise" and often removed to focus on other systematic components.

---

## **Example: Nottingham Monthly Temperature Data**
### **Details**
- Dataset: 20 years of monthly temperature measurements at Nottingham Castle, UK (1920–1940).
- Observations:
  - **Seasonality dominates**: Regular peaks (summer months) and troughs (winter months).
  - **Trend is absent**: No significant upward or downward movement over the period.
  - **Decomposition**: 
    - Top row: Original data.
    - Second row: Seasonal component showing clear repetitions.
    - Third row: Trend component (flat, indicating no trend).
    - Fourth row: Remainder or random component, showing irregular fluctuations.

---

## **Decomposition Overview**
1. **Trend**: Long-term changes in the average level of the series.
   - **Example**: Increasing sales over decades.
   - **Key Features**:
     - No calendar-related influences.
     - Lacks random fluctuations.
     - Reflects changes in the mean level.

2. **Seasonality**: Systematic, calendar-linked effects.
   - **Examples**:
     - Higher sales during festive seasons (e.g., Diwali in India).
     - Increased water consumption in summer.
   - **Complex Seasonality**:
     - Irregular but systematic patterns (e.g., weekly sales fluctuations based on salary cycles).

3. **Cyclicality**: Long-term waves of expansion and contraction.
   - **Examples**:
     - Business cycles with peaks and troughs.
     - Population dynamics of species (e.g., wildcats in Canada).

4. **Random Component**: Unpredictable noise.
   - **Example**: Short-term fluctuations without structure.

---

## **Examples of Dominance in Time Series**
1. **Trend Dominance**: Long-term upward or downward movement.
   - Example: Steady increase in stock prices.
2. **Seasonality Dominance**: Regular, periodic fluctuations.
   - Example: Monthly temperature variations.
3. **Cyclicality Dominance**: Irregular, wave-like patterns.
   - Example: Business cycle.
4. **Random Dominance**: No discernible pattern.
   - Example: Noise in a stock market dataset.

---

## **Conclusion**
Time series decomposition helps identify the dominant component in a dataset. Understanding whether **trend**, **seasonality**, **cyclicality**, or **randomness** dominates enables better analysis, forecasting, and modeling of time series data.
