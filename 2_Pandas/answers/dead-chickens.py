(
    chickweight
    .groupby('chick')
    [['time']]
    .max()
    .loc[lambda df: df['time'] < chickweight['time'].max()]
)
