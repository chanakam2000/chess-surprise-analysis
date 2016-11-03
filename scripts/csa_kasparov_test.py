#%%
from python3.csa import csa
import matplotlib.pyplot as plt
import numpy as np
import importlib
import pickle
importlib.reload(csa)
#%matplotlib inline
# Test
# max_depth = list(range(14, 19))
# low_depths = list(range(1, 8))
# depths = low_depths + max_depth


def save_obj(obj, name):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_obj(name):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)


path_to_pgn = '/home/marx/Documents/Programming/python/python3/csa/games/testgames/kasparov_topalov_1999.pgn'
chess_game = csa.load_game_from_pgn(path_to_pgn)
# board = csa.get_board_at_position(chess_game, 13)
# board
# engine = csa.load_engine()
# cp = csa.evaluate_board(board, engine, depths=range(1, 11), verbose=1)


cp, nodes = csa.evaluate_game(chess_game, bln_reset_engine=True, depths=range(1, 11), verbose=1)
save_obj(cp, 'cp')
save_obj(nodes, 'nodes')
#
# list_values = [ v for v in cp[0].values()]
# list_values
# z_lv = (list_values - np.mean(list_values)) / np.std(list_values)
# plt.plot(list_values)
# plt.plot(z_lv)
#
# np.mean(list_values[12::])
# np.mean(list_values[5:11])
# np.std(list_values[5:11])
# surprise_factor = np.mean(list_values[0:11]) - np.mean(list_values[12::])
# surprise_factor

#---------------------------

# cp_per_move, nodes_per_move = csa.evaluate_game(chess_game, depths=depths)
#
# # Plot half moves
# cp_low_history = []
# cp_high_history = []
# for move in cp_per_move:
#     this_move = cp_per_move[move]
#     avg_cp_low = np.mean([this_move[depth] for depth in low_depths])
#     avg_cp_high = np.mean([this_move[depth] for depth in max_depth])
#     cp_low_history.append(avg_cp_low)
#     cp_high_history.append(avg_cp_high)
#     # print(avg_cp_low)
#
# max_diff = np.argmax(np.abs(cp_low_history) - np.abs(cp_high_history))
# cp_low_history_z = (cp_low_history - np.nanmean(cp_low_history)
#                     ) / np.nanstd(cp_low_history)
# cp_high_history_z = (
#     cp_high_history - np.nanmean(cp_high_history)) / np.nanstd(cp_high_history)
# plt.plot(cp_low_history)
# plt.plot(cp_high_history)
# #plt.plot((44, 44), (-800, 600), 'k-')
# plt.legend(['low', 'high'])
# plt.show()

#%%
from bokeh.io import push_notebook, show, output_notebook
from bokeh.layouts import row, gridplot
from bokeh.plotting import figure, show, output_file
output_notebook()

import numpy as np

x = np.linspace(0, 4*np.pi, 100)
y = np.sin(x)
TOOLS = "pan,wheel_zoom,box_zoom,reset,save,box_select"

p1 = figure(title="Legend Example", tools=TOOLS)
p1.circle(x,   y, legend="sin(x)")
p1.circle(x, 2*y, legend="2*sin(x)", color="orange")
p1.circle(x, 3*y, legend="3*sin(x)", color="green")
show(p1)