from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

die_1 = Die()
die_2 = Die(10)

results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

freq = []
max_result = die_1.num_sides + die_2.num_sides
for val in range(1, max_result+1):
    freq1 = results.count(val)
    freq.append(freq1)


x_val = list(range(2, max_result+1))
data = [Bar(x=x_val, y=freq)]

x_axis_config = {"title":"Result", "dtick":1}
y_axis_config = {"title":"Frequency of result"}
my_layout = Layout(title="Result of rolling D6 and D10 50.000 times", xaxis = x_axis_config, yaxis=y_axis_config)
offline.plot({"data":data, "layout":my_layout}, filename="d6_d10.html")

