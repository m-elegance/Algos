#include <iostream>
#include <vector>
#include <string>

using namespace std;

int n, m;
vector <vector <bool>> used;
vector <vector <int>> graph;
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

void read() {
    cin >> n >> m;
    used.resize(n, vector <bool> (m, false));
    graph.resize(n, vector <int> (m, 0));
    for (int i = 0; i < n; i++) {
        string line;
        cin >> line;
        for (int j = 0; j < m; j++) {
            if (line[j] == '#') graph[i][j] = 1;
            
        }
    }
}
bool is_board(int i, int j){
    return (0 <= i && i < n && 0 <= j && j < m);
}
void dfs(int i, int j, vector < vector <bool>> &used){
    used[i][j] = true;
    for (int k = 0; k < 4; k++) {
        int new_i = i + dy[k];
        int new_j = j + dx[k];
        if (is_board(new_i, new_j)){
            if (graph[new_i][new_j] == 1 && used[new_i][new_j] == false){
                dfs(new_i, new_j, used);
            }
        }
    }

}
void solve() {
    int ans = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++){
            if (graph[i][j] == 1 && used[i][j] == false) {
                dfs(i, j, used);
                ans++;
            }
            
        }
    }
    
    cout << ans << endl;
}




int main(){
    read();
    solve();
    return 0;
}





