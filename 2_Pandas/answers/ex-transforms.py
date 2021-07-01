(
    chickweight
    .assign(mean_weight_diet=lambda d: d.groupby("diet")['weight'].transform('mean'),
            mean_weight_diet_time=lambda d: d.groupby(["diet", "time"])['weight'].transform('mean'),
            num_chickens_diet=lambda d: d.groupby("diet")["chick"].transform(lambda d: d.nunique())
           )
)