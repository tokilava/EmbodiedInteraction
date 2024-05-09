import pandas as pd
from scipy import stats
from scipy.stats import f_oneway
import statsmodels.stats.multicomp as mc
from statsmodels.stats.multicomp import pairwise_tukeyhsd



df = pd.read_csv("HeartRateDifference.txt")

def summary():
    means = df.mean()
    medians = df.median()
    std = df.std()
    print("Means:\n", means, "Medians: \n", medians, "Std: \n", std)

"-----Next we will use a shapiro wilk test to test for normality before doing anything-----"
columns = ("Arial", "Georgia", "TimesNewRoman", "Calibri")
def shapiroWilksTest():
    for item in columns:
        data = df[item]
        statistics, p_value = stats.shapiro(data)

        print("Shapiro-Wilk Test:")
        print("Font: ", item)
        print(f"Test Statistic: {statistics}")
        print(f"P-value: {p_value}")

        alpha = 0.05
        "Null hypothesis is that the data is normally distributed."
        if p_value > alpha:
            print("fail to reject H0")
        else:
            print("reject H0")

def ANOVA():
    f_statistic, p_value = f_oneway(df['Arial'], df['Georgia'], df['TimesNewRoman'], df['Calibri'])

    # Print the results
    print("One-way ANOVA:")
    print(f"F-statistic: {f_statistic}")
    print(f"P-value: {p_value}")

    # Interpret the results
    alpha = 0.05
    if p_value < alpha:
        print("There is a significant difference in means.")
    else:
        print("There is no significant difference in means.")

def TukeysTest():

    # We have to reshape the data to be a one column array for tukeys test
    new_data = pd.melt(df.reset_index(), id_vars=['index'], value_vars=['Arial', 'Georgia', 'TimesNewRoman', 'Calibri'])
    # Perform Tukey's HSD test
    tukey_results = mc.MultiComparison(new_data['value'], new_data['variable']).tukeyhsd()

    # Print the summary of the Tukey's HSD test
    print(tukey_results)

summary()
print("----------Next test----------")
shapiroWilksTest()
print("----------Next test----------")
ANOVA()
print("----------Next test----------")
TukeysTest()
