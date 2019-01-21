import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.utils import shuffle
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn import metrics

#Reading the excel file
excelfile = pd.ExcelFile('TakenMind-Python-Analytics-Problem-case-study-1-1.xlsx')

#Parsing individual excel sheets
emp_present = excelfile.parse('Existing employees')
emp_left = excelfile.parse('Employees who have left')

#Adding new column 'left' to both the dataframes with value 1 for left and 0 for present
emp_present['left'] = 0
emp_left['left'] = 1

#Concatenating both the dataframes into a single dataframe
#Merge two dataframes
emp = pd.concat([emp_present, emp_left])

#Shuffling the dataframe to randomize the value of 'left' column for splitting into train and test data
emp = shuffle(emp)
emp = emp.reset_index(drop=True)
#print(emp.head(10))

#Data PreProcessing

#Checking for Null values
#print(emp.isnull().any()) #No missing or NaN values, hence Imputation is not required

#Statistical summary of all the columns
#print(emp.describe())

#Visualizing each feature to see how it effects whether the employee leaves the company or not
features = ['number_project','average_montly_hours','time_spend_company','Work_accident','promotion_last_5years','dept','salary']
fig=plt.subplots(figsize=(30,15))
for i, j in enumerate(features):
    plt.subplot(4, 2, i+1)
    plt.subplots_adjust(hspace = 1.0)
    sns.countplot(x=j,data = emp, hue='left')
    plt.xticks(rotation=90)
    plt.title("No. of employee")
    plt.savefig('employee.png')



#Label encoding the salary and the department  columns as those are categorical data, so converting in to numeric data for prediction

#creating labelEncoder
le = preprocessing.LabelEncoder()
# Converting string labels into numbers.
emp['salary']=le.fit_transform(emp['salary'])

#print(emp['salary'])

#Train and Test data split

X = emp[['satisfaction_level', 'last_evaluation', 'number_project', 'time_spend_company', 'promotion_last_5years', 'salary']].values
y = emp.iloc[:,10].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30, random_state = 0)

#There are a lot of features to choose from, hence using Dimentionality reduction technique to see those features which has most variance using the
#PCA method

#Feature scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()

X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

#Applying PCA
from sklearn.decomposition import PCA

# PCA class will extract top two principal component with the most variance
pca = PCA()

X_train = pca.fit_transform(X_train)
X_test =  pca.transform(X_test)
explained_variance = pca.explained_variance_ratio_

#print (explained_variance)

#Looking at the variance values, its hard to conclude any specific feature whic has the most influence on employee attrition, all the values are
#closer to each other

#Hence taking all the features for our prediction

#-----  Using Random Forest Algorithm ------------

#Fitting Random Forest algorithm to our dataset

from sklearn.ensemble import RandomForestClassifier
rf_classifier = RandomForestClassifier(random_state = 0)
rf_classifier.fit(X_train, y_train)


#Predicting the test results
yrf_pred = rf_classifier.predict(X_test)



print('-------Random Forest Results--------')
#Checking accuracy
print("Accuracy:", metrics.accuracy_score(y_test, yrf_pred))
# Model Precision
print("Precision:",metrics.precision_score(y_test, yrf_pred))
# Model Recall
print("Recall:",metrics.recall_score(y_test, yrf_pred))


# ----- Using Decision Tree Algorithm -------
from sklearn.tree import DecisionTreeClassifier
dt_classifier = DecisionTreeClassifier(random_state = 0)
dt_classifier.fit(X_train, y_train)

#Predicting the test results
ydt_pred = dt_classifier.predict(X_test)

print('-------Decision Tree results--------')
#Checking accuracy
print("Accuracy:", metrics.accuracy_score(y_test, ydt_pred))
# Model Precision
print("Precision:",metrics.precision_score(y_test, ydt_pred))
# Model Recall
print("Recall:",metrics.recall_score(y_test, ydt_pred))




#------ Gradiest Boosting Classifier ------

from sklearn.ensemble import GradientBoostingClassifier
gb_classifier = GradientBoostingClassifier(random_state = 0)
gb_classifier.fit(X_train, y_train)

#Predicting the test results
ygb_pred = gb_classifier.predict(X_test)

print('--------Gradiest Boost results--------')
#Checking accuracy
print("Accuracy:", metrics.accuracy_score(y_test, ygb_pred))
# Model Precision
print("Precision:",metrics.precision_score(y_test, ygb_pred))
# Model Recall
print("Recall:",metrics.recall_score(y_test, ygb_pred))
