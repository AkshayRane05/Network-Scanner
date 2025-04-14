import csv

devices = ['hello', '1', '2', 'three']


def csv_export(data):
    with open('test.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file)

        csv_writer.writerow(['L1', 'L2', 'L3'])

        for device in devices:
            csv_writer.writerow(device)


# csv_export(devices)

for dev in devices:
    print(dev)
