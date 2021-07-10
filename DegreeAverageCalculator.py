import pandas as pd
import numpy as np

if __name__ == "__main__":
    classes = pd.read_csv("Classes.csv")
    classes = classes.where(classes['Grade'] >= 5.0)

    print(classes)

    semesters = np.unique(classes['Semester'])

    gradeSum = np.zeros(len(semesters))
    ectsSum = np.zeros(len(semesters))

    for i, s in enumerate(semesters):
        gradeSum[i] = np.sum(classes.where(classes['Semester'] == s)['Grade']
                             * classes.where(classes['Semester'] == s)['ECTS'])
        ectsSum[i] = np.sum(classes.where(classes['Semester'] == s)['ECTS'])
        print(f"{s} Semester average: {round(gradeSum[i] / ectsSum[i], 2)}")

    average = np.sum(gradeSum) / np.sum(ectsSum)
    print(f"Total average is: {round(average, 2)}")
