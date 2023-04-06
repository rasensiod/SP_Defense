from Module.data_preprocessing import *
from Neural_Network.Base_model import *
from Random_Forest.rf_model import *
from Module.notification_sns import *

#============== Loading testset ==============
print("\n==============Loading model and weights==============")
df = pd.read_csv('./Dataset/df_sample.csv')
df_std, df_Y = normalization(df)

#============== Loading NN Model ==============
model = Base_NN()
model.load_weights('./Model/NN_large.h5')

#============== Test ==============
#Using the first data pakcet to simulate the real-time attack and detect which ddos attack it is
print("\n\n==============Simulating ddos attack and detect==============")
Y_pred_classes = model.test_demo(df_std)
ddos_type = covert_label(Y_pred_classes[0])
print(f"Warning: A kind of {ddos_type} has been detected!")

#============== Notification ==============
print("\n==============Triggering notification service==============")
notification(ddos_type)






