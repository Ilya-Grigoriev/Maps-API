def selection(toponym):
    coord = toponym['boundedBy']['Envelope']
    ll, ll_2 = list(map(float, coord['lowerCorner'].split())), list(map(float, coord['upperCorner'].split()))
    delta = [str(ll_2[0] - ll[0]), str(ll_2[1] - ll[1])]
    print(delta)
    return delta
