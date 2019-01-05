# coding=utf-8
from keras.models import Sequential
from keras.layers import Dense, BatchNormalization, Dropout, LSTM, GRU
from keras.losses import binary_crossentropy, mse

def build_model(feature_num):
    # feature_num:特征数量
    model = Sequential()
    model.add(LSTM(units=128, return_sequences=True, input_shape=(None,feature_num)))
    model.add(LSTM(units=64, return_sequences=True ))
    model.add(LSTM(units=32, return_sequences=False))

    model.add(Dense(1, activation='sigmoid'))
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])
    return(model)

model = build_model(10)
model.summary()