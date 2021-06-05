import pandas as pd
import numpy as np
from math import isnan

if __name__ == "__main__":
    classes = pd.read_csv("Classes.csv")
    print(classes)

    classes_data = np.array(classes)

    gradeSum = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    ectsSum = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    totalGradeSum = 0.0
    totalEctsSum = 0.0
    for class_data in classes_data:
        if isnan(class_data[2]):
            continue

        grade = class_data[2]
        ects = class_data[3]
        semester = class_data[4] - 1

        gradeSum[semester] += grade * ects
        ectsSum[semester] += ects

    for semester in range(10):
        if gradeSum[semester] == 0.0:
            continue

        totalEctsSum += ectsSum[semester]
        totalGradeSum += gradeSum[semester]
        print(f"{semester + 1} Semester average: {gradeSum[semester] / ectsSum[semester]}")

    average = totalGradeSum / totalEctsSum
    print(f"Total average is: {average}")
