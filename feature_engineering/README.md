# 🔧 Feature Engineering

Feature engineering is a crucial step in building effective machine learning models. This directory contains scripts and notebooks used to process and transform raw Swiggy delivery data into informative features that improve prediction accuracy.

## 📁 Directory Contents

- `Data_Cleaning.ipynb` - Data cleaning and preprocessing pipeline
- `Food_Delivery_EDA.ipynb` - Exploratory Data Analysis and insights
- `Missing_value_imputation.ipynb` - Handling missing values and data imputation
- `Full_project.ipynb` - Complete end-to-end project workflow

## 🔄 Feature Engineering Pipeline

### 1. Data Cleaning & Preprocessing
- **Duplicate Removal**: Identifying and removing duplicate records
- **Data Type Conversion**: Ensuring proper data types for each feature
- **Outlier Detection**: Statistical methods to identify and handle outliers
- **Data Validation**: Checking for logical consistency in the data

### 2. Missing Value Imputation
- **Numerical Features**: Mean, median, or mode imputation based on distribution
- **Categorical Features**: Most frequent category or domain-specific imputation
- **Advanced Techniques**: KNN imputation, iterative imputation
- **Pattern Analysis**: Understanding missing data patterns (MCAR, MAR, MNAR)

### 3. Feature Creation & Transformation

#### Temporal Features
- `order_time_of_day` - Hour-based categorization (Morning, Afternoon, Evening, Night)
- `is_weekend` - Binary indicator for weekend orders
- `pickup_time` - Time taken for order preparation

#### Categorical Encoding
- **One-Hot Encoding**: For nominal categorical variables
- **Label Encoding**: For ordinal categorical variables
- **Target Encoding**: For high-cardinality categorical features

#### Numerical Features
- **Distance Normalization**: Scaling delivery distances
- **Rating Standardization**: Normalizing restaurant and delivery ratings
- **Log Transformations**: For skewed numerical distributions

#### Derived Features
- **Distance Categories**: Short, Medium, Long distance delivery classifications
- **Rush Hour Indicators**: Peak delivery time identifiers
- **Weather Impact Scores**: Combined weather and traffic effects
- **Vehicle Efficiency Metrics**: Vehicle type and condition combinations

### 4. Feature Scaling & Normalization
- **StandardScaler**: Zero mean, unit variance scaling
- **MinMaxScaler**: Scaling to [0,1] range
- **RobustScaler**: Handling outliers in scaling process

## 📊 Exploratory Data Analysis (EDA)

### Key Insights Discovered

#### Order Patterns
- **Peak Hours**: Lunch (12-2 PM) and dinner (7-9 PM) show highest order volumes
- **Weekend Effect**: 15-20% increase in delivery times during weekends
- **Festival Impact**: Significant delays during festival periods

#### Geographic Analysis
- **City Type Distribution**: Urban vs. suburban delivery patterns
- **Distance Patterns**: Most deliveries within 5km radius
- **Traffic Correlation**: Strong correlation between traffic and delivery time

#### Vehicle & Logistics
- **Vehicle Performance**: Motorcycles fastest for short distances, cars better for long distances
- **Multiple Deliveries**: Batch deliveries increase individual delivery times
- **Weather Impact**: Rain increases delivery time by 20-30%

### Statistical Summary
```python
# Example feature statistics
Distance: Mean=3.2km, Std=2.1km, Range=[0.5km, 15km]
Delivery Time: Mean=28min, Std=12min, Range=[10min, 90min]
Weather Clear: 65%, Cloudy: 20%, Rain: 15%
```

## 🛠️ Feature Engineering Techniques

### Custom Transformers
```python
class DeliveryFeatureTransformer:
    def __init__(self):
        self.scaler = StandardScaler()
        self.encoder = LabelEncoder()
    
    def fit_transform(self, X):
        # Custom transformation logic
        return transformed_features
```

### Feature Selection Methods
- **Correlation Analysis**: Removing highly correlated features
- **Mutual Information**: Selecting features with high target correlation
- **Recursive Feature Elimination**: Backward feature selection
- **LASSO Regularization**: L1 regularization for automatic feature selection

## 📈 Feature Importance Analysis

### Top Predictive Features
1. **Distance** (0.25) - Primary factor in delivery time
2. **Traffic Conditions** (0.18) - Major environmental factor
3. **Order Time** (0.15) - Peak hours significantly impact delivery
4. **Weather** (0.12) - Adverse weather increases delivery time
5. **Vehicle Type** (0.10) - Different vehicles have different speeds

### Feature Engineering Impact
- **Baseline Model**: R² = 0.72
- **After Feature Engineering**: R² = 0.89
- **Performance Improvement**: 23.6% increase in predictive accuracy

## 🔧 Data Processing Pipeline

### Preprocessing Steps
```python
# Example preprocessing pipeline
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

preprocessor = ColumnTransformer([
    ('num', StandardScaler(), numerical_features),
    ('cat', OneHotEncoder(), categorical_features)
])

pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('model', model)
])
```

### Quality Checks
- **Data Integrity**: Checking for impossible values (negative distances, etc.)
- **Feature Distribution**: Ensuring proper feature distributions
- **Target Variable**: Validating delivery time ranges
- **Temporal Consistency**: Checking order and pickup time logic

## 📊 Data Quality Metrics

### Before Processing
- **Missing Values**: 12% of records had missing values
- **Duplicates**: 3% duplicate records identified
- **Outliers**: 5% of records flagged as outliers
- **Inconsistencies**: 2% logical inconsistencies found

### After Processing
- **Data Completeness**: 100% complete dataset
- **Quality Score**: 98% data quality score
- **Feature Correlation**: Maximum correlation < 0.85
- **Distribution Normality**: 85% of features follow normal distribution

## 🚀 Usage Instructions

### Running the Notebooks
1. **Setup Environment**:
   ```bash
   pip install pandas numpy scikit-learn matplotlib seaborn
   ```

2. **Execute in Order**:
   - Start with `Data_Cleaning.ipynb`
   - Run `Food_Delivery_EDA.ipynb` for insights
   - Use `Missing_value_imputation.ipynb` for data completion
   - Review `Full_project.ipynb` for complete workflow

### Custom Feature Engineering
```python
# Example custom feature creation
def create_rush_hour_feature(order_time):
    rush_hours = [(11, 14), (18, 21)]  # Lunch and dinner
    return any(start <= order_time.hour <= end for start, end in rush_hours)

df['is_rush_hour'] = df['order_time'].apply(create_rush_hour_feature)
```

## 🤝 Contributing

When adding new features or improvements:
1. Document the feature engineering rationale
2. Include statistical validation of new features
3. Update feature importance analysis
4. Maintain backward compatibility
5. Add unit tests for custom transformers

---

For detailed implementation examples, refer to the Jupyter notebooks in this directory.

