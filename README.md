                                        Company's Employee Attrition Case
Definition: -
Employee Attrition refers to the situation where an employee leaves the company for several reasons such as lack of job satisfaction, poor performance evaluation, less salary or even the burden of work can sometimes take its toll on the employees.
Apart from that, there could be situations when the company had to layoff their employees due to cost costing or other financial related issues. High attrition rate sends a wrong signal to the existing employees as well as to the prospective employees.

Objective: -
Given a two dataset – one with the employees that has already left and the other is about the existing employees.
The objective is to find out what type of employees are leaving, which employees are prone to leave next. 

Understanding the Data: -
Gathering the data and then understanding it to proceed further in the problem set is pivotal for effective analysis. 
The .xlsx sheet provided has two separate tabs – one with ‘Existing employees’ and other with ‘Employees who have left’.
Both of this tabs has the following features –
Emp ID, satisfaction_level, last_evaluation , number_project, average_montly_hours, time_spend_company, Work_accident, promotion_last_5years, Dept, salary 




Conclusion from the Feature Selection methods: -
Based on the visualisation and the dimensionality reduction methods, here are the factors which contributes most to the employee attrition.
•	Low Satisfaction level. 
•	Poor last evaluation.
•	No promotion in the last 5 years.
•	Employees with 3-4 years of experience has more chances of leaving than those who has more than 5 years.
•	More number of projects.
•	Less Salary
So the features I have used for my prediction are – satisfaction_level, last_evaluation, promotion_last_5years, ‘time_spend_company’, number_project and salary.

Metric Validation: -
•	The Random Forest Classifier gave an accuracy of 98.53%, a precision of 98% and a recall of 95.7%.
•	The Decision Tree Classifier gave an accuracy of 97.15%, a precision of 92.5% and a recall of 95.55#%
•	The Gradient Boosting Classifier gave an accuracy of 96.55%, a precision of 94.33% and a recall of 90.8%.

Conclusion:-
Based on the previous metric scores, it could be concluded that the Random Forest Classifier is the best predicator for the dataset and it has correctly predicted which employees will stay and who are prone to leave the company









