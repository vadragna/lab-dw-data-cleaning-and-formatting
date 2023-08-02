def cleaning_up(df):
    df.drop_duplicates()
    styled_df = df.style.set_table_styles([
    {'selector': 'thead th', 'props': [('text-align', 'center')]},
    {'selector': 'th.col_heading', 'props': center_columns(df.columns)}])
    df.rename(columns={'GENDER': 'Gender'}, inplace=True)
    df.rename(columns={'ST': 'State'}, inplace=True)
    centered_df = center_columns(df)
    for col in df.columns:
    df['ST'] = df['State'].replace('AZ', 'Arizona').replace('WA', 'Washington').replace('Cali', 'California')
    df['GENDER'] =  df['Gender'].replace('Femal', 'F').replace('female', 'F').replace('Male', 'M')
    df = df.dropna(subset=['Customer'])
    df = df.drop_duplicates()
    for col in df.columns:
    df['ST'] = df['State'].replace('AZ', 'Arizona').replace('WA', 'Washington').replace('Cali', 'California')
    df['GENDER'] =  df['Gender'].replace('Femal', 'F').replace('female', 'F').replace('Male', 'M')  
    df['Customer Lifetime Value'] = df['Customer Lifetime Value'].str.replace('%', '').astype(float)
    df.dropna(subset=['Customer Lifetime Value'], inplace=True)
