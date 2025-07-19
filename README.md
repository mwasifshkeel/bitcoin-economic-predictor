# Bitcoin Price Prediction using Economic Indicators

A comprehensive data science project that analyzes Bitcoin price movements in relation to economic indicators and news events. This project combines cryptocurrency market data with economic calendar events to build predictive models for Bitcoin price forecasting.

##  Project Overview

This project explores the relationship between Bitcoin price movements and various economic indicators, including:
- **Cryptocurrency Market Data**: Historical Bitcoin price data from Binance API
- **Economic Calendar Events**: Forex Factory economic news and events
- **Machine Learning Models**: Price prediction using multiple algorithms

The goal is to determine if economic events and indicators can be used to predict Bitcoin price movements, providing insights into the correlation between traditional financial markets and cryptocurrency markets.

##  Team Members

| Name | Student ID | GitHub Profile |
|------|------------|----------------|
| Muhammad Muntazar | 470861 | [@Muhammad-Muntazar](https://github.com/overproness) |
| Hafiz Abdul Bast | 472617 | [@Hafiz-Abdul-Bast](https://github.com/230805Abdul) |
| Muhammad Wasif Shakeel | 456092 | [@Muhammad-Wasif-Shakeel](https://github.com/mwasifshkeel) |

##  Project Structure

```
Code/
├── data/                           # Data files
│   ├── btc_historical_data.csv     # Bitcoin historical price data
│   ├── forexfactory_calendar_full.csv # Economic calendar events
│   └── merged_output.csv           # Combined dataset
├── notebooks/                      # Jupyter notebooks
│   ├── Data_Collection.ipynb       # Data collection scripts
│   ├── Dataset_Preprocessing.ipynb # Data cleaning and preprocessing
│   └── IDS_Final_Project.ipynb     # Main analysis and modeling
├── scripts/                        # Python scripts
│   └── newsScrapper.py             # ForexFactory news scraper
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

##  Technology Stack

- **Python 3.8+**: Main programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **Scikit-learn**: Machine learning algorithms
- **XGBoost**: Gradient boosting framework
- **Matplotlib & Seaborn**: Data visualization
- **Selenium**: Web scraping for economic data
- **BeautifulSoup**: HTML parsing
- **Jupyter Notebook**: Interactive development environment

## Prerequisites

Before running this project, ensure you have:

1. **Python 3.8 or higher** installed on your system
2. **Google Chrome browser** (for Selenium web scraping)
3. **ChromeDriver** compatible with your Chrome version
4. **Git** for version control
5. **Jupyter Notebook** or **Jupyter Lab**

##  Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd "Code"
```

### 2. Create Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. ChromeDriver Setup
1. Check your Chrome browser version (Help → About Google Chrome)
2. Download the corresponding ChromeDriver from [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads)
3. Add ChromeDriver to your system PATH or place it in the project directory

### 5. Verify Installation
```bash
python -c "import pandas, numpy, sklearn, xgboost, selenium; print('All packages installed successfully!')"
```

##  Data Sources

### 1. Bitcoin Price Data
- **Source**: Binance API (`https://api.binance.com/api/v3/klines`)
- **Symbol**: BTCUSDT
- **Interval**: 1-hour candles
- **Period**: August 2017 - Present
- **Features**: Open, High, Low, Close prices, Volume

### 2. Economic Calendar Data
- **Source**: ForexFactory Calendar (`https://www.forexfactory.com/calendar`)
- **Period**: April 2017 - November 2019
- **Features**: Event dates, times, currencies, impact levels, actual vs forecast values

## Usage

### 1. Data Collection

#### Collect Bitcoin Data:
```python
# Run the Bitcoin data collection function
from notebooks.Data_Collection import fetch_all_btc_data
fetch_all_btc_data()
```

#### Collect Economic Calendar Data:
```bash
python scripts/newsScrapper.py
```

### 2. Data Processing and Analysis

Open the Jupyter notebooks in order:

1. **Data_Collection.ipynb**: 
   - Contains data collection scripts
   - API calls to Binance
   - Web scraping from ForexFactory

2. **Dataset_Preprocessing.ipynb**:
   - Data cleaning and preprocessing
   - Feature engineering
   - Data merging and alignment

3. **IDS_Final_Project.ipynb**:
   - Exploratory Data Analysis (EDA)
   - Model building and training
   - Results evaluation and visualization

### 3. Running Jupyter Notebooks
```bash
# Start Jupyter Notebook
jupyter notebook

# Or start Jupyter Lab
jupyter lab
```

Navigate to the `notebooks/` directory and run the notebooks in sequence.

##  Key Features

### Data Collection
- **Automated Bitcoin Data Fetching**: Retrieves all available historical data from Binance API
- **Economic Events Scraping**: Multi-threaded scraping of ForexFactory calendar
- **Robust Error Handling**: Automatic backups and recovery mechanisms

### Data Processing
- **Time Series Alignment**: Synchronizes cryptocurrency and economic data
- **Feature Engineering**: Creates technical indicators and event impact scores
- **Data Quality Assurance**: Handles missing values and outliers

### Machine Learning
- **Multiple Algorithms**: Implements various ML models (Linear Regression, Random Forest, XGBoost)
- **Cross-Validation**: Robust model evaluation techniques
- **Performance Metrics**: Comprehensive accuracy and error metrics

##  Expected Outputs

1. **Historical Data Files**:
   - `btc_historical_data.csv`: ~67,000 hourly Bitcoin price records
   - `forexfactory_calendar_full.csv`: ~26,000 economic events

2. **Analysis Results**:
   - Correlation analysis between Bitcoin prices and economic events
   - Feature importance rankings
   - Model performance comparisons
   - Price prediction visualizations

3. **Model Artifacts**:
   - Trained machine learning models
   - Performance metrics and validation results
   - Feature engineering pipelines

##  Important Notes

### Rate Limiting
- **Binance API**: Respects rate limits (1200 requests/minute)
- **ForexFactory Scraping**: Implements delays and concurrent request limits

### Data Availability
- Bitcoin data availability depends on Binance API
- ForexFactory data may have website structure changes over time
- ChromeDriver version must match your Chrome browser version

### Performance Considerations
- Data collection can take 30-60 minutes depending on date range
- Web scraping is I/O intensive and may require stable internet connection
- Machine learning training time varies based on dataset size and model complexity

##  Troubleshooting

### Common Issues

1. **ChromeDriver Issues**:
   ```bash
   # Update ChromeDriver to match Chrome version
   ```

2. **API Rate Limiting**:
   ```python
   # If Binance API calls fail, increase sleep intervals
   time.sleep(1)
   ```

3. **Memory Issues**:
   ```python
   # For large datasets, process data in chunks
   pd.read_csv('large_file.csv', chunksize=1000)
   ```

## Documentation

- **Binance API**: [Official Documentation](https://binance-docs.github.io/apidocs/spot/en/)
- **Selenium**: [Documentation](https://selenium-python.readthedocs.io/)
- **Pandas**: [User Guide](https://pandas.pydata.org/docs/user_guide/)
- **Scikit-learn**: [Documentation](https://scikit-learn.org/stable/)
- **XGBoost**: [Python Package](https://xgboost.readthedocs.io/en/stable/python/)

##  License

This project is developed for academic purposes as part of the Introduction to Data Science course at NUST (National University of Sciences and Technology).

## Acknowledgments

- **NUST Faculty**: For guidance and course structure
- **Binance**: For providing free cryptocurrency market data API
- **ForexFactory**: For economic calendar data
- **Open Source Community**: For the excellent Python libraries used in this project

---

**Note**: This project is for educational purposes only and should not be used for actual financial trading decisions. Cryptocurrency markets are highly volatile and unpredictable.
