def tree_from_traversals(preorder, inorder):
    if len(preorder)!=len(inorder):
        raise ValueError("traversals must have the same length")

    if sorted(preorder)!=sorted(inorder):
        raise ValueError("traversals must have the same elements")

    if len(set(preorder))!=len(preorder) or len(set(inorder))!=len(inorder):
        raise ValueError("traversals must contain unique items")

    if preorder == [] or inorder == []:
        return {}

    raw_idx = list(inorder).index(preorder[0])

    left_inorder = inorder[:raw_idx]
    right_inorder = inorder[raw_idx+1:]

    left_preorder = [item for item in preorder if item in left_inorder]
    right_preorder = [item for item in preorder if item in right_inorder]
    
    tree = {
        "v": preorder[0],
        "l": tree_from_traversals(left_preorder,left_inorder),
        "r": tree_from_traversals(right_preorder,right_inorder)
    }

    return tree