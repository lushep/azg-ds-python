# the base setting 
df1 = chickweight.merge(agg, left_on=["diet", "time"], right_on=["diet", "tijd"], suffixes=("", "_agg"))

# the other way around
df2 = agg.merge(chickweight, right_on=["diet", "time"], left_on=["diet", "tijd"], suffixes=("_agg", ""))

# note that in this case it might have been a better idea to instead 
# make sure that the column names are correct *beforehand*, e.g.

df3 =chickweight.merge(agg.rename({"tijd": "time"}, axis="columns"), on=['diet', 'time'])

# Though it is not strictly necessary in this case, you could also use the "how" argument. 

df4 = chickweight.merge(agg, how="left", left_on=["diet", "time"], right_on=["diet", "tijd"], suffixes=("", "_agg"))
