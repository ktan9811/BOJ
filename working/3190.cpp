// Online C++ compiler to run C++ program online
#include <iostream>
#include <queue>
#include <vector>

using namespace std;
//선언부
bool IsApple(int x, int y);
bool CanGo();
bool IsWall(int x, int y);
bool IsBody(int x, int y);

//입력
int map[101][101];
int N;
queue<pair<int, char>> keyIn;

//출력
int tick = 0;

//변수
int dx[4] = {0, 1, 0, -1}; //U > R > D > L > U
int dy[4] = {1, 0, -1, 0};

pair<int,int> curIn;

struct Snake{
    int _dir = 1;
    pair<int, int> _head = {1, 1};
    pair<int, int> _tail = {1, 1};
};

Snake s;

//함수

void NextTick(){
    if(keyIn.front().first == tick){
        if(keyIn.front().second == 'D') {
            s._dir = (s._dir + 3) % 4;
            cout << "IN D : " << s._dir << endl; 
        }
        else {
            s._dir = (s._dir + 1) % 4;
            cout << "IN L : " << s._dir << endl;
        }
        keyIn.pop();
    }

    int x = s._head.first;
    int y = s._head.second;

    int nx = x + dx[s._dir];
    int ny = y + dy[s._dir];
    
    s._head = {nx, ny};
    map[ny][nx] = -1;

    if(!IsApple(nx, ny)){
        s._tail.first += dx[s._dir];
        s._tail.second += dy[s._dir];
        map[y][x] = 0;
    }
    tick++;
}

bool IsApple(int x, int y){
  if (map[y][x] == 1) return true;
  return false;
};

bool CanGo(){
    int x = s._head.first;
    int y = s._head.second;
    
    int nx = x + dx[s._dir];
    int ny = y + dy[s._dir];
    
    if (IsWall(nx, ny)) return false;
    if (IsBody(nx, ny)) return false;
    return true;
};

bool IsWall(int x, int y){
    if(x < 1 || x > N || y < 1 || y > N) {
        cout << "Is Wall !!" << x << ' ' << y << ' ' << s._dir << endl;
        return true;
    }
    return false;
};

bool IsBody(int x, int y){
    if (map[y][x] == -1){ 
        cout << "Is Body !!" << x << ' ' << y << ' ' << s._dir << endl;
        return true;
    }
    return false;
};

void PrintMap(){
    cout << "-----------------------" << tick << "-----------------" << endl;
    for (int i = 1; i <= 10; i++){
        for (int j = 1; j <= 10; j++){
            cout << map[i][j] << '\t';
        }
        cout << endl;
    }
}

//main
int main() {
    //사과 입력
    int TP;
    cin >> N >> TP;
    for (int i = 0; i < TP; i++){
        int x, y;
        cin >> x >> y;
        map[y][x] = 1;
    }
    
    //명령 입력
    int M;
    cin >> M;
    for (int i = 0; i < M; i++){
        int T;
        char dir;
        cin >> T >> dir;
        keyIn.push({T, dir});
    }
    
    while(true){
        PrintMap();
        if (CanGo()) NextTick();
        else break;
    }
    
    cout << tick;
    return 0;
}