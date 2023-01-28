import xlrd
import csv


# Open the xls file
workbook = xlrd.open_workbook("datasets/COM_2019.xls")

# Open a csv file
with open("datasets/pop-sex-age.csv", "w") as f:
    writer = csv.writer(f)

    # Write rows in the csv file and create a list from it
    for sheet in workbook.sheets():
        for row_num in range(sheet.nrows):
            writer.writerow(sheet.row_values(row_num))
