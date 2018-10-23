import csv

with open('my_details.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1

    with open('my_updated_details.txt', mode='w') as my_file:
        with open('my_details.txt') as csv_file:
            employee_writer = csv.writer(my_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_reader2 = csv.reader(csv_file, delimiter=',')
            for row in csv_reader2:
                employee_writer.writerow([row[0] + ' Singh', row[1], row[2]]);