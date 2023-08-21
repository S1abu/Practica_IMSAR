# import the necessary packages
from pyimagesearch.nn.conv.deepergooglenet import DeeperGoogLeNet
from keras.utils import plot_model


# initialize DeeperGoogLeNet and then write the network architecture
# visualization graph to disk
model = DeeperGoogLeNet.build(224, 224, 3, 10)
plot_model(model, to_file="DeeperGoogLeNet.png", show_shapes=True)

# python visualize_DeeperGoogLeNet.py