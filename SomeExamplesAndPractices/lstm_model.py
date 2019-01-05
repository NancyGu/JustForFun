# using keras
# coding=utf-8
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense, Activation

# look the relationship by time
file_path = "../data/time_passenger_data.csv"
def make_plot():
    df = pd.read_csv('../data/time_passenger_data.csv', sep=',')
    df = df.set_index('time')
    df['passengers'].plot()
    plt.show()
#make_plot()



def load_data( sequence_length=5, split=0.8):
    # sequence_length : 分组。10个一组做训练
    df = pd.read_csv(file_path, sep=',')
    df = df[['passengers']]
    data_all = np.array(df).astype(float)
    scaler = MinMaxScaler()
    data_all = scaler.fit_transform(data_all)
    data = [] # 分好组的数据 1-11 2-12 共计144-10-1 = 133组
    for i in range(len(data_all) - sequence_length - 1):
        data.append(data_all[i: i + sequence_length + 1])
    reshaped_data = np.array(data).astype('float64') # 11*133
    np.random.shuffle(reshaped_data) #打乱顺序

    # 对x进行统一归一化，而y则不归一化
    x = reshaped_data[:, :-1] #每组逆序
    y = reshaped_data[:, -1]  #每组取一个
    #print(len(y))
    split_boundary = int(reshaped_data.shape[0] * split)
    train_x = x[: split_boundary]
    test_x = x[split_boundary:]
    #print(test_x)
    train_y = y[: split_boundary]
    test_y = y[split_boundary:]
    return train_x, train_y, test_x, test_y, scaler

def build_model():
    # input_dim是输入的train_x的最后一个维度，train_x的维度为(n_samples, time_steps, input_dim)
    model = Sequential()
    model.add(LSTM(input_dim=1, output_dim=50, return_sequences=True))
    print(model.layers)
    model.add(LSTM(100, return_sequences=False))
    model.add(Dense(output_dim=1))
    model.add(Activation('linear'))

    model.compile(loss='mse', optimizer='rmsprop')
    return model


def train_model(model,train_x, train_y, test_x, test_y):
    try:
        model.fit(train_x, train_y, batch_size=10, nb_epoch=5, validation_split=0.1)
        predict = model.predict(test_x)
        predict = np.reshape(predict, (predict.size, ))
    except KeyboardInterrupt:
        print(predict)
        print(test_y)
    print(predict)
    print(test_y)
    #try:
        #fig = plt.figure(1)
        #plt.plot(predict, 'r:')
        #plt.plot(test_y, 'g-')
        #plt.legend(['predict', 'true'])
    #except Exception as e:
        #print(e)
    return predict, test_y


if __name__ == '__main__':
    train_x, train_y, test_x, test_y, scaler = load_data()
    #print("train_x:",train_x,"train_y:",train_y)
    #print(len(test_x),test_x[0])
    print train_x.shape, len(train_x.shape[0])

    train_x = np.reshape(train_x, (train_x.shape[0], train_x.shape[1], 1))
    test_x = np.reshape(test_x, (test_x.shape[0], test_x.shape[1], 1))

    #model = build_model()
    #predict_y, test_y = train_model(model,train_x, train_y, test_x, test_y)

    #predict_y = scaler.inverse_transform([[i] for i in predict_y])
    #test_y = scaler.inverse_transform(test_y)
    #fig2 = plt.figure(2)
    #plt.plot(predict_y, 'g:')
    #plt.plot(test_y, 'r-')
    #plt.show()
    print("------------------------------------------")
    sequence_length = 5

    file_path = "../data/time_passenger_data.csv"
    s_df = pd.read_csv(file_path, sep=',')
    df = pd.read_csv('../data/pre.csv', sep=',')
    pre = pd.concat([s_df, df], axis=0)
    p = pre[['passengers']]
    p = p.tail(len(df)*5)

    scaler = MinMaxScaler()
    p = scaler.fit_transform(p)

    np.random.shuffle(p)  # 打乱顺序
    # p = p[:, :-1]  # 每组逆序

    x = np.array(p)
    #predict = model.predict(x.reshape(len(x) / 5, 5, 1))
    #print(predict)