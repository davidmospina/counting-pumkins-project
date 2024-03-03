import json
from statistics import mean, stdev

def calculate_means(data):
    statistics = {
        "mean": {
            "red": mean([int(entry["red"]) for entry in data]),
            "green": mean([int(entry["green"]) for entry in data]),
            "blue": mean([int(entry["blue"]) for entry in data]),
            "hue": mean([int(entry["hue"]) for entry in data]),
            "saturation": mean([int(entry["saturation"]) for entry in data]),
            "value": mean([int(entry["value"]) for entry in data]),
        },
        "std_dev": {
            "red": stdev([int(entry["red"]) for entry in data]),
            "green": stdev([int(entry["green"]) for entry in data]),
            "blue": stdev([int(entry["blue"]) for entry in data]),
            "hue": stdev([int(entry["hue"]) for entry in data]),
            "saturation": stdev([int(entry["saturation"]) for entry in data]),
            "value": stdev([int(entry["value"]) for entry in data]),
        }
    }
    return statistics

def process_json(input_file, output_file):
    with open(input_file, 'r') as file:
        data = json.load(file)

    means = calculate_means(data)

    with open(output_file, 'w') as file:
        json.dump(means, file, indent=2)

process_json('/home/david/Documents/SDU/second_term/large_scale_drone_perception/miniproject/pumpkinsPixels.json', '/home/david/Documents/SDU/second_term/large_scale_drone_perception/miniproject/pixelsMean.json')