import pandas as pd
def chickenpox_by_sex(df):
    vaccinated_df = df[df['vaccinated'] == 1]
    result = {}
    for sex in ['male', 'female']:
        sex_df = vaccinated_df[vaccinated_df['sex'] == sex]
        contracted_chickenpox = sex_df[sex_df['chickenpox'] == 1].shape[0]
        did_not_contract_chickenpox = sex_df[sex_df['chickenpox'] == 0].shape[0]
        if did_not_contract_chickenpox == 0:
            ratio = 0
        else:
            ratio = contracted_chickenpox / did_not_contract_chickenpox
        result[sex] = ratio
    return result
data = {
    'vaccinated': [1, 1, 1, 1, 1, 0, 0, 1],
    'sex': ['male', 'female', 'male', 'female', 'male', 'female', 'male', 'female'],
    'chickenpox': [1, 0, 0, 1, 1, 0, 1, 1]
}
df = pd.DataFrame(data)
result = chickenpox_by_sex(df)
print(result)