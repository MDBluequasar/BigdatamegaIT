import numpy as np
from pandas import DataFrame
from sklearn.impute import SimpleImputer

def getIq(field):
    q1 = field.quantile(q=0.25)
    q3 = field.quantile(q=0.75)
    iqr = q3 - q1
    하한 = q1 - 1.5 * iqr
    상한 = q3 + 1.5 * iqr
    결측치경계 = [하한, 상한]
    return 결측치경계

def replaceOutlier(df, fieldName):
    cdf = df.copy()  # 리스트는 얇은 복사가 되기 때문에 깊은 복사로 바꿔주는 copy를 써서 원본은 보존한다.

    # fieldName[]이 List 가 아니면 List로 변환
    if not isinstance(fieldName, list):
        fieldName = [fieldName]

    for f in fieldName:
        결측치경계 = getIq(cdf[f])
        cdf.loc[cdf[f] < 결측치경계[0], f] = np.nan
        cdf.loc[cdf[f] > 결측치경계[1], f] = np.nan

    return cdf

def replaceMissingValue(df):
    imr = SimpleImputer(missing_values = np.nan, strategy = 'mean')
    df_imr = imr.fit_transform(df.values)
    re_df = DataFrame(df_imr, index = df.index, columns = df.columns)
    return re_df