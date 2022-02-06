from info.all_info import get_clean_records_for_india

df = get_clean_records_for_india()
df.drop(columns=['href','post'], axis=1, inplace=True)
df.to_csv("./data/out/lc_updated_edited.csv", index=False)
