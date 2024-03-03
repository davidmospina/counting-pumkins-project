import json
from statistics import mean, stdev
import numpy as np

def calculate_statistics(data):
    red_values = [int(entry["red"]) for entry in data]
    green_values = [int(entry["green"]) for entry in data]
    blue_values = [int(entry["blue"]) for entry in data]
    red_mean = mean(red_values)
    green_mean = mean(green_values)
    blue_mean = mean(blue_values)

    rgb_values = np.array(list(zip(red_values, green_values, blue_values)))

    statistics = {
        "mean": {
            "red": mean(red_values),
            "green": mean(green_values),
            "blue": mean(blue_values),
            "hue": mean([int(entry["hue"]) for entry in data]),
            "saturation": mean([int(entry["saturation"]) for entry in data]),
            "value": mean([int(entry["value"]) for entry in data]),
        },
        "std_dev": {
            "red": stdev(red_values),
            "green": stdev(green_values),
            "blue": stdev(blue_values),
            "hue": stdev([int(entry["hue"]) for entry in data]),
            "saturation": stdev([int(entry["saturation"]) for entry in data]),
            "value": stdev([int(entry["value"]) for entry in data]),
        },
        "covariance_matrix_rgb": np.cov(rgb_values, rowvar=False).tolist(),
        "mean_rgb": [red_mean,green_mean,blue_mean]
    }

    return statistics

def process_json(input_file, output_file):
    with open(input_file, 'r') as file:
        data = json.load(file)

    means = calculate_statistics(data)

    with open(output_file, 'w') as file:
        json.dump(means, file, indent=2)

process_json('/home/david/Documents/SDU/second_term/large_scale_drone_perception/miniproject/pumpkinsPixels.json', './pumpkinsStatistics.json')