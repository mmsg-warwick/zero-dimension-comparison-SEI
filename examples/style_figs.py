"""
Styling configurations using SciencePlots for project figures and charts.
"""
import matplotlib.pyplot as plt
import scienceplots  # noqa: F401 - Required for plt.style.use(["science", 'muted'])


def set_plotting_format(mode):
    plt.style.use(["science", 'muted'])

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
