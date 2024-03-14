import csv

def csv_data_to_dict(filename: str) -> dict:
    # accumulator value
    ret: dict = {}


    # open csv file containing data
    with open(filename) as f:
        reader = csv.reader(f)
        # iterate through rows of csv to add specific values to ret
        counter: int = 1
        for row in reader:
            data: dict = {"sentiment_label": row[3], "text": row[1]}
            ret[counter] = data
            counter += 1
    return ret


def vader_output_to_label(output: dict) -> str:
    compound = output['compound']
    if compound < 0:
        return 'negative'
    elif compound == 0:
        return 'neutral'
    else:
        return 'positive'