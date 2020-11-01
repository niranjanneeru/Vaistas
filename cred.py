import pickle

with open('pickles/name.pickle', 'wb') as file:
    pickle.dump("Moriarty", file)

with open('pickles/age.pickle', 'wb') as file:
    pickle.dump(18, file)

with open('pickles/gender.pickle', 'wb') as file:
    pickle.dump(1, file)

    # 1 Male
    # 2 Female
    # 3 Prefer Not to Say
with open('pickles/weight.pickle', 'wb') as file:
    pickle.dump(46, file)

with open('pickles/height.pickle', 'wb') as file:
    pickle.dump(168, file)
