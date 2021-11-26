import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def getPeopleIn(data, sex=None, year=None, age=None):
    """
    :param data: dataset - csv file
    :param sex:  choose sex type, 0 or 1
    :param year: choose year, 1900 or 2000
    :param age:  choose age from the set range(0,90,5)
    :return: new dataset that contain only the fields that have been chosen from the input [sex, year, age] and are in
             the input data
    """
    if sex is not None:
        data = data.where(data.Sex == sex)
    if year is not None:
        data = data.where(data.Year == year)
    if age is not None:
        data = data.where(data.Age == age)
    data = data.dropna()
    return data


def main():
    dataset = pd.read_csv('census2000.csv')
    print(dataset)
    df_m_1900 = getPeopleIn(dataset, year=1900, sex=1)
    df_m_2000 = getPeopleIn(dataset, year=2000, sex=1)
    df_w_1900 = getPeopleIn(dataset, year=1900, sex=2)
    df_w_2000 = getPeopleIn(dataset, year=2000, sex=2)

    arr1 = (np.array(df_m_1900.People) + np.array(df_w_1900.People))
    arr2 = (np.array(df_m_2000.People) + np.array(df_w_2000.People))
    Growth = arr2/arr1

    data = {'Age': df_m_1900.Age.astype(int),
            'People in 1900': arr1,
            'People in 2000': arr2,
            'Growth': Growth}
    df_growth = pd.DataFrame(data)
    print(df_growth)
    plt.figure()
    sns.barplot(y='Growth', x='Age', data=df_growth, ci=None)
    plt.title('Growth Ratio of each age group')
    plt.grid()
    plt.xlabel('Age group')
    plt.ylabel('Growth Ratio')

    plt.figure()
    sns.barplot(y='People', x='Age', hue='Year', data=dataset, ci=None)
    plt.title('Number of People in each Age group')
    plt.grid()
    plt.xlabel('Age group')
    plt.ylabel('Number of People')


if __name__ == '__main__':
    main()
