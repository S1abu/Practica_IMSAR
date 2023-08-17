# define the paths to the images directory
IMAGES_PATH = "/media/slabu/DataUbuntu/IMSAR_Files/datasets/kaggle_cats_vs_dogs/train"

# since we do not have validation data or access to the testing
# labels we need to take a number of images from the training
# data and use them instead
NUM_CLASSES = 2
NUM_VAL_IMAGES = 1250 * NUM_CLASSES
NUM_TEST_IMAGES = 1250 * NUM_CLASSES

# define the path to the output training, validation, and testing
# HDF5 files
TRAIN_H5 = "/media/slabu/DataUbuntu/IMSAR_Files/datasets/kaggle_cats_vs_dogs/h5/train.h5"
VAL_H5 = "/media/slabu/DataUbuntu/IMSAR_Files/datasets/kaggle_cats_vs_dogs/h5/val.h5"
TEST_H5 = "/media/slabu/DataUbuntu/IMSAR_Files/datasets/kaggle_cats_vs_dogs/h5/test.h5"

# path to the output model file
MODEL_PATH = "/media/slabu/DataUbuntu/IMSAR_Files/dogs_vs_cats/output/alexnet_dogs_vs_cats.model"

# define the path to the dataset mean
DATASET_MEAN = "/media/slabu/DataUbuntu/IMSAR_Files/dogs_vs_cats/output/dogs_vs_cats_mean.json"

# define the path to the output directory used for storing plots,
# classification reports, etc.
OUTPUT_PATH = "output"
