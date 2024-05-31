import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from database_gen import data_generator as datagen
import algorithm_steps as alg

data = datagen.shuffle(datagen.generate_data(100), 100)
x_axis = range(len(data))
loop_counter = 0

algorithms = [alg.bubble_step, alg.insertion_step, alg.selection_step]
function_position = 0  # change this value to change selected function


def sort_animation(i):
    global loop_counter
    algorithms[function_position](data, loop_counter)
    loop_counter += 1

    if(loop_counter==len(data)):
        ani.event_source.stop()

    plt.cla()
    plt.plot(x_axis, data)


ani = FuncAnimation(plt.gcf(), sort_animation, interval=0, cache_frame_data=False)

plt.tight_layout()
plt.show()