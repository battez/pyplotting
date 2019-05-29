# applied plotting in Python - coursera
- course is about communicating with managers, executives, stakeholders. Or a journalist.
- information visualisation: best practices
- Alberto Cairo (Graphics Lies, Misleading Visuals) and Tufte
- saved in careers folder, transcripts. Date order downloaded.

## primers: https://www.datacamp.com/community/tutorials/matplotlib-tutorial-python  DONE
https://www.datacamp.com/courses/intermediate-python-for-data-science DONE
todo: (if relevant)
https://www.datacamp.com/community/tutorials/matplotlib-3d-volumetric-data

### End of May: DONE
- readings
- peer assignment
- review others

### June:
MatPlotLib.
- assignments work
- pandas skills needed. (Might need read up on some of this).
- small project at end. Extend matplotlib. 
- peer review. 

## Misleading Graphics
1. Hiding relevant data to highlight what benefits us (Favourableness)
2. Displaying too much data so as to obscure reality (Verbosity/dazzling)
3. Using graphic forms in inappropriate ways (distorting the data) (Distortions)

## matplotlib ~ week 2 
- MATLAB origins
- getter setter conventions
- different backends (rendering configs to different end-uses): interactive notebook "inline" is used.

### Artists paradigm for drawing 
- two layers in mpl: backend and artists
	- containers: Figure, Subplot, Axes
	- primitives: line2D, Rectangle etc, collections e.g. PathCollection
	- child objects of Artists layer
	- primitives are the children of the patch class. Which is a MATLAB legacy.
		- patch 2d image has an edge and a face colour
- third layer is Scripting layer to allow us to be intereactive with plots.
	- key to proficiency with matplotlib
	- enables a lot of magic 
	- use "pyplot" - procedural scripting layer
	- creates the objects on the artists layer and organises them

### Plots
- axes and axis different, objects: former is of two of latter.

### MatPlotLib object API -- or painting direct to the Artist layer.
- more verbose
- pyplot does more things automagically for us. 

### Scatter plots 
- arrays of points -- vector approach.
- use lambdas, list comprehensions and zip (packing unpacking)
	- zip -- takes no. iterables, and makes tuples out of them
		- lazy generator, must use list(my_zipped) with it
	- 	- Common scatter() options... s= size , c= colour, alpha=,

### useful and common commands
- get current figure , to modify them etc - gca() and gcf() 
- Put the x-axis on a logarithmic scale
plt.xscale('log')
- clean a plot up anew: plt.clf()
- plt.grid(True)

#### Plot() options
- marker='o'
- c= colours... or color=
- linestyle='--' None etc
- use also ax.set_title() or ax.set_xlabel() etc
- Set axis properties [xmin, xmax, ymin, ymax]
ax.axis([0,6,0,10])

#### useful sanity checks and troubleshooting etc
- plt.gca().get_children() ... To inspect what objects we have.
	- e.g # get the legend from the current axes
legend = plt.gca().get_children()[-2]
	- # you can use get_children to navigate through the child artists
legend.get_children()[0].get_children()[1].get_children()[0].get_children()
- adjust the subplot so the text doesn't run off the image
plt.subplots_adjust(bottom=0.25)

#### subplots
One convention is to plot like this:
fig, ax = plt.subplots()

Then ax.plot(xs, ys)
plt.show()

Can also use for **small multiples**
- subfigures really.
- e.g. plt.subplots(2, 2)
- reference via ax[0, 1].plot()
- or if just one row OR column, use a single lsit ref e.f. ax[1].plot()
- useful options:
	- , sharey=True

#### misc. notes
##### fill the area between the linear data and exponential data
this will paint a fill in an area, eg for conf. intervals etc
plt.gca().fill_between(range(len(linear_data)), 
                       linear_data, exponential_data, 
                       facecolor='blue', 
                       alpha=0.25)
#####  bar charts - stacked, horiz
- Use bar() and specify the bottom= to be the vector of y-values for lower 
- barh() horizontal; and use hieght not width
