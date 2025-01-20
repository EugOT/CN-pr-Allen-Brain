import pandas as pd
import warnings
import os

"""
helper_functions.py

A file for helper functions that my be desirable to be run independantly from notebooks.

create_neural_traces_per_label: A function to summerize all neural activity per trial. Can be changed to be used in other ways if necessary.
"""

def _check_unique_combination(data_grouped, list_unique_column_combination, output_warning = False):
    """
    Check if a combination of columns contains only unique values

    Args:
        data_grouped                    (pandas Dataframe)  Expects one line per trial
        list_unique_column_combination  (list(String))      Expects all column names
        output_warning                  (boolean)           generates warning if True, and if the combinations are not unique

    Returns:
        boolean: True if the combinations are unique, false if they are not
    """

    data_grouped_test = data_grouped.groupby(list_unique_column_combination)

    if len(data_grouped) != len (data_grouped_test):
        if(output_warning): warnings.warn(f"One of these values is not unique for {list_unique_column_combination}: {[s for s in data_grouped.columns.tolist() if s not in list_unique_column_combination]}", UserWarning)
        return False
    
    return True

def create_neural_traces_per_label(data_file_path = "data.csv", columns_of_interest = ["stimulus_presentations_id", "cell_specimen_id", "trace",
                                                                                       "trace_timestamps", "image_name", "image_index", "mouse_id",
                                                                                       "animal_in_image", "close_proximity"]):
    """
    the given dataset contained data to different neurons per stimulus, but divided accross several rows.
    This function outputs a csv file with one row per trial, containing all neuronal activity to that trial.

    Args:
        data_file_path      (str)          File path to the original data csv                                                     Defaults to "data.csv".
        columns_of_interest (list(String)) column Names to be included in the csv. File. Must include a given set of column names Defaults to ["stimulus_presentations_id", "cell_specimen_id", "trace", "trace_timestamps", "image_name", "image_index", "mouse_id", "animal_in_image", "close_proximity"].

    Raises:
        ValueError: The function expects data unique per neuron in the trial, trial and mouse indices. If they are not incuded in "columns_of_interest", the Error is thrown.
    """
    
    columns_necessary = ["stimulus_presentations_id", "mouse_id", "cell_specimen_id", "trace", "trace_timestamps"]
    if not all(s in columns_of_interest for s in columns_necessary):
        raise ValueError(f"The values {columns_necessary} are vital for this function to work. You forgot to include {[s for s in columns_necessary if s not in columns_of_interest]}. Please include it in the 'columns_of_interest'")
    
    data = pd.read_csv(data_file_path)
    data = data[columns_of_interest]

    columns_neuron_dependent = ["cell_specimen_id", "trace", "trace_timestamps"]
    columns_trial_dependent  = [c for c in columns_of_interest if c not in columns_neuron_dependent]
    columns_unique           = ["stimulus_presentations_id", "mouse_id"]
    aggregation_dictionary   = {c: lambda x: list(x) for c in columns_neuron_dependent}

    data_grouped = data.groupby(columns_trial_dependent).agg(aggregation_dictionary).reset_index()

    # Make sure that the data that should be the same per trial are the same. If they are not, the excess trials are deleted.
    if(not _check_unique_combination(data_grouped, columns_unique)):
        counts = data_grouped.groupby(columns_unique).size().reset_index(name='count')                  # Used to extract which "stimulus_presentations_id", "mouse_id" combinations only occur once.
        unique_combinations = counts[counts['count'] == 1][columns_unique]
        filtered_data_grouped = data_grouped.merge(unique_combinations, on=columns_unique, how='inner')

        if(_check_unique_combination(filtered_data_grouped, columns_unique)):
            print(f"The combinations of {columns_unique} is unique. To do so, {len(data.groupby(columns_unique)) - len(filtered_data_grouped)} out of {len(data.groupby(columns_unique))} trials have been ignored.")

        data_grouped = filtered_data_grouped

    data_folder = "data"
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)
    data_grouped.to_csv(f"{data_folder}/neural_activity_per_trial.csv", index=False)
    

create_neural_traces_per_label()