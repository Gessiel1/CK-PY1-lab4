def delete(list_, index=None):
    return[list_[:-1]]

print(delete([0,1,2,2], index=0))  # [0, 1]
print(delete([0, 1, 2, 3,3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4], index=1))  # [0, 1, 2, 3]