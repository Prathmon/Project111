import plotly.graph_objects as go
import plotly.figure_factory as ff
import statistics as ss
import pandas as pd
import random

file1 = pd.read_csv("medium_data.csv")
data = file1["reading_time"].to_list()
population_mean = ss.mean(data)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data))
        value = data[random_index]
        dataset.append(value)
    mean = ss.mean(dataset)
    return mean

def show_fig(mean_list):
    daf = mean_list
    fig = ff.create_distplot([daf], ["time"], show_hist = False)
    fig.show()

mean_list = []
for i in range(0, 100):
    set_of_mean = random_set_of_mean(30)
    mean_list.append(set_of_mean)
show_fig(mean_list)

stdev = ss.mean(mean_list)
mean = ss.mean(mean_list)

first_stdev_start, first_stdev_end = mean-stdev, mean+stdev
second_stdev_start, second_stdev_end = mean-(2*stdev), mean+(2*stdev)
third_stdev_start, third_stdev_end = mean-(3*stdev), mean+(3*stdev)
print("std1", first_stdev_start, first_stdev_end)
print("std2", second_stdev_start, second_stdev_end)
print("std3", third_stdev_start, third_stdev_end)

fig = ff.create_distplot([mean_list], ["time"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.6], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x = [first_stdev_start, first_stdev_start], y = [0, 0.6], mode = "lines", name = "STANDARD DEVIATION 1 START"))
fig.add_trace(go.Scatter(x = [first_stdev_end, first_stdev_end], y = [0, 0.6], mode = "lines", name = "STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x = [second_stdev_start, second_stdev_start], y = [0, 0.6], mode = "lines", name = "STANDARD DEVIATION 2 START"))
fig.add_trace(go.Scatter(x = [second_stdev_end, second_stdev_end], y = [0, 0.6], mode = "lines", name = "STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x = [third_stdev_start, third_stdev_start], y = [0, 0.6], mode = "lines", name = "STANDARD DEVIATION 3 START"))
fig.add_trace(go.Scatter(x = [third_stdev_end, third_stdev_end], y = [0, 0.6], mode = "lines", name = "STANDARD DEVIATION 3 END"))
fig.show()

df = pd.read_csv("sample_2.csv")
data2 = df["reading_time"].to_list()
mean_of_sample2 = ss.mean(data2)
print("Mean of sample 2:- ", mean_of_sample2)
fig = ff.create_distplot([mean_list], ["time"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.6], mode = "lines", name = "SAMPLING MEAN"))
fig.add_trace(go.Scatter(x = [mean_of_sample2, mean_of_sample2], y = [0, 0.6], mode = "lines", name = "MEAN OF SAMPLE 2"))
fig.add_trace(go.Scatter(x = [first_stdev_end, first_stdev_end], y = [0, 0.6], mode = "lines", name = "STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x = [second_stdev_end, second_stdev_end], y = [0, 0.6], mode = "lines", name = "STANDARD DEVIATION 2 END"))
fig.show()

z_score = (mean_of_sample2 - mean)/stdev
print("Z-score is ", z_score)