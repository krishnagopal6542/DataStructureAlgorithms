# Leet Code: 2115
import collections


def main(recipes, ingredients, supplies):
    n = len(recipes)
    st = set(supplies)
    result = []

    adj_list = collections.defaultdict(list)
    indegree = [0] * n
    for i in range(n):
        for ing in ingredients[i]:
            if ing not in st:
                adj_list[ing].append(i)
                indegree[i] += 1

    q = collections.deque()
    for j in range(n):
        if indegree[j] == 0:
            q.append(j)

    while q:
        curr = q.popleft()
        recipe = recipes[curr]
        result.append(recipe)

        for nbr in adj_list[recipe]:
            indegree[nbr] -= 1
            if indegree[nbr] == 0:
                q.append(nbr)

    return result


if __name__ == '__main__':
    recipes = ["bread","sandwich","burger"]
    ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]]
    supplies = ["yeast","flour","meat"]
    print(main(recipes, ingredients, supplies))
