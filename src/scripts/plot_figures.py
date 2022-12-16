from pathlib import Path
from matplotlib import pyplot as plt, cycler, rcParams, cm
import numpy as np

#cmap = cm.get_cmap("Set2").colors
#rcParams['axes.prop_cycle'] = cycler(color=cmap)

rcParams['axes.prop_cycle']= cycler('color',["xkcd:orangeish","xkcd:light navy blue",\
        "xkcd:coral pink","xkcd:soft blue","xkcd:teal blue","xkcd:pale magenta",\
        "xkcd:sand brown","xkcd:dusky rose", "xkcd:bluish green",\
        "xkcd:orange yellow","xkcd:dull red","xkcd:sage","xkcd:bluey grey"])

Path("./figures/").mkdir(parents=True, exist_ok=True) # make sure subdirectory figures exists

wine = '#882255'
teal = '#44AA99'
green = '#117733'
olive = '#999933'
cyan = '#88CCEE'

def plot_imshow(im, xlabel="x [pixels]", ylabel="y [pixels]", plottitle=None, vmin=None, vmax=None, figsize=(5,5),
                extent=None, norm=None, r_trim=0, cbarlabel="count", fig=None, ax=None, origin="lower", cmap="gray",
                interpolation=None, cx=None, cy=None):
    """Plot imshow of im
    Optionally provide different axlabels and cbarlabel (default is x [pixels], y [pixels], count)
    Optionally provide plottitle, default is None
    Optionally provide vmin and vmax
    Optionally provide figsize
    Optionally adjust extent
    Optionally cut out center square with diameter 2*trim + 1
    """
    im2 = im.copy()
    if fig is None:
        fig, ax = plt.subplots(1, figsize=figsize)
    if r_trim>0:
        (nx,ny) = im.shape
        if cx is None:
            cx = int((nx-1) / 2)
        if cy is None:
            cy = int((ny-1) / 2)
        im2 = im2[cy-r_trim:cy+r_trim+1, cx-r_trim:cx+r_trim+1]
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    fig.suptitle(plottitle, fontsize=16)
    image = ax.imshow(im2, vmin=vmin, vmax=vmax, extent=extent, norm=norm, origin=origin, cmap=cmap, interpolation=interpolation)
    plt.colorbar(image, ax=ax, label=cbarlabel, fraction=0.0453)
    plt.tight_layout()
    return fig, ax, image


def plot_xy(x, y_all, linelabels="", xlabel="default", xscale="linear",yscale="linear",
                  ylabel="default", figsize=(10,8), plottitle=None, vspans_min=None, vspans_max=None,
                  hlines=None, hlinelabels="", vlines=None, vlinelabels="", yinvert=False,
                  vspanlabels="",subdir="uncategorised/", filename="xy", ext=".png"):
    """Plot xy-plot.
    Default is x and y labels is columnnames if available, else "provide label"
    Provide subdirectory for saving figure, otherwise it gets placed in figures/uncategorised
    Provide filename, otherwise gets saved as xy.png
    Optionally change xscale (default is linear), yscale (default is linear)
    Optionally provide plottitle
    Optionally change figsize
    Optionally change extension (default is png)
    Optionally add hlines
    Optionally add vspan
    Optionally set yinvert to True to invert y-axis
    """
    dir = "./figures/" + subdir
    Path(dir).mkdir(parents=True, exist_ok=True)  # make sure subdirectory figures exists
    fig, ax = plt.subplots(1, figsize=figsize)
    if type(y_all) != list:
        y_all = [y_all]
    if type(linelabels) != list:
        linelabels = [linelabels]
    if type(x) != list:
        for y, label in zip(y_all, linelabels):
            ax.plot(x, y, lw=1, label=label)
    else:
        for x_p, y, label in zip(x, y_all, linelabels):
            ax.plot(x_p, y, lw=1, label=label)
    # colours for spans and lines
    colours = ["xkcd:marine","xkcd:bluey grey","xkcd:coral pink", "xkcd:bluish green", "xkcd:teal blue"]
    if hlines is not None:
        if type(hlines) != list:
            hlines = [hlines]
        for i, (hline, hlabel) in enumerate(zip(hlines, hlinelabels)):
            ax.axhline(y=hline, linestyle="--", label=hlabel, alpha=0.6, c=colours[i])
    if vlines is not None:
        if type(vlines) != list:
            vlines = [vlines]
        for i, (vline, vlabel) in enumerate(zip(vlines, vlinelabels)):
            ax.axvline(x=vline, linestyle="--", label=vlabel, alpha=0.6, c=colours[i])
    if vspans_min is not None:
        if type(vspans_min) != list:
            vspans_min = [vspans_min]
        if type(vspans_max) != list:
            vspans_max = [vspans_max]
        if type(vspanlabels) != list:
            vspanlabels = [vspanlabels]
        for i, (vspan_min, vspan_max, vspanlabel) in enumerate(zip(vspans_min, vspans_max, vspanlabels)):
            ax.axvspan(vspan_min, vspan_max, alpha=0.2, color=colours[i], label=vspanlabel)
    if xlabel == "default":
        try:
            xlabel = x.name
        except:
            xlabel = "provide xlabel"
    if ylabel == "default":
        try:
            ylabel  = y_all[0].name
        except:
            ylabel = "provide ylabel"
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.xscale(xscale)
    plt.yscale(yscale)
    if yinvert==True:
        ax.invert_yaxis()
    plt.legend(loc="best")
    fig.suptitle(plottitle, fontsize=18)
    plt.tight_layout()
    plt.savefig(dir + filename + ext)
    plt.close(fig)

def plot_errorbar(x, y_all, y_all_err=None, linelabels="", xhlines=None, xhlinelabels=None, xlabel="default",
                  xscale="linear",yscale="linear",ylabel="default", figsize=(10,8), plottitle=None, axvspans_min=None,
                  xylines_x=None, xylines_y=None, xylinelabels="", colours=None,
                  axvspans_max=None, linestyle="None", linewidth=1, yinvert=False, fig=None, ax=None, cs=2, ms=4):
    """Plot errorbar-plot.

    Arguments:
    If no fig and ax instance is given, create new fig and ax
        - Optionally change figsize
    If fig and ax is provide, use provided fig and ax
    Default is x and y labels is columnnames if available, else "provide label"
    Optionally change xscale (default is linear), yscale (default is linear)
    Optionally change linestyle, default is "None"
    Optional change linewidth, default is 1
    Optionally provide plottitle
    Optionally add hlines
    Optionally add vspan
    Optionally add a lineplot
    Optionally set yinvert to True to invert y-axis

    Return fig and ax
    """
    if fig is None:
        fig, ax = plt.subplots(1, figsize=figsize)
    if type(y_all) != list:
        y_all = [y_all]
    if y_all_err is None:
        y_all_err = [None] * len(y_all)
    if type(y_all_err) != list:
        y_all_err = [y_all_err]
    if type(linelabels) != list:
        linelabels = [linelabels]
    if type(x) != list:
        if colours is not None:
            #ax.set_prop_cycle(color=colours)
            for y, y_err, label, c in zip(y_all, y_all_err, linelabels, colours):
                ax.errorbar(x, y, yerr=y_err, linestyle=linestyle, linewidth=linewidth,
                            marker=".", capsize=cs, markersize=ms, label=label, c=c)
        else:
            for y, y_err, label in zip(y_all, y_all_err, linelabels):
                ax.errorbar(x, y, yerr=y_err, linestyle=linestyle, linewidth=linewidth,
                            marker=".", capsize=cs, markersize=ms, label=label)
    else:
        for x_p, y, y_err, label in zip(x, y_all, y_all_err, linelabels):
            ax.errorbar(x_p, y, yerr=y_err, linestyle=linestyle, linewidth=linewidth,
                        marker=".", capsize=cs, markersize=ms, label=label)
    # colours for spans and lines
    colours_line = ["xkcd:dull red","xkcd:sage", "xkcd:orange yellow", "xkcd:coral pink", "xkcd:bluish green", "xkcd:teal blue"]
    if xhlines is not None:
        if type(xhlines) != list:
            xhlines = [xhlines]
        for i, (xhline, xhlabel) in enumerate(zip(xhlines, xhlinelabels)):
            ax.axhline(y=xhline, linestyle="--", label=xhlabel, alpha=0.6, c=colours_line[i])
    if axvspans_min is not None:
        if type(axvspans_min) != list:
            axvspans_min = [axvspans_min]
        if type(axvspans_max) != list:
            axvspans_max = [axvspans_max]
        for i, (axvspan_min, axvspan_max) in enumerate(zip(axvspans_min, axvspans_max)):
            ax.axvspan(axvspan_min, axvspan_max, alpha=0.2, color=colours_line[i])
    if xylines_x is not None:
        if type(xylines_x) != list:
            xylines_x = [xylines_x]
        if type(xylines_y) != list:
            xylines_y = [xylines_y]
        for i, (x_line,y_line,label_line) in enumerate(zip(xylines_x, xylines_y, xylinelabels)):
            ax.plot(x_line, y_line, label=label_line, alpha=0.9, c=colours_line[i], lw=2)
    if xlabel == "default":
        try:
            xlabel = x.name
        except:
            xlabel = "provide xlabel"
    if ylabel == "default":
        try:
            ylabel  = y_all[0].name
        except:
            ylabel = "provide ylabel"
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.xscale(xscale)
    plt.yscale(yscale)
    if yinvert==True:
        ax.invert_yaxis()
    plt.legend(loc="best")
    fig.suptitle(plottitle, fontsize=18)
    return fig, ax

def save_figure(fig, subdir="uncategorised/", filename="xy", ext=".png", tl=True, dpi=None):
    """Save figure to file with filename in subdirectory subdir.
    Default filename is xy
    Default subdirectory is uncategorised
    Default extension is .png
    """
    dir = "./figures/" + subdir
    Path(dir).mkdir(parents=True, exist_ok=True)  # make sure subdirectory figures exists
    if tl==True:
        plt.tight_layout()
    if dpi is None: # default dpi is 100
        plt.savefig(dir + filename + ext)
    else:
        plt.savefig(dir + filename + ext, dpi=dpi)
    plt.close(fig)
