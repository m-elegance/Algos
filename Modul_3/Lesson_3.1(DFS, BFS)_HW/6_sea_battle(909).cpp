#include <iostream>
#include <vector>
#include <queue>



using namespace std;

int n, m;
int cnt_whole = 0;
int cnt_pad = 0;
int cnt_ded = 0;

int di[4] = {1, -1, 0, 0};
int dj[4] = {0, 0, 1, -1};

vector <vector <int>> graph;
vector <vector <bool>> used;

bool is_board(int i, int j){
    return i >= 0 && i < n && j >= 0 && j < m;
}


void read() {
    cin >> n >> m;
    graph.resize(n, vector <int> (m, 0));
    used.resize(n, vector <bool> (m, false));
    for (int i = 0; i < n; i++) {
        string line;
        cin >> line;
        for (int j = 0; j < m; j++) {
            if (line[j] == 'S') {graph[i][j] = 1; }
            else if (line[j] == 'X') {graph[i][j] = 2;}
        }
    }
    // for (int i = 0; i < n; i++) {
    //     for (int j = 0; j < m; j++) {
    //         cout << graph[i][j] << ' ';

    //     }cout << endl;
    // }

}
void bfs(int i, int j, bool &flag) {
    queue <pair <int, int>> q;
    q.push({i, j});
    while (!q.empty()){
        int i_1, j_1;
        i_1 = q.front().first;
        j_1 = q.front().second;
        q.pop();
        for (int k = 0; k < 4; k++) {
            int i_2 = i_1 + di[k];
            int j_2 = j_1 + dj[k];
            if (is_board(i_2, j_2) 
                && (graph[i_2][j_2] == 1 || graph[i_2][j_2] == 2)
                && used[i_2][j_2] == false){

                    used[i_2][j_2] = true;
                    q.push({i_2, j_2});
                    if (graph[i_1][j_1] != graph[i_2][j_2]) flag = true;
            }
        }
    }
    
}

void solve(){
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (graph[i][j] == 1 && used[i][j] == false){
                bool flag = false;
                bfs(i, j,flag);
                
                if (flag) cnt_pad++;
                else cnt_whole++;
            }
            if (graph[i][j] == 2 && used[i][j] == false){
                bool flag = false;
                bfs(i, j, flag);

                if (flag) cnt_pad++;
                else cnt_ded++;
            }
        }
    }
    cout << cnt_whole << ' ' << cnt_pad << ' ' << cnt_ded << endl;
}


int main() {
    
    read();
    solve();
    return 0;

}
