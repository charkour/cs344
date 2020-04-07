from keras.datasets import boston_housing
(train_val_data, train_val_labels), (test_data, test_labels) = boston_housing.load_data()


def print_structures():
    print(
        'training data \
            \n\tcount: {} \
            \n\tdimensions: {} \
            \n\tshape: {} \
            \n\tdata type: {}\n\n'.format(
            len(train_val_data),
            train_val_data.ndim,
            train_val_data.shape,
            train_val_data.dtype
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

# def preprocess_features(df):
#   """Prepares input features from California housing data set.
#
#   Args:
#     california_housing_dataframe: A Pandas DataFrame expected to contain data
#       from the California housing data set.
#   Returns:
#     A DataFrame that contains the features to be used for the model, including
#     synthetic features.
#   """
#   selected_features = df[
#     ["latitude",
#      "longitude",
#      "housing_median_age",
#      "total_rooms",
#      "total_bedrooms",
#      "population",
#      "households",
#      "median_income"]]
#   processed_features = selected_features.copy()
#   # Create a synthetic feature.
#   processed_features["rooms_per_person"] = (
#     df["total_rooms"] /
#     df["population"])
#   return processed_features
#
# # Choose the first 12000 (out of 17000) examples for training.
# training_examples = preprocess_features(train_val_data.head(303))
# training_targets = preprocess_targets(train_val_data.head(303))
#
# # Choose the last 5000 (out of 17000) examples for validation.
# validation_examples = preprocess_features(train_val_data.tail(101))
# validation_targets = preprocess_targets(train_val_data.tail(101))

