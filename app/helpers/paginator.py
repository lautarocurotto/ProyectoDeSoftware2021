def applyLimit(aQuery, aPage, max):
    return aQuery.limit(max).offset(aPage * max)

def hasNextPage(aQuery, aPage, max):
    return aPage < (aQuery.count() / max) - 1