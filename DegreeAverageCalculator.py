import pandas as pd
import numpy as np


if __name__ == "__main__":
    classes = pd.read_csv("Classes.csv")
    print(classes)

    classes_data = np.array(classes)

    gradeSum = 0.0
    ectsSum = 0.0
    for class_data in classes_data:
        grade = class_data[2]
        ects = class_data[3]

        gradeSum += grade * ects
        ectsSum += ects

    average = gradeSum / ectsSum
    print(f"Average is {average}")
