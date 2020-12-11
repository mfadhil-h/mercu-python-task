import base64
from Tkinter import Frame, Tk, Label, YES, BOTH, Button, Entry, NW
from urllib import urlopen

from tkinter import Canvas, PhotoImage

graphs = {
    'A': {'B': 2, 'D': 7, 'F': 12, 'O': 2},
    'B': {'A': 2, 'C': 1, 'D': 4, 'E': 3, 'O': 5},
    'C': {'B': 1, 'E': 4, 'O': 4},
    'D': {'A': 7, 'B': 4, 'E': 1, 'T': 5},
    'E': {'B': 3, 'C': 4, 'D': 1, 'T': 7},
    'F': {'A': 12, 'T': 3},
    'O': {'A': 2, 'B': 5, 'C': 4},
    'T': {'D': 5, 'E': 7, 'F': 3}
}


def dijkstra(graph, start, destination, visited=None, distances=None, predecessors=None):
    if predecessors is None:
        predecessors = {}
    if distances is None:
        distances = {}
    if visited is None:
        visited = []

    if start == destination:
        path = []
        predecessor = destination
        while predecessor is not None:
            path.append(predecessor)
            predecessor = predecessors.get(predecessor, None)
        return path, distances[destination]
    else:
        # initializes the cost (first visit)
        if not visited:
            distances[start] = 0
        # visit the neighbors
        for neighbor in graph[start]:
            if neighbor not in visited:
                new_distance = distances[start] + graph[start][neighbor]
                if new_distance < distances.get(neighbor, float('inf')):
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = start
        # mark as visited
        visited.append(start)
        unvisited = {}
        for k in graph:
            if k not in visited:
                unvisited[k] = distances.get(k, float('inf'))
        x = min(unvisited, key=unvisited.get)
        return dijkstra(graph, x, destination, visited, distances, predecessors)


def do_dijkstra():
    start = str(input_1.get()).upper()
    destination = str(input_2.get()).upper()
    if start not in graphs or destination not in graphs:
        label_length['text'] = "The root or the target of the shortest"
        label_result['text'] = "path tree cannot be found"
    else:
        all_paths, shortest_length = dijkstra(graphs, start, destination)
        all_paths.reverse()
        label_length['text'] = shortest_length
        label_result['text'] = "->".join(all_paths)


app = Tk()
app.title("Tugas Besar 02 - 41520110059 - Muhammad Fadhil")

list_data = []

frame_1 = Frame(app)
Label(frame_1, text="Aplikasi Dijkstra", fg="black").pack()
frame_1.pack(expand=YES, fill=BOTH)

canvas = Canvas(app, width=663, height=333)
canvas.pack()
# convert image tugas besar 02 menjadi gif
image_url = "https://imgur.com/download/XnRSZEs/"
image_byte = urlopen(image_url).read()
image_b64 = base64.encodestring(image_byte)
img = PhotoImage(data=image_b64)
canvas.create_image(0, 0, anchor=NW, image=img)

frame_2 = Frame(app)
label_1 = Label(frame_2, text="Start", fg="black")
label_1.grid(row=0, column=0)
input_1 = Entry(frame_2, fg="black")
input_1.grid(row=1, column=0)
label_2 = Label(frame_2, text=" -> ", fg="black")
label_2.grid(row=1, column=1)
label_3 = Label(frame_2, text="Destination", fg="black")
label_3.grid(row=0, column=2)
input_2 = Entry(frame_2, fg="black")
input_2.grid(row=1, column=2)

input_button = Button(frame_2, text="Search", fg="black", command=lambda: do_dijkstra())
input_button.grid(row=1, column=3)
frame_2.pack(expand=YES)

frame_3 = Frame(app)
label_3 = Label(frame_3, text="Shortest Length:", fg="black")
label_3.grid(row=0, column=0)
label_length = Label(frame_3, text="Waiting...", fg="black")
label_length.grid(row=0, column=1)
label_4 = Label(frame_3, text="Shortest Path:", fg="black")
label_4.grid(row=1, column=0)
label_result = Label(frame_3, text="Waiting...", fg="black")
label_result.grid(row=1, column=1)
frame_3.pack(expand=YES)

app.mainloop()
