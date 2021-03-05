import matplotlib.pyplot as plt
import re

AXES_SIZE = 5  # 设置坐标的宽高
CHINESE_FONT_FAMILY = "Microsoft YaHei"  # 设置使用的中文字体


def use_latex():
    plt.rcParams['text.usetex'] = True
    plt.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'  # 支持LaTeX


def draw_vector(vec, label=None, tail=(0, 0), label_xy=None, color="k"):
    """
    在2D坐标轴上绘制一个向量，加标签

    Matplotlib 将来 再使用 plt.axes() 会创建并返回了，所以调用多次，只能绘制一个向量
    """
    ax = plt.axes()

    # 去除 上、右线
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    # 移动坐标轴
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))
    ax.grid(True)

    ax.set_xlim(-AXES_SIZE, AXES_SIZE)  # 限制 x 轴大小
    ax.set_ylim(-AXES_SIZE, AXES_SIZE)
    ax.set_aspect('equal', adjustable='box')  # 设置整体为立方形，防止格子畸变
    plt.setp(ax.get_xticklabels(), visible=False)  # 去除 x 轴 数字标签
    plt.setp(ax.get_yticklabels(), visible=False)  # 去除 y 轴 数字标签

    ax.set_xticks(range(-AXES_SIZE, AXES_SIZE + 1))  # 以 1 为刻度
    ax.set_yticks(range(-AXES_SIZE, AXES_SIZE + 1))
    ax.quiver(tail[0], tail[1], vec[0], vec[1],
              units="xy", scale=1, color=color)

    if label == None:
        return
    elif len(label) == 1:
        if re.match(r"[A-Z]", label):
            label = "$\overrightarrow {}$".format(label)
        else:
            label = "$\hat {}$".format(label)

    if label_xy == None:
        # 调整 label 坐标位置
        final_point = [vec[0]+tail[0], vec[1]+tail[1]]  # 计算它最后的点
        xy = (
            # x=0时，加0.5
            final_point[0]+0.5 if final_point[0] >= 0 else final_point[0]-0.5,
            # y=0时，减0.5
            final_point[1]+0.5 if final_point[1] > 0 else final_point[1]-0.5,
        )
        ax.annotate(label, xy, fontsize=15,
                    horizontalalignment="center", verticalalignment="center")
    else:
        ax.annotate(label, label_xy, fontsize=15)


# def reset():
#     """
#     调用 `plt.rcdefaults()`
#     """
#     plt.rcdefaults()


def ch_title(title):
    """
    显示中文标题
    """
    plt.title(title, fontfamily=CHINESE_FONT_FAMILY)


# region 扩展方法
# 自定义的扩展方法，用于绘制向量
def axes_draw_vector(self, vec, label=None, tail=(0, 0), label_xy=None, color="k"):
    """
    在2D坐标轴上绘制一个向量，加标签
    """
    # 去除 上、右线
    self.spines['top'].set_color('none')
    self.spines['right'].set_color('none')
    # 移动坐标轴
    self.xaxis.set_ticks_position('bottom')
    self.spines['bottom'].set_position(('data', 0))
    self.yaxis.set_ticks_position('left')
    self.spines['left'].set_position(('data', 0))
    self.grid(True)

    self.set_xlim(-AXES_SIZE, AXES_SIZE)  # 限制 x 轴大小
    self.set_ylim(-AXES_SIZE, AXES_SIZE)
    self.set_aspect('equal', adjustable='box')  # 设置整体为立方形，防止格子畸变
    plt.setp(self.get_xticklabels(), visible=False)  # 去除 x 轴 数字标签
    plt.setp(self.get_yticklabels(), visible=False)  # 去除 y 轴 数字标签

    self.set_xticks(range(-AXES_SIZE, AXES_SIZE + 1))  # 以 1 为刻度
    self.set_yticks(range(-AXES_SIZE, AXES_SIZE + 1))
    self.quiver(tail[0], tail[1], vec[0], vec[1],
                units="xy", scale=1, color=color)

    if label == None:
        return
    elif len(label) == 1:
        import re
        if re.match(r"[A-Z]", label):  # 大写的标签 上面是右箭头
            label = "$\overrightarrow {}$".format(label)
        else:
            label = "$\hat {}$".format(label)

    if label_xy == None:
        # 调整 label 坐标位置
        final_point = [vec[0]+tail[0], vec[1]+tail[1]]  # 计算它最后的点
        xy = (
            # x=0时，加0.5
            final_point[0]+0.5 if final_point[0] >= 0 else final_point[0]-0.5,
            # y=0时，减0.5
            final_point[1]+0.5 if final_point[1] > 0 else final_point[1]-0.5,
        )
        self.annotate(label, xy, fontsize=15,
                      horizontalalignment="center", verticalalignment="center")
    else:
        self.annotate(label, label_xy, fontsize=15)


def axes_ch_title(self, title, fontsize=plt.rcParams['axes.titlesize']):
    """
    显示中文标题
    """
    self.set_title(title, fontsize=fontsize, fontfamily=CHINESE_FONT_FAMILY)


def figure_ch_title(self, title, fontsize=plt.rcParams['axes.titlesize']):
    """
    显示中文标题
    """
    self.suptitle(title, fontsize=fontsize, fontfamily=CHINESE_FONT_FAMILY)
# endregion
