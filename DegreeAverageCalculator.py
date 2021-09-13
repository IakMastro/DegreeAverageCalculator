import pandas as pd
import numpy as np

if __name__ == "__main__":
    classes = pd.read_csv("Classes.csv")
    classes = classes.where(classes['Grade'] >= 5.0)

    print(classes)

    semesters = np.unique(classes['Semester'])

    grade_sum = np.zeros(len(semesters))
    ects_sum = np.zeros(len(semesters))

    for i, s in enumerate(semesters):
        if np.isnan(s):
            continue

        grade_sum[i] = np.sum(classes.where(classes['Semester'] == s)['Grade']
                             * classes.where(classes['Semester'] == s)['ECTS'])
        ects_sum[i] = np.sum(classes.where(classes['Semester'] == s)['ECTS'])
        print(f"{s} Semester average: {round(grade_sum[i] / ects_sum[i], 2)}")

    average = np.sum(grade_sum) / np.sum(ects_sum)
    print(f"Total average is: {round(average, 2)}")
