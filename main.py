from Module.data_preprocessing import *
from Module.data_exploration import *
from Neural_Network.Base_model import *
from Random_Forest.rf_model import *

#============== Loading dataset ==============
df_0311, df_0112 = merge_dataset()
df = loading_dataset(df_0311, df_0112)

#============== Data cleaning & Feature Engineering ==============
df = feature_selection(df)
df_inf, df_std, df_Y, class_weights = data_cleaning(df)

#============== Data exploration ==============
plot_distribution_label(df_inf)
plot_histogram_label(df_inf)
plot_stem_Fwd(df_inf)
plot_bar_Backward(df_inf)
plot_heatmap_features(df_inf)

#============== Dividing dataset ==============
train_X, train_y, valid_x, valid_y, test_X, test_y = dividing_dataset(df_std, df_Y)


#============== Model training & testing ==============
#========= Base Neural Network =========
model = Base_NN()
path_results = './Results_img/base_nn_curves.png'
model.train(train_X, train_y, valid_x, valid_y, path=path_results)
acc_base_nn_score = model.test(test_X, test_y, confusion_mat = True)
print(f'The accuracy score of base_nn model is: {acc_base_nn_score}')

#========= Base Neural Network with weights =========
model = Base_NN()
path_results = './Results_img/base_nn_weighted_curves.png'
model.train_weighted(train_X, train_y, valid_x, valid_y, class_weights, path=path_results)
acc_base_nn_weighted_score = model.test(test_X, test_y, confusion_mat = True)
print(f'The accuracy score of base_nn_weigthed model is: {acc_base_nn_weighted_score}')

#========= Random Forest Model =========
model = random_forest()
model.train(train_X, train_y)
acc_rf_score = model.test(test_X,test_y, confusion_mat = True)
print(f'The accuracy score of rf model is: {acc_rf_score}')

