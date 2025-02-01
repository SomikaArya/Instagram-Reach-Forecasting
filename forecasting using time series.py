from plotly.tools import mpl_to_plotly
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

data = data[["Date", "Instagram reach"]]

result = seasonal_decompose(data['Instagram reach'], 
                            model='multiplicative', 
                            period=100)

plt = plt.figure()
plt = result.plot()

plt = mpl_to_plotly(plt)
plt.show()

pd.plotting.autocorrelation_plot(data["Instagram reach"])

from statsmodels.graphics.tsaplots import plot_pacf
plot_pacf(data["Instagram reach"], lags = 100)
