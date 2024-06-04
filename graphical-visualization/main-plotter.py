import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from database_gen import data_generator as datagen
import algorithm_steps as alg

# getting inputs
datalen = int(input("test array length: "))
max_shuffles = int(input("test array shuffles: "))
print("\n-1 bubble sort"
      "\n-2 insertion sort"
      "\n-3 selection sort"
      "\n-4 bozo sort"
      "\n-5 bogo sort")
sortselection = int(input("//select your sorting method: "))-1

# generating data
data = datagen.shuffle(datagen.generate_data(datalen), max_shuffles)
x_axis = range(len(data))
loop_counter = 0

# creating plots
figure = plt.figure()
ax1 = figure.add_subplot(1, 1, 1)
line = ax1.bar(x_axis, data)

# algorithms list
algorithms = [alg.bubble_step, alg.insertion_step, alg.selection_step, alg.bozo_step, alg.bogo_step]
function_position = sortselection  # change this value to change selected function


def sort_animation(i):
    global loop_counter
    loop_counter = algorithms[function_position](data, loop_counter)

    if(loop_counter>=len(data)):
        ani.event_source.stop()

    for rect, h in zip(line, data):
        rect.set_height(h)


ani = FuncAnimation(plt.gcf(), sort_animation, interval=1, cache_frame_data=False)

plt.tight_layout()
plt.get_current_fig_manager().window.showMaximized()
plt.show()