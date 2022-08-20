from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

die = Die()

results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

freq = []
for val in range(1, die.num_sides+1):
    freq1 = results.count(val)
    freq.append(freq1)


x_val = list(range(1, die.num_sides+1))
data = [Bar(x=x_val, y=freq)]

x_axis_config = {"title":"Result"}
y_axis_config = {"title":"Frequency of result"}
my_layout = Layout(title="Result of rolling one D6 1.000 times", xaxis = x_axis_config, yaxis=y_axis_config)
offline.plot({"data":data, "layout":my_layout}, filename="d6.html")