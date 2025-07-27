#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int n, m;
vector < vector <int>> graph;
vector < vector <int >> ans;
int di[8] = {1, 0, -1, 1, -1, 1, 0, -1};
int dj[8] = {1, 1, 1, 0, 0, -1, -1, -1};

bool is_board(int i, int j){
    return i >= 0 && i < n && j >= 0 && j < m;
}

void read() {
    cin >> n >> m;
    graph.resize(n, vector <int> (m));
    ans.resize(n, vector <int> (m, 0));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> graph[i][j];
            
        }
    }
}
void solve() {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (graph[i][j] == 1) ans[i][j] = 0;
            else{
            queue <pair <int, int>> q;
            q.push({i, j});
            while (!q.empty()) {
                int i_1, j_1;
                i_1 = q.front().first;
                j_1 = q.front().second;
                q.pop();
                for (int k = 0; k < 8; k++){
                    int i_2 = i_1 + di[k];
                    int j_2 = j_1 + dj[k];
                    if (is_board(i_2, j_2)){
                        if (graph[i_2][j_2] == 1){
                            ans[i][j] = abs(i_1 - i_2) + abs(j_1 - j_2);
                            break;
                        }else {
                            q.push({i_2, j_2});
                        }
                    }
                }
            }
            }
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cout << ans[i][j] << ' ';
        } cout << endl;
    }
}
int main(){
    read();
    solve();

    return 0;
}




