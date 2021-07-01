(
    chickweight
    .assign(max_weight_diet=lambda d: d.groupby("diet")['weight'].transform('max'))
    .loc[lambda df: df.weight==df.max_weight_diet]
)