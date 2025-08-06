# Feature Engineering

Feature engineering is a crucial step in building effective machine learning models. This section contains scripts used to process and transform raw Swiggy delivery data into informative features that improve prediction accuracy.

##  Directory Contents

- `Data_Cleaning.ipynb` - Data cleaning and preprocessing pipeline
- `Food_Delivery_EDA.ipynb` - Exploratory Data Analysis and insights
- `Missing_value_imputation.ipynb` - Handling missing values and data imputation
- `Full_project.ipynb` - Complete end-to-end project workflow

### Feature Creation & Transformation

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

  ### Missing Value Imputation
- **Numerical Features**: Mean, median, or mode imputation based on distribution
- **Categorical Features**: Most frequent category or domain-specific imputation
- **Advanced Techniques**: KNN imputation, iterative imputation
- **Pattern Analysis**: Understanding missing data patterns (MCAR, MAR, MNAR)
