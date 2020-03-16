"""
Charles Kornoelje | CS 344 | Lab06 | 3/15/20 | Cal Uni | Numpy
Load the Keras version of the Boston Housing Price dataset
"""

from keras.datasets import boston_housing
(train_data, train_labels), (test_data, test_labels) = boston_housing.load_data()


def print_structures():
    print(
        'training data \
            \n\tcount: {} \
            \n\tdimensions: {} \
            \n\tshape: {} \
            \n\tdata type: {}\n\n'.format(
            len(train_data),
            train_data.ndim,
            train_data.shape,
            train_data.dtype
        ),
        'testing data \
            \n\tcount: {} \
            \n\tdimensions: {} \
            \n\tshape: {} \
            \n\tdata type: {}\n'.format(
            len(test_data),
            test_data.ndim,
            test_data.shape,
            test_data.dtype,
        )
    )

# 6.3.a.i) the length of the data sets
# 6.3.b.ii) .ndim, .shape, .dtype of the data sets.

# training data
# 	count: 404
# 	dimensions: 2
# 	shape: (404, 13)
# 	data type: float64
#  testing data
# 	count: 102
# 	dimensions: 2
# 	shape: (102, 13)
# 	data type: float64

print_structures()