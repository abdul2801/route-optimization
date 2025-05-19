from typing import List


def nearest_insertion(order_ids: List[int], dist_fn) -> List[int]:
    if not order_ids:
        return []
    route = [order_ids[0]]
    un = set(order_ids[1:])
    while un:
        best = None
        best_cost = 1e18
        for o in list(un):
            for i in range(len(route)+1):
                cost = _route_increase(route, o, i, dist_fn)
                if cost < best_cost:
                    best_cost = cost
                    best = (o, i)
        o, i = best
        route.insert(i, o)
        un.remove(o)
    return route


def _route_increase(route, o, insert_idx, dist_fn):
    before = route[insert_idx-1] if insert_idx>0 else route[0]
    after = route[insert_idx] if insert_idx < len(route) else route[-1]
    return dist_fn(before, o) + dist_fn(o, after) - dist_fn(before,