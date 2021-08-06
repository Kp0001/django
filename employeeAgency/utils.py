import matplotlib.pyplot as plt
import base64
from io import BytesIO


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    # retrive entire entire content of code
    image_png = buffer.getvalue()
    # print(image_png)
    # encode the code
    graph = base64.b64encode(image_png)
    # print("graph1",graph)
    # override graph and decode
    graph = graph.decode('utf-8')
    print("graph2", graph)
    buffer.close()
    return graph


def get_plot(x, y):
    # -----------
    plt.switch_backend('AGG')
    plt.figure(figsize=(10, 5))
    plt.title('Jobs Providers W.r.t Pay Rate')
    plt.plot(x, y)
    plt.xticks(rotation=45)  # degree
    plt.xlabel('Company Name')
    plt.ylabel('Job Name')
    # graph should be nicely displayed
    plt.tight_layout()
    graph = get_graph()
    return graph
