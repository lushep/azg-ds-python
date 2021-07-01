(
    chickweight
    .groupby('diet')
    .apply(lambda x: x.loc[x['weight'] == x['weight'].max()])
)
