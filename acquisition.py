import nidaqmx
from nidaqmx.constants import AcquisitionType, TerminalConfiguration
import numpy as np
import matplotlib.pyplot as plt

with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan("Dev1/ai1:2",terminal_config = TerminalConfiguration.RSE, min_val=-10, max_val=10)
    task.timing.cfg_samp_clk_timing(10000.0, sample_mode=AcquisitionType.CONTINUOUS)
    task.start()
    data = task.read(number_of_samples_per_channel=200)
    task.stop()

data = np.array(data)
plt.plot(data[0],'-')    
plt.plot(data[1],'-')
plt.plot(data[0]-data[1],'-')
plt.ylim(-1,1)
plt.grid()
plt.show()