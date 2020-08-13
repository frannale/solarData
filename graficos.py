import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

#crea el grafico, guarda la imagen y retorna el path para levantarla desde servidor
def barrasSumadas():
        
    # datos
    data = [[ 66386, 174296,  75131, 577908,  32015,41455, 577908,  32015,41455]]
    # diferentes parametros de entrada
    columns = ('04:00','06:00','08:00','10:00','12:00','14:00','16:00','18:00','20:00')
    rows = ['asd']

    values = np.arange(0, 500, 900)

    # Get some pastel shades for the colors
    colors = plt.cm.BuPu(np.linspace(0.7, 0.1, len(rows)))
    n_rows = len(data)

    index = np.arange(len(columns)) + 0.99
    bar_width = 0.5

    # Initialize the vertical-offset for the stacked bar chart.
    y_offset = np.zeros(len(columns))

    # Plot bars and create text labels for the table
    cell_text = []
    for row in range(n_rows):
        plt.bar(index, data[row], bar_width, bottom=y_offset, color=colors[row])
        y_offset = y_offset + data[row]
        cell_text.append([ (x ) for x in y_offset])
    # Reverse colors and text labels to display the last value at the top.
    colors = colors[::-1]
    cell_text.reverse()

    # Add a table at the bottom of the axes
    the_table = plt.table(cellText=cell_text,
                        rowLabels=rows,
                        rowColours=colors,
                        colLabels=columns,
                        loc='bottom')

    # Adjust layout to make room for the table:

    plt.ylabel("Kilowats ")
    plt.yticks(values, ['%d' % val for val in values])
    plt.xticks([])
    plt.title(' Comparacion especifico por dato de ultimos 5 dias')
    plt.subplots_adjust(bottom=0.29, right=0.99, left=0.15,top=0.95)
    figure = plt.gcf() # get current figure
    figure.set_size_inches(14, 8)
    path = 'static/figura.png'
    plt.savefig(path,bbox_inches = 'tight',dpi = 100 )
    return path

barrasSumadas()    