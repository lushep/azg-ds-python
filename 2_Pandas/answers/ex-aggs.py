(
    chickweight
    .groupby(['diet', 'time'])
    .agg(max_chick_id = pd.NamedAgg(column='rownum', aggfunc='max'),
         weight_mean = pd.NamedAgg(column='weight', aggfunc='mean'),
         weight_std = pd.NamedAgg(column='weight', aggfunc='std'),
         weight_median = pd.NamedAgg(column='weight', aggfunc=lambda x: x.median())
        )
)