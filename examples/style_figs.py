import matplotlib.pyplot as plt


def set_plotting_format(mode):
    # color_blind = plt.cm.cividis(np.linspace(0, 1, 4))
    # color_blind = plt.cm.get_cmap('tableau-colorblind10').colors[:4]
    # plt.style.use(["science"])
    # plt.rcParams["axes.prop_cycle"] = plt.cycler(color=color_blind)
    #
    # color_blind_friendly = [
    #     '#006BA4', '#FF800E', '#ABABAB', '#595959',
    #     '#5F9ED1', '#C85200', '#898989', '#A2C8EC',
    #     '#FFBC79', '#CFCFCF'
    # ]

    # Use the science style
    plt.style.use(["science", 'muted'])

    # Set the color cycle
    # plt.rcParams["axes.prop_cycle"] = plt.cycler(color=color_blind_friendly)

    if mode == "presentation":
        plt.rcParams.update(
            {
                "font.family": "sans-serif",
                "text.usetex": False,
                "font.size": 12,
                "axes.labelsize": 14,
                "lines.linewidth": 2,
                "xtick.major.size": 6,
                "ytick.major.size": 6,
                "xtick.minor.size": 3,
                "ytick.minor.size": 3,
                "xtick.major.width": 1.5,
                "ytick.major.width": 1.5,
                "xtick.minor.width": 1,
                "ytick.minor.width": 1,
            }
        )
    elif mode == "paper":
        plt.rcParams.update(
            {
                "font.family": "sans-serif",
                "text.usetex": False,
                "font.size": 8,
                "axes.labelsize": 10,
                "xtick.major.size": 4,
                "ytick.major.size": 4,
                "xtick.minor.size": 2,
                "ytick.minor.size": 2,
                "xtick.major.width": 1,
                "ytick.major.width": 1,
                "xtick.minor.width": 0.5,
                "ytick.minor.width": 0.5,

            }
        )
