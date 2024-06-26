int minimumOperations(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize;
    int n = *gridColSize;

    int **count = (int **)malloc(n * sizeof(int *));
    int **dp = (int **)malloc(n * sizeof(int *));
    for (int i = 0; i < n; ++i) {
        count[i] = (int *)calloc(10, sizeof(int));
        dp[i] = (int *)calloc(10, sizeof(int));
    }

    for (int i = 0; i < m; ++i){
        for (int j = 0; j < n; ++j){
            ++count[j][grid[i][j]];
        }
    }

    int result = m * n - dfs(0, 0, m, n,count,dp);

    for (int i = 0; i < n; ++i) {
        free(count[i]);
        free(dp[i]);
    }
    free(count);
    free(dp);

    return result;
}


int dfs(int i, int p, int m, int n,int** count, int** dp){
    if (i == n){
        return 0;
    }
    if (dp[i][p] == 0){
        for (int v = 0; v < 10 ; ++v){
            if (i == 0 || v != p){
                dp[i][p] = fmax(dp[i][p], count[i][v] + dfs(i+1, v, m, n,count,dp));
            }
        }
    }
    return dp[i][p];
}
