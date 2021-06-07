import pandas as pd
import numpy as np

if __name__ == "__main__":
    classes = pd.read_csv("Classes.csv")
    print(classes)

    semesters = np.unique(classes['Semester'])

    gradeSum = np.zeros(len(semesters))
    ectsSum = np.zeros(len(semesters))

    for s in semesters:
        gradeSum[s - 1] = np.sum(classes.where(classes['Semester'] == s)['Grade'] * classes.where(classes['Semester'] == s)['ECTS'])
        ectsSum[s - 1] = np.sum(classes.where(classes['Semester'] == s)['ECTS'])
        print(f"{s} Semester average: {round(gradeSum[s - 1] / ectsSum[s - 1], 2)}")

    average = np.sum(gradeSum) / np.sum(ectsSum)
    print(f"Total average is: {round(average, 2)}")
