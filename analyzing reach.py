#instagram reach trend
plt = go.Figure()
plt.add_trace(go.Scatter(x=data['Date'], 
                         y=data['Instagram reach'], 
                         mode='lines', name='Instagram reach'))
plt.update_layout(title='Instagram Reach Trend', xaxis_title='Date', 
                  yaxis_title='Instagram Reach')
plt.show()

#Instagram Reach by Day
plt = go.Figure()
plt.add_trace(go.Bar(x=data['Date'], 
                     y=data['Instagram reach'], 
                     name='Instagram reach'))
plt.update_layout(title='Instagram Reach by Day', 
                  xaxis_title='Date', 
                  yaxis_title='Instagram Reach')
plt.show()

#Instagram Reach Box Plot
plt = go.Figure()
plt.add_trace(go.Box(y=data['Instagram reach'], 
                     name='Instagram reach'))
plt.update_layout(title='Instagram Reach Box Plot', 
                  yaxis_title='Instagram Reach')
plt.show()
