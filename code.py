import random
import plotly.figure_factory as puf
import csv
import statistics as st
import pandas as pd 
import plotly.graph_objects as go

no_of_samples=1000
len_of_sample=100



def read_data(fileName):
    medicham=pd.read_csv(fileName)
    data=medicham["reading_time"]
    mean=st.mean(data)
    std=st.stdev(data)
    return data

def get_sample_mean(data):
    dataset = []
    for i in range(0, len_of_sample):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = st.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    mean = st.mean(df)
    fig = puf.create_distplot([df], ["temp"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="MEAN"))
    fig.show()

def setup():
    fileName="medium_data.csv"
    data= read_data(fileName)
    mean_list = []
    for i in range(0,no_of_samples):
        set_of_means= get_sample_mean(data)
        mean_list.append(set_of_means)
    # show_fig(mean_list)
    # show_fig(data)
    
    mean = st.mean(mean_list)
    sd= st.stdev(mean_list)
    print("Mean of sampling distribution :-",mean )
    print("sd of sampling distribution :-",sd )


#  samples each of length 100
    mean_sample1 =get_sample_mean(data)
    # mean_sample1 =st.mean(sample_data1)

    # sample_data2 = get_sample_mean(data)
    # mean_sample2 =st.mean(sample_data2)

    # sample_data3 = get_sample_mean(data)
    # mean_sample3 =st.mean(sample_data3)

    if sd!=0:
        z1=(mean_sample1-mean)/sd
    else:
        z1=1
    # z2=(mean_sample2-mean)/sd
    # z3=(mean_sample3-mean)/sd

    one_sd_start=mean-sd
    one_sd_end = mean+sd

    two_sd_start=mean-2*sd
    two_sd_end = mean+2*sd

    tree_sd_start=mean-3*sd
    three_sd_end = mean+3*sd
    print(z1)
    fig = puf.create_distplot([mean_list], ["temp"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="MEAN"))
    fig.add_trace(go.Scatter(x=[mean_sample1, mean_sample1], y=[0, 3], mode="lines", name="mean_sample1"))
    # fig.add_trace(go.Scatter(x=[mean_sample2, mean_sample2], y=[0, 1], mode="lines", name="mean_sample2"))
    # fig.add_trace(go.Scatter(x=[mean_sample3, mean_sample3], y=[0, 1], mode="lines", name="mean_sample3"))
    fig.add_trace(go.Scatter(x=[one_sd_start, one_sd_start], y=[0, 3], mode="lines", name="one_sd_start"))
    fig.add_trace(go.Scatter(x=[one_sd_end, one_sd_end], y=[0, 3], mode="lines", name="one_sd_end"))
    fig.add_trace(go.Scatter(x=[two_sd_start, two_sd_start], y=[0, 3], mode="lines", name="two_sd_start"))
    fig.add_trace(go.Scatter(x=[two_sd_end, two_sd_end], y=[0, 3], mode="lines", name="two_sd_end"))
    fig.add_trace(go.Scatter(x=[tree_sd_start, tree_sd_start], y=[0, 3], mode="lines", name="tree_sd_start"))
    fig.add_trace(go.Scatter(x=[three_sd_end, three_sd_end], y=[0, 3], mode="lines", name="three_sd_end"))
   

    
    fig.show()







setup()
