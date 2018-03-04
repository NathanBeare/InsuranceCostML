# Unfair-Healthcare
Medical Treatment Cost Inequalities by State

This program utilizes the data set from Kaggle.com "Hospital Charges for Inpatients"
(https://www.kaggle.com/speedoheck/inpatient-hospital-charges)

This dataset contains about 100,000 rows of data regarding patient's visits to hospitals and total charges incurred

We parsed our data to filter our reasons for medical treatment into 8 major diagnosis

In addition we created a dictionary of our states in alphabetical order (plus D.C) on {0,50}

The selection of medical diagnosis is plugged into our model, which in return calculates the national average cost, as well 
as each individual state's average cost, and displays the the lowest value and its state acronym

A bar graph is displayed in addition of each state's average cost, and the national average for the corresponding diagnosis
