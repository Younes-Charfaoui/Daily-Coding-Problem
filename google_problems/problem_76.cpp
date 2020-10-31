/*This problem was asked by Google.

Given a binary search tree and a range [a, b] (inclusive), return the sum of the 
elements of the binary search tree within the range.

For example, given the following tree:

    5
   / \
  3   8
 / \ / \
2  4 6  10
and the range [4, 9], return 23 (5 + 4 + 6 + 8).
*/

void dfs(Tree* root, int a, int b, int& sum) {
    if (!root) return;
    int v = root->value;
    if (v <= b && v >= a) sum += v;
    dfs(root->left, a, b, sum);
    dfs(root->right, a, b, sum);
}

int solve(Tree* root, int a, int b) {
    int sum = 0;
    dfs(root, a, b, sum);
    return sum;
}
