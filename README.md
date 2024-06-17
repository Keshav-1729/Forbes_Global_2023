# Forbes Global 2000 2023 EDA Web Application

This repository contains the implementation of a web application that performs exploratory data analysis (EDA) on the Forbes Global 2000 2023 dataset. The application is built using Streamlit and deployed using Streamlit Cloud.

## Table of Contents

- [Project Description](#project-description)
- [Business Use Case](#business-use-case)
- [Methodology](#methodology)
  - [Data Collection](#data-collection)
  - [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
  - [Web Application](#web-application)
- [Deployment](#deployment)
- [Usage](#usage)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Project Description

This project aims to provide an interactive web application for performing exploratory data analysis on the Forbes Global 2000 2023 dataset. Users can explore various aspects of the dataset through visualizations and insights presented in the web app.

## Business Use Case

The EDA web application can be used by:
- Business analysts and researchers to gain insights into the top global companies.
- Investors to analyze trends and patterns in the financial performance of leading companies.
- Academics and students for educational purposes and data exploration.

## Methodology

### Data Collection

The dataset used in this project is sourced from Forbes Global 2000 2023. It includes various features such as company name, country, industry, revenue, profit, assets, and market value.

### Exploratory Data Analysis (EDA)

EDA was conducted on the dataset to uncover patterns, trends, and relationships within the data. Key steps included:
- Data cleaning and preprocessing to handle missing values and inconsistencies.
- Descriptive statistics to summarize the data.
- Visualization techniques to explore the distribution and correlation of features.

### Web Application

The web application was built using Streamlit, a popular open-source framework for creating interactive web apps with Python. The app allows users to:
- View summary statistics of the dataset.
- Explore various visualizations such as bar charts, histograms, scatter plots, and more.
- Filter and sort data based on different criteria.

## Deployment

The web application is deployed using Streamlit Cloud, making it accessible online for users to interact with. The deployment process involves:
- Creating a Streamlit Cloud account and linking it to the GitHub repository.
- Configuring the deployment settings and requirements.
- Deploying the app and sharing the URL for public access.

## Usage

To run the web application locally, follow these steps:

1. Clone the repository to your local machine:
    ```sh
    git clone https://github.com/yourusername/forbes-global-2000-eda.git
    cd forbes-global-2000-eda
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:
    ```sh
    streamlit run app.py
    ```

4. Access the app in your web browser at `http://localhost:8501`.

To access the deployed web application, visit the URL provided by Streamlit Cloud.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the Streamlit community for their valuable tools and resources.
- Inspired by the need for accessible and interactive data analysis tools.

