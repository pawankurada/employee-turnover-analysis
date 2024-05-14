# Operational Efficiency and Employee Experience Analysis

This repository contains all the code and analyses conducted for the Ball Corporation case study focused on enhancing operational efficiency and understanding employee experience within manufacturing facilities.

## Project Overview

This project aims to identify key factors contributing to the success of Ball Corporation's manufacturing facilities and to establish strategies that foster an optimal workforce environment, thereby enhancing operational efficiency and reducing turnover.

## Table of Contents

- [Data Preparation and Analysis](#data-preparation-and-analysis)
- [Methodology](#methodology)
- [Results](#results)
- [Tools and Technologies Used](#tools-and-technologies-used)
- [License](#license)

## Data Preparation and Analysis

1. **Initial Exploratory Data Analysis (EDA):** Initial assessment of the data to understand the distributions, missing values, and basic statistics.
2. **Survey Data Analysis:** Conversion of survey results into crosstabs for enhanced analytical clarity.
3. **Operational Metrics Combination:** Utilization of Principal Component Analysis (PCA) to combine four key operational metrics (Efficiency, Safety (TRIR), Spoilage, Quality (HFI)) into a single variable for a consolidated view.

## Methodology

1. **Multiple Regression Analyses:**
   - Conducted multiple regressions to identify determinants of operational efficiency with targets set on individual operational metrics.
   - Extended the analysis to include a PCA-combined metric to encapsulate overall operational performance.
2. **K-means Clustering:**
   - Implementation of K-means clustering to categorize plants into distinct groups for effective benchmarking and targeted improvement strategies.
3. **GenAI Powered Sentiment Analysis:**
   - Scraping of online reviews from Glassdoor and Indeed.
   - Deployment of a Mixtral 8x7B Language Model to power a generative AI chatbot, facilitating advanced sentiment analysis regarding employee experiences and perceptions.

## Results

Detailed findings and interpretations from the regression analyses, PCA, and clustering are documented, highlighting the relationships between workforce attributes and operational metrics. Insights from sentiment analysis provide additional context to the quantitative data, offering a comprehensive view of employee satisfaction and its impact on operational success.

## Tools and Technologies Used

- Python for data analysis and machine learning.
- Libraries: pandas, numpy, sklearn, matplotlib, seaborn.
- APIs for web scraping reviews.
- Mixtral 8x7B LLM for generating the AI-powered chatbot.



## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

