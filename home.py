import streamlit as st
import numpy as np
import csv

# open the csv file in reading mode
with open('datasets/pop-sex-age.csv', 'r') as f:
    # use csv.reader to read the csv produce in data_manipulation
    reader = csv.reader(f)
    # convert datas in list
    data = list(reader)
    # convert list into a numpy array
    data = np.array(data)

# concatenation of CR & DR to make an unique identifier for cities

col1 = data[13:, 1:2]

col2 = data[13:, 2:3]
result = np.column_stack((col1, col2))
print(result)


def main():
    st.header("home page")
    st.title("this is a test for 5team company")
    # display a sample of the first nparray in home page
    st.write(data[10:25, 5:15])


if __name__ == '__main__':
    main()
st.text("Hello")
