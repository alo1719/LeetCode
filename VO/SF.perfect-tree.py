class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Snowflake VOE
def isPerfectTree(root: Optional[TreeNode]) -> bool:
    q = []
    q.append(root)
    num_per_level = 1
    while q:
        new_q = []
        for node in q:
            if node.left: new_q.append(node.left)
            if node.right: new_q.append(node.right)
        num_per_level *= 2
        if not new_q: break
        if len(new_q) != num_per_level:
            return False
        q = new_q
    return True

def fill2PerfectTree(root):
    exisiting_node, exisiting_level = 1, 1
    # check
    q = []
    q.append(root)
    while q:
        new_q = []
        for node in q:
            if node.left:
                new_q.append(node.left)
                exisiting_node += 1
            if node.right:
                new_q.append(node.right)
                exisiting_node += 1
        if not new_q: break
        exisiting_level += 1
        q = new_q
    # choose fill or delete
    fill_node_num = 2**exisiting_level - 1 - exisiting_node
    delete_node_num = exisiting_node - 2**(exisiting_level-1) + 1
    # fill or delete
    current_level = 1
    if fill_node_num < delete_node_num:
        q = []
        q.append(root)
        while q:
            new_q = []
            for node in q:
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
                if current_level == exisiting_level - 1:
                    if not node.left:
                        node.left = TreeNode()
                    if not node.right:
                        node.right = TreeNode()
            if not new_q: break
            current_level += 1
            q = new_q
    else:
        q = []
        q.append(root)
        while q:
            new_q = []
            for node in q:
                if current_level == exisiting_level - 1:
                    if node.left:
                        node.left = None
                    if node.right:
                        node.right = None
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            if not new_q: break
            current_level += 1
            q = new_q