def tree_from_traversals(preorder, inorder):
    if set(preorder) != set(inorder) or len(set(preorder)) != len(preorder):
        raise ValueError("Incorrect traversals")

    if preorder == []:
        return {}

    l, r = ''.join(inorder).split(preorder[0])

    return {"v": preorder[0],
            "l": tree_from_traversals([c for c in preorder if c in l], list(l)),
            "r": tree_from_traversals([c for c in preorder if c in r], list(r))}
