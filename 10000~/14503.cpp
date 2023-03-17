#include <iostream>
#include <algorithm>

using namespace std;

//INPUT
int map[52][52];
int N, M, x, y;
int dir;

//Variable
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};
char test[4] = {'U', 'R', 'D', 'L'};

//Output
int cnt = 0;

void PrintMap(){
    cout << "--------------- " << cnt << " --------------- " << test[dir] << endl;
    for (int i = 1; i <= N; i++){
        for (int j = 1; j <= M; j++){
            cout << map[i][j] << '\t';
        }
        cout << endl;
    }
}

//MainLogic
//whlie(true)
//1.청소되지 않은 경우 현 좌표 청소, cnt++
//2.주변 좌표 탐색 만약 주변이 깨끗할 경우
//ㄴ 한칸 후진
//   ㄴ 불가능 할 경우 retrun
//3. 깨끗하지 않은 경우
//ㄴ 반시계 회전
//   ㄴ 앞이 더러울 경우 전진

bool CleanAround(){
    if ((map[x-1][y] != 0) && (map[x+1][y] != 0) && (map[x][y-1] != 0) && (map[x][y+1] != 0)){
        return true;
    }
    return false;
}

void Simulate()
{
    while (true){
        //1
        if (map[x][y] == 0){
            map[x][y] = 2;
            cnt++;
        }
        //2
        if (CleanAround()){
            if(map[x-dx[dir]][y-dy[dir]] != 1){
                x = x - dx[dir];
                y = y - dy[dir];
            }
            else return;
        }
        
        //3
        else {
            dir = (dir + 3) % 4;

            if (map[x+dx[dir]][y+dy[dir]] == 0){
                x = x + dx[dir];
                y = y + dy[dir];
            }
        }
    }
}

int main()
{
    //맵을 전부 1로 세팅함으로써 외각 벽을 1로 처리
    fill(map[0], map[52], 1);
    
    cin >> N >> M;
    cin >> x >> y >> dir;
    
    //외각에 벽을 한줄 더 만들었기에 좌표 ++
    x+=1;
    y+=1;
    
    for (int i = 1; i <= N; i++){
        for (int j = 1; j <= M; j++){
            cin >> map[i][j];
        }
    }
    //
    Simulate();
    //test
    cout << cnt;
    return 0;
}