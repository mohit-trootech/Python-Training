import ast


class MyOptimizer(ast.NodeTransformer):

    def visit_BinOp(self, node: ast.BinOp):
        node.left = self.visit(node.left)
        node.right = self.visit(node.right)
        if isinstance(node.left, ast.Num) and isinstance(node.right, ast.Num):
            if isinstance(node.op, ast.Add):
                result = ast.Num(n=node.left.n + node.right.n)
                return ast.copy_location(result, node)
            elif isinstance(node.op, ast.Mult):
                result = ast.Num(n=node.left.n - node.right.n)
                return ast.copy_location(result, node)
        return node

    def visit_Name(self, node: ast.Name):
        if node.id == "pi":
            result = ast.Num(n=1)
            return ast.copy_location(result, node)
        return node


tree = ast.parse("y = 2 * pi;print(y)")
print(ast.dump(tree))
optimizer = MyOptimizer()
tree = optimizer.visit(tree)
exec(compile(tree, "<string>", "exec"))
