from keras_visualizer import visualizer

import graphviz
import re
import os


def remove_labels(keras_viz_source, no_labels_dot_file):
    # Read the original .dot file
    with open(keras_viz_source, 'r') as file:
        content = file.read()

    # Regular expression to match nodes with multi-line labels
    label_node_pattern = re.compile(
        r'^\s*\d+\s*\[label="(?:[^"]|\\")*"\s*(?:[^\]]*\s*)?\]$', re.MULTILINE
    )

    # Replace matched nodes with an empty string
    modified_content = re.sub(label_node_pattern, '', content)

    # Write the modified content back to a new .dot file
    with open(no_labels_dot_file, 'w') as file:
        file.write(modified_content)

def draw_from_source(source, output):
    # Load the .dot file
    with open(source, 'r') as file:
        dot_data = file.read()

    # Regex to find the graph options list and add rankdir=LR if not present
    dot_data = re.sub(
        r'(graph\s*\[.*?)(\])',
        r'\1 rankdir=LR\2',
        dot_data,
        flags=re.DOTALL
    )
    # Create a Graphviz source object
    dot = graphviz.Source(dot_data)

    # Render the graph to a file (e.g., PNG format)
    path = dot.render(output, format='png', cleanup=True, view=True)
    return path

def ai_talks_visualizer(model, keras_viz_source = 'neural_network', no_labels_dot_file = 'nn_no_labels', png_render_file = 'model_no_labels'):
    visualizer(model, file_name='neural_network', file_format='dot', view=False)
    remove_labels(keras_viz_source, no_labels_dot_file)
    return draw_from_source(no_labels_dot_file, png_render_file)

def clean_dir(directory):
    for filename in os.listdir(directory):
        # Get the file extension
        file_path = os.path.join(directory, filename)
        file_extension = os.path.splitext(filename)[1]
        
        # Check if the file has .png, .dot extensions, or no extension
        if file_extension in ['.png', '.dot'] or file_extension == '':
            try:
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")


"""
model = models.Sequential([
    layers.Input((3,)),
    layers.Dense(6, activation='softmax'),
    layers.Dense(8, activation='softmax'),
    layers.Dense(8, activation='softmax'),
    layers.Dense(6, activation='softmax'),
    layers.Dense(5, activation='softmax'),
    layers.Dense(1)

])

"""


"""

model = models.Sequential([
    layers.Input((3,)),
    layers.Dense(3, activation='selu'),
    layers.Dense(5, activation='selu'),
    layers.Dense(7, activation='selu'),
    layers.Dense(5, activation='selu'),
    layers.Dense(3, activation='selu'),
    layers.Dense(1)
])

"""

