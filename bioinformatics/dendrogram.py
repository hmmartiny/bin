import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec as gridspec

"""
An attempt at making a class for drawing advanced dendrograms with Python.py
Both linear and circular (polar) dendrograms.
"""

class Dendogram:
    """Inspired by https://stackoverflow.com/a/52517178/15704316"""
    def __init__(self, dendrogram, annotations):
        
        self.icoord = dendrogram['icoord']
        self.dcoord = dendrogram['dcoord']
        
        self.leave_labels = dendrogram['ivl']
        self.leaves = dendrogram['leaves']
        self.get_leave_coords()
        
        self.annotations = annotations
        
        
    def get_leave_coords(self):
        
        # flatten
        icoord_flattened = [item for sublist in self.icoord for item in sublist]
        dcoord_flattened = [item for sublist in self.dcoord for item in sublist]
        
        # extract
        leave_coords = [(x,y) for x,y in zip(icoord_flattened, dcoord_flattened) if y == 0]
        
        # get leave order in dendrogram
        leave_order = np.argsort([x for x, _ in leave_coords])
        
        # map id to coordinates
        self.leaveid_to_coord = dict(zip(
            self.leaves,
            [leave_coords[idx] for idx in leave_order]
        ))
        self.coord_to_leave = {v: k for k, v in self.leaveid_to_coord.items()}
        
        # map id to label
        self.leaveid2leavelabel = {lid: ll for lid, ll in zip(self.leaves, self.leave_labels)}
        
    def _branches(self, ax, icoords, dcoords, color='black', lw=1, limit=None, plot_leaves=True, leaf_args={}):
        
        max_coord = 0
        
        for i, (xs, ys) in enumerate(zip(icoords, dcoords)):
            ax.plot(xs, ys, color="black", lw=lw)
            
            if plot_leaves:
                self._leaf(ax, xs, ys, **leaf_args)
            
            if max(xs) > max_coord: max_coord = max(xs)
            if isinstance(limit, int) and i > limit: break
            
        ax.set_xlim(-.1, max_coord + 2)
    
    def get_leaf_formatting(self, node, column, default):
        
        try:
            nf = self.annotations.loc[self.annotations.node == node, column].item()
        except:
            nf = default
            
        return nf
    
    def _leaf(self, ax, xs, ys, leaf_shape=None, leaf_color=None, leaf_size=2):
        for x, y in zip(xs, ys):
            if y == 0:
                
                try:
                    leaf_id = self.coord_to_leave[(x,y)]
                except:
                    continue
                
                leaf_label = self.leaveid2leavelabel[leaf_id] 
                
                shape = self.get_leaf_formatting(node=leaf_label, column=leaf_shape, default='o')
                color = self.get_leaf_formatting(node=leaf_label, column=leaf_color, default='black')    
                ax.plot(x, y, shape, color=color, ms=leaf_size)
    
    def plot_linear(self, figsize, limit=None, plot_leaves=True, leaf_args = {}):
        
        fig = plt.figure(figsize=figsize)
        gs = gridspec.GridSpec(nrows=1, ncols=1)#, **gridspec_kw)
        
        ax = fig.add_subplot(gs[0])
        #ax_leaf = fig.add_subplot(gs[1], sharex=ax)
        
        # plot branches and leaves
        self._branches(ax, self.icoord, self.dcoord, limit=limit, plot_leaves=plot_leaves, leaf_args=leaf_args)
            
        ax.get_xaxis().set_visible(False)
            
        ax.set_ylim(-.1, ax.get_ylim()[1] + .1)
            
        for spine in ['top', 'right']:
            ax.spines[spine].set_visible(False)
        
        plt.close(fig)
        return fig
    
    def polar_leaf(self, ax, x, y, xo, yo, leaf_shape=None, leaf_color=None, leaf_size=2):
        try:
            leaf_id = self.coord_to_leave[(xo, yo)]
            leaf_label = self.leaveid2leavelabel[leaf_id] 
            shape = self.get_leaf_formatting(node=leaf_label, column=leaf_shape, default='o')
            color = self.get_leaf_formatting(node=leaf_label, column=leaf_color, default='black')    
        except:
            shape, color = 'o', 'black'
        ax.plot(x, y, shape, color=color, ms=leaf_size)

    def plot_circular(self, figsize, limit=None, plot_leaves=True, leaf_args={}, lw=1):
        
        fig = plt.figure(figsize=figsize)
        gs = gridspec.GridSpec(nrows=1, ncols=1)
        ax = fig.add_subplot(gs[0], polar=True)
        
        dcoords = -np.log(np.asarray(self.dcoord) + 1)
        gap = .1
        
        icoord = np.asarray(self.icoord)
        imax = icoord.max()
        imin = icoord.min()
        icoords = ((icoord - imin) / (imax - imin) * (1-gap) + gap / 2) * 2 * np.pi
        
        #self._branches(ax, icoords, dcoords, plot_leaves=plot_leaves)
        for i, (xs, ys) in enumerate(zip(icoords, dcoords)):            
            
            if plot_leaves:
                for j, (x, y) in enumerate(zip(xs, ys)):
                    if y == 0:
                        xo, yo = (self.icoord[i][j], self.dcoord[i][j])
                        self.polar_leaf(ax, x, y, xo, yo, **leaf_args)
                        
            xss = np.concatenate([[xs[0]], np.linspace(xs[1], xs[2], 100), [xs[3]]])
            yss = np.concatenate([[ys[0]], np.linspace(ys[1], ys[2], 100), [ys[3]]])
            ax.plot(xss, yss, color='black', lw=lw)
        
            if limit is not None and i > limit:
                break
        
        
        ax.spines['polar'].set_visible(False)
        ax.xaxis.grid(False)
        ax.set_xticklabels([])
        plt.close(fig)
        return fig
        
        
if __name__ == '__main__':
    dnd = Dendogram(dend, anno)

    leaf_args = {'leaf_color': 'gene_color', 'leaf_shape': 'shape','leaf_size': 2}

    dnd.plot_linear(figsize=(10, 10), plot_leaves=True, leaf_args=leaf_args, limit=10)
    dnd.plot_circular(figsize=(10, 10), plot_leaves=True, lw=.05, leaf_args=leaf_args, limit=10)
