import pandas as pd
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR


def sort_dataset(dataset_df):
    sort_df=dataset_df.sort_values(by='year')
    return sort_df


def split_dataset(dataset_df):	
    X = dataset_df.drop(columns="salary", axis=1)
    y = dataset_df["salary"] * 0.001  

    X_train = X[:1718]  
    X_test = X[1718:]   
    y_train = y[:1718]  
    y_test = y[1718:]

    return X_train, X_test, y_train, y_test

def extract_numerical_cols(dataset_df):
    extract_df = dataset_df[['age', 'G', 'PA', 'AB', 'R', 'H', '2B', '3B', 'HR', 'RBI', 'SB', 'CS', 'BB', 'HBP', 'SO', 'GDP', 'fly', 'war']]
    return extract_df

def train_predict_decision_tree(X_train, Y_train, X_test):
    dt_reg = DecisionTreeRegressor() 
    dt_reg.fit(X_train, Y_train)
    predictions = dt_reg.predict(X_test)
    return predictions


def train_predict_random_forest(X_train, Y_train, X_test):
    rf_reg = RandomForestRegressor()
    rf_reg.fit(X_train, Y_train)
    predictions = rf_reg.predict(X_test)
    return predictions

def train_predict_svm(X_train, Y_train, X_test):
    svr_pipe = make_pipeline(
        StandardScaler(),
        SVR()
    )
    svr_pipe.fit(X_train, Y_train)
    predictions = svr_pipe.predict(X_test)
    return predictions

def calculate_RMSE(labels, predictions):
    cal_RMSE = np.sqrt(np.mean((predictions-labels)**2))
    return cal_RMSE

if __name__=='__main__':
	#DO NOT MODIFY THIS FUNCTION UNLESS PATH TO THE CSV MUST BE CHANGED.
	data_df = pd.read_csv('2019_kbo_for_kaggle_v2.csv')
	
	sorted_df = sort_dataset(data_df)	
	X_train, X_test, Y_train, Y_test = split_dataset(sorted_df)
	
	X_train = extract_numerical_cols(X_train)
	X_test = extract_numerical_cols(X_test)

	dt_predictions = train_predict_decision_tree(X_train, Y_train, X_test)
	rf_predictions = train_predict_random_forest(X_train, Y_train, X_test)
	svm_predictions = train_predict_svm(X_train, Y_train, X_test)
	
	print ("Decision Tree Test RMSE: ", calculate_RMSE(Y_test, dt_predictions))	
	print ("Random Forest Test RMSE: ", calculate_RMSE(Y_test, rf_predictions))	
	print ("SVM Test RMSE: ", calculate_RMSE(Y_test, svm_predictions))