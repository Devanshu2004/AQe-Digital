# AQe Digital - Data Science Internship Projects

This repository contains the project I completed during my Data Science Internship at AQe Digital. The work demonstrates practical application of data science methodologies to solve real-world business problems.

## About AQe Digital

AQe Digital is a technology company focused on delivering innovative digital solutions. During my internship, I had the opportunity to work on data-driven projects that contribute to the company's mission of leveraging data for business intelligence and decision-making.

## Internship Overview

**Position**: Data Science Intern  
**Company**: AQe Digital  
**Duration**: 4 months 
**Focus Areas**: Data Analysis, Machine Learning, Business Intelligence

## Project: HomerunHub

### Project Description

HomerunHub is a comprehensive data science project that analyzes baseball statistics, predicts game outcomes and provides insights for team management. This project showcases the end-to-end data science workflow from data collection to model deployment.

### Problem Statement

- **Wild card** – fan experience: Think outside the batter's box! This is your chance to knock our socks off with any project that uses the provided datasets to redefine how fans experience the game we love.
- **Personalized fan highlights**: Ditch the one-size-fits-all highlights! Build a system that curates personalized audio, video, and text digests based on a fan’s favorite teams, players, and even preferred language.
- **Real-time "tool tips"**: Turn casual viewers into armchair analysts with an interactive application that delivers real-time strategic insights. Explain the "why" behind every steal, strikeout, and home run as it happens.
- **Generate Statcast data from old videos**: Give classic games the Statcast treatment! Use computer vision to extract key metrics (pitch speed, exit velocity, etc.) from archival game footage. Think Moneyball meets the digital age.
- **Prospect prediction**: Can your code spot the next MLB superstar? Build a platform that analyzes prospect data to project future MLB potential and career impact, leveraging historical comparisons and predictive modeling.

### Key Features

- **Data Collection**: Automated data gathering from multiple sources
- **Data Processing**: Comprehensive data cleaning and feature engineering
- **Exploratory Data Analysis**: In-depth statistical analysis and visualization
- **Machine Learning Models**: Implementation of predictive models
- **Performance Metrics**: Evaluation of model accuracy and business impact
- **Visualization Dashboard**: Interactive charts and graphs for stakeholder presentation

### Technologies Used

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=matplotlib&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=for-the-badge&logo=seaborn&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

### Data Sources

- Google MLB Data

### Methodology

1. **Data Collection & Integration**
   - Gathered data from multiple sources
   - Implemented data validation and quality checks
   - Created unified dataset for analysis

2. **Exploratory Data Analysis**
   - Statistical analysis of key variables
   - Identification of trends and patterns
   - Data visualization for insights discovery

3. **Feature Engineering**
   - Created relevant features from raw data
   - Applied feature selection techniques
   - Handled missing values and outliers

4. **Model Development**
   - Implemented multiple machine learning algorithms
   - Performed hyperparameter tuning
   - Cross-validation for model reliability

5. **Model Evaluation**
   - Used appropriate metrics for model assessment
   - Compared different algorithms
   - Selected best performing model

6. **Results Interpretation**
   - Translated model outputs to business insights
   - Created visualizations for stakeholder communication
   - Provided actionable recommendations

### Repository Structure

```
HomerunHub/
├── Dataset/
│   └── data
├── build/
│   ├── locales/
|   |   |── en/
|   |   |   └── translation.json
|   |   |── es/
|   |   |   └── translation.json
|   |   └── ja/
|   |       └── translation.json
│   ├── static/
|   |   |── css/
|   |   |   |── main.10c47941.css
|   |   |   └── main.10c47941.css.map
|   |   |── js/
|   |   |   |── 38.48744e28.chunk.js
|   |   |   |── 38.48744e28.chunk.js.map
|   |   |   |── 488.b5c88247.chunk.js
|   |   |   |── 488.b5c88247.chunk.js.map
|   |   |   |── main.201c8bed.js
|   |   |   |── main.201c8bed.js.LICENSE.txt
|   |   |   └── main.201c8bed.js.map
|   |   └── media/
|   |       └── logo.8dd1714135259688f2c2.png
│   ├── asset-mainfest.json
│   ├── favicon.ico
│   ├── index.html
│   ├── logo192.png
│   ├── logo512.png
│   ├── manifest.json
│   └── robots.txt
├── public/
│   ├── locales/
|   |   |── en/
|   |   |   └── translation.json
|   |   |── es/
|   |   |   └── translation.json
|   |   └── ja/
|   |       └── translation.json
│   ├── index.html
│   ├── logo192.png
│   ├── logo512.png
│   ├── manifest.json
│   └── robots.txt
├── src/
│   ├── components/
|   |   |── Admin/
|   |   |   |── AdminPanel.js
|   |   |   |── Card.js
|   |   |   └── Sidebar.js
|   |   └── Home/
|   |   |   └── HomePage.js
|   |   |── LanguageContext.js
|   |   |── NavBar.js
|   |   |── PlayerDashboard.js
|   |   |── Router.js
|   |   └── logo.png
│   ├── App.css
│   ├── App.js
│   ├── App.test.js
│   ├── Layout.js
│   ├── i18n.js
│   ├── index.css
│   ├── index.js
│   ├── logo.svg
│   ├── reportWebVitals.js
│   └── setupTests.js
├── README.md
├── app.py
├── merged_mega.csv
├── package-lock.json
├── package.json
└── tailwind.config.js
```

### Installation and Setup

1. **Clone the repository**
```bash
git clone https://github.com/Devanshu2004/AQe-Digital.git
cd AQe-Digital/HomerunHub
```
2. **Run Jupyter notebooks**
```bash
jupyter notebook
```

### Usage

1. Start with the data exploration notebook to understand the dataset
2. Follow the numbered notebooks in sequence for the complete analysis
3. Refer to the final report for comprehensive findings and recommendations

### Key Learnings

Through this project, I gained experience in:
- Real-world data science project management
- Working with complex, multi-source datasets
- Business-oriented data analysis and interpretation
- Stakeholder communication and presentation
- Industry best practices in data science workflows

### Future Improvements

- Implementation of real-time data processing
- Development of web-based dashboard for interactive exploration
- Integration of additional data sources for enhanced predictions
- Deployment of models for production use

### Acknowledgments

- **AQe Digital** for providing the internship opportunity and project guidance
- **Mentors and colleagues** at AQe Digital for their support and feedback
- **Open-source community** for the tools and libraries that made this project possible

## Contact

**Devanshu**  
Data Science Intern at AQe Digital  
- **GitHub**: [@Devanshu2004](https://github.com/Devanshu2004)
- **Kaggle**: [@devanshujoshi01](https://www.kaggle.com/devanshujoshi01)
- **LinkedIn**: [Devanshu Joshi](https://www.linkedin.com/in/devanshu-joshi-2614d/)
- **Email**: [Devanshu](devanshu1268@gmail.com)

---

**Note**: This project was completed as part of my Data Science Internship at AQe Digital. The code and analysis represent work done under the company's guidance and mentorship.

**Last Updated**: September 2025
