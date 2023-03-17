#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;

//입력
int height[502];
int N, M;

//출력
int res = 0;

//접근
//Peak 점들의 index와 value를 기록,
//인접한 두 Peak 중 최소값을 기준으로 사이에 공간에 물을 채움

//variable
queue<pair<int, int>> peak;

int main()
{
    cin >> N >> M;
    
    //양 옆 값을 비교할 것이기에 배열의 맨 앞, 맨 뒤에 0을 하나씩 배치함.
    for (int i = 1; i <= M; i++){
        cin >> height[i];
    }
    
    //peak점 기록 (양 옆과 비교해서 자기가 가장 큰 값보다 크거나 같을 시 peak)
    for (int i = 1; i <= M; i++){
        if ((height[i] >= height [i - 1]) && (height[i] >= height [i + 1])){
            peak.push({i, height[i]});
        }
    }

    cout << "Peak Size " << peak.size() << endl; 
    //peak 점을 기준으로 계산
    while(true){
        int leftidx = peak.front().first;
        int leftval = peak.front().second;
        cout << leftidx << endl;
        peak.pop();
        
        if (peak.empty()) break;
        
        int rightidx = peak.front().first;
        int rightval = peak.front().second; 
        int minval = min(leftval, rightval);
        
        for (int i = leftidx; i <= rightidx; i++){
            res += max(minval - height[i], 0);
        }
    }
    cout << res;
    return 0;
}