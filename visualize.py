import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

pallete = ['darkgreen', 'tomato', 'yellow', 'darkblue', 'darkviolet', 'indianred', 'yellowgreen', 'mediumblue', 'cyan',
           'black', 'indigo', 'pink', 'lime', 'sienna', 'plum', 'deepskyblue', 'forestgreen', 'fuchsia', 'brown',
           'turquoise', 'aliceblue', 'blueviolet', 'rosybrown', 'powderblue', 'lightblue', 'skyblue', 'lightskyblue',
           'steelblue', 'dodgerblue', 'lightslategray', 'lightslategrey', 'slategray', 'slategrey', 'lightsteelblue',
           'cornflowerblue', 'royalblue', 'ghostwhite', 'lavender', 'midnightblue', 'navy', 'darkblue', 'blue',
           'slateblue', 'darkslateblue', 'mediumslateblue', 'mediumpurple', 'rebeccapurple', 'darkorchid',
           'darkviolet', 'mediumorchid']
color_pallete = ['lightsalmon', 'lightseagreen', 'lavenderblush', 'aquamarine', 'palegreen', 'yellow', 'firebrick', 'maroon', 'darkred', 'red', 'salmon', 'darksalmon', 'coral', 'orangered',
                 'lightcoral', 'chocolate', 'saddlebrown', 'sandybrown', 'olive', 'olivedrab', 'darkolivegreen',
                 'greenyellow', 'chartreuse', 'lawngreen', 'darkseagreen', 'lightgreen', 'limegreen',
                 'green', 'seagreen', 'mediumseagreen', 'springgreen', 'mediumspringgreen', 'mediumaquamarine',
                 'mediumturquoise', 'lightcyan', 'paleturquoise', 'darkslategray',
                 'darkslategrey', 'teal', 'darkcyan', 'aqua', 'cyan', 'darkturquoise', 'cadetblue', 'thistle',
                 'violet', 'purple', 'darkmagenta', 'magenta', 'orchid', 'mediumvioletred', 'deeppink', 'hotpink',
                 'palevioletred', 'crimson', 'lightpink']


def cuboid_data(o, size=(1, 1, 1)):

    l, w, h = size
    x = [[o[0], o[0] + l, o[0] + l, o[0], o[0]],
         [o[0], o[0] + l, o[0] + l, o[0], o[0]],
         [o[0], o[0] + l, o[0] + l, o[0], o[0]],
         [o[0], o[0] + l, o[0] + l, o[0], o[0]]]
    y = [[o[1], o[1], o[1] + w, o[1] + w, o[1]],
         [o[1], o[1], o[1] + w, o[1] + w, o[1]],
         [o[1], o[1], o[1], o[1], o[1]],
         [o[1] + w, o[1] + w, o[1] + w, o[1] + w, o[1] + w]]
    z = [[o[2], o[2], o[2], o[2], o[2]],
         [o[2] + h, o[2] + h, o[2] + h, o[2] + h, o[2] + h],
         [o[2], o[2], o[2] + h, o[2] + h, o[2]],
         [o[2], o[2], o[2] + h, o[2] + h, o[2]]]
    return np.array(x), np.array(y), np.array(z)


def plotcuboid(pos=(0, 0, 0), size=(1, 1, 1), ax=None, **kwargs):
 
    if ax is not None:
        X, Y, Z = cuboid_data(pos, size)
        ax.plot_surface(X, Y, Z, rstride=1, cstride=1, **kwargs)


def draw(pieces, color_index=[], title=""):
    positions = []
    sizes = []
    colors = []
    sorted_size = []
    for each in pieces:
        positions.append(each[0:3])
        sizes.append(each[3:])
        sorted_size.append(set(each[3:]))
    if len(color_index) == 0:
        colors = pallete[:len(positions)]
        color_index = [sorted_size, colors]
    else:
        dim = color_index[0]
        clr = color_index[1]
        for each in sorted_size:
            index = dim.index(each)
            colors.append(clr[index])
    plt.interactive(True)
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')  
    #ax.set_xticks([0,100,200,300,400,500,600])
    #ax.set_yticks([0,50,100,150,200,250])
    #ax.set_zticks([0,50,100,150,200,250])
    #ax = Axes3D(fig)
    #ax.axes.set_xlim3d(left=0, right=587) 
    #ax.axes.set_ylim3d(bottom=0, top=228) 
    #ax.axes.set_zlim3d(bottom=0, top=259) 
    #ax.set_xlim3d(0, 587)
    #ax.set_ylim3d(0, 228)
    #ax.set_zlim3d(0, 259)
    for p, s, c in zip(positions, sizes, colors):
        plotcuboid(pos=p, size=s, ax=ax, color=c)
    plt.title(title)
    #ax.set_box_aspect((np.ptp(587), np.ptp(228), np.ptp(259)))
    #zline = np.linspace(587, 228, 259)
    #ax.plot3D(0,0,zline, 'gray')
    plt.show()
    return color_index
